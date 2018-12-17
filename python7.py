import math #Importing the math library to Python

#Operators and Expressions
#Most statements will contain expressions and are made up of operators and operands
#Operators are function-defined terms
#Operands are some sort of data

#Example:
x = 2 + 3
#NOTE: '+' is the operators, '2' and '3' are the operands
print(x)

#-------------------------------------------------------------------------------------------------------
print('\n\n') #Just leaving some lines in the main program
#-------------------------------------------------------------------------------------------------------

#Operator List (different from some other languages, must TAKE NOTE!!!)
#----'+' --> ADD
#----'-' --> SUBTRACT; ADD NEGATIVE NUMBERS
#----'*' --> MULTIPLY
#----'/' --> DIVIDE
#----"**" --> POWER
#----"//" --> DIVIDE AND ROUND FLOAT TO NEAREST INTEGER
#----"%" --> MODULO (NOTE: NOT MODULUS FUNCTION; BUT FINDS REMAINDER FROM DIVISION)
#----"<<" --> LEFT-SHIFT: Shift the bits of the number to the left by the number of bits specificied
#----">>" --> RIGHT-SHIFT: Shift the bits of the number to the right by the numver of bits specificed
#----"&" --> bit-wise AND
#----"|" --> bit-wise OR
#----"^" --> bit-wise XOR
#----"~" --> bit-wise NOT or... bit-wise invert
#----"<" --> less than
#----"<=" --> Less than or equal to
#----"==" --> Equal to
#----"!=" --> Not equal to
#----">" --> Greater than
#----">=" --> Greater than or equal to
#----"not" --> boolean NOT
#----"and" --> boolean AND
#----"or" --> boolean OR

#ADDITION
print('addition of numbers')
x = 5 + 3
print(x, '\n')

print('addition of words')
x = 'hue'
y = 'hue'
z = x + y
print(z, '\n')

#SUBTRACTION
print('subtraction of numbers')
x = 9 - 6
print(x, '\n')

#print('subtraction of words') #NOTE:You can't subtract words. Unhashtag this
#x = 'Drath'                   #group of statement to see the error. Hashtag
#y = 'kus'                     #it to ignore this error
#z = x - y
#print(z, '\n')

#MULTIPLICATION
print('multiplication of number')
x = 9 * 6
print(x, '\n')

print('multiplication of words')
x = 'ha'
y = 5
z = x * y
print(z, '\n')

#DIVISION
print('division of numbers')
x = 13
y = 3
z = x / y
print(z, '\n')

#POWER
print('power of numbers')
x = 18
y = 9
z = x ** y
print(z)
#OR
x = 18
y = math.exp(x)
print(y, '\n')

#DIVIDE AND ROUND OFF
print ('Division of numbers & rounding off')
x = 18
y = 4
z = x // y
print(z, '\n')

#MODULO
print('modulo')
x = 18
y = 4
z = x % y
print(z, '\n')

#Left-shift and Right-shift are bitwise operations and bitwise operations
#require binary calculation if answer is needed to be found manually

#LEFT-SHIFT
print('bitwise left-shift')
x = 3
y = 1
z = x << y
print(z, '\n')

#RIGHT-SHIFT
print('bitwise right-shift')
x = 4
y = 0
z = x >> y
print(z,'\n')

#FOR USE WITH 'AND', 'OR', 'NOT', 'XOR' LOGIC, REFER TO LOGIC GATE
#TABLE FOR REFERENCE TO UNDERSTAND THESE BIT-WISE OPERATION CONCEPT

#BIT-WISE AND
print('bitwise and')
x = 5
y = 8
z = y and x
print(z, '\n')

#BIT-WISE OR
print('bitwise or')
x = 5
y = 8
z = y or x
print(z, '\n')

#BIT-WISE XOR
print('bitwise xor')
x = 3
y = 15
z = x ^ y
print(z, '\n')

#BIT-WISE NOT/INVERT
print('bitwise not')
x = 9
z = ~x
print(z, '\n')
#NOTE: BIT-WISE NOT/INVERT of a value 'x' is y = -(x+1) = -x-1

#LESS THAN
print('print less than function with true or false')
x = 4
y = 8
print(x < y)
print(y < x, '\n')

#LESS THAN OR EQUAL TO
print('less than or equal to function with true or false')
x = 4
y = 8
z = 8
print(x <= y)
print(y <= z)
print(z <= x, '\n')

#MORE THAN
print('print more than function with true or false')
x = 21
y = 16
print(x > y)
print(y > x, '\n')

#MORE THAN OR EQUAL TO
print('print more than or equal to function with true or false')
x = 21
y = 16
z = 16
print(x >=y)
print(y >= x)
print(x >= z, '\n')

#EQUAL TO
print('equal to function with true or false for a number')
x = 21
y = 21
z = 16
print(x == y)
print(y == z)
print(z == x, '\n')

print('equal to function with true or false for a string')
a = 'Anna'
b = 'Anna'
print(a == b)
a = 'Ed Sheeran'
b = 'Taylor Swift'
print(a == b, '\n')

#NOT EQUAL TO
print('not equal to function with true or false')
x = 21
y = 21
z = 16
print(x != y)
print(y != z)
print(z != x, '\n')

#BOOLEAN NOT
print('boolean NOT function with true or false')
a = True
b = not a
print(a, '--> boolean NOT function -->', b)
c = False
d = not b
print(c, '--> boolean NOT function -->', d, '\n')
#IF A VARIABLE IS TRUE, IT RETURNS FALSE

#BOOLEAN AND
print('boolean AND function with true and false')
b = False
a = False
z = a and b
print(z)
b = True
a = True
z = a and b
print(z)
b = False
a = True
z = a and b
print(z, '\n')
#BOOLEAN AND RETURNS FALSE AS LONG AS THERE IS 1 FALSE IN THE COMBINATION
#OF TRUES AND FALSES.

#BOOLEAN OR
print('boolean OR function with true and false')
b = False
a = False
z = a or b
print(z)
b = True
a = False
z = a or b
print(z)
b = False
a = True
z = a or b
print(z)
b = True
a = True
z = a or b
print(z, '\n')
#AS LONG AS 1 CONDITION IS TRUE, IT WILL RETURN TRUE 

#USING TRIGONOMETRY 
print('trigonometry functions')
x = math.sin(math.pi)
print(x)
y = math.cos(math.pi)
print(y)
z = math.tan(math.pi)
print(z, '\n')
#TRIGONOMETRY USES RADIAN BY DEFAULT

#Value of Pi
print('value of pi')
x = math.pi
print(x,'\n')

#Value of e
print('value of e')
x = math.e
print(x, '\n')

#Value of tau
print('value of tau')
x = 2 * math.pi
print(x)
#OR... (SINCE TAU = 2 PI)
y = math.tau
print(y)
print(x == y, '\n')

#-------------------------------------------------------------------------------------------#

#ERROR FUNCTION
print('examples of error function')
def theta(x):
    'Cumulative distribution function for the standard normal distribution'
    return((1.0 + math.erf(x / math.sqrt(2.0))) / 2.0)
print(x, '\n')

#COMPLEMENTARY ERROR FUNCTION
print('examples of complementary error function')
def theta(x):
    'Cumulative distribution function for the standard normal distribution'
    return(1.0 - math.erf(x))