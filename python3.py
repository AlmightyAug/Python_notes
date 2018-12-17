#Methods to formatting

age = 18
name = 'Drathkus'

print('{0} was {1} years old when he gave her a flower'.format(name, age))
print('Why did {0} give her that flower?'.format(name))

#ability to set order of set information inside the {x} parenthesis
#with .format(x,y)
#such that '... {x} ... {y} ...'.format(x,y)

#format method can be called to substitute thse specification within
#the corresponding arguments in in the .format()

#Python starts counting from 0, not 1!!!
#So, 0, 1, 2, 3, 4 and so on

#Alternatively, you can leave it blank and let the computer count from
#the beginning of the statement to the end of the statement

age = 18
name = 'Drathkus'

print('{} was {} years old when he gave her a flower'.format(name, age))
print('Why did {} give her that flower?'.format(name))

#OR...

age = 18
name = 'Drathkus'

print('{name} was {age} years old when he gave her a flower'.format(name=name, age=age))
print('Why did {name} give her that flower?'.format(name=name))

#For, Python 3.6 and above then you can use f-strings to reduce wordy code
#and shorten it. It helps when speed is needed so the computer can
#automatically decide in which order should the computer output information

age = 18
name = 'Drathkus'

print(f'{name} was {age} years old when he gave her a flower')
print(f'Why did {name} give her that flower?')

#Notice the lack of a '.format' function and the addition of the f-string?
#Yep, that is the convenience of an f-string, however you should avoid it at  
#all cost to improve ease of reading the code and reduce time to code across
#all members in a team

#However if you insist on understanding the f-string, here is an example... 

#decimal (.) sets the precision of 'x' for the number of decimal places, for float '18.00000'
#the number for 'x' determines the number of decimal places, not significant figures
#notice that are 5 zeros behind the decimal places because of .5f
print('{0:.5f}'.format(54/3)) 

#to centre your text, place underscores with an odd number
# (^) points how many underscores to put in total on the left and right side of the word
print('{0:_^11}'.format('hello'))

#then

print('{name} was {age} years old when he gave her a flower'.format(name = 'Drathkus', age = '18'))
print('Why did {name} give her that flower?'.format(name = 'Drathkus'))

#If you want to print information on the same line in your programme, but not in the same parenthesis, then
print('{name} was {age} years old when he gave her a flower'.format(name = 'Drathkus', age = '18'), end= ' ') 
print('Why did {name} give her that flower?'.format(name = 'Drathkus'))
#These 2 lines will be printed on the same line

#and if you want to print a blank line, then
print(' ')

#----------------------------------------------------------------------------------------

#WHAT MAKES CODE UGLY AND ERROR-PRONE?? LOOK NO FURTHER
# print(name + 'is' + str(age) + ' years old')

print(name + ' was ' + str(age) + ' years old when he gave her a flower')
#by the way, 'str' stands for 'string'
#it is the string variable used to store a word or
#a few letters in that variable holder
#You may accidentally add integers if var type is changed 
#or weird fatal error/bug will appear
#---------------------------------------------------------------------------------------



