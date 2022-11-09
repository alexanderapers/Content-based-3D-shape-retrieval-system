import trimesh
from trimesh.exchange.export import export_mesh
import numpy as np
from trimesh.repair import fill_holes
from trimesh.repair import fix_inversion
from trimesh.repair import fix_normals
from trimesh.repair import fix_winding
from trimesh.repair import broken_faces
from trimesh.repair import stitch
from trimesh import scene
import os
import re
#import open3d as o3d

class Mesh:
    def __init__(self, mesh_file_path):
        self.mesh_file_path = mesh_file_path
        sep = os.sep
        
        self.name = os.path.split(mesh_file_path)[-1]
        self.category = os.path.split(mesh_file_path)[-2]
        self.mesh = trimesh.load(mesh_file_path)
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()
        self.alignment = self.get_alignment()
        self.scale = self.get_scale()
        self.flip = self.get_flip()

    def show(self):
        self.mesh.show()


    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.category, self.n_vertices, self.n_faces)


    def basic_mesh_info(self):
        return [self.name, self.category, self.n_vertices, self.n_faces, self.d_centroid_origin, self.scale]


    def get_AABB(self):
        return self.bounding_box


    def subdivide(self):
        self.mesh = self.mesh.subdivide()
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()
        self.scale = self.get_scale()
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()


    def subdivide_to_size(self):
        # TODO do this properly? take 0.01 and square root
        self.mesh = self.mesh.subdivide_to_size(np.sum(self.mesh.extents ** 2), max_iter=1000)
        #self.mesh = trimesh.base.Trimesh(vertices = vertices, faces = new_faces)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()
        self.scale = self.get_scale()
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()


    def decimation(self):
        self.mesh = self.mesh.simplify_quadratic_decimation(3500)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()
        self.scale = self.get_scale()
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()

    def apply_transform(self, matrix):
        self.mesh.apply_transform(matrix)
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()
        self.scale = self.get_scale()

    def transform_vertices(self, matrix):
        new_vertices = []
        for v in self.mesh.vertices:
            new_vertices.append(np.dot(matrix, v))

        self.mesh = trimesh.base.Trimesh(vertices = new_vertices, faces = self.mesh.faces)
        fix_inversion(self.mesh)
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()
        self.scale = self.get_scale()

    def normalize_scale(self):
        self.mesh.apply_scale(1.0 / max(self.mesh.extents))
        self.scale = self.get_scale()
        #print(1.0/max(self.mesh.extents))
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)
        self.centroid = self.mesh.centroid
        self.d_centroid_origin = self.get_distance_centroid_origin()

    def normalize_flipping(self):
        I = np.eye(4)
        for i in range(3):
            coords = self.get_vertices()[:,i]
            flip = np.sign(np.sum(np.sign(coords) * (coords ** 2)))
            I[i, i] = flip
        self.apply_transform(I)
        self.flip = self.get_flip()

    def normalize_translation(self):
        # First, we set barycenter on origin.
        transformVector = -self.centroid
        transformMatrix = trimesh.transformations.translation_matrix(transformVector)
        self.apply_transform(transformMatrix)

    def normalize_alignment(self):
        # Calculate covariance and eigenvectors...
        covariance = np.cov(np.transpose(self.get_vertices()))
        eigenvalues, eigenvectors = np.linalg.eig(covariance)

        idx = eigenvalues.argsort()[::-1]
        sorted_eigenvectors = eigenvectors[:,idx]
        sorted_eigenvectors[:, 2] = np.cross(sorted_eigenvectors[:, 0], sorted_eigenvectors[:, 1])
        sorted_eigenvectors = sorted_eigenvectors.T
        sorted_eigenvectors_homo = np.hstack([np.vstack([sorted_eigenvectors, np.array([0,0,0])]), np.array([[0],[0],[0],[1]])])
        self.apply_transform(sorted_eigenvectors_homo)

    def get_n_vertices(self):
        return self.mesh.vertices.shape[0]

    def get_vertices(self):
        return self.mesh.vertices

    def get_faces(self):
        return self.mesh.faces

    def get_n_faces(self):
        return self.mesh.faces.shape[0]


    def export(self, file_path):
        export_mesh(self.mesh, file_path, self.name.split(".")[-1])


    def get_distance_centroid_origin(self):
        return sum(self.centroid * self.centroid) ** 0.5


    def is_normalised(self, verbose=True):
        if self.d_centroid_origin > 1e-3:
            if verbose:
                print("mesh is not centered")
            return False
        if (np.max(self.mesh.extents) - 1) ** 2 > 1e-3:
            if verbose:
                print("mesh is not unit scaled")
                print(np.max(self.mesh.extents))
            return False
        # covariance = np.cov(np.transpose(self.get_vertices()))
        # eigenvalues, eigenvectors = np.linalg.eig(covariance)
        # idx = eigenvalues.argsort()[::-1]
        # sorted_eigenvectors = eigenvectors[:,idx]
        # if np.sum(np.diagonal(sorted_eigenvectors) ** 2) - 3 > 1e-3:
        #     if verbose:
        #         print(self.name + " one of the diagonals is not parallel to axes")
        #         print(sorted_eigenvectors)
        #     return False
        #
        # I = np.eye(4)
        # for i in range(3):
        #     coords = self.get_vertices()[:,i]
        #     flip = np.sign(np.sum(np.sign(coords) * (coords ** 2)))
        #     I[i, i] = flip
        # if not (I == np.eye(4)).any():
        #     return False
        return True


    def get_alignment(self):
        covariance = np.cov(np.transpose(self.get_vertices()))
        eigenvalues, eigenvectors = np.linalg.eig(covariance)
        idx = eigenvalues.argsort()[::-1]
        sorted_eigenvectors = eigenvectors[:,idx]
        return np.absolute(np.diagonal(sorted_eigenvectors))


    def get_scale(self):
        return np.sqrt(np.sum(self.mesh.extents ** 2))


    def get_face_areas_in_bins(self, bins):
        return np.histogram(self.mesh.area_faces, bins)[0]


    def get_flip(self):
        if not self.is_normalised(verbose=False):
            new_mesh = trimesh.base.Trimesh(vertices = self.get_vertices(), faces = self.get_faces())
            transformVector = -new_mesh.centroid
            transformMatrix = trimesh.transformations.translation_matrix(transformVector)
            new_mesh.apply_transform(transformMatrix)
            covariance = np.cov(np.transpose(new_mesh.vertices))
            eigenvalues, eigenvectors = np.linalg.eig(covariance)
            idx = eigenvalues.argsort()[::-1]
            sorted_eigenvectors = eigenvectors[:,idx]
            sorted_eigenvectors[:, 2] = np.cross(sorted_eigenvectors[:, 0], sorted_eigenvectors[:, 1])
            sorted_eigenvectors = sorted_eigenvectors.T
            sorted_eigenvectors_homo = np.hstack([np.vstack([sorted_eigenvectors, np.array([0,0,0])]), np.array([[0],[0],[0],[1]])])
            new_mesh.apply_transform(sorted_eigenvectors_homo)
            new_mesh.apply_scale(1.0 / max(new_mesh.extents))
        else:
            new_mesh = self.mesh

        flips = np.zeros(shape=3)
        for i in range(3):
            coords = new_mesh.vertices[:,i]
            flip = np.sign(np.sum(np.sign(coords) * (coords ** 2)))
            flips[i] = flip
        return flips


    def get_face_areas(self):
        return self.mesh.area_faces


    def fix_mesh(self):
        self.mesh = self.mesh.process(validate=False)
        fill_holes(self.mesh)
        fix_normals(self.mesh, multibody=True)
        #faces = broken_faces(self.mesh)
        #stitch(self.mesh, faces=faces)

    def resample_mesh(self):
        self.subdivide_to_size()
        while self.n_vertices < 1000:
            self.subdivide()
        self.decimation()


    def normalize_mesh(self):
        self.fix_mesh()
        self.normalize_translation()
        self.normalize_alignment()
        self.normalize_scale()
        self.normalize_flipping()

    def save_thumbnail(self):
        # rotation angle chosen based on what looks okayish
        cat = re.split(r'\\|/', self.category)[-1] # god shit fuck i hate developing for both windows and mac
        filepath = "thumbnails" + os.sep + cat + os.sep
        filename = self.name.split('.')[-2] + ".png"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        if os.path.exists(filepath + filename):
            return False # skip meshes that alrdy exist

        angle = 0.25 * np.pi
        rot = trimesh.transformations.rotation_matrix(angle, (1, 0, 0)) # x
        rot = np.dot(rot, trimesh.transformations.rotation_matrix(-0.5 * angle, (0, 1, 0))) # y
        rot = np.dot(rot, trimesh.transformations.rotation_matrix(0.5 * angle, (0, 0, 1))) # z
        self.mesh.apply_transform(rot) # rotating the mesh is way easier since it's at origin
        sc = scene.Scene(geometry=self.mesh)
        sc.camera.resolution = [240,240]
        sc.camera_transform = sc.camera.look_at(self.mesh.vertices, distance = 1.41) # zoom out i think? not sure

        png = sc.save_image(resolution=[240, 240], visible=True)
        with open(filepath + filename, 'wb') as f:
            f.write(png)
            f.close()
        
        return True