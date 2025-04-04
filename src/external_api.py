import requests
# from utils import get_for_city

# def transaction_amount(rub: str, currency: str, amount: int) ->int:
#    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
#    url = f"https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={currency}&amount={amount}"
#
#    payload = {}
#    headers = {
#        "apikey": "4eqwQKlbHSqkmPa0xAJQamC7lY4sszYL"
#    }
#
#    response = requests.request("GET", url, headers=headers, data=payload)
#
#    status_code = response.status_code
#    result = response.text




# # a = get_for_city("data/operations.json")
# print(transaction_amount("RUB", "USD", 50))
# # print(a)
a = "RUB"
b = "USD"
c = 25
url = f"https://api.apilayer.com/exchangerates_data/convert?to={a}&from={b}&amount={c}"

payload = {}
headers= {
  "apikey": "4eqwQKlbHSqkmPa0xAJQamC7lY4sszYL"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)