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


def get_info_meshes():
    with open("basic_mesh_info.txt", "w") as conn:
        conn.write("mesh_name class n_vertices n_faces\n")
        for mesh_file_path in get_all_meshes():
            name = mesh_file_path.split("/")[-1]
            c = mesh_file_path.split("/")[-2]
            mesh = trimesh.load(mesh_file_path)
            n_vertices = mesh.vertices.shape[0]
            n_faces = mesh.faces.shape[0]
            if mesh.faces.shape[1] != 3:
                print("We have some non-triangular meshes")

            conn.write("{0} {1} {2} {3}\n".format(name, c, n_vertices, n_faces))


if __name__ == "__main__":
    # to write basic mesh info to a txt file
    #get_info_meshes()

    if len(sys.argv) == 2:
        show_mesh(sys.argv[1])
    else:
        show_mesh("m0.ply")
