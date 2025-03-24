# WHILE kisérletezes
szam:int = 1
probalkozasok:int = 0
tipp:int = 0
i = 0
while i < szam:
  i = input('ird')
  if i == 0:
    continue
  print(i)

# while tipp == szam: tipp = int(input('gondoltam egy szamra, probald meg kitalalni!(1 és 100 közötti számra tippelj) '))
# probalkozasok =+ 1
# if tipp == 0 or tipp > 100: tipp = int(input('1 és 100 közötti számra tippelj! '))
# if 0 < tipp < 101: print(f'tipped: {tipp}')
# if tipp > szam: print('tul magas!')
# elif tipp < szam: print('tul alacsony!')
# else: print('eltalaltad!')
# print(f'probalkozasaid szama: {probalkozasok}')

# ------------------------------------

gondolt:int = randint(1, 100)

print('gondoltam egy számra [1, 100] között, próbáld meg kitalálni!')

tipp:int = -1
proba:int = 0
    
while tipp != gondolt:
    tipp:int = int(input('mi a tipped?'))
    if gondolt < tipp: print('nem, ennél kisebb számra gondoltam, próbáld újra!')
    elif gondolt > tipp: print('nem, ennél nagyobb számra gondoltam, próbáld újra!')
    proba += 1
    
print(f'gratulálok, kitaláltad! próbálkozásaid száma: {proba}')