from random import randint

def av03_feladat01() -> None:
    valasz_lista:list[int] = []
    abc:str = "ABCDEF"
    op = ""
    for i in range(6):
        valasz_lista.append(int(randint(2, 5)))
        # print(f'{abc[i]*valasz_lista[i]}')
        op += f'{abc[i]*valasz_lista[i]} '
    print(f'{op}')
        
        
av03_feladat01()