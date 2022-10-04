import os
from os.path import join
from mesh import Mesh
import trimesh
from dataset import Dataset
import numpy as np

def normalize(dataset):
    for mesh in dataset:
        #if mesh.name != "m14.ply":
        #    continue

        mesh.show()

        # first, align the oriented bounding box to the axis
        alignTransform, postExtent = mesh.bounding_box_oriented 
        # this property actually doesn't return the oriented bounding box, but rather a transform matrix to transform the oriented bounding box to axis aligned
        # (and the dimensions of the oriented bounding box which we don't really need as the mesh will contain that anyway after transforming)
        # which makes it a fucking shit name for a property but actually surprisingly easy to use
        mesh.apply_transform(alignTransform)

        print(mesh.bounding_box_oriented)

        # postExtent contains the eigenvalue of each axis, so we need to sort them to get the desired new axes
        newXindex = int(np.where(postExtent == max(postExtent))[0][0]) #oh my god this feels illegal
        newZindex = int(np.where(postExtent == min(postExtent))[0][0])
        newYindex = 3 - (newXindex + newZindex) # sum of indices is 3
        
        axisTransform = trimesh.transformations.translation_matrix([0,0,0]) # empty translation matrix
        axisTransform[:, [0,1,2]] = axisTransform[:, [newXindex,newYindex,newZindex]] # swap old axes to new axes
        mesh.apply_transform(axisTransform)
        # why do the eigenvalues in the oriented bounding box not change after this rotation oh god oh fuck did i do something wrong?

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
        print(mesh.bounding_box_oriented)
        mesh.show()

        return
        #mesh.export(join(join(path, mesh.category), mesh.name))

    print("Done normalising meshes!")
    input()
