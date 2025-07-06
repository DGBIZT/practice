import csv

rows = [{'Name': 'Alice', 'Age': '25', 'Gender': 'Female'},
        {'Name': 'Bob', 'Age': '30', 'Gender': 'Male'},
        {'Name': 'Charlie', 'Age': '35', 'Gender': 'Male'}]

with open('file.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'Gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

# import csv
# with open('students.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#     for row in reader:
#         name, age, avg_grade = row
#         if float(avg_grade) > 4.5:
#            print(f"{name} ({age} лет) - средний балл: {avg_grade}")

# import pandas as pd

# reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# italy_reviews = reviews.loc[(reviews.country == "Italy") | (reviews.points >= 90)]

# Проверяет, содержится ли значение в определенном столбце в заданном списке значений
# italy_reviews = reviews.loc[reviews.country.isin(["Italy", "France"])]

# Отображение значений столбца - строк которые не пустые
# italy_reviews = reviews.loc[reviews.price.notnull()]

# italy_reviews = reviews.loc[reviews.country.isin(["Italy"]) & (reviews.points >= 90)]
# italy_reviews = reviews.loc[((reviews.country == "Italy") | (reviews.points >= 90)) & (reviews.price.notnull()) & (reviews.designation.notnull())]

# Создание нового столбца с обратным индексом(нумерацией)
# reviews['index_backwards'] = range(len(reviews), 0, -1)

# Статистика столбца points
# static_points = reviews.points.describe()
# Среднее значение столбца points
# middle_points = reviews.points.mean()

# Для получения списка уникальных значений столбца taster_name
# unique_taster = reviews.taster_name.unique()

# Количество упоминаний каждого имени
# middle_points = reviews.points.mean()

# Функция map в Python — позволяет применить функцию к каждому элементу списка.
# reviews.points.map(lambda p: p - middle_points)
# reviews['description_lenght'] = reviews.description.map(len)
# b = reviews['description_lenght'].describe()
# print(b)

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
#
# # result = df.apply(pd.Series.mean)
# # print(result)
#
# def rang_of_series(series):
#     return series.max() - series.min()
#
# result = df.apply(rang_of_series)
# print(result)

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6]
# })
#
# result = df.sum(axis=0)
# print(result)

# Реализована функция для считывания финансовых операций из CSV.
# Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями.
# import pandas as pd
# import csv
# import os
#
# def read_transactions_csv(file_path: str) -> list:
#     base_dir = os.path.dirname(__file__)
#     full_path = os.path.join(base_dir, file_path)
#
#     with open(full_path) as csvfile:
# # df = pd.read_csv(file_path)
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             return row
#
# csv_file = read_transactions_csv("data/transactions.csv")
# print(csv_file)

# import csv
# with open('students.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#     for row in reader:
#         name, age, avg_grade = row
#         if float(avg_grade) > 4.5:
#            print(f"{name} ({age} лет) - средний балл: {avg_grade}")