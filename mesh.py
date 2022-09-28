import trimesh

class Mesh:
    def __init__(self, mesh_file_path):
        self.mesh_file_path = mesh_file_path
        self.name = mesh_file_path.split("/")[-1]
        self.category = mesh_file_path.split("/")[-2]
        self.mesh = trimesh.load(mesh_file_path)
        self.n_vertices = self.mesh.vertices.shape[0]
        self.n_faces = self.mesh.faces.shape[0]


    def show(self):
        self.mesh.show()


    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.category, self.n_vertices, self.n_faces)


    def basic_mesh_info(self):
        return [self.name, self.category, self.n_vertices, self.n_faces]
