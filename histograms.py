import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

fontsize =12


#vertices histogram

#df = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# vertices = df['n_vertices']
# vertices = [x for x in vertices if int(float(x))<= 20000]
# plt.hist(vertices,color='plum', bins=80)
# plt.xlabel('number_of_vertices')
# plt.ylabel('frequency')
# plt.title("Distribution of number of vertices before normalization")
# plt.savefig("resample_plots/num_vertices")
# plt.show()


#category histogram
# df = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# df2 = df['category'].value_counts().plot(kind ='barh', color='plum')
# plt.ylabel('category')
# plt.xlabel('frequency')
# plt.title("Distribution by category")
# plt.savefig("resample_plots/categories")
# plt.show()

#faces histogram before
# df = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# faces = df['n_faces']
# faces = [x for x in faces if x <= 20000]
# plt.hist(faces, color='plum', bins=80)
# plt.xlabel('number_of_faces')
# plt.ylabel('frequency')
# plt.title("Distribution of number of faces before normalization")
# plt.savefig("resample_plots/num_faces")
# plt.show()


#centroid before translation histogram
# df2 = pd.read_csv('csv/Princeton_basic_mesh_info.csv')
# centroid_origin = df2['d_centroid_origin']
# plt.hist(centroid_origin[centroid_origin < 2], color='plum', bins=100)
# plt.xlabel('distance centroid to origin')
# plt.ylabel('frequency')
# plt.title("Translation distribution before normalization")
# plt.savefig("resample_plots/translation_before")
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
#
# fontsize =12
# df_raw.hist(column=['alignment_x'], bins=100, color='plum')
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("$|e_1 \cdot x|$")
# plt.savefig("resample_plots/alignment_x_before")

# df_raw.hist(column=['alignment_y'], bins=100, color='plum')
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("$|e_2 \cdot y|$")
# plt.savefig("resample_plots/alignment_y_before")

# df_raw.hist(column=['alignment_z'], bins=100, color='plum')
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("$|e_3 \cdot z|$")
# plt.savefig("resample_plots/alignment_z_before")
#plt.show()

#scaling distribution before normalization
csv_name ="./csv/Princeton_basic_mesh_info.csv"
plt_name = "scale before normalization"
df = pd.read_csv(csv_name)
plt.hist(df["scale"][df["scale"] < 5], color='plum', bins=np.arange(0, 3, 0.05))
plt.suptitle(plt_name, fontsize=fontsize)
plt.xlim([0, 3])
#plt.ylim([0, 220])
#plt.axis([xmin, xmax, ymin, ymax])
plt.ylabel("frequency")
plt.xlabel("length of diagonal box of the axis aligned bounding box")
plt.savefig("resample_plots/scaling_before")
plt.show()



# #flipping
# csv_name ="./csv/Princeton_flipping.csv"
# plt_name = "Flipping distribution before normalization"
# df = pd.read_csv(csv_name)
# cx = df['flip_x'].value_counts()[1]
# cy = df['flip_y'].value_counts()[1]
# cz = df['flip_z'].value_counts()[1]
# print(cx,cy,cz)
# data = {'flip_x': cx, 'flip_y': cy, 'flip_z': cz}
# df = pd.Series(data)
# plt.bar(range(len(df)), df.values, align='center', color='plum', width = 0.3)
# plt.xticks(range(len(df)), df.index.values, size='small')
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylim([0, 1814])
# plt.ylabel("frequency")
# plt.xlabel("number of meshes with correct orientation in each dimension")
# plt.savefig("resample_plots/flipping_before")
# plt.show()
