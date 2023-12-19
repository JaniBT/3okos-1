szamok_osszege = 0
szamok_db = 0

with open('./vers/after-z.txt', 'r', encoding='utf8') as f:
    for line in f:
        for i in range(0, len(line.strip()) - 1):
            if line[i] == "Z":
                szamok_osszege += int(line[i+1])
                szamok_db += 1

eredmeny = szamok_osszege // szamok_db
print(eredmeny)