from random import randint

def feltolt(elemszam:int=100, legisebb:int=10, legnagyobb:int=99) -> list[int]:
    lst:list[int] = []
    for _ in range(elemszam):
        vsz:int = randint(legisebb, legnagyobb)
        lst.append(vsz)
    return lst


def kiir(lst:list[int], sortores:int = 10) -> None:
    for i in range(len(lst)):
        print(f'{lst[i]}', end=' ')
        if (i+1) % sortores == 0: print(end='\n')


def random_karakter() -> chr:
    karakterek:str = [
        '23456789',
        'ANCDERGHJKMNPQRSTWXYZ'
        'abcdefghjkmnpqrstwxyz'
        '_()[]<>#!$%+&@*?']
    ki:int = randint(0, len(karakterek)-1)
    return karakterek[ki][randint(0, len(karakterek[ki])-1)]


def random_jelszo(hossz:int = 8) -> str:
    pwd:str = ''
    for _ in range(hossz):
        pwd += random_karakter()
    return pwd
