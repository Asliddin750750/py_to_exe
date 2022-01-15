import json
import random

uz = open('./uz.json')
en = open('./en.json')

uz_data = json.load(uz)
en_data = json.load(en)

uz_list = []
for k in uz_data:
    uz_list.append({k: uz_data[k]})

total = 0
count = int(input("Testlar soni: "))
while count > len(uz_list):
    count = int(input("Buncha so'z mavjud emas. Iltimos qaytadan kiriting: "))

uz_random = random.sample(uz_list, count)

i = 1
for j in uz_random:
    for k, v in j.items():
        print(f"{i}.{v}")
        answer = input("Javob: ")
        if answer.lower() == en_data[k].lower():
            total = total + 1
    i = i + 1
    print()

print(f"Jami: {total} ta to'g'ri javob")



