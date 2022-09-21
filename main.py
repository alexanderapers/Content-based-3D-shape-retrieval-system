import os
import trimesh
import random

if __name__ == "__main__":
    # set paths to folder containing 3D shapes

    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".obj"):
            # use trimesh to load and display 3D meshes
            turtle_mesh = trimesh.load(filename)
            turtle_mesh.show()
