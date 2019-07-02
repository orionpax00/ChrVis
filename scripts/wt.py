import numpy as np
import pywt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mprobc_chr1_100kb.csv",delimiter=',', header=None)

header = df.pop(0)
df.head()

coeffs2 = pywt.dwt2(df.values, 'bior1.3')

print(coeffs2[0])
np.save('wt',np.absolute(coeffs2[0]))
#
plt.imshow(coeffs2[0])
plt.show()
