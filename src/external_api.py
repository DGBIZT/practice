import requests
from utils import get_for_city
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
def transaction_amount(transaction_list: list) ->list:
   """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
   new_list = []
   for transaction in transaction_list:
      if 'operationAmount' in transaction and transaction['operationAmount']['currency']['code'] != "RUB":
         to_forex = "RUB"
         from_forex = transaction['operationAmount']['currency']['code']
         amount_forex = transaction['operationAmount']['amount']

         url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_forex}&from={from_forex}&amount={amount_forex}"

         payload = {}
         headers = {
            "apikey": f"{api_key}"
         }

         response = requests.request("GET", url, headers=headers, data=payload)

         # status_code = response.status_code
         result = response.text
         json_data = json.loads(result)
         transaction['operationAmount']['amount'] = json_data["result"]
      new_list.append(transaction['operationAmount']['amount'])
   return new_list

transaction_json_list = get_for_city("data/operations.json")

print(transaction_amount(transaction_json_list))

