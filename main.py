#import sys
from dataset import Dataset
from mesh import Mesh
#import face_area_plots
#from reorder import reorder_dataset
from distance import Distance
import os



if __name__ == "__main__":
    dataset = Dataset("Princeton_remeshed_normalized", write_basic_csv = False, write_other_csv = False)
    dataset.save_thumbnails()

    # count = 0
    # path = os.path.join(os.getcwd(), "thumbnails")
    # print(path)
    # for dir in os.listdir(path):
    #     subdir = os.path.join(path, dir)
    #     print(subdir)
    #     for f in os.listdir(subdir):
    #         if os.path.isfile(os.path.join(subdir, f)):
    #             count += 1
    # print(count)

    #dataset_remeshed = Dataset("Princeton_remeshed", write_basic_csv = False, write_other_csv = False)
    #dataset_remeshed.resample()
    #dataset_remeshed_normalized = Dataset("Princeton_remeshed_normalized", write_basic_csv = False, write_other_csv = False)
    #dataset_remeshed_normalized.resample()
    #dataset_remeshed_normalized.normalize()
    #dataset_remeshed_normalized.write_elementary_features()
    #dataset_remeshed_normalized.write_shape_features()
    #dataset_remeshed_normalized.write_all_features_normalized()

    Distance("Princeton_remeshed_normalized", ["m1693.ply"])

    #reorder_dataset(dataset_original)
    #reorder_dataset(dataset_remeshed)
    #reorder_dataset(dataset_remeshed_normalized)

    # takes a while to run and makes big files
    #face_area_plots.plot_face_area(dataset_original, dataset_remeshed)

    # if len(sys.argv) == 2:
    #     dataset_remeshed_normalized.show_mesh(sys.argv[1])
    # else:
    #     dataset_remeshed_normalized.show_mesh("m0.ply")
