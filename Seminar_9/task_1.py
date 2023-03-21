import pandas as pd

df = pd.read_csv('Seminar_9/california_housing_train.csv')

# Average
res = df['median_house_value'].loc[df['population'] < 500].mean()
print(f'Average value is {res:.2f}')

# Max and Min
res = df['households'].loc[df['population'].idxmin()]
print(f'Maximum value is {res:.2f}')