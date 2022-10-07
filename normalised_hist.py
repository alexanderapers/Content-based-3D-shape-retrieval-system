import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Princeton_normalized_basic_mesh_info.csv')


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
centroid_origin = df['d_centroid_origin']
plt.hist(centroid_origin, bins=10)
plt.xlabel('distance centroid to origin')
plt.ylabel('frequency')

plt.title("Translation distribution after normalization")

#print(centroid_origin)


plt.show()