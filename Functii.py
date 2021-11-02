# FUNCTII = o bucata de cod care poate fi refolosita ori de cate ori avem nevoie
# parametru = o variabila ce intra in functie cu valori diferite la fiecare apelare (
# return = rezultatul functiei
# atat parametri cat si return-ul sunt optionale
# parametri pot fi oricati in functie de nevoi
# rezultatul este unul singur
# paralela cu o masina de tocat carne - parametri = ce introducem pe deasupra (doar porecla, fara valori)
# apelarea functiei - este ca si cand invartim maneta (se executa logica din interior)
# la final , carnea tocata este rezultatul UNIC, expus prin return
# putem sa punem carnea tocata intr-ul bol ( variabila)

def sum(a, b): # sus definim numele fucntiei si parametrii care are nevoie
    s = a+b # la mijloac rezolvam logica problemei, folosind variabile fara valori
    return s # jos expunem un rezoltat dupa cuvantul rreturn


def sum2(a,b): # varianta scurta a exemplului de deasupra
    return a+b

bol = sum(1, 3) # demonstram ca punem rezultatul unei functii intr-o variabila
print(bol) # printam valoarea variabilei
print(sum2(1,3)) # printam direct prin APELAREA functiei



# EXEMPLE
#1 - functie simpla, fara paraemtri si fara return
def happyBday():
    print('La multi ani!') # printul NU este unr return. nu avem ce salva in variabila
    print('Cu sanatate')

happyBday()
happyBday()

#2. - functie cu param, fara return
def happyBdayX(nume, varsta):
    print(f'La multi ani, {nume}!')
    print (f'Felicitari pentru veritabila varsta de, {varsta} de ani!')

happyBdayX('Andy', 34)
happyBdayX('Crina', 36)
happyBdayX('Ares', 0.3)

#3. - functie fara param dar cu return

def show_pi():
    return 3.14

def zile_sapt():# putem returna orice tip de date cunoscut (ex:lista)
    return['luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']

print(show_pi())
#ctrl+click
print (zile_sapt())

#4 - o functie cu param si return (cea mai folosita)
def ariaDreptunghiului(lungime, latime):
    aria = lungime * latime
    return aria

print(ariaDreptunghiului(10,5))
print(ariaDreptunghiului(20, 10))
print(len('abc'))# ' abc este parametrul functiei len
#len ne returneaza dimensiunea lui 'abc' , adica 3
#rezultatul returnat de len este de fapt parametru pentru fucntia print

#Probleme
#1. - afiseaza nr de litere din numele tau complet (nume, nume mijlociu, prenume)
def nr_litere_nume(nume, mijlociu, prenume):#numele variabilelor nu se scriu nicioadata intre ghilimele
    numar = len(nume) + len(mijlociu) + len(prenume)
    return numar

print(nr_litere_nume('Barbulescu', 'Larisa', 'Elena'))
print(nr_litere_nume('Sinpetrean', 'Daniela', 'Andrei'))
print(nr_litere_nume('Muraretu', 'Alina', 'Maria'))

#2. afisati media a 3 numere
def media_numerelor(a,b,c):
    media = (a+b+c) / 3
    return media
print(media_numerelor(2,3,4))
print(media_numerelor(10,20,30))

#3. afisati daca un trunghi este isoscel, echilateral  sau oarecare
def felul_triunghiului(latura1, latura2, latura3):
    if latura1 == latura2 == latura3:
        return 'Triunghiul este echilateral'
    elif latura1 == latura2 or latura1 == latura3 or latura2 == latura3:
        return 'Triunghiul este isoscel'
    else:
        return 'Triunghiul este oarecare'

print(felul_triunghiului(2,2,2)) #echilateral
print(felul_triunghiului(2,2,6)) #isoscel
print(felul_triunghiului(2,10,2)) #isoscel
print(felul_triunghiului(15,2,2)) #isoscel
print(felul_triunghiului(5,6,7)) # oarecare

