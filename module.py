from os import system
from random import randint
from time import sleep

def koszon(nev:str, napszak:str) -> None:
    print(f"Szia {nev}!")
    valasz:str = input(f'Hogy vagy ma {napszak}? ')
    if 'jól' in valasz:
        print(f'Örömmel hallom!')
    elif 'szarul' in valasz:
        print(f'Sajnálattal hallom... :(')
    else: print('k, az jo')


def kerdes() -> bool:
    rsz:int = randint(1, 10)
    ered:int = int(input(f'mennyi {rsz} négyzete?:'))
    if rsz**2 == ered:
        return True
    else:
        return False


def befejezes(nev:str) -> None:
    print(f'rendben {nev}, mára végeztünk!')
    print('Viszont látásra!')
    for x in range(3):
        print(end=f'{3-x}')
        for y in range(3):
            print(end='.')
            sleep(.5)
        system('cls')
