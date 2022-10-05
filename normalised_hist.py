import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Princeton_normalized_basic_mesh_info.csv')


#vertices histogram
# vertices = df['n_vertices']
# plt.hist(vertices, bins=100)
# plt.xlabel('num_vertices')
# plt.ylabel('frequency')
# plt.title("Distribution of number of vertices")

#vertices histogram
# faces = df['n_faces']
# plt.hist(faces, bins=100)
# plt.xlabel('num_faces')
# plt.ylabel('frequency')
# plt.title("Distribution of number of faces")


#translation before histogram
centroid_origin = df['d_centroid_origin']
plt.hist(centroid_origin, bins=10)
plt.xlabel('translation')
plt.ylabel('frequency')
plt.title("Translation distribution before normalization")

plt.show()