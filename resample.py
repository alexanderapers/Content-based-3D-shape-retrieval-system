import csv
import os
import sys
from mesh import Mesh
import trimesh
from trimesh.exchange import export

# -> just drag the mesh info csv onto this file to make it do things
csvfilepath = sys.argv[1]

# Default values chosen semi-arbitrarily. Can be changed at program startup or if our remeshing isn't well-liked.
minVerts = int(input("Please specify a minimum vertex goal: ") or "1000") 
minFaces = int(input("Please specify a minimum faces goal: ") or "1600")

# safety reasons
overwriteSave = False
if (input("Overwrite when saving? Y/N ") or "n") == "y":
    overwriteSave = True

print(overwriteSave)

iterator = 0

with open(csvfilepath, newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
    
        if row[0] == "mesh_name":
            continue

        if int(row[2]) <= 100 or int(row[3]) <= 100:
            iterator += 1
            print("Outlier found: " + ', '.join(row))

            # find mesh in folder
            meshfile = row[0]
            for root, dir, files in os.walk("Princeton\\"):
                if meshfile in files:
                    mesh_file_path = os.path.join(root, meshfile)

            # load mesh and do magic to it
            mesh = trimesh.load(mesh_file_path)
            while mesh.vertices.shape[0] < minVerts or mesh.faces.shape[0] < minFaces:
                mesh = mesh.subdivide()
                
            # mmmm printing
            print("Mesh subdivided! New # of vertices: " + str(mesh.vertices.shape[0]) + ", faces: " + str(mesh.faces.shape[0]))

            # don't overwrite shit unless you're 100% sure
            if not overwriteSave:
                meshfile = "[SUBDIVIDED]" + meshfile

            outputPath = os.path.join(root, meshfile)

            export.export_mesh(mesh, outputPath, "ply")
            print("Mesh exported to " + outputPath)

print("Done!\n" + str(iterator) + " meshes resampled.")
input()