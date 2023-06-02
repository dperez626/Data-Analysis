import pandas as pd
df = pd.read_csv('diabetes.csv')

import pandas_profiling as pp
pp.ProfileReport(df)

print(df)
