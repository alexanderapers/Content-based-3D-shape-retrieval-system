import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os import path

def plot_face_area(dataset_original, dataset_remeshed):
    if not path.exists("csv/{}_face_area.csv".format(dataset_original.folder_name_dataset)) and not path.exists("csv/{}_face_area.csv".format(dataset_remeshed.folder_name_dataset)):
        dataset_original.write_face_area_csv()
        print("Writing very big face area csv")
        dataset_remeshed.write_face_area_csv()
        print("Writing another very big face area csv")

    df = pd.read_csv("csv/{}_face_area.csv".format(dataset_original.folder_name_dataset))
    plt.hist(df, color='plum', bins=np.arange(0, 1e-4, 5.5e-7), weights=np.ones(len(df)) / len(df))
    plt.ylim([0,0.15])
    plt.xlabel('area of faces')
    plt.ylabel('frequency')
    plt.title("Distribution of area of faces before normalization")
    plt.savefig("resample_plots/face_areas_before")
    plt.clf()

    df2 = pd.read_csv("csv/{}_face_area.csv".format(dataset_remeshed.folder_name_dataset))
    plt.hist(df2, color='plum', bins=np.arange(0, 1e-4, 5.5e-7), weights=np.ones(len(df2)) / len(df2))
    plt.ylim([0,0.15])
    plt.xlabel('area of faces')
    plt.ylabel('frequency')
    plt.title("Distribution of area of faces after normalization")
    plt.savefig("resample_plots/face_areas_after")
