import numpy as np
import matplotlib.pyplot as plt

from Util import Util

df = Util.grad_descent("x**4+x**2", start_x=5, learning_rate=0.1)
print df

plt.figure(figsize=(4, 4))
l = np.linspace(-5, 5, 100)
plt.plot(l, l ** 4 + l ** 2)
plt.scatter(df[0].values, df[1].values, marker='X', color='red')
plt.xlabel("theta")
plt.ylabel("y = J(theta)")
plt.show()
