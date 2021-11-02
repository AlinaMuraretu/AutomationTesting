"""
#liste = insiruire de elemente de orice tip, separate de virgula, care se definesc intre paranteze drepte
lista_mea = ['alb', True, 3, 3.14,[1,2,3]]# putem pune orice elemente
print(lista_mea)
cars = ['Volvo', 'Audi', 'Dacia', 'BMW','Trabant']
#elementele au index, index care incepe de la 0
print(cars[1:]) # => Volvo
#slicing - adica parcurgere mai smecherasa, de unde pana unde
print(cars[1:]) # => ['Audi', 'Dacia', 'BMW','Trabant'] (de la unu pana la final}
print(cars[1:3]) # => ['Audi', 'Dacia'] (de la unu pana la 3, dar fara ultimul]
print(cars[0:5:2]) # => ['Volvo', 'Dacia','Trabant'] ( de la 0 la 5 din 2 in 2) - 2 este pasul
print(cars[::-1]) # => ['Trabant', 'BMW', 'Dacia','Audi','Volvo', ] (parcurgem lista invers)
print(cars[3:1:-1]) # => ['BMW, ' Dacia'] (parcurgem invers de la 3 la 1, dar fara ultimul, ultimul fiind 1)

#cateva metode specifice listelor
cars.append('Toyota') #adauga la final inca un element
print(cars) #=>['Volvo', 'Audi', 'Dacia', 'BMW', 'Trabant', 'Toyota']
cars.remove('Trabant') #scoate un element dupa nume (exact asa cum e el)
print(cars) # => ['Volvo', 'Audi', 'Dacia', 'BMW', 'Toyota']
cars.insert(1, 'Porche') #adauga un element la o anumita pozitie
print(cars) #=>['Volvo', 'Porche', 'Audi', 'Dacia', 'BMW', 'Toyota']
ultimul_elemnt = cars.pop() #eliminam ultimul element dar il si returnam (adica il putem salva in variabila
print(ultimul_elemnt) #=>Toyota
print(cars)#>=['Volvo', 'Porche', 'Audi', 'Dacia', 'BMW']
print(cars.index('BMW'))# => 4
cars.append('Volvo') # adauga la final inca un element, Volvo
print(cars.count('Volvo'))# =>2
print(cars.reverse()) #inverseaza lista dar o si salveaza, ca sa vedem rezultatul, mai printam o data lista
print(cars) # =>['Volvo', 'BMW', 'Dacia', 'Audi', 'Porche', 'Volvo']
cars.sort() #sortare alfametica, sortare crescatoare
print(cars)# =>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo']
cars2 = cars.copy() # ne face un backup la lista, salvam lista intr-o noua lista
print(cars2) #=>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo']
cars.clear()  #stergem lista
print(cars) #=> [] (o lista goala)
#PFEW! noroc ca aveam BACKUP, aducem inapoi masinile
cars = cars2.copy() #o aducem inapoi, cum? copiem in cars continutul listei cars2
print(cars) #=>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo'] (lista initiala)
expensive_cars = ['Lamborghini', ' Ferrari']
all_cars1 = cars + expensive_cars # aduna 2 liste
print(all_cars1)
cars.extend(expensive_cars)# modifica cars prin adaugarea elementelor din expensive cars la final
print(cars) #=>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo', 'Lamborghini', ' Ferrari']


print(len(cars)) #=> cate elemente avem in lista adica 8
#Problema: vreau sa printez PENULTIMUL element dintr-o lista
culori = ['alb', 'rosu', 'albastru', 'verde', 'roz']
print(culori[len(culori)-2])
#la fel cu cea des sus
culori = ['alb', 'rosu', 'albastru', 'verde', 'roz']
index = len(culori)-2
print(culori[index])

#lista cu 5 fotbalisti, facem o schimbare , scoatem jucatorul A, si introducem jucatorul B, afisam noua echipa
lista = ['a', 'b', 'c', 'd', 'e']
print(lista)
jucator = input('jucatorul scos este: ')
if jucator in lista:
    lista.remove(jucator)
    print(f'jucatorul {jucator} a fost scos') #daca jucatorul este in lista, la linia  urmatoare il scoatem afara fol metoda remove
else: #altfel
    print('jucatorul nu este pe teren') #afisam o eroare
print(lista)
noul_jucator = input('jucatorul introdus este:' )
if noul_jucator in lista:
    print('jucatorul este deja in teren')
else:
    lista.append(noul_jucator)
    print(f'am introdus jucatorul {noul_jucator}')
print(lista)
"""
#tema
# avand o lista de forme geometrice
# forme = ['cerc', 'triunghi', 'dreptunghi', 'patrat']
# vreau sa imi introduceti in lista, un 'trapez'. Dar acesta sa fie tot timpul pozitionat dupa triunghi. Indiferent unde ar fi acesta
# rezultat: ['cerc', 'triunghi', 'trapez', 'dreptunghi', 'patrat']
# repet, codul trebuie sa mearga la fel de bine, fara alte interventii si pentru o lista care arata asa ['cerc', 'dreptunghi', 'triunghi', 'patrat']
# sau asa ['cerc', 'dreptunghi', 'patrat', 'triunghi']

# forme = ['cerc', 'triunghi', 'dreptunghi', 'patrat']
# index = forme.index('triunghi')
# forme.insert(index+1, 'trapez')
# print(index)
# print(forme)

forme = ['cerc', 'triunghi', 'dreptunghi', 'patrat']
triunghi = bool
if 'triunghi' in forme:
    index = forme.index('triunghi')
    forme.insert(index + 1, 'trapez')
    print(forme)
else:
    print('nu avem triunghi in forme')

