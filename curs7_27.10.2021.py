# #FUNCTII
# def addition():
#     'this make an addition of two number'
#     a = 5
#     b = 6
#     print('prima suma',a+b) # nu face nimic si trebuie sa o apelez prin addition()
#
# def sum():
#     suma = 0
#     for i in range(5):
#         suma = suma+i #merge si cu sum+ = i
#     #print(suma)
#     return(suma)
#
#
# def prod():
#     produs = 1
#     for i in range(1,5):
#         produs = produs*i #merge si cu sum+ = i
#     #print(produs)
#     return(produs)
#
# def summaTotala():
#     print(sum() + prod())
#
# addition()
# sum()
# prod()
# summaTotala()

# def addition(a,b):
#     'this make an addition of two number'
#     print('prima suma',a+b) # nu face nimic si trebuie sa o apelez prin addition()
# addition(100,100)


# def sum(n):
#     suma = 0
#     for i in range(n):
#         suma = suma+i #merge si cu sum+ = i
#     #print(suma)
#     return(suma)
#
# sum(555)

# def person(name, age, high):
#     print(f'{name}, has {age} year(s) old and is {high} high')
# person('Ana', 4, 90)#trebuie sa le dam pe toate si in ordine ca la def person

# def person(name='John', age=5, high=5):
#     if (age<18):
#         print('is little')
#     print(f'{name}, has {age} year(s) old and is {high} high')
# person(high=23, age=34,name='dgf')#trebuie sa le dam pe toate si in ordine ca la def person


# Exemplu1
# def sum(*num):#sau arg
#     sum = 0
#     for i in num:
#         sum = sum+i
#     print(sum)
#
# sum(1,2,3,4)


# # exemplu 2
# def person2(**student):
#     print('name is', student['name'])
#
# person2(name='ana')


#OOP programare orientata pe obiect (object oriented programing)

# class Dog: #clasa e tot timpul cu litera mare, tot timpul o sa aiba o funtie init(ne ajuta sa construim clasa caine, self se refera la obiectul in sine
#     def __init__(self, name, age):
#         pass
#
#
# spark = Dog() # ca si la functie se apeleaza
#
# print(spark)

# class Dog: #clasa e tot timpul cu litera mare, tot timpul o sa aiba o funtie init(ne ajuta construim clasa caine, self se refera la obiectul in sine
#     def __init__(self, name, age, rasa):
#         #pass
#          self.name = name
#          self.age = age
#          self.rasa = rasa
#
#     def latra(self):
#         print('ham ham')
#
#     def dogInfo(self):
#         print(self.name + ' is ' + str(self.age) + ' year(s) old')
#
#     def birthday(self):
#         self.age = self.age + 1
#
# spark = Dog('Spark',3, 'labrador') # ca si la functie se apeleaza
# ozzy = Dog('Ozzy', 5,'lup')
# rex = Dog('rex',2, 'shitsu')
# # ozzy.age = ozzy.age + 1
#
#
# ozzy.latra()
# print(spark.age)
# print(spark.name)
# print(ozzy.name)
# print(spark.rasa)
# #print(ozzy.name + ' is ' + str(ozzy.age) + ' year(s) old')
# ozzy.dogInfo()
# ozzy.birthday()
# spark.dogInfo()
# ozzy.dogInfo()
# rex.dogInfo()



class Figure:
    def __init__(self, lungime=0, latime=0, inaltime=0, raza=0):
        self.lungime = lungime
        self.latime = latime
        self.inaltime = inaltime
        self.raza = raza
    def area(self):
        print(self.lungime*self.latime)


patrat = Figure()
patrat.lungime = 5
patrat.latime = 5
patrat.area()

