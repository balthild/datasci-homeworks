from pandas import DataFrame, read_csv

data: DataFrame = read_csv('aapl.csv')

vol: list = data['Volume']

print('Average value of Volumes:', sum(vol) / len(vol))
