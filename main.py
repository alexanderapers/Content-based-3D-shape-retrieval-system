
import sys
from dataset import Dataset
#from resample import resample
#from normalize import normalize
#from matplotlib import pyplot as plt
#import pickle
#import numpy as np

if __name__ == "__main__":
    dataset_original = Dataset("Princeton", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed = Dataset("Princeton_remeshed", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed.resample()
    dataset_remeshed_normalized = Dataset("Princeton_remeshed_normalized", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed_normalized.resample()
    dataset_remeshed_normalized.normalize()



    # if len(sys.argv) == 2:
    #     dataset.show_mesh(sys.argv[1])
    # else:
    #     dataset.show_mesh("m0.ply")
