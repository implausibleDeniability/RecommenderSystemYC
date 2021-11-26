import numpy as np
import pandas as pd
from tqdm import tqdm
import pickle


def compute_mnap(submission):
    """Computes MNAP metric for the given submission
    The metric is implemented as it is explained in the competition
    MNAP score formula is in 'other/mnap_formulae.png'
    Uses data from timestamp > 1050 as the groundtruth for the estimation
    """
    with open("data/true_orgs.pickle", "rb") as file:
        true_orgs = pickle.load(file)
    mnaps = []
    for user_id, target in tqdm(zip(submission.index, submission.target)):
        if user_id not in true_orgs:
            continue
        true_org = true_orgs[user_id]
        if len(true_org) == 0:
            continue
        predicted_orgs = target.split()
        scores = []
        multipliers = []
        for predicted_org in predicted_orgs:
            if predicted_org in true_org:
                scores.append(1)
            else:
                scores.append(0)
            multipliers.append(sum(scores) / len(scores))
        mnaps.append(np.dot(scores, multipliers) / min(20, len(true_org)))
    return np.mean(mnaps)
