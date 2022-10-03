
import sys
from dataset import Dataset
from resample import resample
from cubenormalize import normalize


if __name__ == "__main__":
    #dataset_original = Dataset("Princeton", write_basic_csv = False, write_AABB = False)

    #resample(dataset_original)

    dataset = Dataset("Princeton_normalized", write_basic_csv = False, write_AABB = False)

    normalize(dataset)

    if len(sys.argv) == 2:
        dataset.show_mesh(sys.argv[1])
    else:
        dataset.show_mesh("m0.ply")
