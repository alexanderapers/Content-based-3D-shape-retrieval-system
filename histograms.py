import pandas as pd
import matplotlib.pyplot as plt

#print(df)

# df = pd.read_csv('basic_mesh_info.csv')
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
df2 = pd.read_csv('Princeton_normalized_basic_mesh_info.csv')
centroid_origin = df2['d_centroid_origin']
plt.hist(centroid_origin[centroid_origin < 2], bins=15)
plt.xlabel('distance centroid to origin')
plt.ylabel('frequency')
plt.title("Translation distribution before normalization")


plt.show()



