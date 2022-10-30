import csv
import numpy as np
from numba import njit
import time


class Distance:
    def __init__(self, dataset):
        self.dataset = dataset
        self.csv = "features/" + dataset.folder_name_dataset + "_all_features_normalized.csv"
        self.features = self.csv_to_dict()

        # compiling numba
        self.manhatten(np.array([1.0]), np.array([1.0]))
        self.euclidean(np.array([1.0]), np.array([1.0]))
        self.cosine(np.array([1.0]), np.array([1.0]))

        start_time = time.perf_counter()
        for mesh_name in self.features.keys():
            if mesh_name not in self.dataset.exclude_list:
                self.distance("m1.ply", mesh_name, self.cosine)
                #print(mesh_name, self.distance("m1.ply", mesh_name, self.manhatten))
        print("--- %s seconds ---" % (time.perf_counter() - start_time))


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
        a = self.features[mesh_name_1]
        b = self.features[mesh_name_2]
        return metric(a, b)


    @staticmethod
    @njit()
    def euclidean(mesh_features_1, mesh_features_2):
        return np.linalg.norm(mesh_features_1 - mesh_features_2)


    @staticmethod
    @njit()
    def manhatten(mesh_features_1, mesh_features_2):
        return np.sum(np.abs(mesh_features_1 - mesh_features_2))


    @staticmethod
    @njit()
    def cosine(mesh_features_1, mesh_features_2):
        norm_1 = np.linalg.norm(mesh_features_1)
        norm_2 = np.linalg.norm(mesh_features_2)
        return 1 - (np.dot(mesh_features_1, mesh_features_2) / (norm_1 * norm_2))
