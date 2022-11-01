import time
import csv
import numpy as np
#from numba import njit
from mesh import Mesh
from features_mesh import Features_Mesh
from shape_features_mesh import Shape_Features_Mesh
from scipy.stats import wasserstein_distance


class Distance:
    def __init__(self, dataset_name, exclude_list):
        self.csv = "features/" + dataset_name + "_all_features_normalized.csv"
        self.features = self.csv_to_dict()
        self.exclude_list = exclude_list
        self.norm_info = np.load("norm_info.npy")
        # edit this to tweak weights
        self.weights = np.concatenate([np.repeat(1/10, 5), np.repeat(1/100, 50)])

        # compiling numba
        #self.manhatten(np.array([1.0]), np.array([1.0]))
        #self.euclidean(np.array([1.0]), np.array([1.0]))
        #self.cosine(np.array([1.0]), np.array([1.0]))

        self.query("LabeledDB_new/Octopus/121.off", self.euclidean, k=10)


    def query(self, mesh_file_path, metric, k=10):
        start_time = time.perf_counter()
        query_mesh = self.meshify(mesh_file_path)
        query_features = self.extract_features_mesh(query_mesh)
        result = self.find_k_most_similar(query_features, metric, k)
        print("--- %s seconds ---" % (time.perf_counter() - start_time))
        return result


    def csv_to_dict(self):
        with open(self.csv, 'r') as read_obj:
            features_dict = dict()
            csv_reader = csv.reader(read_obj)
            next(csv_reader)
            for row in csv_reader:
                mesh_name = row[0]
                mesh_features = np.array(row[2:]).astype(float)
                features_dict[mesh_name] = mesh_features
            return features_dict


    def distance(self, mesh_name_1, mesh_name_2, metric):
        a = self.weights * self.features[mesh_name_1]
        b = self.weights * self.features[mesh_name_2]
        return metric(a, b)


    def meshify(self, query_mesh_file_path):
        mesh = Mesh(query_mesh_file_path)
        mesh.resample_mesh()
        mesh.normalize_mesh()
        return mesh


    def extract_features_mesh(self, query_mesh):
        elem_features = Features_Mesh(query_mesh).get_all_elementary_features()
        shape_features = Shape_Features_Mesh(query_mesh).get_all_shape_features()
        elem_features[2:] = (elem_features[2:] - self.norm_info[:, 0]) / self.norm_info[:, 1]
        return np.array(elem_features[2:] + shape_features[1:])


    def find_k_most_similar(self, query_features, metric, k=10):
        distances = {x: 0 for x in self.features}
        for mesh_name in self.features:
            distances[mesh_name] = metric(query_features, self.features[mesh_name])
        return sorted(distances.items(), key=lambda item: item[1])[:k]


    @staticmethod
    #@njit()
    def euclidean(mesh_features_1, mesh_features_2):
        return np.linalg.norm(mesh_features_1 - mesh_features_2)


    @staticmethod
    #@njit()
    def manhatten(mesh_features_1, mesh_features_2):
        return np.sum(np.abs(mesh_features_1 - mesh_features_2))


    @staticmethod
    #@njit()
    def cosine(mesh_features_1, mesh_features_2):
        norm_1 = np.linalg.norm(mesh_features_1)
        norm_2 = np.linalg.norm(mesh_features_2)
        return 1 - (np.dot(mesh_features_1, mesh_features_2) / (norm_1 * norm_2))
