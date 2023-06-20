import random
import time
sozluk = {}
with open("kelimeler.txt","r",encoding="utf-8") as file:
    kelime = []
    for i in file:
        i = i.strip()
        i = i.split(":")
        kelime.append(i)

for i,j in kelime:
    sozluk[i]=j

while True:
    sec = input("Seçim Yap:")
    if sec.lower() == "q":
        break
    elif sec == "1":
        anahtar = random.choice(list(sozluk.keys()))
        deger = sozluk[anahtar]
        print(anahtar)
        time.sleep(4)
        print(deger)
    elif sec == "2":
        anahtar = random.choice(list(sozluk.keys()))
        deger = sozluk[anahtar]
        print(deger)
        time.sleep(4)
        print(anahtar)
    else:
        print("yanlış bir tuş girdiniz")



