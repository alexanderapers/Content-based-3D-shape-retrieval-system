#from reorder import make_category_shapes_dict
from ANN import Annoy
from distance import Distance
import time
from tqdm import tqdm
#import pickle
#import os
#from os.path import join
#from collections import defaultdict
#import matplotlib.pyplot as plt
#from sklearn.metrics import auc


class Timing:
    def __init__(self, dataset, exclude_list):
        self.dataset = dataset
        self.exclude_list = exclude_list
        self.ann = Annoy("Princeton_remeshed_normalized", exclude_list, n_bins=30)
        self.dist = Distance("Princeton_remeshed_normalized", exclude_list)

        times = 0
        n = len(list(self.dataset.get_all_meshes_file_paths())[:50])
        for mesh_file_path in tqdm(list(self.dataset.get_all_meshes_file_paths())[:50]):
            mesh_name = mesh_file_path.split("/")[-1]
            if mesh_name not in self.exclude_list:
                start_time = time.perf_counter()
                #result = self.dist.query_inside_db(mesh_file_path, self.dist.euclidean_EMD, k=1813)
                #result = self.ann.query_inside_db(mesh_file_path, k=1813)
                #result = self.dist.query(mesh_file_path, self.dist.euclidean_EMD, k=1813)
                result = self.ann.query(mesh_file_path, k=1813)
                stop_time = time.perf_counter()
                times += stop_time - start_time
        print(times/n, "seconds per query")
