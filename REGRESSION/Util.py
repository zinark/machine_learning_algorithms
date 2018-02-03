import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import sympy as sp


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

    @staticmethod
    def grad_descent(cost_func_exp, learning_rate=.1, start_x=5., max_iter=100):
        from sympy.parsing.sympy_parser import parse_expr
        x = sp.symbols("x")
        # f = x ** 2
        f = parse_expr(cost_func_exp)
        f_diff = sp.diff(f, x)

        f_cost = sp.lambdify(x, f)
        f_derive = sp.lambdify(x, f_diff)
        sp.pprint (f)
        sp.pprint (f_diff)

        results = []
        for step in range(max_iter):
            y = f_cost(start_x)
            move = f_derive(learning_rate * start_x)
            results.append([start_x, y])
            start_x -= move
            if start_x <= 0.01:
                break

        df = pd.DataFrame(results)
        return df
