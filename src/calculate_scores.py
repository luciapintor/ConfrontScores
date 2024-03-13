# by Lucia Pintor
import pandas as pd

from src.capture_score import CaptureScore
from src.get_data import get_data_from_captures
from src.get_ground_truth import get_ground_truth
from src.utils.create_missing_folder import create_missing_folder


def calculate_scores(ground_truth, participant_summary, participant_name):
    """
    This function iterates the three output files of each participant to calculate their scores.
    :param ground_truth:
    :param participant_summary:
    :param participant_name:
    :return:
    """
    scores = []
    scores_dict = []

    for i, c in enumerate(["A", "B", "C"]):
        single_capture_score = calculate_score_single_capture(capture_id=c, capture_gt=ground_truth[i],
                                                              capture_ps=participant_summary[i])
        scores.append(single_capture_score)
        scores_dict.append(single_capture_score.__dict__)

    # save as csv
    scores_df = pd.DataFrame(scores_dict)
    report_folder = create_missing_folder("data/reports/")
    scores_df.to_csv(report_folder + participant_name + ".csv")

    return scores


def calculate_score_single_capture(capture_id, capture_gt, capture_ps):
    """
    This function compares the ground truth with the capture score to evaluate the score of a single file.
    :param capture_id:
    :param capture_gt:
    :param capture_ps:
    :return:
    """
    capture_score = CaptureScore(capture_id=capture_id)

    capture_score.calculate_error(devices_true=capture_gt["devices"], devices_count=capture_ps["devices"])
    capture_score.discarded = capture_ps["discarded"]

    if capture_id != "C":
        capture_score.samples = len(capture_gt["labels"])
        capture_score.calculate_v_measure(true_labels=capture_gt["labels"], calculated_labels=capture_ps["labels"])

    else:
        capture_score.samples = 3061

    capture_score.calculate_score()

    return capture_score


if __name__ == "__main__":
    ground_truth = get_ground_truth()

    data_folder = "data/participants/"
    participant_name = "example"

    participant_summary = get_data_from_captures(data_folder + participant_name + "/")

    scores = calculate_scores(ground_truth, participant_summary, participant_name)

    for score in scores:
        print(score.score)
