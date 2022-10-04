import os
from os.path import join
from mesh import Mesh
import trimesh
from dataset import Dataset

def normalize(dataset):
    for mesh in dataset:

        mesh.show()

        # first, align the oriented bounding box to the axis
        alignTransform, postExtent = mesh.bounding_box_oriented 
        # this property actually doesn't return the oriented bounding box, but rather a transform matrix to transform the oriented bounding box to axis aligned
        # (and the dimensions of the oriented bounding box which we don't really need as the mesh will contain that anyway after transforming)
        # which makes it a fucking shit name for a property but actually surprisingly easy to use
        mesh.apply_transform(alignTransform)

        # then, scale the mesh into a unit cube
        mesh.normalize_scale()

        # # create transform matrix to set barycenter on origin
        transformVector = -mesh.centroid
        transformMatrix = trimesh.transformations.translation_matrix(transformVector)
        mesh.apply_transform(transformMatrix)

        path = dataset.folder_name_dataset
        if not os.path.exists(join(path, mesh.category)):
            os.mkdir(join(path, mesh.category))
        
        print(mesh.bounding_box)
        print(mesh.centroid)
        print(mesh.bounding_box_oriented)

        mesh.show()
        return
        #mesh.export(join(join(path, mesh.category), mesh.name))

    print("Done normalising meshes!")
    input()
