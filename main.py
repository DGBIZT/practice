# import logging
# from src.save_to_file import save_to_file
# from src.news import get_news
# from datetime import datetime

#
# logger = logging.getLogger("main")
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler('logs/main.log', mode='a', encoding="utf-8", delay=False)
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s)')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
#
#
# def main():
#     """Главная функция для работы приложения"""
#     try:
#         logger.info('запрос у пользователя ключевых слов')
#
#         query = input("Введите ключевые слова:  ")
#         exclude_word = input("Введите слова фильтрации (через запятую):  ").split(',')
#         today = datetime.today()
#         today_string = today.strftime("%Y-%m-%d")
#
#         logger.info('Получение новостей')
#         articles_list = get_news(query, exclude_word )
#
#         logger.info('Запись новостей в файл')
#         file_name = f'{today_string}_{query.replace(" ", "_")}.json'
#         file_path = f'news/{file_name}'
#         save_to_file(articles_list, file_path)
#
#     except Exception as ex:
#         logger.error(f"Произошла ошибка: {ex}")
#
# if __name__ == '__main__':
#     main()


# import logging
#
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('example.log')
# file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
#
# logger.debug('Debug message')
# logger.info('Info message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')

# import random
# import json
#
# def generate_users(first_names,last_names, cities ):
#     """Генерирует пользователя."""
#     while True:
#         user = {
#             'first_name': random.choice(first_names),
#             'last_name': random.choice(last_names),
#             'age': random.randint(18, 65),
#             'city': random.choice(cities)
#         }
#         yield user
#
#
# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
# last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']
#
# users = generate_users(first_names, last_names, cities)
#
# user_group1 = [next(users) for i in range(2)]
# user_group2 = [next(users) for i in range(1)]
#
# print("User group #1")
# print(json.dumps(user_group1, indent=4))

# import requests
#
# API_KEY = 'd8ff009b07400f3ac480dd31e35d777a'
#
# response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=Moscow&appid={API_KEY}")
#
# lat = response.json()[0]['lat']
# lon = response.json()[0]['lon']
#
# print(lat, lon)
#
# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
# print(response.json())
# import json
# import requests

#
# def get_avg_for_city(path: str, city: str) -> bool:
#     """Получение сведений температуры за неделю для города"""
#     try:
#         with open(path) as city_file:
#             try:
#                 city_data = json.load(city_file)
#             except json.JSONDecodeError:
#                 print("Ошибка декодирования файла")
#                 return False
#     except FileNotFoundError:
#         print("Файл не найден")
#         return False
#
#     avg_temp = round(sum(city_data[city].values()) / len(city_data[city].keys()), 2)
#     out_data ={
#         city:{
#             'Average temperature': avg_temp
#         }
#     }
#
#     with open("out.json", "w") as out_file:
#         json.dump(out_data, out_file, indent=4)
#
#     return True
#
#
# if __name__ == '__main__':
#   get_avg_for_city("data.json", "Moscow")

# def get_github_repos(username: str) -> list[str]:
#     """Получение списков репозиториев пользователя"""
#     response = requests.get(f"https://api.github.com/users/{username}/repos")
#
#     if response.status_code == 200:
#         repos = [repo["full_name"] for repo in response.json()]
#     else:
#         repos = list()
#
#     return repos
#
# if __name__ == "__main__":
#     repos = get_github_repos('octocat')
#     print(repos)

# a ={
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560",
#     }
# amount = a["operationAmount"]["amount"]
# currency = a["operationAmount"]["currency"]["code"]
#
# if currency == "RUB":
#     print(round(float(amount), 2))
# else:
#     print(float(amount) * 95)
#
# # for transaction in a:
#     if "operationAmount" in transaction and transaction["operationAmount"]["currency"]["code"] == "RUB":
#         if type(['operationAmount']['amount']) == str:
#             ['operationAmount']['amount'] = float(['operationAmount']['amount'])
#         print(['operationAmount']['amount'])
#     else:
#         if type(['operationAmount']['amount']) == str:
#             ['operationAmount']['amount'] = float(['operationAmount']['amount'])
#             print(['operationAmount']['amount'])





# for transaction in a:
#     if type(transaction["operationAmount"]["amount"]) == str:
#         transaction['operationAmount']['amount'] = float(transaction['operationAmount']['amount'])
#         new_list.append(transaction['operationAmount']['amount'])
#     else:
#         new_list.append(transaction['operationAmount']['amount'])
# print(type(new_list[0]))

# for list_new in new_list:
#     if type(list_new) == str:
#         list_new = float(list_new)
#
#         new_list.append(list_new)
# print(new_list)

# a = "25"
# a = float(a)
# print(type(a))
#########################################################################
# import re
# from collections import Counter
#
# def list_dict_operation(list_dict: list[dict[str, str]], search_string: str) -> list[dict[str, str]]:
#
#     pattern = re.compile(search_string)
#     new_list_dict = list()
#     for item in list_dict:
#         b= item.get("state")
#         if b and pattern.match(b):
#             new_list_dict.append(item)
#     return new_list_dict
#
#
# list_sort_data =  [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     ]
#
# print(list_dict_operation(list_sort_data, "EXECUTED"))
#
# def count_operations_by_category(operations: list[dict[str, str]], categories: list) -> dict:
#
#     # all_categories = [operation.get("description") for operation in operations]
#
#     all_categories = list()
#
#     for operation in operations:
#         transaction_category = operation.get("description")
#         all_categories.append(transaction_category)
#
#     category_count = Counter(all_categories)
#
#     # filtered_category_count = {category: category_count[category] for category in categories}
#     filtered_category_count = {}
#     for category in categories:
#         if category in category_count:
#             filtered_category_count[category] = category_count[category]
#
#     return filtered_category_count
#
# operations = [
#     {"id": 1, "amount": 100.0, "description": "groceries"},
#     {"id": 2, "amount": 200.0, "description": "utilities"},
#     {"id": 3, "amount": 50.0, "description": "groceries"},
#     {"id": 4, "amount": 150.0, "description": "entertainment"},
# ]
#
# categories = ["groceries", "utilities", "entertainment", "transport"]
#
# print(count_operations_by_category(operations, categories))

#################

# my_dict = [{'apple': 'red'}, {'banana': 'yellow'}, {'cherry': 'red'}]
# pattern = re.compile(r'red')
# my_list = list()
# for item in my_dict:
#     b = item.get('apple')
#     if b and pattern.match(b):
#         my_list.append(item)
# print(my_list)


# print(list_dict_operation(my_dict, "red"))

# def count_operations_by_category(operations: list[dict[str, str]], categories: list) -> dict:
#     category_count = {category: 0 for category in categories}
#     for operation in operations:
#         category = operation.get("description")
#         if category in category_count:
#             category_count[category] += 1
#     return category_count

#Пример использования функции


# result = count_operations_by_category(operations, categories)
# print(result)

# category_count = {}
# for category in categories:
#     category_count[category] = 0
# print(category_count)
#
# for operation in operations:
#
#     category = operation.get("description")
#     if category in category_count:
#         category_count[category] += 1
#
#
# print(category_count)

##################################

