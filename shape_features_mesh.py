import trimesh
import numpy as np
from trimesh.sample import sample_surface_even
from trimesh.points import PointCloud
import logging
#import time
import matplotlib.pyplot as plt

class Shape_Features_Mesh:
    def __init__(self, mesh, n_samples=6500, minimum_n_samples=2000):
        #start_time = time.time()
        self.turn_off_logger()
        self.mesh = mesh
        self.n_samples = n_samples
        self.minimum_n_samples = minimum_n_samples
        self.get_all_points()

        self.A3 = self.get_A3()
        self.D1 = self.get_D1()
        self.D2 = self.get_D2()
        self.D3 = self.get_D3()
        self.D4 = self.get_D4()

        # created 10 evenly spaced bins on interval [0, pi]
        self.hist_A3, _ = np.histogram(self.A3, bins=np.arange(0, np.pi + np.pi/10, np.pi/10), weights=np.ones(len(self.A3)) / len(self.A3))

        # 0.968 is highest occurring value. 95 percentile is 0.508
        # created 9 evenly spaced bins on interval [0, 0.508]. 10th bin is [0.508, 1].
        self.hist_D1, _ = np.histogram(self.D1, bins=self.get_bins(0, 0.508, 1, 10), weights=np.ones(len(self.D1)) / len(self.D1))

        # 1.607 is highest occurring value. 95 percentile is 0.793
        # created 9 evenly spaced bins on interval [0, 0.793]. 10th bin is [0.793, 1.732]
        self.hist_D2, _ = np.histogram(self.D2, bins=self.get_bins(0, 0.793, 1.732, 10), weights=np.ones(len(self.D2)) / len(self.D2))

        # 0.830 is highest occurring value. 95 percentile is 0.372
        # created 9 evenly spaced bins on interval [0, 0.372]. 10th bin is [0.372, 0.9]
        self.hist_D3, _ = np.histogram(self.D3, bins=self.get_bins(0, 0.372, 0.9, 10), weights=np.ones(len(self.D3)) / len(self.D3))

        # 0.526 is highest occurring value. 95 percentile is 0.206
        # created 9 evenly spaced bins on interval [0, 0.206]. 10th bin is [0.206, 0.6]
        self.hist_D4, _ = np.histogram(self.D4, bins=self.get_bins(0, 0.206, 0.6, 10), weights=np.ones(len(self.D4)) / len(self.D4))

        #print("--- %s seconds ---" % (time.time() - start_time))


    def get_pointcloud(self):
        samples, _ = sample_surface_even(self.mesh.mesh, count=self.n_samples)
        iter = 2
        while len(samples) < self.minimum_n_samples:
            samples, _ = sample_surface_even(self.mesh.mesh, count=iter*self.n_samples)
            iter += 1
        return PointCloud(samples)


    def get_A3(self):
        # theoretical maximum: np.pi
        edge1 = self.points1 - self.points2
        edge2 = self.points3 - self.points2

        dot = np.sum(edge1*edge2, axis=1)
        norm_edge1 = np.linalg.norm(edge1, axis=1)
        norm_edge2 = np.linalg.norm(edge2, axis=1)
        cosine_angle = dot / (norm_edge1 * norm_edge2)
        angles = np.arccos(cosine_angle)
        #degree_angles = np.rad2deg(angles)

        return angles


    def get_D1(self):
        return np.sqrt(np.sum(np.square(self.points1), axis=1))


    def get_D2(self):
        return np.sqrt(np.sum(np.square(self.points1 - self.points2), axis=1))


    def get_D3(self):
        edge1 = self.points1 - self.points2
        edge2 = self.points3 - self.points2

        cross = np.cross(edge1, edge2)
        return np.sqrt(np.linalg.norm(cross, axis=1) / 2)


    def get_D4(self):
        # i guess it's always less than 1/2
        ad = self.points1 - self.points4
        bd = self.points2 - self.points4
        cd = self.points3 - self.points4
        volume = np.abs(np.sum(ad * np.cross(bd, cd), axis=1)) / 6

        return np.cbrt(volume)


    # def validate_points(self):
    #     return not (
    #     (self.points1 == self.points2).any() or
    #     (self.points2 == self.points3).any() or
    #     (self.points3 == self.points4).any() or
    #     (self.points4 == self.points1).any() or
    #     (self.points1 == self.points3).any() or
    #     (self.points2 == self.points4).any()
    #     )
    #
    # def reshuffle(self):
    #     np.random.shuffle(self.points1)
    #     np.random.shuffle(self.points2)
    #     np.random.shuffle(self.points3)
    #     np.random.shuffle(self.points4)

    def get_all_points(self):
        self.points1 = np.random.permutation(self.get_pointcloud().vertices)
        self.points2 = np.random.permutation(self.get_pointcloud().vertices)
        self.points3 = np.random.permutation(self.get_pointcloud().vertices)
        self.points4 = np.random.permutation(self.get_pointcloud().vertices)
        cutoff = min(len(self.points1), len(self.points2), len(self.points3), len(self.points4))
        self.points1 = self.points1[:cutoff]
        self.points2 = self.points2[:cutoff]
        self.points3 = self.points3[:cutoff]
        self.points4 = self.points4[:cutoff]
        # i = 0
        # while not self.validate_points():
        #     self.reshuffle()
        #     i+=1
        # print(i)

    def turn_off_logger(self):
        L = logging.getLogger("trimesh")
        L.setLevel(logging.ERROR)


    def get_bins(self, min_value, percentile95, max_value, n_bins):
        return np.concatenate([np.arange(min_value, percentile95+percentile95/(n_bins-1), percentile95/(n_bins-1)),
         np.array([max_value])])


    def get_all_shape_features(self):
        return [self.mesh.name] + list(np.concatenate([self.hist_A3, self.hist_D1, self.hist_D2, self.hist_D3, self.hist_D4]))
