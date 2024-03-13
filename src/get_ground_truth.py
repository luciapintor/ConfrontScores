# by Lucia Pintor

from src.get_data import get_data


def get_ground_truth():
    gt_folder = "data/ground_truth/"

    ground_truth = get_data(gt_folder)

    return ground_truth


if __name__ == "__main__":

    ground_truth = get_ground_truth()

    for gt in ground_truth:
        print("devices: {}".format(gt[1]))
        print("discarded: {}".format(gt[2]))
