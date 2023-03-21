import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# First way
data['human'] = [1 if i == 'human' else 0 for i in data['whoAmI']]
data['robot'] = [1 if i == 'robot' else 0 for i in data['whoAmI']]
print(data.head(5))

# # Second way
# ohc_data = np.array([[1, 0] if i == 'human' else [0, 1] for i in data.values])
# df = pd.DataFrame(ohc_data, columns=['human','robot'])
# print(df.head(5))

