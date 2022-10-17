import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fontsize =12
from matplotlib import ft2font


#vertices histogram after

# df = pd.read_csv('csv/Princeton_remeshed_normalized_basic_mesh_info.csv')
# vertices = df['n_vertices']
# plt.clf()
# plt.hist(vertices, color='plum', bins = 80)
# plt.xlabel('number_of_vertices')
# plt.ylabel('frequency')
# plt.title("Distribution of number of vertices after normalization")
# plt.xlim(xmin = 0, xmax = 20000)
# plt.savefig("resample_plots/normalized_vertices")
# plt.show()

#faces histogram after
# df = pd.read_csv('csv/Princeton_remeshed_normalized_basic_mesh_info.csv')
# faces = df['n_faces']
# plt.hist(faces, color='plum')
# plt.xlabel('number_of_faces')
# plt.ylabel('frequency')
# plt.title("Distribution of number of faces after normalization")
# plt.xlim(xmin = 0, xmax = 20000)
# plt.savefig("resample_plots/normalized_faces")
# plt.show()


#centroid after translation histogram
#axis is very small here because of centralised data (mention in report)

# df = pd.read_csv('csv/Princeton_remeshed_normalized_basic_mesh_info.csv')
# centroid_origin = df['d_centroid_origin']
# plt.hist(centroid_origin, range=[0,1.1], bins = 100, color='plum')#range =[0.000000003, 0.00000001], bins = 15, color='plum')
# plt.xlabel('distance centroid to origin')
# plt.ylabel('frequency')
# plt.title("Translation distribution after normalization")
# #plt.xlim(xmin = 0.00000000003, xmax = 0.)
# #print(centroid_origin)
# plt.savefig("resample_plots/translation_after")
# plt.show()


#alignment after distribution
# csv_name ="./csv/Princeton_remeshed_normalized_alignment.csv"
# csv_file_name = csv_name.split("/")[-1]
# #print('File Name:', csv_name.split("\\")[-1])
# print(csv_name)
# df = pd.read_csv(csv_name)
# #plt_histogram(df,csv_file_name)
# df_raw =df
# #data_dict = df_raw.to_dict()
# plt_name = csv_file_name.split('.')[:1]
# plt_name = str(plt_name[0])
# #
# fontsize =12
# df_raw.hist(column=['alignment_x'], bins=100, color='plum', range = [0,1])
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("$|e_1 \cdot x|$")
# plt.savefig("resample_plots/alignment_x_after")

# df_raw.hist(column=['alignment_y'], bins=100, color='plum', range = [0,1] )
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("$|e_2 \cdot y|$")
# plt.savefig("resample_plots/alignment_y_after")

# df_raw.hist(column=['alignment_z'], bins=100, color='plum', range = [0,1])
# plt.suptitle(plt_name, fontsize=fontsize)
# plt.ylabel("frequency")
# plt.xlabel("$|e_3 \cdot z|$")
# plt.savefig("resample_plots/alignment_z_after")
# plt.show()


#scaling distribution after normalization
csv_name ="./csv/Princeton_remeshed_normalized_basic_mesh_info.csv"
plt_name = "scale after normalization"
df = pd.read_csv(csv_name)
df.hist(column=["scale"], color='plum')
plt.xlim([1, 5])
plt.suptitle(plt_name, fontsize=fontsize)
plt.ylabel("frequency")
plt.xlabel("average value to tightly fit unit cube ")
plt.savefig("resample_plots/scaling_after")
plt.show()


#flipping distribution after normalization
csv_name ="./csv/Princeton_remeshed_normalized_flipping.csv"
plt_name = "Flipping distribution before normalization"
plt.figure(2)
df = pd.read_csv(csv_name)
cx = df['flip_x'].value_counts()[1]
cy = df['flip_y'].value_counts()[1]
cz = df['flip_z'].value_counts()[1]
print(cx,cy,cz)
data = {'flip_x': cx, 'flip_y': cy, 'flip_z': cz}
df = pd.Series(data)
plt.bar(range(len(df)), df.values, align='center', color='plum')
plt.xticks(range(len(df)), df.index.values, size='small')
plt.suptitle(plt_name, fontsize=fontsize)
plt.ylabel("frequency")
plt.xlabel("number of correct flips in each dimension")
plt.savefig("resample_plots/flipping_after")
plt.show()
