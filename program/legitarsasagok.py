import pprint

legitarsasagok_neve = []

with open('./flights/legitarsasagok.txt', 'r', encoding='utf-8') as file:
    file.readline()
    for line in file:
        adatok = line.strip().split(',')
        legitarsasag = {"carrier_name": adatok[3]}
        legitarsasagok_neve.append(legitarsasag)

legitarsasagok_neve_uj = []

mar_latott_nevek = set()

for legitars in legitarsasagok_neve:
    nev = legitars["carrier_name"]
    if nev not in mar_latott_nevek:
        mar_latott_nevek.add(nev)
        legitarsasagok_neve_uj.append(legitars)
        
# pprint.pprint(legitarsasagok_neve_uj)

with open("legitarsasagokneve.txt", "w", encoding="utf-8") as file:
    for sor in legitarsasagok_neve_uj:
        print(sor["carrier_name"], file=file)

legitarsasagok_adatai = []
'''
with open('./flights/legitarsasagok.txt', 'r', encoding='utf-8') as f:
    for sor in f:
        adatok = sor.strip().split(',')
        legitars = {"year": adatok[0], "month": adatok[1], "carrier": adatok[2], "carrier_name": adatok[3],"airport": adatok[4], "airport_name": adatok[5], "arr_flights": adatok[6], "arr_del15": adatok[7], "carrier_ct": adatok[8], "weather_ct": adatok[9], "nas_ct": adatok[10], "security_ct": adatok[11], "late_aircraft_ct": adatok[12],"arr_cancelled": adatok[13], "arr_diverted": adatok[14], " arr_delay": adatok[15], "carrier_delay": adatok[16],"weather_delay": adatok[17], "nas_delay": adatok[18], "security_delay": adatok[19], "late_aircraft_delay": adatok[20]}
        legitarsasagok_adatai.append(legitars)
        
pprint.pprint(legitarsasagok_adatai)
'''