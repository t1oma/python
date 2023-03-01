import json
#
# f = open("data.json", "w", encoding='utf-8')
# salad = {
#     "Tomato": [5, "Cut"],
#     "Cucumber": [3, "Сheck cucumbers for bitterness", "Cut"],
#     "Salt": "add to taste",
#     "Sugar": False
# }
# text = [False, None, 3.13, 3, (1, 2, 3)]
# json.dump(salad, f) # dump - запись в файл
# # print(json.dump(text)) # перевод в json, но без записи
# f.close()

# f = open("data.json", "r", encoding="utf-8")
# content = json.load(f)
# print(content)
# f.close()

# задача 1

# f = open("file.txt", "r", encoding='utf-8')
# a = f.readlines()
# print(a)
# f.close()
# dame = {}
# for i in a:
#     k = i.split(': ')
#     dame[k[0]] = k[1].rstrip('\n')
# print(dame)
# b = open("data.json", "w", encoding='utf-8')
# json.dump(dame, b, ensure_ascii=False)
# b.close()

# задача 2
# f = open("data.json", "r", encoding='utf-8')
# content = json.load(f)
#
# f.close()
# print(content)
# for i, elem in enumerate(content):
#     a = type(elem)
#     if a == str:
#         content[i] += "!"
#     elif a in (int, float):
#         content[i] += 1
#     elif a == bool:
#         content[i] = not content[i]
#     elif a == list:
#         content[i] *= 2
#     elif a == dict:
#         content[i]["newkey"] = None
# print(content)

import requests

resp = requests.get(url="http://api.open-notify.org/iss-now.json")
data = resp.json()['iss_position']
print(f"Широта: {data['latitude']} Долгота: {data['longitude']}")
