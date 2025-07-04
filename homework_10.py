import pandas as pd

# Task 1
data = pd.read_csv('ratings.csv')
def classify(param):
    if param <= 2:
        return 'Низкий'
    elif param <= 4:
        return 'Средний'
    else:
        return 'Высокий'

unique_movies = data[['movieId', 'rating']].groupby('movieId').agg('mean').reset_index()[['movieId', 'rating']]


# Task 2
data = pd.read_csv('keywords.csv')

geo_data = {
    'Центр': ['москва', 'тула', 'ярославль'],
    'Северо-Запад': ['петербург', 'псков', 'мурманск'],
    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

def get_region(param, geo_data): 
    param = param.lower()
    cities_dict = {}
    for reg, cities in geo_data.items(): # Меняю структуру данных, чтобы был быстрый доступ по ключу
        for city in cities:
            cities_dict[city] = reg

    for city in cities_dict:
        if city in param:
            return cities_dict[city]
    else:
        return 'undefined'

data['region'] = data['keyword'].apply(get_region, geo_data=geo_data)

# Task 3

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

def get_production_year(title):
    years = [str(i) for i in range(1950, 2011)]
    for year in years:
        if year in title:
            return year
    else:
        return '1900'

movies['year'] = movies['title'].apply(get_production_year)
avg_ratings_by_movie = ratings.groupby('movieId').agg({'rating':'mean'}).reset_index()
big_table = (
    pd.merge(movies, avg_ratings_by_movie, on='movieId', how='left')
    .groupby('year').agg({'rating': 'mean', 'movieId':'count'})
    .reset_index() # не знаю, нужно ли снимать индекс с year
    .sort_values(by='rating', ascending=False)
)