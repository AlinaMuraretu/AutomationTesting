# dictionar / disctiona / dict
# masina = metoda de transport
#https://www.w3schools.com/python/python_dictionaries.asp
# este o structura de date in care tinem perechi de valori - cheie:valoare
# este ca o lista dar in loc de index, folosim niste porecle

# MediaiMate = {
#     'Andy': 7,
#     'Alina': 10,
#     'Larisa': 8,
#     'Bianca': 8,
#     'Roxana': 8
# }
# print(MediaiMateMate)
#
# "string" #alte limbaje de programare
# #char 'c'#alte limbaje de programare
#
# noteMate = {
#     'Andy': [7, 6, 8, 9], # putem avea ce tip de date vrei noi atat la cheie cat si la valoare
#     'Alina': [10, 10, 10, 9],
#     'Larisa': [9,7,9],
#     'Bianca': 8,
#     'Roxana': 8
# }
# print(noteMate)
# premiantiClasei = {1:'Alina', 2:['Larisa','Bianca','Roxana'], 3: 'Andy'}
# print('premiantiClasei', premiantiClasei)
#
# #problema: cum vedem doar premiul 1?
# print('premiul 1 este', premiantiClasei[1])
#
# #probleme: cum modificam valorile unor chei? marire de nota pt Larisa din 8 in 9
# mediaMate['Larisa'] = 9
# print('printam doar media Larisei', mediaMate['Larisa'])

# de la Andy
mediaMate = {
    'Andy': 7,
    'Alina': 10,
    'Larisa': 8,
    'Bianca': 8,
    'Roxana': 8
}
print('mediaMate este', mediaMate)

noteMate = {
    'Andy': [7, 6, 8, 9], # putem avea ce tip de date vrem noi atat la cheie cat si la valoare, in f de nevoi
    'Alina': [10, 10, 10, 9],
    'Larisa': [9, 7, 9],
    'Bianca': 8,
    'Roxana': 8
}
print('noteMate sunt', noteMate)
premiantiiClasei = {1: 'Alina', 2: ['Larisa', 'Bianca', 'Roxana'], 3: 'Andy'}
print('premiantii clasei sunt', premiantiiClasei)

# problema: cum vedem doar premul 1? (2 metode)
print('premiul 1 este', premiantiiClasei[1])
print('premiul 1 este - metoda2', premiantiiClasei.get(1))


# problema: cum modificam valorile unor chei? marire de nota pt Larisa, din 8 in 9
mediaMate['Larisa'] = 9
print('printam doar media Larise', mediaMate['Larisa'])

#prblema: sa adaugam o noua pereche cheie: vine un elev nou inclasa
mediaMate['Lore'] = 9
print('printam iar media la mate dupa ce adaugam  o noua persoana(cheie', mediaMate)

#problema: pleaca un elev din clasa, deci va trebui sa eliminam cheia corespunzatoare (2 variante)
mediaMate.pop('Andy')
del mediaMate['Lore']
print('media fara Andy si Lore', mediaMate)

#SETS
#un set este o structura de date in care elementele au voie sa apara o singura data
#intr-un set nu conteaza ordinea, toate au aceeasi importanta => elementele se vor afisa aleatoriu
fructe = {'apple', 'banana', 'cherry', 'apple'}
print('printam fructe',fructe) #observam ca apple apare o singura data desi este definit de 2 ori din greseala

#adaugam elemente
fructe.add('apple') # daca exista deja nu se mai adauga
fructe.add('watermelon')
print('fructe dupa de adaugam pepene', fructe)

fructe2 = {'apple','orange'}
print('uniunea dintre seturi', fructe.union(fructe2))
print('intersectia dintre seturi', fructe.intersection(fructe2))
print('diferenta dintre seturi', fructe2.difference(fructe))#diferenta din pespectiva fructe2

#TUPLES
#tuple = structura de date in care elementele nu pot fi schimbate, adaugate/sterse, ulterior
#este ca o lista dar IMUTABILA
#poate avea de mai multe ori acelasi element
#este ordonata, deci are index
reteta_bunicii = (
    '1 L de apa plata',
    'zeama de lamaie dintr-o lamaie stoarsa',
    'o lingurita de miere',
    'o frunza de menta',
    'o frunza de menta'
)
print('reteta bunicii limonada',reteta_bunicii)
print('ce pun prima data?', reteta_bunicii[0])# un element se poate accesa prin index ca intr-o lista

# nu putem modifica reteta
# reteta_bunicii[0] = '2 L de apla plata' => NE DA EROARE
# print('verificam daca am reusit sau nu sa schimbam elementul 0', reteta_bunicii)

# putem cauta un index
print('ce index are menta?', reteta_bunicii.index('o frunza de menta'))

# sa numaram de cate ori apare un element
print('cate frunze de menta punem?', reteta_bunicii.count('o frunza de menta'))

if 'o lingurita de miere' in reteta_bunicii:
    print('limonada va fi dulce')
else:
    print('limonada este acrisoara')


#declara si afiseaza 3 tari cu capitalele lor
capitaleleLumii = {
    'Romania': 'Bucuresti',
    'Franta': ' Paris',
    'Italia': 'Roma'
}
print(capitaleleLumii)
print('Capitala Italiei este:', capitaleleLumii['Italia'])
print('Capitala Italiei este:', capitaleleLumii.get('Italia'))
capitaleleLumii['Spania'] = 'Madrid'
print((capitaleleLumii))
capitaleleLumii.pop('Romania')
print(capitaleleLumii)

#configuratorul culorilor unei masini
culori = {
    'alb',
    'rosu',
    'rosu',
    'albastru'
}
print(culori)
culori.add('galben')
print(culori)
culori.remove('rosu')
print(culori)
culori2 = {
    'galben',
    'alb',
    'negru'
}
print(culori2.issubset(culori)) #un subset cuprinde toate elementele din set(initial: galben si alb (True), galben, alb si negru (False)

#afiseaza coordonatele unei locatii
coordonate = (
    123,
    876
)
#de aratat 3 puncte de pe harta cu latitudine si longitudine
harta = [
    (123, 344),
    (765, 785),
    coordonate,
    {'cluj': (674, 536)}
]
print(harta[3]['cluj'][1])
#3 - ne da un dictionar
#in cadrul dictionarului putem naviga pe chei, Cluj
#cheia cluj ne da ca si valoare un tuplu (674,536)
# intr-o tupla se poate pune o alta lista[] sau tupla()
#in tuplu putem naviga cu index, [1] ne va da 536

print(harta[2][0])

#selectez ce vreau dau ctrl si click si ma duce unde vreau
