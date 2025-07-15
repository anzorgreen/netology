import pandas as pd

# asignment 1

log = pd.read_csv('visit_log.csv', sep=';')

def set_source_type(row):
    source = row['traffic_source'].lower()
    if source in ('yandex', 'google'):
        return 'organic'
    elif source in ('paid', 'email'):
        if row['region'] == 'Russia':
            return 'ad'
        else: return 'other'
    else: return row['traffic_source']
    
log['source_type'] = log.apply(set_source_type, axis=1)

# asignment 2

news = pd.read_csv('URLs.txt')

news = news[news.url.str.contains('/\d{8}-')]

# asignment 3

ratings = pd.read_csv('ml-latest-small/ratings.csv')

ratings = (ratings
           .groupby('userId')
           .agg(
               review_count=('rating', 'count'),
               time_last=('timestamp', 'max'),
               time_first=('timestamp', 'min'))
           )

average_lifetime = (
    ratings[ratings['review_count'] > 100]
    .apply(lambda row: row['time_last'] - row['time_first'], axis=1)
).mean()



# asignment 4
rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)


air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

revenue = rzd.merge(auto, on='client_id', how='outer')
revenue = revenue.merge(air, on='client_id', how='outer')

revenue_with_address = client_base.merge(revenue, on='client_id')
