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
import json
import requests

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

def get_github_repos(username: str) -> list[str]:
    """Получение списков репозиториев пользователя"""
    response = requests.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code == 200:
        repos = [repo["full_name"] for repo in response.json()]
    else:
        repos = list()

    return repos

if __name__ == "__main__":
    repos = get_github_repos('octocat')
    print(repos)