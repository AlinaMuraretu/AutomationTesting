# print('Hello automation testers', 'Hello world', sep='***', end='\n')
# print('Hello automation testers', 'Hello world', sep='***', end='', file=sys.stderr) #imi da eroare
"""

"""""""
learing functions
"""
def my_print(message = 'hello world'):
    """
    printing data
    :return:None
    """
    print(f'My custom message is {message}')
"""
my_print()
my_print('test')
print(my_print.__doc__)
"""

"""
Exercise3
"""

def say_hello(name = 'John Doe', emoji=':)'):
   return f'Hello {name},I hope you have a {emoji} day'
x = say_hello()
print(x)

my_print()
