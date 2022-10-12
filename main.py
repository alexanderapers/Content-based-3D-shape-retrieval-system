
import sys
from dataset import Dataset
import face_area_plots

if __name__ == "__main__":
    dataset_original = Dataset("Princeton", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed = Dataset("Princeton_remeshed", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed.resample()
    dataset_remeshed_normalized = Dataset("Princeton_remeshed_normalized", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed_normalized.resample()
    dataset_remeshed_normalized.normalize()

    # takes a while to run and makes big files
    #face_area_plots.plot_face_area(dataset_original, dataset_remeshed)




    # if len(sys.argv) == 2:
    #     dataset.show_mesh(sys.argv[1])
    # else:
    #     dataset.show_mesh("m0.ply")
