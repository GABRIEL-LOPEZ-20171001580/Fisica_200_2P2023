import pandas as pd   

df = pd.read_csv('./NOTAS_FS_200_18_07_2023.csv')

cols = [df.columns.values[0]]

for i in range(3,15):
    cols.append(df.columns.values[i])

X = df[cols]

X.to_csv('./NOTAS_FS_200_18_07_2023_1.csv')
