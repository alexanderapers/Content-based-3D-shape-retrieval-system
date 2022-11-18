import trimesh
import numpy as np
from trimesh.sample import sample_surface_even
from trimesh.points import PointCloud
import logging
#import time
#from numba import njit


class Shape_Features_Mesh:
    def __init__(self, mesh, n_samples=6500, minimum_n_samples=2000):
        #start_time = time.time()
        self.turn_off_logger()
        self.mesh = mesh
        self.n_samples = n_samples
        self.minimum_n_samples = minimum_n_samples
        self.cutoff = self.get_all_points()
        self.n_bins = 30

        self.A3 = self.get_A3(self.points1, self.points2, self.points3)
        self.D1 = self.get_D1(self.points1)
        self.D2 = self.get_D2(self.points1, self.points2)
        self.D3 = self.get_D3(self.points1, self.points2, self.points3)
        self.D4 = self.get_D4(self.points1, self.points2, self.points3, self.points4)

        # create 30 evenly spaced bins on interval [0, pi]
        self.hist_A3, _ = self.make_histogram(inp=self.A3, max_value=np.round(np.pi, 5))

        # create 30 evenly spaced bins on interval [0, 0.9677]
        self.hist_D1, _ = self.make_histogram(inp=self.D1, max_value=0.9677)

        # create 30 evenly spaced bins on interval [0, 1.6031]
        self.hist_D2, _ = self.make_histogram(inp=self.D2, max_value=1.6031)

        # create 30 evenly spaced bins on interval [0, 0.8410]
        self.hist_D3, _ = self.make_histogram(inp=self.D3, max_value=0.8410)

        # create 30 evenly spaced bins on interval [0, 0.5738]
        self.hist_D4, _ = self.make_histogram(inp=self.D4, max_value=0.5738)

        #print("--- %s seconds ---" % (time.time() - start_time))


    def get_pointcloud(self):
        samples, _ = sample_surface_even(self.mesh.mesh, count=self.n_samples)
        iter = 2
        while len(samples) < self.minimum_n_samples:
            samples, _ = sample_surface_even(self.mesh.mesh, count=iter*self.n_samples)
            iter += 1
        return PointCloud(samples)


    @staticmethod
    #@njit()
    def A3_sub1(points1, points2, points3):
        # theoretical maximum: np.pi
        edge1 = points1 - points2
        edge2 = points3 - points2

        dot = np.sum(edge1*edge2, axis=1)
        return (dot, edge1, edge2)


    @staticmethod
    #@njit()
    def A3_sub2(dot, norm_edge1, norm_edge2):
        cosine_angle = dot / (norm_edge1 * norm_edge2)
        angles = np.arccos(cosine_angle)
        #degree_angles = np.rad2deg(angles)

        return angles


    @staticmethod
    def get_A3(points1, points2, points3):
        dot, edge1, edge2 = Shape_Features_Mesh.A3_sub1(points1, points2, points3)

        norm_edge1 = np.linalg.norm(edge1, axis=1)
        norm_edge2 = np.linalg.norm(edge2, axis=1)

        return Shape_Features_Mesh.A3_sub2(dot, norm_edge1, norm_edge2)


    @staticmethod
    #@njit()
    def get_D1(points1):
        return np.sqrt(np.sum(np.square(points1), axis=1))


    @staticmethod
    #@njit()
    def get_D2(points1, points2):
        return np.sqrt(np.sum(np.square(points1 - points2), axis=1))


    @staticmethod
    #@njit()
    def D3_sub(points1, points2, points3):
        edge1 = points1 - points2
        edge2 = points3 - points2

        cross = np.cross(edge1, edge2)
        return cross


    @staticmethod
    def get_D3(points1, points2, points3):
        cross = Shape_Features_Mesh.D3_sub(points1, points2, points3)
        return np.sqrt(np.linalg.norm(cross, axis=1) / 2)


    @staticmethod
    #@njit()
    def get_D4(points1, points2, points3, points4):
        # i guess it's always less than 1/2
        ad = points1 - points4
        bd = points2 - points4
        cd = points3 - points4
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
        self.points1 = self.permute(self.get_pointcloud().vertices)
        self.points2 = self.permute(self.get_pointcloud().vertices)
        self.points3 = self.permute(self.get_pointcloud().vertices)
        self.points4 = self.permute(self.get_pointcloud().vertices)
        cutoff = min(len(self.points1), len(self.points2), len(self.points3), len(self.points4))
        self.points1 = self.points1[:cutoff]
        self.points2 = self.points2[:cutoff]
        self.points3 = self.points3[:cutoff]
        self.points4 = self.points4[:cutoff]
        return cutoff
        # i = 0
        # while not self.validate_points():
        #     self.reshuffle()
        #     i+=1
        # print(i)

    def turn_off_logger(self):
        L = logging.getLogger("trimesh")
        L.setLevel(logging.ERROR)


    @staticmethod
    #@njit()
    def permute(inp):
        return np.random.permutation(inp)


    def make_histogram(self, inp, max_value):
        return np.histogram(inp[inp < max_value], bins=np.arange(0, max_value + max_value/self.n_bins, max_value/self.n_bins), weights=np.ones(len(inp[inp < max_value])) / len(inp[inp < max_value]))


    def get_all_shape_features(self):
        return [self.mesh.name] + list(np.concatenate([self.hist_A3, self.hist_D1, self.hist_D2, self.hist_D3, self.hist_D4]))
