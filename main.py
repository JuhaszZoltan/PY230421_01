from module import *
from random import randint

nev:str = input('hogy hívnak?: ')
nsz:str = input('milyen napszak van?: ')

koszon(nev, nsz)

print('akkor kezdjük a munkát!')

pont:int = 0
for x in range(5):
    print(f'{x+1}:', end=' ')
    kiert:bool = kerdes()
    if kiert == True:
        print('helyes')
        pont += 1
    else: print('sajnos nem :(')

print(f'találatok száma: {pont}/5')

befejezes(nev)