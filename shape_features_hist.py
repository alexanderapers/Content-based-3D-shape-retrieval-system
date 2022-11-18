import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#histograms for vector features

#setting up
df = pd.read_csv('features/Princeton_remeshed_normalized_shape_features.csv')
with open('princeton_labels.txt') as file:
    categories = file.read().splitlines()

a3_labels = ['A3_1']
d1_labels = ['D1_1']
d2_labels = ['D2_1']
d3_labels = ['D3_1']
d4_labels = ['D4_1']
for i in range(2, 11):
    a3_labels.append('A3_' + str(i))
    d1_labels.append('D1_' + str(i))
    d2_labels.append('D2_' + str(i))
    d3_labels.append('D3_' + str(i))
    d4_labels.append('D4_' + str(i))

a3_bins = [9, 27, 45, 63, 81, 99, 117, 135, 153, 171]
ten_bins = range(0, 10)

#A3
fig, plots = plt.subplots(12, 4, figsize=(15, 25))
fig.subplots_adjust(hspace=0.5)
for i in range(0, len(categories)):
    x_index = i % 4
    y_index  = int(i / 4)
    category = categories[i]
    info = df.loc[df['category'] == category]
    a3 = info[a3_labels]
    for index, row in a3.iterrows():
        plots[y_index, x_index].plot(a3_bins, row.values)
    plots[y_index, x_index].set(xlabel=category)

fig.suptitle("Angle between 3 random points")
fig.savefig('resample_plots/combined_A3')
fig.show()

#D1
fig, plots = plt.subplots(12, 4, figsize=(15, 25))
fig.subplots_adjust(hspace=0.5)
for i in range(0, len(categories)):
    x_index = i % 4
    y_index  = int(i / 4)
    category = categories[i]
    info = df.loc[df['category'] == category]
    d1 = info[d1_labels]
    for index, row in d1.iterrows():
        plots[y_index, x_index].plot(ten_bins, row.values)
    plots[y_index, x_index].set(xlabel=category)

fig.suptitle("Distance between barycenter and random vertex")
fig.savefig('resample_plots/combined_D1')
fig.show()

#D2
fig, plots = plt.subplots(12, 4, figsize=(15, 25))
fig.subplots_adjust(hspace=0.5)
for i in range(0, len(categories)):
    x_index = i % 4
    y_index  = int(i / 4)
    category = categories[i]
    info = df.loc[df['category'] == category]
    d2 = info[d2_labels]
    for index, row in d2.iterrows():
        plots[y_index, x_index].plot(ten_bins, row.values)
    plots[y_index, x_index].set(xlabel=category)

fig.suptitle("Distance between 2 random vertices")
fig.savefig('resample_plots/combined_D2')
fig.show()

#D3
fig, plots = plt.subplots(12, 4, figsize=(15, 25))
fig.subplots_adjust(hspace=0.5)
for i in range(0, len(categories)):
    x_index = i % 4
    y_index  = int(i / 4)
    category = categories[i]
    info = df.loc[df['category'] == category]
    d3 = info[d3_labels]
    for index, row in d3.iterrows():
        plots[y_index, x_index].plot(ten_bins, row.values)
    plots[y_index, x_index].set(xlabel=category)

fig.suptitle("Square root of area of triangle given by 3 random vertices")
fig.savefig('resample_plots/combined_D3')
fig.show()

#D4
fig, plots = plt.subplots(12, 4, figsize=(15, 25))
fig.subplots_adjust(hspace=0.5)
for i in range(0, len(categories)):
    x_index = i % 4
    y_index  = int(i / 4)
    category = categories[i]
    info = df.loc[df['category'] == category]
    d4 = info[d4_labels]
    for index, row in d4.iterrows():
        plots[y_index, x_index].plot(ten_bins, row.values)
    plots[y_index, x_index].set(xlabel=category)

fig.suptitle("Cube root of volume of tetrahedron formed by 4 random vertices")
fig.savefig('resample_plots/combined_D4')
fig.show()

    #print(len(info))


#D1
