import csv
import os
from mesh import Mesh

class Dataset:
    def __init__(self,  folder_name_dataset, write_csv=False):
        self.folder_name_dataset = folder_name_dataset
        self.meshes_file_paths = self.get_all_meshes_file_paths()
        self.meshes = self.make_all_meshes()
        if write_csv:
            self.write_csv()


    def write_csv(self):
        with open(os.getcwd() + "/basic_mesh_info.csv", "w") as conn:
            writer = csv.writer(conn)
            writer.writerow(["mesh_name", "category", "n_vertices", "n_faces"])
            for mesh in self.meshes:
                writer.writerow(mesh.basic_mesh_info())


    def __iter__(self):
        return self.meshes


    def to_list(self):
        return list(self.meshes)


    def make_all_meshes(self):
        """ Returns an iterator with all meshes """
        for mesh_file_path in self.meshes_file_paths:

            #with open(mesh_file_path):


            mesh = Mesh(mesh_file_path)
            yield mesh


    def get_all_meshes_file_paths(self):
        """ Returns an iterator with all the file paths to meshes in the Princeton folder """
        shape_dir = os.getcwd() + "/{}/".format(self.folder_name_dataset)
        for folder in os.listdir(shape_dir):
            if not folder.startswith("."):
                for filename in os.listdir(shape_dir + folder):
                    if filename.endswith(".ply") or filename.endswith(".obj") or filename.endswith("off"):
                        file_path = shape_dir + folder + "/" + filename
                        yield file_path


    def get_mesh(self, mesh_name):
        for mesh in self.meshes:
            if mesh.name == mesh_name:
                return mesh
        raise Exception("This mesh was not found.")


    def show_mesh(self, mesh_name):
        found = False
        for mesh_file_path in self.get_all_meshes_file_paths():
            if mesh_file_path.split("/")[-1] == mesh_name:
                found = True
                Mesh(mesh_file_path).show()
        if not found:
            raise Exception("This mesh was not found.")
