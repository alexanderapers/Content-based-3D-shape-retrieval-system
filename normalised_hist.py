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


#centroid before translation histogram
centroid_origin = df['d_centroid_origin']
plt.hist(centroid_origin[centroid_origin < 2], bins=15)
plt.xlabel('distance cebtroid to origin')
plt.ylabel('frequency')
#plt.xlim(xmin=0, xmax = 1)
#plt.ylim(ymin=1, ymax = 0)
plt.title("Translation distribution before normalization")

#print(centroid_origin)


plt.show()