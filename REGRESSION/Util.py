import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


class Util(object):
    @classmethod
    def top_coefficiants(cls, df, y):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("dataframe!")

        clf = LinearRegression()
        model = make_pipeline(StandardScaler(), clf)
        model.fit(df.values, y)
        d = list(zip(np.abs(clf.coef_), df.columns))
        return pd.DataFrame(d, columns=["coeff", "name"]).set_index("name").sort_values(by="coeff", ascending=False)
