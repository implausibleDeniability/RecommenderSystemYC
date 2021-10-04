import numpy as np
import pandas as pd
from tqdm import tqdm
import pickle


def compute_mnap(submission):
    # load all organization that the user rated 4 or 5 from ts 1050
    # sample_submission.csv used ts > 1000
    with open('data/true_orgs.pickle', 'rb') as file:
        true_orgs = pickle.load(file)
    mnaps = []
    for user_id, target in tqdm(zip(submission.index, submission.target)):
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