import math

# decimal (.) precision of 5 for float '0.333'
print('{0:.5f}'.format(90/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^13}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python')) 
print(' ')
print('{name} was {age} years old when he gave her a flower'.format(name = 'Drathkus', age = 54/3))

x = math.sin(math.pi*0.5)
print(x)




#string -> str "hi, what's on today's menu"
#integer -> int 90
#float -> float 3.1415 

#COMPLEMENTARY ERROR FUNCTION
