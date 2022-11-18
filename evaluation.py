from reorder import make_category_shapes_dict
from ANN import Annoy
from distance import Distance
from tqdm import tqdm
import pickle
import os
from os.path import join
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.metrics import auc


class Evaluation:
    def __init__(self, dataset, exclude_list):
        self.dataset = dataset
        self.exclude_list = exclude_list
        self.map_mesh_name_to_category = self.mesh_name_to_category()
        self.meshes_per_category_dict = self.create_dict()

        self.ann = Annoy("Princeton_remeshed_normalized", exclude_list, n_bins=30)
        self.dist = Distance("Princeton_remeshed_normalized", exclude_list)

        #self.ROC_curve_dists(steps=5)
        self.ROC_curve_per_class("ann", steps=1)
        self.ROC_curve_per_class("custom", steps=1)

    def ROC_curve_per_class(self, method, steps):
        a, b, c, d = self.ROC_curve(method=method, steps=steps)
        plt.rcParams["figure.figsize"] = (17,15)
        aucs = defaultdict(int)
        for c in a[0]:
            cx = []
            cy = []
            for i in range(len(a)):
                sens = a[i][c]
                spec = b[i][c]
                cx.append(sens)
                cy.append(spec)
            plt.plot(cx, cy, "-", label=c)
            aucs[c] = auc(cx, cy)
        with open("results/AUCs_{}.txt".format(method), "w") as handle:
            for c in sorted(aucs.items(), key=lambda item: item[1], reverse=True):
                handle.write("Class " + c[0] + " has AUC of " + str(c[1]) + "\n")
        plt.legend()
        plt.xlabel("sensitivity")
        plt.ylabel("specificity")

        #plt.show()
        plt.savefig("results/sens_spec_{}_per_class.png".format(method))
        plt.clf()


    def ROC_curve_dists(self, steps):
        _, _, c, d = self.ROC_curve("custom", steps=steps)
        _, _, g, h = self.ROC_curve("ann", steps=steps)

        plt.plot(g, h, "--", label="ANN (L2)", color="crimson", linewidth=2)
        plt.plot(c, d, "--", label="custom distance (L2 + EMD weighted)", color="plum", linewidth=2)
        plt.legend()
        plt.xlabel("sensitivity")
        plt.ylabel("specificity")

        print("ANN (L2) AUC:", auc(g, h))
        print("custom distance (L2 + EMD weighted):", auc(c, d))

        #plt.show()
        plt.savefig("results/sens_spec.png")
        plt.clf()


    def ROC_curve(self, method, steps):
        sens_all_query_lengths = []
        spec_all_query_lengths = []
        global_sens_all_query_lengths = []
        global_spec_all_query_lengths = []

        for k in tqdm(range(1, len(self.dataset) - len(self.exclude_list) + 1, steps)):
            sensitivities, specificities, global_sensitivity, global_specificity = self.sensitivity_specificity_at_k(method, k)
            global_sens_all_query_lengths.append(global_sensitivity)
            global_spec_all_query_lengths.append(global_specificity)
            sens_all_query_lengths.append(sensitivities)
            spec_all_query_lengths.append(specificities)

        return sens_all_query_lengths, spec_all_query_lengths, global_sens_all_query_lengths, global_spec_all_query_lengths


    def querying(self, method):
        map_query_mesh_to_result = dict()

        for mesh_file_path in tqdm(list(self.dataset.get_all_meshes_file_paths())):
            mesh_name = mesh_file_path.split("/")[-1]

            if mesh_name not in self.exclude_list:
                if method == "custom":
                    result = self.dist.query_inside_db(mesh_file_path, self.dist.euclidean_EMD, k=len(self.dataset)-len(self.exclude_list))
                elif method == "ann":
                    result = self.ann.query_inside_db(mesh_file_path, k=len(self.dataset)-len(self.exclude_list))
                else:
                    print("Not a valid distance function")

                map_query_mesh_to_result[mesh_name] = [x[0] for x in result]

        with open('query_results/{}_querying_results.pickle'.format(method), 'wb') as handle:
            pickle.dump(map_query_mesh_to_result, handle)

        return map_query_mesh_to_result


    def sensitivity_specificity_at_k(self, method, k):
        with open('query_results/{}_querying_results.pickle'.format(method), "rb") as handle:
            query_results = pickle.load(handle)

        dataset_size = 1813
        sensitivities = defaultdict(int)
        specificities = defaultdict(int)
        global_sensitivity = 0
        global_specificity = 0

        for mesh_file_path in list(self.dataset.get_all_meshes_file_paths()):
            mesh_name = mesh_file_path.split("/")[-1]

            if mesh_name not in self.exclude_list:
                true_label = mesh_file_path.split("/")[-2]
                result = query_results[mesh_name][:k]
                categories = [self.map_mesh_name_to_category[x] for x in result]
                TP = categories.count(true_label)
                FN = self.meshes_per_category_dict[true_label] - TP
                TN = dataset_size - k - FN
                FP = k - TP
                specificity = TN / (FP + TN)
                recall = TP / self.meshes_per_category_dict[true_label]

                sensitivities[true_label] += recall
                specificities[true_label] += specificity
                global_sensitivity += recall
                global_specificity += specificity

        for c in sensitivities:
            sensitivities[c] /= self.meshes_per_category_dict[c]
            specificities[c] /= self.meshes_per_category_dict[c]

        global_sensitivity /= dataset_size
        global_specificity /= dataset_size

        return sensitivities, specificities, global_sensitivity, global_specificity


    def create_dict(self):
        result = dict()
        folder_path = join(os.getcwd(), self.dataset.folder_name_dataset)
        for cat in os.listdir(folder_path):
            if os.path.isdir(join(folder_path, cat)):
                result[cat] = len(os.listdir(join(folder_path, cat)))
        for m in self.exclude_list:
            result[self.map_mesh_name_to_category[m]] -= 1

        return result


    def mesh_name_to_category(self):
        result = {}
        for mesh_file_path in list(self.dataset.get_all_meshes_file_paths()):
            mesh_name = mesh_file_path.split("/")[-1]
            mesh_category = mesh_file_path.split("/")[-2]
            result[mesh_name] = mesh_category

        return result
