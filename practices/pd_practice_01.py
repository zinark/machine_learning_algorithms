import pandas as pd

df1 = pd.DataFrame({
    "uid": [1, 2],
    "email": ["a@a.com", "b@b.com"]
})

df2 = pd.DataFrame({
    "uid" : [1, 1, 1, 2, 2, 2],
    "worked" : [10, 3, 4, 8, 7, 8]
})

df3 = pd.DataFrame({
    "uid" : [1, 2],
    "clicks" : [100, 103]
})

join = df1.merge(df2, on="uid").merge (df3, on="uid")