class Dolgozo:
    def __init__(self, row:str):
        tmp:list[str] = row.strip().split(";")
        self.nev:str = tmp[0]
        self.nem:str = tmp[1]
        self.reszleg:str = tmp[2]
        self.belepes:str = int(tmp[3])
        self.ber:str = int(tmp[4])

# --- beolvasás ---
dolgozok:list[Dolgozo] = []
STREAM = open('berek2020mod.txt', encoding='utf-8')
for r in STREAM: dolgozok.append(Dolgozo(r))

# --- sorok szama ---
print(f'dolgozok szama: {len(dolgozok)}')

# --- szélsőérték ---
maxi:int = 0
for i in range(1, len(dolgozok)):
    if dolgozok[i].ber > dolgozok[maxi].ber:
        maxi = i
print('legnagyobb fizu:')
print(f'\tnev: {dolgozok[maxi].nev}')
print(f'\treszleg: {dolgozok[maxi].reszleg}')
print(f'\tber: {dolgozok[maxi].ber}')


# --- kiválogatás ---

ertekesitok:list = []
for d in dolgozok:
    if d.reszleg == 'értékesítés':
        ertekesitok.append(d.nev)
print(f'értékesítésen dolgozok: ')
for e in ertekesitok:
    print(f'{e}')

# --- megszámlálás ---

c:int = 0
for d in dolgozok:
    if d.reszleg == 'értékesítés': c += 1
print(f'értékesítésen dolgozok száma: {c}')

# --- összegzés és/vagy átlag ---

sum:int = 0
for d in dolgozok:
    if d.reszleg == 'értékesítés': sum += d.ber

print(f'értékesítésen dolgozok száma: {sum/c:.2f} ') #

# --- input alapján történő keresés ---

# részleg nevét beírom és kiadja
kr:str = input('kerem egy részleg nevét: ')

itt_dolgozok:list[Dolgozo] = []
for d in dolgozok:
    if d.reszleg == kr: itt_dolgozok.append(d)

if len(itt_dolgozok) == 0: print('nincs ilyen részleg a cégnél')
else:
    mini:int = 0
    for i in range(1, len(itt_dolgozok)):
        if itt_dolgozok[i].ber < itt_dolgozok[mini].ber:
            mini = i
    print(f'{kr} leggyatrabb fizetesu dolgozoja:')
    print(f'\tnev: {dolgozok[mini].nev}')
    print(f'\treszleg: {dolgozok[mini].reszleg}')

kn:str = input('kerek egy nevet: ')
i:int = 0
while i < len(dolgozok) and kn != dolgozok[i].nev:
    i += 1
if i < len(dolgozok):
    print(f'{kn} reszlege: {dolgozok[i.reszleg]}')
else: print('nincs ilyen nevű dolgozó')

# --- osszegzes es/vagy ---


# --- distinct - egyedi kiválasztás ---

reszlegek:list[str] = []

for d in dolgozok:
    if d.reszleg not in reszlegek:
        reszlegek.append(d.reszleg)

print('részlegek')
for r in reszlegek:
    print(f'\t- {r}')

for d in dolgozok:
    if d.reszleg not in reszlegek and d.reszleg:
        reszlegek.append(d.reszleg)

print('részlegek')
for r in reszlegek:
    print(f'\t- {r}')



# RENDEZÉS
# --- egyszerű csere ---

# NASCAR - első futam 1970-es években
