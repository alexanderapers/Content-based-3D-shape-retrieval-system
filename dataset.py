import csv
import os
from mesh import Mesh
import numpy as np

class Dataset:
    def __init__(self, folder_name_dataset, write_basic_csv=False, write_other_csv=False):
        self.folder_name_dataset = folder_name_dataset
        #self.meshes_file_paths = self.get_all_meshes_file_paths()
        #self.meshes = self.make_all_meshes()
        if write_basic_csv:
            self.write_basic_info_csv()
        if write_other_csv:
            self.write_bounding_box_csv()
            self.write_alignment_csv()


    def write_basic_info_csv(self):
        with open(os.getcwd() + "/csv/" + self.folder_name_dataset + "_basic_mesh_info.csv", "w") as conn:
            writer = csv.writer(conn)
            writer.writerow(["mesh_name", "category", "n_vertices", "n_faces", "d_centroid_origin"])
            for mesh in self.make_all_meshes():
                writer.writerow(mesh.basic_mesh_info())


    def write_bounding_box_csv(self):
        with open(os.getcwd() + "/csv/" + self.folder_name_dataset + "_bounding_box.csv", "w") as conn:
            writer = csv.writer(conn)
            writer.writerow(["mesh name"] + ["corner{0}{1}".format(i, j) for i in range(1,9) for j in ["x", "y", "z"]])
            for mesh in self.make_all_meshes():
                writer.writerow([mesh.name] + list(mesh.get_AABB().flatten()))


    def write_alignment_csv(self):
        with open(os.getcwd() + "/csv/" + self.folder_name_dataset + "_alignment.csv", "w") as conn:
            writer = csv.writer(conn)
            writer.writerow(["mesh name", "alignment_x", "alignment_y", "alignment_y"])
            for mesh in self.make_all_meshes():
                writer.writerow([mesh.name] + list(mesh.get_alignment()))


    def write_face_area_csv(self):
        with open(os.getcwd() + "/csv/" + self.folder_name_dataset + "_face_area.csv", "w") as conn:
            writer = csv.writer(conn)
            writer.writerow(["mesh name", "face", "area"])
            for mesh in self.make_all_meshes():
                for i, face_area in enumerate(mesh.get_face_areas()):
                    writer.writerow([mesh.name, i, face_area])


    def get_face_areas_in_bins(self, bins):
        A = np.zeros(shape = len(bins)-1)
        for mesh in self.make_all_meshes():
            A += mesh.get_face_areas_in_bins(bins)
        return A / np.sum(A)


    def __iter__(self):
        #return self.meshes
        return self.make_all_meshes()


    def __len__(self):
        return len(list(self.get_all_meshes_file_paths()))


    def to_list(self):
        return list(self.make_all_meshes())


    def make_all_meshes(self):
        """ Returns an iterator with all meshes """
        for mesh_file_path in self.get_all_meshes_file_paths():
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
        for mesh in self.make_all_meshes:
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


    def is_normalised(self):
        for mesh in self.make_all_meshes():
            if not mesh.is_normalised():
                return False
        return True
