# by Lucia Pintor
import os
import pandas as pd


def get_data(data_folder):
    data_summary = []

    data_files = os.listdir(data_folder)
    data_files.sort()

    for data_file in data_files:
        if "_C.csv" in data_file:
            data_df = pd.read_csv(data_folder + data_file)
            data_summary.append([None, int(data_df.devices.iloc[0]), int(data_df.discarded.iloc[0])])

        elif ".csv" in data_file:
            data_df = pd.read_csv(data_folder + data_file)
            labels = get_labels(data_df)
            devices = len(labels.unique())
            discarded = get_discarded(labels)
            data_summary.append([list(labels), devices, discarded])

    return data_summary


def get_labels(data_df):
    """
    This function gets the column of labels, which is "true_label" in the ground-truth files and
    "label" in the participant files.
    :param data_df:
    :return:
    """
    if "true_label" in data_df.columns:
        return data_df.true_label
    else:
        return data_df.label


def get_discarded(labels):
    """
    This function counts the number of discarded samples (identified by -1 values)
    :param labels: it is a series with the list of labels
    :return:
    """
    value_counts = labels.value_counts()
    if -1 in value_counts:
        return value_counts[-1]
    else:
        return 0


if __name__ == "__main__":

    data_folder = "data/participants/example/"

    data_summary = get_data(data_folder)

    for ds in data_summary:
        print("devices: {}".format(ds[1]))
        print("discarded: {}".format(ds[2]))
