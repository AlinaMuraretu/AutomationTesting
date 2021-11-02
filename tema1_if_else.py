# o #masina merge pe strada si computerul de bord ne anunta daca suntem pe loc, in localitate, drum judetean sau autostrada
# definim o variabila viteza actuala unde tinem viteza
# si verificam daca e pe loc (0), sau daca e in localitate (unde poti merge cu max 50),
# sau pe drum judetean unde poti merge cu pana in 90, sau pe autostrada unde poti merge cu peste 90
# si printam de fiecare data situatia masinii, unde se afla
# iar daca viteza e cu -, printam valoare invalida

viteza_actuala = 50
if viteza_actuala < 0:
    print('Valoare invalida')
elif viteza_actuala == 0:
    print('Masina sta pe loc')
elif viteza_actuala <= 50:
    print('Masina este in localitate')
elif viteza_actuala <=90:
    print('Masina este pe un drum judetean')
elif viteza_actuala > 90:
    print('Masina  este pe autostrada')
