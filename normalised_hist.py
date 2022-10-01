import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Princeton_normalized_basic_mesh_info.csv')

vertices = df['n_vertices']
plt.hist(vertices, bins=100)
plt.xlabel('num_vertices')
plt.ylabel('frequency')
plt.title("Distribution of number of vertices")

# faces = df['n_faces']
# plt.hist(faces, bins=100)
# plt.xlabel('num_faces')
# plt.ylabel('frequency')
# plt.title("Distribution of number of faces")


plt.show()