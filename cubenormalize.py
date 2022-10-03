import os
from os.path import join
from mesh import Mesh
import trimesh
from dataset import Dataset

def normalize(dataset):
    for mesh in dataset:
        # first scale the mesh into a unit cube
        mesh.normalize_scale()

        # create transform matrix to set barycenter on origin
        transformVector = -mesh.centroid
        transformMatrix = trimesh.transformations.translation_matrix(transformVector)
        mesh.apply_transform(transformMatrix)

        path = dataset.folder_name_dataset
        if not os.path.exists(join(path, mesh.category)):
            os.mkdir(join(path, mesh.category))

        mesh.export(join(join(path, mesh.category), mesh.name))

    print("Done normalising meshes!")
    input()
