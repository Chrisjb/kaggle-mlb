import pandas as pd
import pickle
import os

from processing_helpers import unpack_json, unpack_data

training = pd.read_csv('raw_data/train.csv')

# Convert training data date field to datetime type
training['date'] = pd.to_datetime(training['date'], format="%Y%m%d")
training = training.set_index('date').to_period('D')
print("\nTraining dataset:")
print(training.info())

json_cols = training.columns.difference(['date'])
print("\nColumns to Transform:")
print(json_cols)

# Unpack nested dataframes and store in dictionary `training_dfs`
# set to only 1 worker to avoid warning:
#UserWarning: A worker stopped while some jobs were given to the executor. This can be caused by a too short worker timeout or by a memory leak.
#  warnings.warn(
training_dfs = unpack_data(training, dfs=json_cols, n_jobs = 1) 
print("Train DFs created:")
print(training_dfs.keys())

for tt in training_dfs.keys():
    with open('raw_data/train_' + tt + '.pkl', 'wb') as out:
        pickle.dump(training_dfs[tt], out)
    print("\nOutput " + tt)
    print(training_dfs[tt].shape)