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
    df2 = pd.read_csv("csv/{}_face_area.csv".format(dataset_remeshed.folder_name_dataset))
    plt.hist(df, bins=np.arange(0, 1e-4, 5.5e-7))
    plt.hist(df2, bins=np.arange(0, 1e-4, 5.5e-7))
    plt.savefig("resample_plots/face_areas")
    plt.show()
