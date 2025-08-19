import pandas as pd

# Задание 1
df = pd.read_csv('horse_data.csv', names=[n for n in range(1, 29)], na_values='?')

dict_needed_data = {
    1: 'surgery?', # categ
    2: 'Age',      # num
    4: 'rectal temperature', # num
    5: 'pulse',   # num 
    6: 'respiratory rate', # num 
    7: 'temperature of extremities', # categ
    11: 'pain', # categ
    23: 'outcome' # categ
}
df = df[dict_needed_data.keys()]
df.rename(columns=dict_needed_data, inplace=True)

df['surgery?'] = df['surgery?'].astype('object')
df['temperature of extremities'] = df['temperature of extremities'].astype('object')
df['pain'] = df['pain'].astype('object')
df['pain'] = df['pain'].astype('object')


df.loc[df['surgery?'] == 1, 'surgery?'] = 'yes'
df.loc[df['surgery?'] == 2, 'surgery?'] = 'no'


df.loc[df['temperature of extremities'] == 1, 'temperature of extremities'] = 'Normal'
df.loc[df['temperature of extremities'] == 2, 'temperature of extremities'] = 'Warm'
df.loc[df['temperature of extremities'] == 3, 'temperature of extremities'] = 'Cool'
df.loc[df['temperature of extremities'] == 4, 'temperature of extremities'] = 'Cold'


df.loc[df['pain'] == 1, 'pain'] = 'alert, no pain'
df.loc[df['pain'] == 2, 'pain'] = 'depressed'
df.loc[df['pain'] == 3, 'pain'] = 'intermittent mild pain'
df.loc[df['pain'] == 4, 'pain'] = 'intermittent severe pain'
df.loc[df['pain'] == 5, 'pain'] = 'continuous severe pain'


df.loc[df['outcome'] == 1, 'outcome'] = 'lived'
df.loc[df['outcome'] == 2, 'outcome'] = 'nodied'
df.loc[df['outcome'] == 3, 'outcome'] = 'was euthanized'


print(df.head())
print()

# Задание 2

stats_df = df.describe()
completeness_row = df.count() / len(df)
stats_df.loc['completeness'] = completeness_row
print(stats_df)


def get_outliers_from_df(df, col_name):
    col = df[col_name]
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return df[~col.between(lower_bound, upper_bound)].dropna()[col_name]

# print(get_outliers_from_df(df, 'Age'))
# print(get_outliers_from_df(df, 'rectal temperature'))
# print(get_outliers_from_df(df, 'pulse'))
# print(get_outliers_from_df(df, 'respiratory rate'))


# Задание 3ю
completeness_row = df.count() / len(df)
# Так как процент заполнения для всех столбцов достаточно высокий,
# мы можем оботись без удаления значений


# Для pulse и respiratory rate среднее заметно выше медианы. 
# Это говорит о том, что в данных есть выбросы,  которые "утягивают" среднее вверх.
#  Медиана более устойчива к таким выбросам, поэтому используем её.

median_temp = df['rectal temperature'].median()
median_pulse = df['pulse'].median()

# Для rectal temperature реднее и медиана почти совпадают,
# так что здесь подойдёт любой из показателей (медиана или среднее)
median_resp_rate = df['respiratory rate'].median()


# Значения нечисловых стобцов заполним модой, кроме outcome, 
# это столбец несёт слишком важное значение, чтобы угадывать его значения. 
mode_surgery = df['surgery?'].mode()[0]
mode_pain = df['pain'].mode()[0]
mode_temperature_of_extremities = df['temperature of extremities'].mode()[0]


fill_values = {
    'rectal temperature': median_temp,
    'pulse': median_pulse,
    'respiratory rate': median_resp_rate,
    'surgery?': mode_surgery,
    'temperature of extremities': mode_temperature_of_extremities,
    'pain': mode_pain
}

df.fillna(fill_values, inplace=True)

# Тут можно удалить и пустые значения outcome

df.dropna(subset=['outcome'], inplace=True)





