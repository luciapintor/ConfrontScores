# by Lucia Pintor
import copy
import os

import pandas as pd

from src.calculate_scores import calculate_scores
from src.get_data import get_data_from_captures
from src.get_ground_truth import get_ground_truth

if __name__ == "__main__":

    data_folder = "data/participants/"
    report_folder = "data/reports/"

    report_scores = []

    ground_truth = get_ground_truth()

    participant_folders = os.listdir(data_folder)
    participant_folders.sort()

    for pf in participant_folders:
        print(pf)
        participant_summary = get_data_from_captures(data_folder + pf + "/")

        scores = calculate_scores(ground_truth, participant_summary, pf)
        total_score = 0.0

        participant_scores = {"id": pf}

        for score in scores:
            participant_scores[score.capture_id] = score.score
            total_score += score.score

        participant_scores["tot"] = total_score
        report_scores.append(copy.copy(participant_scores))

    report_scores_df =pd.DataFrame(report_scores)
    report_scores_df.to_csv("data/reports/summary.csv")
