import glob
import os
import numpy as np

# HOW TO USE: copy to the Princeton(_remeshed(_normalized)) folder you want to reorder and just run the script!
# DO NOT MOVE princeton_labels.txt!

# currentdir = os.getcwd()
# parentdir = os.path.dirname(currentdir)
#
# print("Starting file relabeling!")
# with open(parentdir + "/princeton_labels.txt") as f:
#     lines = f.readlines()
#
#     for line in lines:
#         args = line.split(' ')
#
#         label = args[0]
#         start = int(args[1])
#         end = int(args[2])
#
#         print("------------------------\nCATEGORY: " + label)
#         folder = currentdir + "/" + label
#         if os.path.exists(folder):
#             print("Folder " + folder + " already exists!")
#         else:
#             print("Making folder " + folder)
#             os.makedirs(folder)
#
#         numMeshes = end + 1 - start
#         moved = 0
#         skipped = 0
#
#         for i in range(start, end+1):
#             filename = "m" + str(i) + ".ply"
#             path = glob.glob(currentdir + "/**/" + filename)
#
#             # safeguard thing: make sure there's no deletions or duplicates
#             # tbh not quite sure what to do if there are any but at least you'll know
#             if len(path) == 0 or len(path) > 1:
#                 if(len(path) == 0):
#                     print("Mesh " + filename + " not found!")
#                 else:
#                     print("Mesh " + filename + " has " + len(path) + " copies!")
#                 input()
#                 quit()
#
#             oldpath = os.path.normpath(path[0])
#
#             newpath = os.path.normpath(folder + "/" + filename)
#
#             if oldpath == newpath:
#                 skipped += 1
#             else:
#                 os.rename(oldpath, newpath)
#                 moved += 1
#
#         print("Moved " + str(moved) + "/" + str(numMeshes) + " meshes. " + str(skipped) + " were in the correct category.")
#
# print("\n----------------\nMove completed. Attempting to remove empty folders...")
# emptydirs = list()
# for (dirpath, dirnames, filenames) in os.walk(currentdir):
#     if len(dirnames) == 0 and len(filenames) == 0:
#         emptydirs.append(dirpath)
# if len(emptydirs) > 0:
#     for dir in emptydirs:
#         print("Removing empty directory " + dir)
#         os.rmdir(dir)
# else:
#     print("No empty directories found. Why did you run this script if this directory is already sorted?")
#
# print("\n----------------\nDone! Press ENTER to exit.")
# input()

def make_category_shapes_dict():
    with open("princeton_labels_numbered.txt") as f:
        lines = f.readlines()
        reorder = dict()
        for line in lines:
            args = line.split(' ')

            label = args[0]
            start = int(args[1])
            end = int(args[2])
            reorder[label] = [start, end]
        return reorder


def reorder_dataset(dataset):
    reorder = self.make_category_shapes_dict()

    currentdir = os.getcwd()
    dataset_dir = currentdir + "/" + dataset.folder_name_dataset

    for label in reorder:
        if not os.path.exists(dataset_dir + "/" + label):
            os.mkdir(dataset_dir + "/" + label)

    for file_path in dataset.get_all_meshes_file_paths():
        mesh_number = int(file_path.split("/")[-1].split(".")[0][1:])
        for label in reorder:
            if mesh_number >= reorder[label][0] and mesh_number <= reorder[label][1]:
                new_file_path = dataset_dir + "/" + label + "/m" + str(mesh_number) + ".ply"
                os.rename(file_path, new_file_path)
