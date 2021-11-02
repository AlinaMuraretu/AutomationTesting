# 1.Using while loop, if statement and str() function;
#  iterate through the list and if there is a 100, print it with its index number. i.e.: "There is a 100 at index no: 5"
#  lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

# lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# i = 0
# while i < len(lst):
#     if lst[i] == 100:
#         print('There is a 100 at index no: ' + str(i))
#     i = i+1



# 2.Write a python program to find the sum of all even numbers from 0 to 10 (nr pare)

# sum = 0
# i = 0
# while i <= 10:
#     if i%2 == 0:
#         sum = sum + i
#     i=i+1
# print(f'The sum o all even number from 0 to 10 is: {sum}')


# 3. Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’
# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
# c=int(input("Enter the number"))
# lista = [a,b]
# i = 1
# while i < len(lista):
#     if lista[0] % c == 0 and lista[1] % c == 0:
#         print(f'numbers {i}')
#         i+=1



# 4.Print the following patterns using loop:
# a.
#     *
#    **
#  ****
# *****

# b.
# 1010101
# 10101
# 101
# 1
#
# i = 7
# s = 0
# k=3
# while (i>=0 and k>=0):
#         a=(''*s+"10"*k+"1"+" "*s)
#         print(a)
#         k=k-1
#         i=i-2
#         s=s+1

# 5.Write a Python program to reverse a number.13456 -> 65431

# num = 13456
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print("Reversed Number: " + str(reversed_num))


# # 6.Write a program to display the first 7 multiples of 7.
# i = 0
# while i < 49:
#     if i % 7 == 0:
#         print(i)
#     i = i + 1
