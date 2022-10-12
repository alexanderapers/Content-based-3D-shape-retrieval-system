import pandas as pd
import matplotlib.pyplot as plt

def plot_face_area(dataset_original, dataset):
    dataset_original.write_face_area_csv()
    print("Writing very big face area csv")
    dataset.write_face_area_csv()
    print("Writing another very big face area csv")

    df = pd.read_csv("csv/Princeton_face_area.csv")
    df2 = pd.read_csv("csv/Princeton_normalized_face_area.csv")
    plt.hist(df, bins=np.arange(0, 1e-4, 5.5e-7))
    plt.hist(df2, bins=np.arange(0, 1e-4, 5.5e-7))
    #plt.savefig("face_areas")
    plt.show()
