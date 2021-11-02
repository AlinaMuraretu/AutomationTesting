"""#1.Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
sum = x + y
print ('Display the sum of 5+10 = ', sum)
"""

"""#2. Creați cȃte o variabilă de tipul: string, int și float, după cum urmează:
Variabila de tip int va reține valoarea 20.
Variabila de tip float va reține valoarea 10.
Variabila de tip string reține valoarea “python”.
#se creaza variabila string
name = "python"
print (name)
#se creaza variabila integer
score = 20
print (score)
#se creaza variabila float
result = 10.00
print (result)
"""

"""3. Utilizȃnd funcția type, determinați tipul următoarelor variabile:
restanta = 0
notaFinala = 10.0
laborator = “Introducere in informatica”
print (type(restanta), type(notaFinala), type(laborator))
"""

"""4. Verificaţi dacă un cuvânt este palindrom. Un cuvânt este palindrom dacă scris de la dreapta la
stanga, este tot acel cuvânt.(folositi assert pt verificare)

# Program to check if a word is palindrome or not
word = 'ana'
# make it suitable for caseless comparison
word = word.casefold()
# reverse the word
rev_word = reversed(word)
# check if the word is equal to its reverse
if list(word) == list(rev_word):
   print("The word is a palindrome.")
else:
   print("The word is not a palindrome.")

#varianta2
word = "ana"
rev_word = word[::-1]
if list(word) == list(rev_word):
    print("The word is a palindrome.")
else:
   print("The word is not a palindrome.")
"""


"""5. Remove first n characters from a string (n il cititi de la tatatura)
"Ana are mere" daca n=3 va afisa " are mere"

text = "Ana are mere"
print (text[3:12])

#varianta2
text = "Ana are mere"
n=3
print (text[n:len(text)])
"""



"""5.reads two numbers and multiplies them together and print out their product
x = 3
y = 4
product = 3 * 4
print (product)
"""


"""6.Check if the first and last number of a string  is the same stringul il cititi de la tastatura
sample_str = "alina"
if sample_str[0] == 'a' and sample_str[-1] == 'a':
   print("First and Last character are the same")
else:
   print ("First and Last character are different")
#varianta2
sample_str = "alina"
if sample_str[0] == sample_str[-1]:
   print("First and Last character are the same")
else:
   print ("First and Last character are different")
"""
"""7. Write a program to find how many times substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"

str_x = "Emma is good developer. Emma is a writer"
print (str_x.count("Emma",0,len(str_x)-1))
"""

"""8. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
pt "eu merg la mare" sa imi afiseze "eure"

string = "eu merg la mare"
print (string[0:2] + string[-2:])
"""

"""9. Write a Python program to calculate the length of a string.
pt "eu merg la mare" ->15

string = "eu merg la mare"
print (len(string))
"""

"""10. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'

sample_string = "restart"
print (sample_string.replace("restart","resta$t"))
"""

"""11. Utilizand tipurile de print pe care vi le-am aratat:
afisati in consola I have 1000 dollars so I can buy 3 football for 450.00 dollars.
pt datele
#varianta1
totalMoney = int(1000)
quantity = int(3)
price = float (450)
print ("I have", totalMoney, "dollars so I can buy", quantity, "football for", price, "dollars.")

#varianta2
totalMoney = 1000
quantity = 3
price = 450
print (f'I have {totalMoney} dollars so I can buy {quantity} football for  {price}  dollars.')
print ('I have {} dollars so I can buy {} football for  {} dollars.'.format('1000','3','450'))
print ('I have {0} dollars so I can buy {1} football for  {2} dollars.'.format(totalMoney,quantity,price))
"""

"""12.Build a program to calculate the followings using the input from the user for a, b, c or r 
• triangle area using input
• rectangle area and perimeter
• circle area

# Python Program to find the area of triangle
a = 5
b = 6
c = 7
# Uncomment below to take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

# Python Program to find the circle area
PI = 3.14
# Uncomment below to take inputs from the user
r = float(input("Enter the radius of a circle:"))
# calculate the area
area = PI * r * r
print("Area of a circle = %.2f" %area)

# Python Program to find the rectangle area and perimeter
l=int(input("Length : "))
w=int(input("Width : "))

# calculate the area and perimeter
area=l*w
perimeter=2*(l+w)
print("Area of Rectangle : ",area)
print("Perimeter of Rectangle : ",perimeter)
"""
"""13. Which of the following are valid ways to specify the string literal foo'bar in Python:
• 'foo\'bar’ e ok daca glilimele sunt corecte
""""""""" """foo'bar""” e ok daca glilimele sunt corecte
""""""• "foo'bar” e ok daca glilimele sunt corecte
"""""""• 'foo''bar’ nu e ok daca glilimele sunt corecte
"""""""• 'foo'bar’ nu e ok daca glilimele sunt corecte
"""

"""14.Password checker script
Define a username getting input from the console
Define a password getting input from the console
Display the following message ‘The password for user Paul is
********* is 9 characters long)

#varianta1
username= input("Please enter a username:\n")
password = input("Please enter a password:\n")
print(f'The password for user {username} is {password} is 9 characters long')
"""
""""#varianta2
username = input("Username:")
password = input ("Password")
print ('The password for user', username, 'is', ('*'*len(password)), 'is', len(password), 'characters long')
"""
"""15.Write a program to take three names as input from a user in the single input() function call.

name = input("Enter student's name separated by space:\n").split()
print("Student Name:", name)
"""


"""16. Display float number with 2 decimal places using print() pt num = 458.541315 afisati 458.54
num = 458.541315
print("\nOriginal Number: ", num)
print("Formatted Number: "+"{:.2f}".format(num));
"""







