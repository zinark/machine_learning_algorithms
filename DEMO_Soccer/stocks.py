import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
from Integration import Integration

df = Integration.get(2018, 1, 2)
print df.head()
