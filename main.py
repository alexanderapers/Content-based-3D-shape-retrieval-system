
import sys
from dataset import Dataset


if __name__ == "__main__":
    dataset = Dataset("Princeton", write_basic_csv = False, write_AABB = False)

    if len(sys.argv) == 2:
        dataset.show_mesh(sys.argv[1])
    else:
        dataset.show_mesh("m0.ply")

