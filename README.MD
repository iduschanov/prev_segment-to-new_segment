Клиенты обладают рядом статусов, закодированных цифрами: 0 - 'улица', 1 - 'зарплатник', 2 - 'премиум', 3 - 'пенсионер', 4 - 'студент'. У нас есть матрица с логами смен статусов за некоторый период, требуется развернуть ее в матрицу статус - статус с частотами перехода между ними.

client_id | prev_segment | new_segment|
--- | --- | ---
1 | 0 | 1
2 | 0 | 2
3 | 4 | 3

Результат должен выглядеть так:

segment |0 | 1 | 2 | 3 | 4 
--- | --- | --- | --- | --- | ---
0 | 0 | 0.5 | 0.5 | 0 | 0 
1 | 0 |0 | 0 | 0 | 0
2 | 0 | 0 | 0 | 0 | 0
3 | 0 | 0 | 0 | 0 | 0
4 | 0 | 0 | 0 | 1 | 0