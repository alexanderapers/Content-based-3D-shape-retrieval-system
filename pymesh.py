import os
import trimesh
import random

# set paths to folder containing 3D shapes
psb_path = "Models/"
turtle = os.listdir(psb_path)

# use trimesh to load and display 3D meshes
turtle_mesh = trimesh.load(psb_path + turtle[0] )
turtle_mesh.show()