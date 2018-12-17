#Logical & Physical Line
#Physical Line --> What the programmer sees when he/she write the program
#Logical Line --> This is what Python sees as a single statement
#NOTE!!! Python implicitly assumes that each physical line = logical line
#Python encourages the use of a single statement per line which makes the code more readable
#Hence, if you want to specify more than 1 logical line, on a physical line,
#then you need to indicate with a semicolon

#Taking from the previous lesson

x = 8
y = ' is the magic integer'
print(x, y)

#And adding semicolons would be

x = 8; 
y = ' is the magic integer'; 
print(x, y); 

#And it is the same as
x = 8; y = ' is the magic integer'; print(x, y)

#It is also the same as
x = 8; y = ' is the magic integer'; print(x, y); 

#NOTE!!! Try not to use semicolons in your programs as that will rack up
#unwanted warnings and degrade code readability
#The only time you use semicolons is when that specific line of code is long
#However, you can use the 'explicit line joining' function to do the job especially
#if it is a string. Example below,

z = 'This a string. \
This continues the string.'
print(z)

#Alternatively,
x = 8
print(x)
#is the same as
x = \
8
print(x)

#-----------------------------------------------------------------------------------#

#Indentation --> Whitespaces at the beginning of that particular line
#IMPORTANT because it helps to improve readability of the code
#Used to determine the grouping of statements
#Oh yes, wrong indentation can give rise to fatal, deadly, murderous errors

#An example of an error, (when you don't need to test it, put a hashtag in front of 
#every line of error code so that)

x = 8
# print('Value is ', x)
#This is where the error come in, the addition whitespace can cause interpreter
#error.
#NOTE: NEW BLOCKS OF STATEMENTS CANNOT BE ARBITRARILY STARTED EXCEPT FOR THE DEFAULT MAIN BLOCK
#Hashtag that line to ignore the error so that you can interpret the rest of the notes
#and test it for yourselves
print('I repeat, the value is ', x)


#HOW TO INDENT???
#Use 4 spaces, and have a consistent number of indentation, otherwise the program will have unexpected
#behaviour