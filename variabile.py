"""
variabile = zone din memorie, care fac referire la un tip de date / structura de date
incept cu litera mica, nu pot sa contina spatii, pot sa contina numere, dar sa nu inceapa cu numere
(o variabila este o porecla pentru o valuare)
"""
#Principalele 4 tipuri de date
nume_utilizator = "roxana lucuta" #string (str) = sir de caractere delimitat de ghilimele
print(nume_utilizator)
varstaUtilizator = 30 #integer (int) = un numar intreg
inaltimeUtilizator = 1.7 #float (float) = numar zecimal
print(inaltimeUtilizator)
vegetarian = False #boolean (bool) = notiunea de adevarat sau fals
print(3>1)
#ctrl+/ = comenteaza / decomenteaza

#string format (f) = cand vrem sa concatenam / adunam un string cu un numar
print(f'numele este {nume_utilizator} si are varsta de {varstaUtilizator}')  #este  corecta

#print('numele este {nume_utilizator} si are varsta de {varstaUtilizator}')  #este gresit

#print('numele este ' + nume_utilizator + ' si are varsta de ' + str(varstaUtilizator)) #to cast (a casta) = atunci cand schimbam tipul de date il alt timp

#suprascriere = cand ii dam o alta valoare unei variabile existente
varstaUtilizator  = 31
varstaUtilizator = varstaUtilizator + 1 #ctrl+z reda inapoi modificarea
print(varstaUtilizator)

#metode / functii ajutatoare stringuri  (se leaga cu punct cu o variabila)
print(nume_utilizator.lower())

#un sir de caractere este ca o lista, iar fiecare caracter are un index pornind de la zero. Indexul merge in paranteza patrata
print(nume_utilizator[0].upper() + nume_utilizator[1:13])  #[1:] = se numeste slicing, specificam de unde pana unde se afiseaza lista
                                                           # [1: 13]  = daca in slicing nu specificam pana unde mergem atunci se merge pana la final
print(nume_utilizator[::-1]) #parcurgem stringul invers (ex pt palindrom)
print(nume_utilizator[0:13:2]) #parcurgem sirul din 2 in 2

#inlocuim o litera
print(nume_utilizator.replace('r',' '))

print(nume_utilizator.count('uc'))  #numaram de cate ori apare un substring intr-un string

#w3schools.com - site cautare
#stackoverflow - site cautare

nume = 'orice'
print(nume.upper().lower().upper().islower())

#input = metoda care ne ajuta sa luam date de la tastatura; daca nu specificam altceva ele vor ramane string
numar1 = input('alege numarul 1: ') # mesajul dintre paranteze va aparea in Consola / Terminal
numar2 = input('alege numarul 2: ')
print(numar1 + numar2) #va concatena / aduna cele 2 numere ca fiind 2 stringuri (3+7=37)
print(int(numar1) + int(numar2))
print(float(numar1) + float(numar2))
