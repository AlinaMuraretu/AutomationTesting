#tema nefacuta

# 15 Given a dictionary of food keys and topping values, modify and return the dictionary as follows:
# if the key "potato" has a value, set that as the value for the key "fries".
# If the key "salad" has a value, set that as the value for the key "spinach".
# {"potato": "ketchup"} → {"fries": "ketchup", "potato": "ketchup"}
# {"potato": "butter"} → {"fries": "butter", "potato": "butter"}
# {"salad": "oil", "potato": "ketchup"} → {"salad": "oil", "fries": "ketchup", "spinach": "oil", "potato": "ketchup"}
#
# Rezolvare:

# dictionary = {"potato": "ketchup", 'castraveti': 'muraturi'}
# print(dictionary.keys())
# if 'potato' in dictionary.keys():
#     dictionary.update({'fries': dictionary[' potato']})
#     print(dictionary)

#Andrei
# dictionary = {"potato": "mustard" , "castraveti" : "muraturi"}
#
# print( dictionary.keys())
#
# if "potato" in dictionary.keys():
#     dictionary.update({"fries": dictionary["potato"]}) ##Andrei

# dictionary1 = {"salad": "oil", "potato": "ketchup"}
# if 'salad' in dictionary1. keys():
#     dictionary1.update({'spinach': dictionary1['salad']})
#     print(dictionary1)
#
# 5.Write a Python program to check the validity of password input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
#
# Rezolvare:
#password = input('Please enter the password: ')
#if 6 <= len(password) <= 16: #o prima varianta
#if len(password) in range(6,17): #alta varianta
#password = 'Start193'
#numarul_literelor_mici >=1, numarul_literelor_mari >= 1, numarul_caracterelor_speciale>=1, numarul_numerelor >=1
# numarul_literelor_mari = 0
# numarul_literelor_mici = 0
# numarul_caracterelor_speciale = 0
# numarul_cifrelor = 0
# if len(password) >= 6 and len(password) <= 16: # alta varianta
#     for character in password:
#         if character.isdigit(): #isdigit se refera la numere
#             numarul_cifrelor = numarul_cifrelor + 1
#         if character.islower():
#             numarul_literelor_mici = numarul_literelor_mici + 1
#         if character.isupper():
#             numarul_literelor_mari = numarul_literelor_mari + 1
#         if character in ['#', '@', '.']: #isalpha pt toate caracterele
#             numarul_caracterelor_speciale = numarul_caracterelor_speciale + 1
#
#     if numarul_cifrelor == 0:
#         print('trebuie sa ai cel putin un nr in parola')
#     if numarul_literelor_mici == 0:
#         print('trebuie sa ai cel putin o litera mica')
#         if numarul_literelor_mari == 0:
#             print('trebuie sa ai cel putin o litera mare')
#             if numarul_caracterelor_speciale == 0:
#                 print('trebuie sa ai cel putin un caracter special')
# else:
#     print('nu are numarul necesar de caractere')


#exercitii noi

#pentru toate nr de la 20 la 60 sa se afle suma nr pare dintre ele
# suma = 0
# for i in range(20,60):
#     if i % 2 == 0:
#         suma = suma+i
# print(suma)

#pentru fiecare din intervalul 1 si 10 sa se afiseze toate nr inmultite pana la el
# m = 1
# for nr in range(1,11):
#     m = m*nr
#     print(f'nr factorial {nr} este {m}')

#printati doar valorile care au prima litera d
dictionar = {'ana' : 'femeie', 'vasile' : 'barbat', 'alexandru' : 'dragon', 'vlad': 10}
for i in dictionar.values():
    if i.isalpha():
        if i[0] == 'd':
            print(i)






