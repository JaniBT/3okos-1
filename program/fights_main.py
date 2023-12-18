X_szama = Y_szama = W_szama = 0
with open('./vers/count-x-y-w.txt') as f:
    for line in f:
        for karakter in line.strip():
            if karakter == 'X':
                X_szama += 1
            elif karakter == 'Y':
                Y_szama += 1
            elif karakter == 'W':
                W_szama += 1
            
eredmeny = X_szama + Y_szama - W_szama
print(eredmeny)