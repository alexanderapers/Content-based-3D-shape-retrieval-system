import os
import trimesh
import sys

def show_mesh(mesh_name):
    for mesh_file_path in get_all_meshes():
        if mesh_file_path.split("/")[-1] == mesh_name:
            mesh = trimesh.load(mesh_file_path)
            mesh.show()


def get_all_meshes():
    """ Returns an iterator with all the file paths to meshes in the Princeton folder """
    shape_dir = os.getcwd() + "/Princeton/"
    for folder in os.listdir(shape_dir):
        if not folder.startswith("."):
            for filename in os.listdir(shape_dir + folder):
                if filename.endswith(".ply"):
                    file_path = shape_dir + folder + "/" + filename
                    yield file_path


if __name__ == "__main__":

    if len(sys.argv) == 2:
        show_mesh(sys.argv[1])
    else:
        show_mesh("m0.ply")
