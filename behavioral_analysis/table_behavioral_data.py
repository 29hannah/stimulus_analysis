import pandas as pd
from functools import reduce

# Read tables
listener1 = pd.read_table('example_final_1.csv', sep=',')
listener2 = pd.read_table('example_final_2.csv', sep=',')
listener3 = pd.read_table('example_final_3.csv', sep=',')

data_frames = [listener1, listener2, listener3]

# Merge tables with one matching column
df_merged = reduce(lambda left, right: pd.merge(left, right, on=['sound_id'], how='outer'), data_frames)


df_merged = reduce(lambda left, right: pd.merge(left, right, on=['sound_id'], how ='outer'), data_frames).fillna('void')

pd.DataFrame.to_csv(df_merged, 'merged.csv', sep=',', na_rep='.', index=False)
