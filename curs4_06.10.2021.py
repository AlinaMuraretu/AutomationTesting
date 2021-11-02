"""
recapitulare
"""
"""
#tup-uri
tup(1,2,3)
tup.append(28)
print(tup) #atribute error
"""
"""
if else
"""
#verificam temperatura dintr-o camera

"""temperatura = int(input('Temperatura este: '))
if(temperatura > 20):
    print('este prea cald')
    temperatura = 56
else:
    print('este prea frig')
print(temperatura)
"""
"""
password = input('password: ')
if(len(password) <=7):
    print('parola trebuie sa fie mai mare ca 7')
else:
    if(password.count('.') > 0):
        print('parola contine punct')
    else:
        print('parola trebuie sa contina.')
"""
"""
maleRabbits = int(input('no, of male rabbits:'))
femaleRabbits = int(input('no, of female rabbits:'))
if maleRabbits > 0 and femaleRabbits > 0: #&& inseamna and in alte coduri
    breed = input('Do you want to breed?')
    if breed == 'No':
         print('Keep male and female rabbits apart!')
         
"""
"""
#verifica daca numarul este par sau impar
numar = int(input('Numarul este: '))
if numar == 0:
    print('Numarul trebuie sa fie mai mare decat 0')
elif numar % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')
"""
"""
#citim un string si verificam  daca primele 2 caractere  = ultimele 2 caractere
a = input('cuvantul este: ')
print(a[0:2])
b = len(a)
print(a[b-2:b])

if a[0:2] == a[b-2:b]:
    print('primele 2 caractere  = cu ultimele 2 caractere')
else:
    print('primele 2 caractere nu sunt gale cu ultimele 2 caractere')
"""
"""
#citim 2 numere de la tastatura, daca numerele sunt egale printam dublul sumei lor (2*sum), daca nu sunt egale printam doar suma lor
numar1 = int(input('Alegem primul numar: '))
numar2 = int(input('Alegem al doilea numar: '))
if numar1 == numar2:
    print('dublul sumei este:',(numar1+numar2)*2)
else:
    print('suma este:',  numar1+numar2)
"""
"""
#Write pseudo code that performs the following: Ask a user to enter a number. If the number is between 0 and 10,
# write the word blue. If the number is between 10 and 20, write the word red. if the number is between 20 and 30,
# write the word green. If it is any other number, write that it is not a correct color option.
r = range(20,31)
numar = int(input('Insert number: '))
if numar >=0 and numar<= 10:
    print('blue')
elif 10 < numar and numar <= 20:
    print('red')
elif numar in r: #sau in range(20,31)
    print('green')
else:
    (print('it is not a correct color'))
"""
"""FOR
"""
"""
list = [1,328,6]
for i in list: #i in python nu se declara
    if (i%2 ==0):
        print(i)
"""
for i in range(0,20):
    if (i%2 ==0):
        print(i)

nume = ['ion', 'vasile', 'carmen', 'ana']
for valoare in nume:
    if (valoare[0] =='a'):
        print(valoare)