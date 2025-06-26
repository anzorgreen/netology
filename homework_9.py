import pandas as pd


# assignment 1
data = pd.read_csv('ratings.csv')
result = (data[data.rating == 5]
          .groupby('movieId')
          ['rating'].count()
          .sort_values(ascending=False)
          .index[0]
          )
print(result)
# >> 318


# assignment 2
data = pd.read_csv('power.csv')

result = (
    data[
        (data.quantity >= 0)
        & (data.country.isin(['Estonia', 'Latvia', 'Lithuania']))
        & (data.category.isin([4, 12, 21]))
        & (data.year.isin(range(2005, 2011)))
    ]
    ['quantity'].count()
)
print(result)
# >> 408


# assignment 3
raw_data = pd.concat((pd.read_html('https://fortrader.org/quotes')))
print(type(raw_data))
# >> <class 'pandas.core.frame.DataFrame'>
