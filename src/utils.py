import json

def get_for_city(file_path: str) -> bool:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(f'{file_path}', "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                print([])
                return False
    except FileNotFoundError:
        print([],"...")
        return False

print(get_for_city("data/operations.json"))







