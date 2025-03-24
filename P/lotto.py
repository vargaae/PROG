from random import randint
from time import sleep

# -> "választás"
print("LOTTÓSORSOLÁS")

tipus = '0'
while tipus not in ['5', '6', '7']:
    tipus = input('Milyen lottóhúzást szeretnél emulálni? [5, 6, 7]: ')
tipus = int(tipus)

max_szam = 0
match tipus:
    case 5: max_szam = 90
    case 6: max_szam = 45
    case 7: max_szam = 35

# ------------------
# -> "szelvény"

# 5: 1 -> 90
# 6: 1 -> 45
# 7: 1 -> 35

print('töltsd ki a szelvényt:')
szelveny = []
while len(szelveny) < tipus:
    szam = int(input(f'{len(szelveny) + 1}. szám: '))
    if szam not in szelveny and (1 <= szam <= max_szam):
        szelveny.append(szam)
    else: print('ez a szám nem megfelelő (vagy már megjelölted, vagy határértéken kívül esik)!')

szelveny.sort()
print('a szelvény kitöltése megtörtént.')
print(f'számaid:', end=' ')
for szam in szelveny: print(szam, end=' ')
print(end='\n')

# ------------------
# -> "sorsolás"

nyeroszamok = []
while len(nyeroszamok) < tipus:
    huzott = randint(1, max_szam)
    if huzott not in nyeroszamok:
        nyeroszamok.append(huzott)

nyeroszamok.sort()

print('nyerőszámok:', end= ' ')
for szam in nyeroszamok:
    print(szam, end=' ')
    sleep(2.5)
print(end='\n')

# -> "kiértékelés"
talalatok = 0
for szam in szelveny:
    if szam in nyeroszamok:
        talalatok += 1

print(f'sikeres találataid száma: {talalatok}')
if talalatok == tipus:
    print("az oszt' igen! Telitalálat!")
elif talalatok >= (tipus - 3):
    print("gratulálok, nyertél (valamit)")