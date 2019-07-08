import numpy as np
import pywt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
#

df = pd.read_csv("../../mprobc_250kb.csv",delimiter=',', header=None)


header = df.pop(0)
scaler = MinMaxScaler()
scaled_values_t = scaler.fit_transform(df)

# coeffs2 = pywt.dwt2(scaled_values_t, 'bior1.3')

# print(coeffs2[0])
# np.save('wt',np.absolute(coeffs2[0]))
#
plt.imshow(scaled_values_t)
plt.show()
