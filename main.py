
import sys
from dataset import Dataset
from resample import resample
from normalize import normalize
from matplotlib import pyplot as plt
import pickle
import numpy as np
import pandas as pd

if __name__ == "__main__":
    dataset_original = Dataset("Princeton", write_basic_csv = False, write_other_csv = False)
    resample(dataset_original)

    dataset = Dataset("Princeton_normalized", write_basic_csv = False, write_other_csv = False)

    #dataset_original.write_face_area_csv()
    #dataset.write_face_area_csv()

    df = pd.read_csv("csv/Princeton_face_area.csv")
    df2 = pd.read_csv("csv/Princeton_normalized_face_area.csv")
    plt.hist(df, bins=np.arange(0, 1e-4, 5.5e-7))
    #plt.show()
    plt.hist(df2, bins=np.arange(0, 1e-4, 5.5e-7))
    plt.show()
    # A = dataset_original.get_face_areas_in_bins(bins = np.arange(0, 5.5e-4, 5.5e-5))
    # B = dataset.get_face_areas_in_bins(bins = np.arange(0, 5.5e-4, 5.5e-5))
    # plt.bar(np.arange(0, 4.95e-4, 5.5e-5), A, width=5.5e-5/2)
    # plt.savefig("test")
    #
    # plt.bar(np.arange(0, 4.95e-4, 5.5e-5), B, width=5.5e-5/2)
    # plt.savefig("test2")

    #check if dataset is normalized
    # if not dataset.is_normalised():
    #     normalize(dataset)
    #dataset.write_basic_info_csv()
    #dataset.write_bounding_box_csv()


    # if len(sys.argv) == 2:
    #     dataset.show_mesh(sys.argv[1])
    # else:
    #     dataset.show_mesh("m0.ply")
