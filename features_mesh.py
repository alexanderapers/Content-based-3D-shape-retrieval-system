import trimesh
import numpy as np
from scipy.spatial.distance import cdist
#from numba import njit

class Features_Mesh:
    def __init__(self, mesh):
        self.mesh = mesh
        self.area = self.get_area_mesh()
        self.diameter = self.get_diameter_mesh()
        self.eccentricity = self.get_eccentricity_mesh(np.array(self.mesh.get_vertices()))
        self.compactness = self.get_compactness_mesh()
        self.AABB_volume = self.get_AABB_volume_mesh()


    def get_diameter_mesh(self):
        try:
            convex_hull = self.mesh.mesh.convex_hull
            return self.conv_hull_diameter(convex_hull.vertices)
        except:
           print(self.mesh.name, "didn't work")
           return 0


    @staticmethod
    #@njit()
    def conv_hull_diameter(verts):
        return np.max(cdist(verts, verts, metric="euclidean"))


    @staticmethod
    #@njit()
    def get_eccentricity_mesh(verts):
        covariance = np.cov(np.transpose(verts))
        eigenvalues, eigenvectors = np.linalg.eig(covariance)
        if np.min(eigenvalues) >= 1e-5:
            return np.max(eigenvalues) / np.min(eigenvalues)
        else:
            return 0


    def get_volume_mesh(self):
        return self.mesh.mesh.volume


    def get_area_mesh(self):
        return self.mesh.mesh.area


    def get_compactness_mesh(self):
        if self.get_volume_mesh() <= 1e-5:
            return 0
        compactness = self.get_area_mesh() ** 3 / (36 * np.pi * self.get_volume_mesh() ** 2)
        return min(compactness, 10_000)


    def get_AABB_volume_mesh(self):
        return self.get_volume_mesh() / np.prod(self.mesh.mesh.extents)


    def get_all_elementary_features(self):
        return [self.mesh.name, self.mesh.category, self.area, self.compactness, self.AABB_volume, self.diameter, self.eccentricity]
