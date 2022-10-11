
import sys
from dataset import Dataset
from resample import resample
from normalize import normalize

if __name__ == "__main__":
    dataset_original = Dataset("Princeton", write_basic_csv = False, write_AABB = False)
    resample(dataset_original)

    dataset = Dataset("Princeton_normalized", write_basic_csv = False, write_AABB = False)
    # check if dataset is normalized
    # if not dataset.is_normalised():
    #     normalize(dataset)
    dataset.write_basic_info_csv()
    dataset.write_bounding_box_csv()


    # if len(sys.argv) == 2:
    #     dataset.show_mesh(sys.argv[1])
    # else:
    #     dataset.show_mesh("m0.ply")
