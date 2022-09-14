import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
# кладет всю переменную в объект
obj = json.loads(json_text)
# обращается к большой части, после к 2 элементу объекта, после к параметру message
print(obj['messages'][1]['message'])

