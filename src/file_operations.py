# Реализована функция для считывания финансовых операций из CSV.
# Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями.
import pandas as pd
import csv
import os

def read_transactions_csv_and_output(file_path: str) -> list[dict[str, str]]:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        reader = pd.DataFrame(list(reader))
        reader.columns = reader.iloc[0]  # Установи первую строку как заголовки столбцов
        reader = reader.drop(0)  # Удали первую строку, так как она теперь заголовок
        list_of_dicts = reader.to_dict(orient='records')
        return list_of_dicts
b = read_transactions_csv_and_output("data/transactions.csv")
print(b)


def read_transactions_excel_and_output(file_path: str) -> list[dict[str, str]]:
    excel_data = pd.read_excel(file_path)
    list_of_dicts = excel_data.to_dict(orient='records')
    return list_of_dicts[:3]

a = read_transactions_excel_and_output("data/transactions_excel.xlsx")
print(a)