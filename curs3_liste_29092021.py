"""fructe = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
print (fructe[0])
"""


"""fructe = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
legume = ["cartofi", "varza"]
cos = legume[:]
print(cos)
print(fructe[::2])
"""
"""fructe = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
legume = ["cartofi", "varza"]
cos = legume[:]
print(cos)
print(fructe[::2])
"""
""""#adaugare
legume = ["cartofi", "varza"]
legume.append("morcovi")
cos=legume
print(legume)
print(cos)
"""
"""fructe = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
legume = ["cartofi", "varza"]
#concateneaza doua liste
legume.extend(fructe)
print (legume)
"""
""""#stergere element din lista
fructe = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
legume = ["cartofi", "varza",466]
legume.remove(466)
print(legume)
"""
"""
#stergere pozitie
fructe = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
legume = ["cartofi", "varza",466]
legume.pop(2)
print(legume)
"""

"""fructe1 = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
fructe1 = fructe1[3:]
print(fructe1)
"""
"""#sterge toata lista
fructe1 = [["cirese", "caspsuni", 45,78], "banane", "cirese"]
fructe1.clear()
print(fructe1)
"""

"""#sorteaza in ordine crescatoare doar int si float
age = [3, 5, 67, 78.5, 3.6]
age.sort()
print(age)"""

""""#pt polindrom
nume="ioan vasile anton"
print(nume[::-1])
"""
"""fructe = [["cirese", "caspsuni", 45,78], "banane", "cirese",466]
print(fructe[::-1])
"""

"""lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
"""

"""""#verificare element in lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
print(1 in lista)
print(10 in lista)
"""

"""lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
print(1 in lista)
print(10 in lista)
print (lista.index(1))
print()
"""

"""myList = [17, 12, 9, 3, 2]
yourList = myList[-1:1]
print(yourList)
"""
"""myList = [17, 12, 9, 3, 2, 27]
print (27 in myList)"""


"""age = [3, 5, 67, 78.5, 3.6]
print(5 in age)
print(age.count(5))
print(age.count(5)>0)
"""

"""mylist = []
yourlist = mylist[:]
yourlist.append(7)
"""


#Dictionare

"""password = {"yahoo":"ana", "facebook": 123456, "gmail":"122hjg"}
print(password.get("yahoo"))
print(password.items())
print(password.keys())
print(password.values())
print(password.popitem())
print(password)
password.update({"yahoo":"dfg"})
print(password)
"""
"""password = {"yahoo":"ana", "facebook": 123456, "gmail":"122hjg"}
password.update({"emag":"dfg"})
password.update({"yahoo":"fghjkk"})
print (password)
"""

