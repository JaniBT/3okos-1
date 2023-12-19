angol_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uj_angol_abc = angol_abc[16:] + angol_abc[:16]

vers = ''
with open('./vers/caesar.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for ch in line:
            if ch.upper() in angol_abc:
                index = uj_angol_abc.find(ch.upper())
                if ch.upper() == ch:
                    vers += angol_abc[index]
                else:
                    vers += angol_abc[index].lower()
            else:
                vers += ch

print(vers)

with open('versike.txt', 'w', encoding='utf-8') as file:
    print(vers, file=file)