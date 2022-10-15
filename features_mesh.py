import trimesh
import numpy as np

class Features_Mesh:
    def __init__(self, mesh):
        self.mesh = mesh
        self.area = self.get_area_mesh()
        self.diameter = self.get_diameter_mesh()
        self.eccentricity = self.get_eccentricity_mesh()
        self.compactness = self.get_compactness_mesh()
        self.AABB_volume = self.get_AABB_volume_mesh()


    def get_diameter_mesh(self):
        try:
            convex_hull = self.mesh.mesh.convex_hull
            max_dist = 0
            for v1 in convex_hull.vertices:
                for v2 in convex_hull.vertices:
                    if (v1 != v2).any():
                        dist = np.linalg.norm(v1 - v2)
                        if dist > max_dist:
                            max_dist = dist
            return max_dist
        except:
            print(self.mesh.name, "didn't work")


    def get_eccentricity_mesh(self):
        covariance = np.cov(np.transpose(self.mesh.get_vertices()))
        eigenvalues, eigenvectors = np.linalg.eig(covariance)
        return np.max(eigenvalues) / np.min(eigenvalues)


    def get_volume_mesh(self):
        return self.mesh.mesh.volume


    def get_area_mesh(self):
        return self.mesh.mesh.area


    def get_compactness_mesh(self):
        if self.get_volume_mesh() <= 0:
            return 0
        compactness = self.get_area_mesh() ** 3 / (36 * np.pi * self.get_volume_mesh() ** 2)
        return compactness


    def get_AABB_volume_mesh(self):
        return np.prod(self.mesh.mesh.extents)


    def get_all_elementary_features(self):
        return [self.mesh.name, self.area, self.compactness, self.AABB_volume, self.diameter, self.eccentricity]
