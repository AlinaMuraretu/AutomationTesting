# FOR_WHILE AMBELE SUNT CICLURI REPETITIVE / loops

#problema: printam 101 dalmatieni
#rezolvare cu while
#
# i = 1
# while i <= 101: #conditia este supapa de intrare, daca ea este adevarata rezulta se executa codul din while
#     print('dalmatianul cu nr: ' + str(i))
#     i = i+1 #i+=1 - incremenam pe i cu 1. adica in fiecare ciclu il crestem pe i


# #rezolvare cu for pentru dalmatieni
# for j in range(1,102): #pt j de la 1 la 102, (fara ultimul index 102)
#     print(f'dalmatianul cu numarul {j}')

# # while_else exista, dar se fol mai rar, while dr fol daca supapa este inchisa sau conditia e falsa
# bool_var = True
# while bool_var:
#     print('intram o sata aici')
#     bool_var = False
# else:
#     print('else se executa de fiecare data la final')


#Problema: Super mario are 3 vieti. de fiecare data cand moare afisam o viata iar la final afisam game over
# print('start game')
# superMario = 3
# while superMario >=1:
#     print('Continua jocul si pierde o viata')
#     superMario = superMario - 1
# else:
#     print('Game over')

# #exercitiu cu for: numaram de la 0 la 7
# for index in range(8): # daca nu punem de unde sa inceapa incepe de la 0
#     print(index)
#
# #rezolvare cu for pt dalmatieni - numaram din 2 in 2
# for n in range(1,102,2):
#     print(f'dalmatianul cu numarul {n}')

# for each = pentru fiecare element dintr-o lista
# telefoane = ['iphone 7', 'samsung galaxy 10', 'HTC']
# for telefon in telefoane: #telefon este o variabila denumita de noi de obicei la singular
#     print('reducere mare: ' + telefon)

#for each  = pentru fiecare elem dintr-un string (string = ca o lista de caractere)
# nume = 'Andy'
# for litera in nume: #pentru fiecare litera din Andy
#     litera = litera.upper()
#     print(litera)

#for cu else
# for x in 'banana':
#     print(x)
# else:#ca si la while se executa o data la final
#     print('am terminat banata')

# BREAK / CONTINUE
# break = forteaza iesirea din ciclu;
#continue - sare peste executia respectiva, dar continua restul iteratiilor

#problema:printam 101 dalmatieni si il cautam pe Pogo(7) (cautam acul in carul cu fan, iar Pogo e acul)
#varianta break
# for dalmatian in range(1,102):
#     print(f'dalmatianul: {dalmatian}')
#     if dalmatian == 7:
#         print('l-am gasit pe Pogo')
#         break #opreste executia DE TOT

#####tema de gasit pe Pogo cu varianta while

# variata continue: vreau sa nu afisez parintii(7,17 - Perdida)
# for dalmatian in range(1,102):
#     if dalmatian == 7 or dalmatian == 17:
#         continue #opreste DOAR aceasta iteratie; ne trimite la FOR
#     print(f'dalmatianul: {dalmatian}')
#     print('test')
#
######tema acelasi lucru cu while


#luam produse de la tastatura si le adaugam in stoc (lista)pana cand scriem stop
# stoc = [] #declaram o lista goala de produse
# produs = ''#declaram un produs ca si string gol
# while produs != 'stop': #atat timp cat produsul este diferit de stop, vom continua sa luam produse de la tastatura
#     produs = input('introdu produsul in stoc: ') #luam produse de la tastatura si le pastram in variabila produs
#     if produs!='stop':
#         stoc.append(produs)#adaugam produsul in lista stoc
# print(stoc)

#scoatem cu remove valoarea stop
#stoc.remove('stop')

#parsam/parcurgem lista fara ultimul element (folosindu-ne de un for cu range sau folosind slicing)
# for y in range(len(stoc)-1):
#     print(stoc[y]) #print repetitiv al tuturor elementelor din lista, inafara de ultimul

#sau folosind slicing stoc[0, len(stoc)]
#print(stoc[0:len(stoc)-1])

#scoatem ultimul element drint-o lista folosind indexul lui
# stoc.pop(len(stoc)-1) #pop va scoate ultimul element by default, dar putem si sa specificam noi indexu; intre()
# print(stoc)

#scoatem ultimul element dintr-o lista folosind metoda pop (care scoate fix ultimul element)
#stoc.pop()

#nu adaugam stopul in stoc - noi l-am folosit

#ghicitoare de numere
#avem un nr secret
#cerem un nr de la tastatura intre 1 si 30
#daca e mai mic dam indiciu, daca e mai amre la fel
#daca e acelasi, felicitari

# secret = 17
# ghicit = 0
# print('alege un nr intre 1 si 30')
# while secret != ghicit: # jocul incepe cand jucat0rul nu a ghicit nr secret
#     ghicit = int(input())#luam nr de la tastatura si in castam / fortam la int
#     if ghicit < secret:
#         print('alege un nr mai mare')
#     elif ghicit > secret:
#         print('alege un nr mai mic')
#     else:
#         print('Felicitari!')



#
# ###### Tema 24.10.2021:
# # tineti 7 L de benzina intr-o variabila. Atata timp cat masina mai are benzina printati "Acceleram! Vruum Vruum!".
# # De fiecare data cand masina accelereaza se consuma 1 L de benzina. La final, pe un else, afisati "STOP! Nu mai este benzina"
#
# combustibil = 7
# while combustibil > 0:
#     print('Acceleram! Vruum Vruum!')
#     combustibil = combustibil - 1
# else:
#     print('STOP! Nu mai este benzina')

# ######## Tema cu varianta while  pentru problema: printam 101 dalmatieni si il cautam pe Pogo(7) (cautam acul in carul cu fan, iar Pogo e acul)
#
# i=1
# while i <= 101:
#     print(f'dalmatianul: {i}')
#     i=i+1
#     if i == 7:
#         print('l-am gasit pe Pogo')
#         break



# ######## Tema cu variata while: vreau sa nu afisez parintii (7,17 (Perdida))
# i=1
# while i <= 101:
#     if i == 7 or i == 17:
#         i = i + 1
#         continue
#     print(f'dalmatianul: {i}')
#     i = i + 1
#
# #sau avrianta
# i=1
# while i <= 101:
#     print(f'dalmatianul: {i}')
#     i = i + 1
#     if i == 7 or i == 17:
#         continue
#
