'''
Kasutame:
print(), input(), float(), int(), upper(), lower(), capitalize(), type() funktsioonid
math, random moodulide funktsioonid: pi, round(), randint()
'''

'''
[1]
- Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
- Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
- Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
'''
print("Tere, maailm!")
nimi = input("Palun sisesta oma nimi!: "); print(f"Tervitan sind {nimi}");

try:
    vanus = int(input("Palun sisesta oma vanus!: "))
except ValueError:
    vanus = int(input("Peab olema täisarv! Palun proovida uuesti: "))

print(f"Sa oled {vanus} aastat vana\n")


'''
[2]
Mis tüüpi on järgnevad muutujad:

a) vanus = 18
b) eesnimi = "Jaak"
c) pikkus = 16.5
d) kas_käib_koolis = True
Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
Kirjuta kood tüüpide kontrollimiseks.
'''
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print(f"vanus = 18               -     [TYPE]: {type(vanus)}")
print(f"eesnimi = \"Jaak\"         -     [TYPE]: {type(eesnimi)}")
print(f"pikkus = 16.5            -     [TYPE]: {type(pikkus)}")
print(f"kas_käib_koolis = True   -     [TYPE]: {type(kas_käib_koolis)}\n")

# Näide boolean
print(f"{vanus == 18}")

'''
[3]
- Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). 
Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.

- Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.
'''
from random import randint
num_of_candies = randint(10, 99)
print(
        f"""
        -------------------------
        |                       |
        |           {num_of_candies}          |
        |                       |
        -------------------------
        """
)
wanna_candies = int(input("Kui palju sa tahad võtta kommid?: "))
print(f"Nüüd laual on: {num_of_candies - wanna_candies} kommid\n")


'''
[4]
- Puu läbimõõdu arvutamine
Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu
'''
from math import pi
umbermoodu = int(input("Palun sisesta puu ümbermõõdu: "))
labimoodu = umbermoodu / pi
print(f"Puu läbimõõdu: {round(labimoodu, 3)}\n")


'''
5.
- Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, 
mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
'''
from math import sqrt
n = int(input("Palun sisesta ristkülikukujulike maatüki N(m): "))
m = int(input("Palun sisesta ristkülikukujulike maatüki M(m): "))
diagonaal = sqrt((n ** 2) + (m ** 2))
print(f"Maatüki diagonaal suurus: {round(diagonaal, 3)}\n")


'''
6
- Leidke järgnevast näiteprogrammist loogiline viga:

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print("Sinu kiirus oli " + str(kiirus) + " km/h")
'''
aeg = float(input("Mitu tundi kulus sõiduks?: "))
teepikkus = float(input("Mitu kilomeetrit sõitsid?: "))
kiirus = teepikkus / aeg

print(f"Sinu kiirus oli {round(kiirus, 3)} km/h\n")


'''
[7]
Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.
'''
a, b, c, d, e = int(input("Sisesta 1 arv: ")), int(input("Sisesta 2 arv: ")), int(input("Sisesta 3 arv: ")), int(input("Sisesta 4 arv: ")), int(input("Sisesta 5 arv: "))
keskmine = (a + b + c + d + e) / 5
print(f"\n  {a} + {b} + {c} + {d} + {e}\n -------------------   =  {round(keskmine, 0)}\n          5    \n")

'''
[8]
Joonista samasugune konn
   @..@
   (----)
  ( \__/ )
^^ "" ^^
'''
kass = " @..@\n (---)\n( \\__/ )\n^^ \"\" ^^\n\n"
print(kass)

'''
[9]
- Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. 
Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
'''
print("Arvutame kolmnurga ümbermõõdu")
a, b, c = int(input("Sisesta a: ")), int(input("Sisesta b: ")), int(input("Sisesta c: "))
p = a + b + c
print(f"Kolmnurga ümbermõõdu: {p}\n")


'''
[10]
Pitsa

Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
Jätate teenindajale 10% jootraha.
Koosta programm, mis arvutab, kui palju igaüks peab maksma.
'''
hind = 12.90
inimeste_arv = int(input("Sisestage mitme inimese peale võtate pitsat: "))
jootraha = 12.90 * 0.1
print(f"Jätsite {round(jootraha, 2)} jootraha. Igaüks peab maksma: {round((hind - jootraha) / inimeste_arv, 2)}")

'''
[11]
- Tutvuge õpiku punktiga 1.14 ja kasutage oma koodis konstruktsiooni try-except, 
et vältida programmi kokkujooksmist, kui kasutaja sisestab oodatud tüübi asemel midagi muud.
'''

# ok. Vaata esimene ülesanne
