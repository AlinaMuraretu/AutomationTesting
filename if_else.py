"""
este o structura care evalueaza niste conditii de sus in jos, iar in momentul in care o gaseste pe prima adevarata executa codul corespunzator acesteia
"""
#calculeaza impozitul la o masina
cm_cubi = 2400
impozit = 0
if cm_cubi < 0:
     print('Date invalide') #daca conditia este adevarata se executa zona aceasta de cod care este aliniata (indentata)
elif cm_cubi <=50: #optional, si putem pune oricate avem nevoie
    print('motocicleta')
    impozit = 50
elif cm_cubi <=2000:
    print('masina mica')
    impozit = 160
else: #in toate celelalte cazuri, optional si putem pune doar maxim unul
    print('masina mare')
    impozit = 700
print(f'Impozitul este {impozit}')

afara_ploua = False
if afara_ploua==True: #== este operator de comparare, intoarce True daca stanga este egal cu dreapta
    print('Umbrela')
else:
    print('ochelari de soare')
#!= verifica daca stanga este diferit de dreapta

if afara_ploua!=True: #True!=True => nu, atunci nu se executa linia 28 si trece la linia 29
    print('ochelari de soare')
else:
    print('umbrela')

#assert verifica daca conditia estre True
assert cm_cubi > 0

#Verificati daca x este intre -5 si 13
x = 15
if x >= -5 and x <= 13:
    print('corect')
else:
    print('incorect')

#prezenta sedinta ori cu mama, ori cu tata, ori cu bunica si bunicu
mama = False
tata = True
bunica = True
bunicul = False
if mama or tata or (bunica and bunicul): #daca este indeplinita minim una din conditii este buna pentru noi
    print('corect')
else:
    print('gresit')

#verificati daca x are minim 4 cifre
#valoare n = 1000
#gresit n = 999
n = 888
if n >= 1000 or n <=-1000:
    print('n are minim 4 cifre')
    raspuns = True
else:
    print('n nu are 4 cifre')
    raspuns = False
assert raspuns == True    #n nu are 4 minim cifre
