import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#print(df)

# df = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# vertices = df['n_vertices']
# vertices = [x for x in vertices if int(float(x))<= 20000]
# plt.hist(vertices, bins=80)
# plt.xlabel('num_vertices')
# plt.ylabel('frequency')
# plt.title("Distribution of number of vertices")

#category histogram
# df2 = df['category'].value_counts().plot(kind ='barh')
# plt.ylabel('category')
# plt.xlabel('frequency')
# plt.title("Distribution by category")

#faces histogram
# faces = df['n_faces']
# faces = [x for x in faces if x <= 20000]
# plt.hist(faces, bins=80)
# plt.xlabel('num_faces')
# plt.ylabel('frequency')
# plt.title("Distribution of number of faces")

#centroid before translation histogram
# df2 = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# centroid_origin = df2['d_centroid_origin']
# plt.hist(centroid_origin[centroid_origin < 2], bins=15)
# plt.xlabel('distance centroid to origin')
# plt.ylabel('frequency')
# plt.title("Translation distribution before normalization")

#scaling distribution before normalization
df3 = pd.read_csv('csv/Princeton_bounding_box.csv')
A = np.array(df3.iloc[:, 1:])
corners = []
for i in range(8):
    corner_xyz = A[:, 3*i : 3*i + 3]
    corners.append(corner_xyz)
    len(corners)
    corners[-1]
    np.linalg.norm([
    [0,0,0],
    [1,1,1]
])**2

euclideanDist = lambda u, v: np.linalg.norm([u, v])

# distance between 2 corners for a given row
def dist(row, i, j):  # i, j are corner-indices
    # construct corner-vectors from indices
    v_i = row[3*i : 3*i + 3]
    v_j = row[3*j : 3*j + 3]

    return euclideanDist(v_i, v_j)

def maxDist(row):
    dists = []
    for i in range(8):
        for j in range(i+1, 8):
            dists.append(dist(row, i, j))

    return max(dists)

maxDist(A[0])
maxDists = [maxDist(row) for row in A]
<<<<<<< HEAD
plt.hist(np.log(maxDists), bins=64)
plt.xlabel('length of diagonal of bounding box')
=======
plt.hist(np.log(maxDists), bins=512)
plt.xlabel('corners')
>>>>>>> 258ddebf455385252fa561087046ca80b8c0d1c5
plt.ylabel('frequency')
plt.title("Scaling distribution before normalization")


plt.show()

#alignment distribution before normalization 



