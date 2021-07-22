#https://www.kaggle.com/columbia2131/mlb-lightgbm-starter-dataset-code-en-ja?scriptVersionId=65896391&cellId=4

import pandas as pd
import pickle
import os
import numpy as np 
import gc

null = np.nan
true = True
false = False

print("\nRaw Training Frame:")
train = pd.read_csv('raw_data/train.csv')

#process date and set as index
train['date'] = pd.to_datetime(train['date'], format="%Y%m%d")
train = train.set_index('date').to_period('D')

print(train.shape)
print(train.head(1))

for col in train.columns:

    print("\nProcessing Column:")
    print(col)

    if col == 'date': continue

    _index = train[col].notnull()
    train.loc[_index, col] = train.loc[_index, col].apply(lambda x: eval(x))

    outputs = []
    for index, date, record in train.loc[_index, ['date', col]].itertuples():
        _df = pd.DataFrame(record)
        _df['index'] = index
        _df['date'] = date
        outputs.append(_df)

    outputs = pd.concat(outputs).reset_index(drop=True)

    print(outputs.shape)
    print(output.head(1))

    outputs.to_csv(f'raw_data/train_{col}_train.csv', index=False)
    outputs.to_pickle(f'raw_data/train_{col}.pkl')

    del outputs
    del train[col]
    gc.collect()