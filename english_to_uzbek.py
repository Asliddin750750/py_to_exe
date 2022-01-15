import json
import random

uz = open('./uz.json')
en = open('./en.json')

uz_data = json.load(uz)
en_data = json.load(en)

en_list = []
for k in en_data:
    en_list.append({k: en_data[k]})

total = 0
count = int(input("Testlar soni: "))
while count > len(en_list):
    count = int(input("Buncha so'z mavjud emas. Iltimos qaytadan kiriting: "))

en_random = random.sample(en_list, count)

i = 1
for j in en_random:
    for k, v in j.items():
        print(f"{i}.{v}")
        answer = input("Javob: ")
        if answer.lower() == uz_data[k].lower():
            total = total + 1
    i = i + 1
    print()

print(f"Jami: {total} ta to'g'ri javob")



