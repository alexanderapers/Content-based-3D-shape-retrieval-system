import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

#vertices histogram

# df = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# vertices = df['n_vertices']
# vertices = [x for x in vertices if int(float(x))<= 20000]
# plt.hist(vertices, bins=80)
# plt.xlabel('number_of_vertices')
# plt.ylabel('frequency')
# plt.title("Distribution of number of vertices before normalization")
# plt.savefig("resample_plots/num_vertices")
# plt.show()


#category histogram
# df = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# df2 = df['category'].value_counts().plot(kind ='barh')
# plt.ylabel('category')
# plt.xlabel('frequency')
# plt.title("Distribution by category")
# plt.savefig("resample_plots/categories")
# plt.show()

#faces histogram before
df = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
faces = df['n_faces']
faces = [x for x in faces if x <= 20000]
plt.hist(faces, bins=80)
plt.xlabel('number_of_faces')
plt.ylabel('frequency')
plt.title("Distribution of number of faces before normalization")
plt.savefig("resample_plots/num_faces")
plt.show()


#centroid before translation histogram
# df2 = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# centroid_origin = df2['d_centroid_origin']
# plt.hist(centroid_origin[centroid_origin < 2], bins=15)
# plt.xlabel('distance centroid to origin')
# plt.ylabel('frequency')
# plt.title("Translation distribution before normalization")
# plt.savefig("resample_plots/translation_before")
# plt.show()

#scaling distribution before normalization
# df3 = pd.read_csv('csv/Princeton_bounding_box.csv')
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
# plt.hist(np.log(maxDists), bins=64)
# plt.xlim(xmin = 0, xmax = 2)
# plt.xlabel('length of diagonal of bounding box')
# plt.ylabel('frequency')
# plt.title("Scaling distribution before normalization")
# plt.savefig("resample_plots/scaling_before")
# plt.show()



#alignment distribution before normalization 
# csv_name ="./csv/Princeton_alignment.csv"
# csv_file_name = csv_name.split("/")[-1]
# #print('File Name:', csv_name.split("\\")[-1])
# print(csv_file_name)
# df = pd.read_csv(csv_name)
# df_raw =df
# #data_dict = df_raw.to_dict()
# plt_name = csv_file_name.split('.')[:1]
# plt_name = str(plt_name[0])

# fontsize =12
# df_raw.hist(column=['alignment_x'])
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("|$e_1$ * x|")
# plt.savefig("resample_plots/alignment_x_before")

# df_raw.hist(column=['alignment_y'])
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("|$e_2$ * y|")
# plt.savefig("resample_plots/alignment_y_before")

# df_raw.hist(column=['alignment_z'])
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("|$e_3$ * z|")
# plt.savefig("resample_plots/alignment_z_before")
# plt.show()