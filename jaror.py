#!/urs/bin/python3
# -*- coding:utf-8 -*-
"""2013.oktober.18.--adikai erettsegi megoldas Python programozasi nyelven. """
"""1. feladat be kell olvasni az adatokat a jarmu.txt--bol en ezt egy szotarba gondoltam megtenni.
jarmu={ido amikor elmentek{
"rendszam" = TI-2342
"rendszam lista" = ['T','I','-','2','3','4','2']
"rendezett rendszam" = abc sorrendbe rendezett rendszam
 }
}
"""
from datetime import datetime, timedelta
jarmu = {}

with open("jarmu.txt", "rt", encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n","").split(" ")
        alapido = datetime(1999, 1, 1, 0, 0, 0)
        ido = alapido+timedelta(hours=int(sor[0]), minutes=int(sor[1]), seconds=int(sor[2]) )
        jarmu[ido] = {}
        jarmu[ido]['rendszam'] = sor[3]
        jarmu[ido]["rendszam lista"] = []
        for a in sor[3]:
            jarmu[ido]['rendszam lista'].append(a)
        
print(jarmu)
print("2. feladat")
"""Meg kell hatarozni hogy hany orat dolgoztak a rendorok """
munka = list(set([k.hour for k in jarmu.keys()]))
print("{} orat dolgoztak a rendorok. ".format(len(munka)))

print("3. feladat")
"""Minden ora elso jarmuvenek a rendszamat ki kell irni. """
elozo_ora = int()
for k, a in sorted(jarmu.items(), key=lambda k:k):
    for h in munka:
        if k.hour == h:
            if k.hour != elozo_ora:
                print("{0} ora: {1}".format(k,a["rendszam"]))
    elozo_ora = k.hour

print("4. feladat")
"""Rendszam elso karaktere kulon jelentessel bi ha B akkor busz ha K akkor kamion ha M akkor motor tobbi szemelygepjarmu.Meg kell jelenjteni hogy eggyes /
karakterekbol hany haladt el az ellenorzesi ponton. """
jarmuvek ={
    'busz':0,
    'kamion':0,
    'motor':0,
    'kocsi':0
}
for a in jarmu.values():
    for d in jarmuvek.keys():
        if a['rendszam'][0] == "B":
            if d == 'busz':
                jarmuvek[d]+=1
        elif a['rendszam'][0] == "K":
            if d == 'kamion':
                jarmuvek[d]+=1
        elif a['rendszam'][0] == "M":
            if d == 'motor':
                jarmuvek[d]+=1
        else:
            if d == 'kocsi':
                jarmuvek[d]+=1

print(jarmuvek)

print("5. feladat")
"""Mettol meddig tartott a legnagyobb forgalom mentes idoszak meg kell jeleniteni a kepernyon."""

sorban = [k for k in sorted(jarmu.keys(), key=lambda k:k)]
sorban.reverse()
szotar = {}
n = 0
d = True
for a in sorban:
    if n in range(0, len(sorban)-2):
        n+=2
        key = str(sorban[n-1].hour)+":"+str(sorban[n-1].minute)+':'+str(sorban[n-1].second)+' - '+str(sorban[n].hour)+":"+str(sorban[n].minute)+':'+str(sorban[n].second)
        szotar[key] = sorban[n] - sorban[n-1]
li = [k for k,v in sorted(szotar.items(), key=lambda v:v)] 
print(li[-1])
print("6. feladat")
"""Rendorok egy balaese kornyeken latott autot keresnek aminek a hianyzo karakteret csillagal jelolok. """
bekeres = str(input("Kerem irja be a rendszamot es a hianyzo karaktereket helyettesitse * karakterrel."))
rendszamok = [sorted(a['rendszam lista']) for a in jarmu.values()]
beker = sorted([a for a in bekeres])
#print(rendszamok)


print("7. feladat")
"""Minden 5 percben megallitott a rendorseg egy kocsit es ellenorizte ki kell irni fajlba a idot es a rendszamot a szamoknak kell tartalmaznia a 0-akat. """

lista = []
h = -1
for k,v in sorted(jarmu.items(), key=lambda k:k):
    h+=1
    if h == 0:
        lista.append(k)
    lista.append(lista[h]+timedelta(minutes=5))
print(lista)
with open("viszgalt.txt", "wt", encoding="utf-8") as g:
    for a in lista:
        for k,v in sorted(jarmu.items(), key=lambda k:k):
            if k.hour == a.hour and k.minute == a.minute: 
                    g.write("{0} {1} \n".format(k.strftime("%H %M %S"), v["rendszam"]))
