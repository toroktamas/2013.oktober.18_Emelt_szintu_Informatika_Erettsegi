
""" Eltaroljuk egy szotarban:
szotar = {
    datetime(2000, 1, 1, 9, 12, 48): {
        "rendszam": "TI-2342",
        "elozo_utan": timedelta(92356),
        "hanyadik_auto": 1
    },
    {
        ....
    }
}
"""
from datetime import datetime, timedelta

szotar = {}
with open("jarmu.txt", "rt", encoding="utf-8") as f:
    n = 0
    for s in f:
        n += 1
        s = s.replace('\n','').split(' ')
        key = datetime(2000, 1, 1, int(s[0]), int(s[1]), int(s[2]))
        szotar[key] = {}
        szotar[key]['rendszam'] = s[3]
        szotar[key]['hanyadik_auto'] = n

        # kiszamoljuk hogy mikor ment el az elozo - az elso autonal ez sajat maga
        if n == 1:            
            elozo_elment = key
        szotar[key]['elozo_utan'] = key - elozo_elment

        elozo_elment = key  # a kovetkezo menethez meglegyen
        
# print(szotar)

print("2. feladat")

print("{0} orat dolgoztak ma a rendorok.".format(len(set([k.hour for k in szotar]))))

print("3. feladat")

elozo_ora = 0
for k in sorted(szotar):
    if k.hour != elozo_ora:
        print("{0} ora: {1}".format(k.hour, szotar[k]['rendszam']))
        elozo_ora = k.hour

print("4. feladat")

statisztika = {
    "autobusz": 0,
    "kamion": 0,
    "motor": 0,
    "szemelygepkocsi": 0
}

for v in szotar.values():
    if v['rendszam'][0] == 'B':
        statisztika['autobusz'] += 1
    elif v['rendszam'][0] == 'K':
        statisztika['kamion'] += 1
    elif v['rendszam'][0] == 'M':
        statisztika['motor'] += 1
    else:
        statisztika['szemelygepkocsi'] += 1

print(statisztika)

print("5. feladat")

# fent mar kiszamoltam az autok kozotti kozt
elozo_k = datetime(2000, 1, 1, 0, 0, 0)
max_auto_koz = max([v['elozo_utan'] for v in szotar.values()])
#print(max_auto_koz)
for k in sorted(szotar):
    if szotar[k]['elozo_utan'] == max_auto_koz:
        print("{0}:{1}:{2} - {3}:{4}:{5}".format(elozo_k.hour, elozo_k.minute, elozo_k.second, k.hour, k.minute, k.second))
    elozo_k = k
   

print("6. feladat")

keresett = str(input("Adja meg a keresett rendszamot *-al az ismeretlen karaktereket: "))

megfelelo = True
for k, v in szotar.items():
    megfelelo = True
    for i, x in enumerate(keresett):
        #print("{0} {1}".format(i, x))
        if x != '*' and x != v['rendszam'][i]:
            megfelelo = False
    
    if megfelelo:
        print(v['rendszam'])


print("7. feladat")

elozo_ellenorzes = datetime(2000, 1, 1, 0, 0, 0)
with open("vizsgalt.txt", "wt", encoding="utf-8") as f:
    for k in sorted(szotar):
        if elozo_ellenorzes + timedelta(minutes=5) < k:
            f.write("{0} {1}\n".format(datetime.strftime(k, "%H %M %S"), szotar[k]['rendszam']))
            elozo_ellenorzes = k
    




