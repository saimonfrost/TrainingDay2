import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
length = len(response.history) #количество редиректов

print(f'Количество редиректов = {length}')
print(f'Итоговый URL = {response.url}')