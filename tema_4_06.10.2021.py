"""#1.Take two int values from user and print greatest among them
user_1 = int(input('First value is: '))
user_2 = int(input('Second value is: '))
if user_1 >= user_2:
    print(user_1, 'is greater')
else:
    print(user_2, 'is greater')
"""
"""
# 2.A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
mark = int(input('The mark is: '))
if mark < 25:
    print('Corresponding grade is F ')
elif mark >=25 and mark < 45:
    print('Corresponding grade is E ')
elif mark >= 45 and mark < 50:
    print('Corresponding grade is D ')
elif mark >= 50 and mark < 60:
    print('Corresponding grade is C ')
elif mark >= 60 and mark < 80:
    print('Corresponding grade is B ')
else:
    print('Corresponding grade is A ')
"""

"""
#3.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
quantity = int(input('Quantity is: '))
if quantity*100 > 1000:
    print('Cost is', (quantity*100)-(.1*quantity*100))
else:
    print('Cost is', (quantity*100))
"""
"""
#4.Write an if statement that asks for the user's name via input() function.
#If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print "Good morning NAME". (Replace Name with user's name)

users_name = input("User's name is: ")
if users_name == 'Bond':
    print('Welcome on board 007')
else:
    print(f'Good morning, {users_name}')
"""
"""
# 5.Write a Python program to check the validity of password input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

password = input('The password is: ')
minimum_lenght ==
if (len(password) < 6 or len(password) > 12
    print =
"""

"""
#6.Write a Python program that tells a user that the number they entered is not a 5 or a 6.
number = int(input('Enter the number: '))
list = [5, 6]
if number in list:
    print('The number is a 5 or a 6. Try another number!')
else:
    print('The number is not a 5 or a 6')
"""

"""
# 7.Write an algorithm to print from 1 to 10
for i in range(1, 11):
    print(i)
# print all multiples of 5 between 1 and 100 (including both 1 and 100).
for number in range(1,100):
    if number % 5 == 0:
        print(number)
# read three numbers and writes them all in sorted order.
numere = []
one = numere.append(int(input("Please input a number : ")))
two = numere.append(int(input("Please input a second number : ")))
three = numere.append(int(input("Please input a third number : ")))
for num in sorted(numere):
    print(num)
"""

#8.We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
#Return true if we are in trouble.

# 9.Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.


""""
#10.Given a string, return true if the string starts with "hi" and false otherwise.
string = input('The string is: ')
if string.startswith('hi'):
   print('True')
else:
    print('False')
"""

"""
#11.Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
a = int(input('First number: '))
b = int(input('Second number: '))
sum = a+b
if sum in range(10,20):
    print(20)
else:
    print(sum)
"""
"""


# 12. return the number of 9's in a list
# [1, 2, 9] → 1
# [1, 9, 9 ]→ 2
# [1, 9, 9, 3, 9] → 3
a = [1, 2, 9]
b = [1, 9, 9 ]
c = [1, 9, 9, 3, 9]
for i in a:
    if i == 9:
        print(a.count(i))
for i in b:
    if i == 9:
        print(b.count(i))
for i in c:
    if i == 9:
        print(c.count(i))
       

#13.We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11. 
#Return true if the given non-negative number is special.         
 """

# 14.Modify and return the given dictionary as follows: if the key "a" has a value, set the key "b" to have that same value. In all cases remove the key "c",
# leaving the rest of the dictionary unchanged.
# {"b": "bbb", "c": "ccc", "a": "aaa"} → {"b": "aaa", "a": "aaa"}
# {"b": "xyz", "c": "ccc"} → {"b": "xyz"}
# {"d": "hi", "c": "meh", "a": "aaa"} → {"d": "hi", "b": "aaa", "a": "aaa"}

# 15 Given a dictionary of food keys and topping values, modify and return the dictionary as follows: if the key "potato" has a value, set that as the value for the key "fries". If the key "salad" has a value, set that as the value for the key "spinach".
#
# {"potato": "ketchup"} → {"fries": "ketchup", "potato": "ketchup"}
# {"potato": "butter"} → {"fries": "butter", "potato": "butter"}
# {"salad": "oil", "potato": "ketchup"} → {"salad": "oil", "fries": "ketchup", "spinach": "oil", "potato": "ketchup"}



# #16.Print n asterisks
# n = ('*')
# for i in n:
#     print(i*5)

# 17. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
#  between 1500 and 2700 (both included).
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i,end='; ')

# 18. Write a Python program to count the number of even and odd numbers from a series of numbers.
#  Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# count_odd = 0
# count_even = 0
# for x in numbers:
#     if not x % 2:
#         count_even+=1
#     else:
#         count_odd+=1
# print("Number of even numbers :",count_even)
# print("Number of odd numbers :",count_odd)

# #19. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
# for x in range(6):
#     if (x != 3 and x != 6):
#         print(x,end=' ')

# #20. Print sum of the numbers between 20 and 100
# sum1 = sum(range(20,100))
# print(f'Sum of 20 to 100 is: {sum1}')