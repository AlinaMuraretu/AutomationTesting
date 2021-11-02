#1. Write a Python program to display astrological sign for given date of birth
#  Expected Output:
# 	Input birthday: 15
# 	Input month of birth (e.g. march, july etc): may
# 	Your Astrological sign is : Taurus

# day = int(input('Birth: '))
# month = input('Month of birth: ')
# if month == 'december':
#     astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
# elif month == 'january':
#     astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
# elif month == 'february':
#     astro_sign = 'Aquarius' if (day < 19) else 'pisces'
# elif month == 'march':
#     astro_sign = 'Pisces' if (day < 21) else 'aries'
# elif month == 'april':
#     astro_sign = 'Aries' if (day < 20) else 'taurus'
# elif month == 'may':
#     astro_sign = 'Taurus' if (day < 21) else 'gemini'
# elif month == 'june':
#     astro_sign = 'Gemini' if (day < 21) else 'cancer'
# elif month == 'july':
#     astro_sign = 'Cancer' if (day < 23) else 'leo'
# elif month == 'august':
#     astro_sign = 'Leo' if (day < 23) else 'virgo'
# elif month == 'september':
#     astro_sign = 'Virgo' if (day < 23) else 'libra'
# elif month == 'october':
#     astro_sign = 'Libra' if (day < 23) else 'scorpio'
# elif month == 'november':
#     astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
# print("Your Astrological sign is :", astro_sign)

#2. Calculate the square of each number from 23 to 67 (putearea a doua)

# for i in range(23,68):
#     square = i**2  # num * num
#     print(square)

# 3. Calculate the average of list of numbers
# numbers = [10, 20, 30, 40, 50] #(media lor - calculam suma, apoi impartim la cate sunt)
# avg_value = int(sum(numbers) / len(numbers))
# print(avg_value)
#
# 4. counts the number of words that contain the letter: "l" in a given string.
# string = input('The string is: ')
# print(string.count('l'))

# # 5. returns the number of words that start with letter "a" in a string.
# str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's" #-> 1
# x = len(str))



# 6. Write a method with a while loop to prints 1 through n in square brackets. For example, if n = 6 print [1] [2] [3] [4] [5] [6]
# Print: (numarul ultimelor stelute il citim de la tastatura - aici e 6
# *
# **
# ***
# ****
# *****
n = ('*')
for i in n:
    print(i*5)

nefinalizata