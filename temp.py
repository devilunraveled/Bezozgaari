import pandas as pd

out = pd.read_csv('results.csv')
test = pd.read_csv('dataset/test.csv')
out['index'] = test['index']
out.to_csv('results.csv', index=False)