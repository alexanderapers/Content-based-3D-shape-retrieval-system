import sys
from dataset import Dataset
from shape_features_mesh import Shape_Features_Mesh
import face_area_plots
from reorder import reorder_dataset

if __name__ == "__main__":
    dataset_original = Dataset("Princeton", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed = Dataset("Princeton_remeshed", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed.resample()
    dataset_remeshed_normalized = Dataset("Princeton_remeshed_normalized", write_basic_csv = False, write_other_csv = False)
    dataset_remeshed_normalized.resample()
    dataset_remeshed_normalized.normalize()
    #dataset_remeshed_normalized.write_elementary_features()

    #reorder_dataset(dataset_original)
    #reorder_dataset(dataset_remeshed)
    #reorder_dataset(dataset_remeshed_normalized)
    
    # i=0
    # for mesh in dataset_remeshed_normalized:
    #   Shape_Features_Mesh(mesh)
    #   i += 1
    #   if i > 10:
    #       break

    # takes a while to run and makes big files
    #face_area_plots.plot_face_area(dataset_original, dataset_remeshed)

    # if len(sys.argv) == 2:
    #     dataset_remeshed_normalized.show_mesh(sys.argv[1])
    # else:
    #     dataset_remeshed_normalized.show_mesh("m0.ply")
