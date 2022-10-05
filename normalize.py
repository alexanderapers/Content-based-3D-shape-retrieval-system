import os
from os.path import join
import random
from mesh import Mesh
import trimesh
from dataset import Dataset
import numpy as np

def normalize(dataset, debug=False):
    progress = 0
    for mesh in dataset:
        os.system('clear')
        os.system('cls')
        print("Progress: " + str(progress).rjust(5) + "/1814 (" + str(int(progress/1814 * 100)).rjust(3) + "%)")
        progress += 1

        show_interims = False
        if random.randint(0,100) == 0 and debug:
            show_interims = True
            mesh.show()

        print(mesh.name)

        print("Original centroid: " + str(mesh.centroid))
        # First, we set barycenter on origin.
        transformVector = -mesh.centroid
        transformMatrix = trimesh.transformations.translation_matrix(transformVector)
        mesh.apply_transform(transformMatrix)
        print("New centroid:      " + str(mesh.centroid))

        # Calculate covariance and eigenvectors...
        covariance = np.cov(np.transpose(mesh.get_vertices()))
        eigenvalues, eigenvectors = np.linalg.eig(covariance)
        
        # Determine which eigenvector is largest...
        newXindex = int(np.where(eigenvalues == max(eigenvalues))[0][0]) #oh my god this feels illegal
        newZindex = int(np.where(eigenvalues == min(eigenvalues))[0][0])
        newYindex = 3 - (newXindex + newZindex) # sum of indices is 3

        # construct third vector by cross product of x and y...
        thirdVector = np.cross(eigenvectors[:,newXindex], eigenvectors[:,newYindex])

        # put them in an array...
        ordered_eigenvectors = [eigenvectors[:,newXindex], eigenvectors[:,newYindex], thirdVector]

        # and transform!
        mesh.transform_vertices(ordered_eigenvectors)

        # now that the mesh is centered on origin and aligned, we can scale it such that its max diameter is 1.
        mesh.normalize_scale()

        print("Bounding box after alignment and scaling:\n" + str(mesh.get_AABB()))

        if show_interims:
            print("==> eigenvalues for (x, y, z)")
            print(eigenvalues)
            print("\n==> eigenvectors")
            print(eigenvectors)
            print("Order: " + str([newXindex, newYindex, newZindex]))
            print(ordered_eigenvectors)
            mesh.show()

        if not os.path.exists(join(dataset.folder_name_dataset, mesh.category)):
            os.mkdir(join(dataset.folder_name_dataset, mesh.category))

        print("Exporting to " + join(join(dataset.folder_name_dataset, mesh.category), mesh.name))
        mesh.export(join(join(dataset.folder_name_dataset, mesh.category), mesh.name))

    print("Done normalising meshes! Press ENTER to continue.")
    input()
