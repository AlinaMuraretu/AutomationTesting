# #while si do
# executa cat timpt ()
# {
#

#WHILE
# # n = int(input('numarul este: '))
# n=3
# sum = 0
# i = 0
# while i != n+1:
#     sum = sum+i
#     i = i+1
# print(sum)
#
# #exemplu cu for
# for i in range(0,n+1):
#     sum =sum+i
#
#Exercitii
#1.printeaza toate numerele  mai mici de 20 divizibile cu 3 si cu 2
#n = 19
# #nr_div = 0
# for i in range(0,20):
#     if i%3==0 and i%2==0:
#         print(i)

# i=0
# while i < 20:
#     if i%3 == 0 and i%2 == 0:
#         print(i)
#     i = i + 1

#2.avem o lista de numere, iar din lista vrem sa aflam suma nr mai mari decat 30
# lista = [5,6,40,30,10,389]
# suma = 0
# for element in lista:
#     if element > 30:
#         suma = suma+element
# print('suma este:', suma)

#varianta de while
# lista = [5,6,40,30,10,389]
# suma = 0
# i = 0
# while i < len(lista):
#     if lista[i] > 30:
#         suma = suma+lista[i]
#     i=i+1
# else: #exista si else la while, intai printeaza cucurigu si apoi suma
#     print('cucurigu')
# print('suma este:', suma)

# while 20<30:
#     print('hello') # merge la infinit,
#
# for i in range(10):
#     if i ==7:
#         print(7)
#     print('The number is:', i)

# lista  = ['ana','vasile','edfgggjjjj', '3%#dd4j', 'paul']
# for cuvant in lista:
#     print(cuvant)
#     if len(cuvant) == 7:
#         print(cuvant)
#         break


# lista  = ['ana','vasile','edfgggjjjj', '3%#dd4j', 'paul','FFD', 'WERRTRE']
# for i in range(len(lista)):
#     print(lista[i])
#     if lista[i][0:1].isdigit():
#         continue
#     lista[i] = 'a' +lista[i][1:]
# print(lista)

#3.Print:(numarul ultimelor stelute il citim de la tastatura - aici e 5

# n = int(input('enter your number:'))
# for i in range(0,n+1):
#     print('*'*i)

n = int(input('enter your number:'))
i = 0
while i<=n:
    print('*'*i)
    i=i+1

 #4.este o fraza si la freaza respectiva , toate cuvintele care nu incep cu litera mare sa pun ana

# fraza = 'ana are mere Si Pere In cos'
# i = 0
# cuvant = 0
# lista = fraza.split()
# print(lista)
# while i < len(lista):
#     print(lista[i].istitle())
#     if not lista[i][0].isupper():
#         lista[i] = 'ana' + lista[i]
#     i = i+1
# print(lista)