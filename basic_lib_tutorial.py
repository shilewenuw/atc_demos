import pandas as pd
import numpy as np

# create a 2x2 numpy array
a = np.array([[1, 2],
              [3, 4]])

x = pd.DataFrame([[1, 2, 100],
                  [3, 4, 200]],
                 columns=['apples eaten', 'IQ', 'weight'])
x.index = ['01/01/2018', '01/02/2018']
print(x)
print(x['apples eaten'])
cols_wanted = ['apples eaten', 'weight']
print(x[cols_wanted]) # equivalent to x[['apples eaten', 'weight']], separated list to make the double brackets less confusing

import matplotlib.pyplot as plt


# x = np.random.normal(0, 2, 1000)
# plt.hist(x)

plt.plot(x['apples eaten'], x['IQ']) # use 2 pandas columns to make graph, first arg is x values, second arg is y values.
plt.show() # this method just puts whatever you plotted on to the screen