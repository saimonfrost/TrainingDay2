import requests

# Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get("https://playground.learnqa.ru/api/compare_query_type")
print(response.text, response.status_code)

# Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response1 = requests.head("https://playground.learnqa.ru/api/compare_query_type")
print(response1.text, response1.status_code)

# Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
payload = {"method": "GET"}
response2 = requests.get("https://playground.learnqa.ru/api/compare_query_type", params=payload)
print(response2.text, response2.status_code)

# С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method

list = ["GET", "POST", "PUT", "DELETE"]
result = []
for n in list:
    payload2 = {"method": n}
    response3 = requests.get("https://playground.learnqa.ru/api/compare_query_type", params=payload2)
    response4 = requests.post("https://playground.learnqa.ru/api/compare_query_type", data=payload2)
    response5 = requests.put("https://playground.learnqa.ru/api/compare_query_type", data=payload2)
    response6 = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data=payload2)
    result.extend((n, response3.text, response4.text, response5.text, response6.text))
print(result)