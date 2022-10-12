import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('csv/Princeton_normalized_basic_mesh_info.csv')


#vertices histogram
# vertices = df['n_vertices']
# plt.hist(vertices, bins=100)
# plt.xlabel('num_vertices')
# plt.ylabel('frequency')
# plt.title("Distribution of number of vertices")

#faces histogram
# faces = df['n_faces']
# plt.hist(faces, bins=100)
# plt.xlabel('num_faces')
# plt.ylabel('frequency')
# plt.title("Distribution of number of faces")

#centroid after translation histogram
# centroid_origin = df['d_centroid_origin']
# plt.hist(centroid_origin, bins=15)
# plt.xlabel('distance centroid to origin')
# plt.ylabel('frequency')

# plt.title("Translation distribution after normalization")

# print(centroid_origin)

#scaling distribution after normalization
# df3 = pd.read_csv('csv/Princeton_normalized_bounding_box.csv')
# A = np.array(df3.iloc[:, 1:])
# corners = []
# for i in range(8):
#     corner_xyz = A[:, 3*i : 3*i + 3]
#     corners.append(corner_xyz)
#     len(corners)
#     corners[-1]
#     np.linalg.norm([
#     [0,0,0],
#     [1,1,1]
# ])**2

# euclideanDist = lambda u, v: np.linalg.norm([u, v])

# # distance between 2 corners for a given row
# def dist(row, i, j):  # i, j are corner-indices
#     # construct corner-vectors from indices
#     v_i = row[3*i : 3*i + 3]
#     v_j = row[3*j : 3*j + 3]

#     return euclideanDist(v_i, v_j)

# def maxDist(row):
#     dists = []
#     for i in range(8):
#         for j in range(i+1, 8):
#             dists.append(dist(row, i, j))

#     return max(dists)

# maxDist(A[0])
# maxDists = [maxDist(row) for row in A]
# plt.hist(maxDists, bins=64) ;
# plt.xlabel('length of diagonal of bounding box')
# plt.ylabel('frequency')
# plt.title("Scaling distribution after normalization")

# plt.show()

#alignment after distribution 
csv_name ="./csv/Princeton_normalized_alignment.csv"
csv_file_name = csv_name.split("/")[-1]
#print('File Name:', csv_name.split("\\")[-1])
print(csv_name)
df = pd.read_csv(csv_name)
#plt_histogram(df,csv_file_name)
df_raw =df
#data_dict = df_raw.to_dict()
plt_name = csv_file_name.split('.')[:1]
plt_name = str(plt_name[0])

fontsize =12
df_raw.hist(column=['alignment_x'])
plt.suptitle(plt_name, fontsize=fontsize)
plt.ylabel("frequency")
plt.xlabel(" x = [1,0,0]")

df_raw.hist(column=['alignment_y'])
plt.suptitle(plt_name, fontsize=fontsize)
plt.ylabel("frequency")
plt.xlabel("y = [0,1,0]")

df_raw.hist(column=['alignment_z'])
plt.suptitle(plt_name, fontsize=fontsize)
plt.ylabel("frequency")
plt.xlabel("z =  [0,0,1]")
plt.show()