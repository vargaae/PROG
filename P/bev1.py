from random import randint

def av01_feladat01() -> None:
    szamegyes: int = int(input('elso szam?'))
    szamkettes: int = int(input('masodik szam?'))
    if szamegyes == 0 or szamkettes == 0: return
    eredmeny = (szamegyes+szamkettes)/(szamegyes*szamegyes)
    print(f'[({szamegyes}+{szamkettes})/({szamegyes}*{szamkettes})={eredmeny}]')
    if eredmeny % 1 == 0: print(f'egesz')
    else: print(f'valos')
    
av01_feladat01()


def av02_feladat01() -> None:
    szul_ev: int = int(input('mikor szulettel?'))
    if szul_ev > 2023:
        print('Hibás érték!')
        return
    print(f'2023ban {2023-szul_ev} eves leszel/voltal')
    
# av02_feladat01()


def av03_feladat01() -> None:
    valasz_lista:list[int] = []
    alphabet: str = 'ABCDEF'
    op: str = ''
    for i in range(6):
        valasz_lista.append(int(randint(2, 5)))
        op += f'{alphabet[i]*valasz_lista[i]} '
        
    print(f'f1 output: {op}')
    
av03_feladat01()


def av04_feladat01() -> None:
    valasz: str = (input('j vagy ly van a to_ás szóban?')).lower()
    if valasz == "j":
        print('Helyes válasz!')
        return
    else: print(f'Hibás válasz')
    
# av04_feladat01()