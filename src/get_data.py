# by Lucia Pintor
import os
import pandas as pd


def get_data_from_captures(data_folder):
    """
    This function gets the data needed to calculate the score of a participant of the challenge.
    There should be 3 files:
    - capture_A.csv - it has two columns: id and label
    - capture_B.csv - it has two columns: id and label
    - capture_C.csv - it has two columns: devices and discarded
    Challenge available at: https://sites.unica.it/net4u/confront-challenge-on-wifi-frame-fingerprinting-for-people-counting-and-trackingconfront/
    :param data_folder:
    :return:
    """
    data_summary = []

    data_files = os.listdir(data_folder)
    data_files.sort()

    for data_file in data_files:
        if "_C.csv" in data_file:
            data_df = pd.read_csv(data_folder + data_file)
            data_summary.append(
                {
                    "labels": None,
                    "devices": int(data_df.devices.iloc[0]),
                    "discarded": int(data_df.discarded.iloc[0]),
                }
            )

        elif ".csv" in data_file:
            data_df = pd.read_csv(data_folder + data_file)
            labels = get_labels(data_df)
            devices = len(labels.unique())
            discarded = get_discarded(labels)

            # there is the "-1" extra class
            if discarded > 0:
                devices -= 1

            data_summary.append(
                {
                    "labels": list(labels),
                    "devices": devices,
                    "discarded": discarded,
                }
            )

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

    data_summary = get_data_from_captures(data_folder)

    for ds in data_summary:
        print("devices: {}".format(ds["devices"]))
        print("discarded: {}".format(ds["discarded"]))
