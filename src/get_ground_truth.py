# by Lucia Pintor

from src.get_data import get_data_from_captures


def get_ground_truth():
    """
    This function returns an array with the list of labels of the ground truth, the number of devices,
    and discarded samples.
    :return:
    """
    gt_folder = "data/ground_truth/"

    ground_truth = get_data_from_captures(gt_folder)

    return ground_truth


if __name__ == "__main__":

    ground_truth = get_ground_truth()

    for gt in ground_truth:
        print("devices: {}".format(gt["devices"]))
        print("discarded: {}".format(gt["discarded"]))
