import trimesh
from trimesh.exchange.export import export_mesh
from trimesh.repair import fix_inversion
import numpy as np
#import open3d as o3d

class Mesh:
    def __init__(self, mesh_file_path):
        self.mesh_file_path = mesh_file_path
        self.name = mesh_file_path.split("/")[-1]
        self.category = mesh_file_path.split("/")[-2]
        self.mesh = trimesh.load(mesh_file_path)
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()
        self.scale = self.get_scale()


    def show(self):
        self.mesh.show()


    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.category, self.n_vertices, self.n_faces)


    def basic_mesh_info(self):
        return [self.name, self.category, self.n_vertices, self.n_faces, self.d_centroid_origin]


    def get_AABB(self):
        return self.bounding_box


    def subdivide(self):
        self.mesh = self.mesh.subdivide()
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()


    def decimation(self):
        self.mesh = self.mesh.simplify_quadratic_decimation(6400)
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()

    def apply_transform(self, matrix):
        self.mesh.apply_transform(matrix)
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()

    def transform_vertices(self, matrix):
        new_vertices = []
        for v in self.mesh.vertices:
            new_vertices.append(np.dot(matrix, v))

        self.mesh = trimesh.base.Trimesh(vertices = new_vertices, faces = self.mesh.faces)
        fix_inversion(self.mesh)
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()

    def normalize_scale(self):
        self.mesh.apply_scale(1.0 / max(self.mesh.extents))
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()

    def get_n_vertices(self):
        return self.mesh.vertices.shape[0]

    def get_vertices(self):
        return self.mesh.vertices


    def get_n_faces(self):
        return self.mesh.faces.shape[0]


    def export(self, file_path):
        export_mesh(self.mesh, file_path, self.name.split(".")[-1])


    def get_distance_centroid_origin(self):
        return sum(self.centroid * self.centroid) ** 0.5


    def get_scale(self):
        # assert self.bounding_box[0][0] != self.bounding_box[6][0]
        # assert self.bounding_box[0][1] != self.bounding_box[6][1]
        # assert self.bounding_box[0][2] != self.bounding_box[6][2]
        #
        # return sum((self.bounding_box[6] - self.bounding_box[0]) ** 2) ** 0.5
        #raise notImplementedError()
        return None
