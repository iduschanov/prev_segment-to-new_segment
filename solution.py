import numpy as np
import pandas as pd

# Сгенерируем данные для задачи
data = pd.DataFrame(
    np.random.randint(low=0, high=4, size=(50000000, 2)), # 50000000
    columns=['prev_segment', 'new_segment'])

# Создаем переменные с уникальными значения индекса и колонок
index = data['prev_segment'].unique()
columns = np.sort(data['new_segment'].unique())

 # Создаем новый DataFrame куда будем записывать наши полученные значения
df = pd.DataFrame(np.zeros(shape=(index.max()+1, len(columns))),
                  columns=columns, index=range(index.max()+1), dtype=int)

# Добавляем новую колонку для подсчета переходов клиентов из одной категории в другую
data["new_col"] = 1
df_new = data.groupby(["prev_segment", "new_segment"]).count().reset_index()
print('Data with counts: \n: ', df_new)

# Полученные количество переходов записываем в результирующий DataFrame
for idx, col in df_new.iterrows():
  df[col[1]].loc[col[0]] = col[2]
print(df)

# Далее делим на сумму и получить частотную таблицу переходов
df = df.div(df.sum(axis=1), axis=0)
df.fillna(0, inplace=True)
print('Solution: \n', df) 

