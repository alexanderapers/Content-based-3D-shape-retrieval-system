#import csv
import os
from os.path import join
#import sys
from mesh import Mesh
import trimesh
from dataset import Dataset

# # -> just drag the mesh info csv onto this file to make it do things
# csvfilepath = sys.argv[1]
#

#
# # safety reasons
# overwriteSave = False
# if (input("Overwrite when saving? Y/N ") or "n") == "y":
#     overwriteSave = True
#
# print(overwriteSave)
#

def resample(dataset):
    new_name = dataset.folder_name_dataset + "_normalized"
    if not os.path.exists(new_name):
        os.mkdir(new_name)
        # Default values chosen semi-arbitrarily. Can be changed at program startup or if our remeshing isn't well-liked.
        #minVerts = int(input("Please specify a minimum vertex goal: ") or "3000")
        #minFaces = int(input("Please specify a minimum faces goal: ") or "4800")

        for mesh in dataset:
            mesh.subdivide_to_size()
            while mesh.n_vertices < 1000:
                mesh.subdivide()
            mesh.decimation()
            # if mesh.n_vertices <= minVerts or mesh.n_faces <= minFaces:
            #     #print("Outlier found:", mesh.name)
            #     while mesh.n_vertices < minVerts or mesh.n_faces < minFaces:
            #         mesh.subdivide()
            #
            # if mesh.n_vertices >= 5000 or mesh.n_faces >= 8000:
            #     mesh.decimation()

            print("Mesh remeshed! New # of vertices: " + str(mesh.n_vertices) + ", faces: " + str(mesh.n_faces))

            if not os.path.exists(join(new_name, mesh.category)):
                os.mkdir(join(new_name, mesh.category))

            mesh.export(join(join(new_name, mesh.category), mesh.name))
#
# with open(csvfilepath, newline='') as csvfile:
#     reader = csv.reader(csvfile)
#
#     for row in reader:
#
#         if row[0] == "mesh_name":
#             continue
#
#         if int(row[2]) <= 100 or int(row[3]) <= 100:
#             iterator += 1
#             print("Outlier found: " + ', '.join(row))
#
#             # find mesh in folder
#             meshfile = row[0]
#             for root, dir, files in os.walk("Princeton\\"):
#                 if meshfile in files:
#                     mesh_file_path = os.path.join(root, meshfile)
#
#             # load mesh and do magic to it
#             mesh = trimesh.load(mesh_file_path)
#             while mesh.vertices.shape[0] < minVerts or mesh.faces.shape[0] < minFaces:
#                 mesh = mesh.subdivide()
#
#             # mmmm printing
#             print("Mesh subdivided! New # of vertices: " + str(mesh.vertices.shape[0]) + ", faces: " + str(mesh.faces.shape[0]))
#
#             # don't overwrite shit unless you're 100% sure
#             if not overwriteSave:
#                 meshfile = "[SUBDIVIDED]" + meshfile
#
#             outputPath = os.path.join(root, meshfile)
#
#             export.export_mesh(mesh, outputPath, "ply")
#             print("Mesh exported to " + outputPath)
#
# print("Done!\n" + str(iterator) + " meshes resampled.")
# input()
