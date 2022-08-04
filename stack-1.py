## stack overflow questions
## https://stackoverflow.com/questions/73067277/group-by-2-columns-python

import pandas as pd

df = pd.DataFrame(
    {'id':[1,2,3,4,1,2,4], 
    'V':[0,1,0,0,0,0,1]})

# gs = df.groupby(['id','V'])
# print(df.groupby(['id','V'])['V'].count().to_frame('Count').reset_index().set_index(['id', 'V']).unstack().fillna(0))
# print(df.groupby(['id','V'])['V'].count().to_frame('Count').reset_index().set_index(['id', 'V']).unstack().fillna(0))
print(df.groupby(['id','V'])['V'].count().unstack().T.fillna(0).astype(int).to_json())
# .set_index(['id', 'V']).unstack()

# for k, v in gs:
#     g = gs.get_group(k)
#     print(g)
