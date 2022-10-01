import trimesh
from trimesh.exchange.export import export_mesh

class Mesh:
    def __init__(self, mesh_file_path):
        self.mesh_file_path = mesh_file_path
        self.name = mesh_file_path.split("/")[-1]
        self.category = mesh_file_path.split("/")[-2]
        self.mesh = trimesh.load(mesh_file_path)
        self.n_vertices = self.get_n_vertices()
        self.n_faces = self.get_n_faces()
        self.bounding_box = trimesh.bounds.corners(self.mesh.bounds)


    def show(self):
        self.mesh.show()


    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.category, self.n_vertices, self.n_faces)


    def basic_mesh_info(self):
        return [self.name, self.category, self.n_vertices, self.n_faces]


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


    def get_n_vertices(self):
        return self.mesh.vertices.shape[0]


    def get_n_faces(self):
        return self.mesh.faces.shape[0]


    def export(self, file_path):
        export_mesh(self.mesh, file_path, self.name.split(".")[-1])
