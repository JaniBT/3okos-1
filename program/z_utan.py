szamok_osszege = 0
szamok_db = 0

with open('../vers/after-z.txt', 'r', encoding='utf8') as f:
    for line in f:
        for karakter in line.strip():
            if karakter == 'Z':
                pass