import math as M #importing math library, as M so we can say M.cos, M.sin etc
import convert as c
import sys


cars = 20
capacity = 4
carpoolCapacity = cars*capacity
bat = "bat"
man = "man"

batman = bat + man

msg1 = 'There are ', cars, 'each with a capacity of ', capacity
msg2 = 'The total carpool capacity is ', carpoolCapacity
print("There are ", cars, "each with a capacity of ", capacity)
print("The total carpool capacity is ", carpoolCapacity)
print(bat+man) #adding strings concatenates them
print(batman)
print(msg1) #Using "" seems to keep the quotation marks and parentheses in
print(msg2)

m = 18
n = 12
print("m is ", m)
print("n is ", n)
print("m + n =", m + n)
print(msg1)

def greet(person):
    print("hello", person)
    print("how are you today")

greet("Donnell")

my_name = 'Donnell'
my_age = 20 #my age as of 26/07/2019
my_height = 1.75 #my height 
my_weight = 70.4 #my weight as of 26/07/2019
my_eyes = 'Brown' 

print('My name is %s and my height is %.2f metres' %(my_name, my_height))
# %s for string, %f for floating point, %d for integers, Same syntax as java
# but %r is for any variable type, %.xr makes the printed variable occupy x character spaces.
print('My age is ', my_age) 
print('My weight is ', my_weight)
print('My eye colour is ', my_eyes)

def BMI(height, weight): #Note how I don't need to define the variable type returned from the function
    return weight / (height * height)

print('My BMI is %.6r' %(BMI(my_height, my_weight)))

#----------------------------------------------------------------------------------------------------------

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those that know %s and those who %s." % (binary, do_not)
print(x)
print(y)
# The operator s % o where s is a string and o is an object inserts the string form of o into the string,
# at the position %o* is at (where o* represents the variable type of o)
# We can have o be a tuple, in which case it inserts each of the n members into the corresponding n positions

print("I said: %r" %x)
print("I also said: '%s'." % y) #Use single quotes inside a string of double quotes
print('How does this go "Decently well" he said') #And double quotes inside of a string with single quotes
hilarious = False
joke = "Isn't that joke so funny?! %r"

print(joke % hilarious) #And we do the same thing here, creating new strings

w = "This is the left side of..."
e = " a string with a right side"

print(w + e)

#We use %r for debugging as it shows raw data, and %s,%d, etc for displaying to users
#So %r is for debugging, and other formats are better for display

#Boolean types True and False are capitalised, unlike in Java

fourmatter = "%r %r %r %r"
print(fourmatter % (1, 2, 3, 4))
print(fourmatter % ('one', 'two', 'three', 'four'))
print(fourmatter % (True, False, True, False))
print(fourmatter % (fourmatter, fourmatter, fourmatter, fourmatter))
print(fourmatter % (
    "I had this thing",
    "That you could type up right",
    "But it didn't sing",
    "So I said goodnight"
))

stringmatter = "%s %s %s %s" #We see the difference between %r and %s here
#%s makes the displayed string look nicer, for display
#%r displays is in the most efficient way possible, for debugging
print(stringmatter % (
    "I had this thing",
    "That you could type up right",
    "But it didn't sing",
    "So I said goodnight"
))

days = "\nMon\tTue\tWed\tThu\tFri\tSat\tSun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nOct\nNov\nDec"
print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
there's something going on here.
with the three double-quote.
we'll be able to type as much as we like.
even 4 lines if we want, or 5, or 6.
""")#Triple quotes allow multi-line formatting

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
blackslash_cat = "I'm \\ a \\ cat"
fat_cat = """ 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(blackslash_cat)
print(fat_cat)

#Testing inputs for the program

"""
age = eval(input("What is the your age? "))
height = eval(input("What is your height in metres? ")) #eval() converts the string representation of a number to a numerical value
weight = eval(input("What is your weight in kilograms? "))
"""

#print("""So your age is %r years old
#You're %r metres tall 
#And your weight is %rkg""" %(age, height, weight))



"""
test = input("Testing ")
print(test)

g = 9.81
l = 1
angle = eval(input("Give me the angle: "))
acceleration = -(g / l) * M.sin(angle)
print("The acceleration of the pendulum is %.2f m/s^2" %acceleration)

def factorial(n):
    if not isinstance(n, int):
        print("Factorial function only defined for integers")
        return None
    elif (n < 0):
        print("Factorial only defined for positive integers")
        return None
    elif (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(factorial(i))

ans = eval(input("Enter an arithmetic expression: "))
print(ans) #eval can evaluate entire arithmetic expressions

x, y = eval(input("Enter a number: ")), eval(input("Enter another number: "))

sum_, diff, prod, quod = x + y, x - y, x * y, x / y

oper = input("Enter an operation: ")
#elif is else if
if(oper == '*'):
    print("%.2f %s %.2f =  %.2f" %(x, oper, y, prod))
elif(oper == '+'):
    print("%.2f %s %.2f =  %.2f" %(x, oper, y, sum_))
elif(oper == '-'):
    print("%.2f %s %.2f =  %.2f" %(x, oper, y, diff))
elif(oper == '/'):
    print("%.2f %s %.2f =  %.2f" %(x, oper, y, quod))
else:
    print("Enter a valid arithmetic operation")
"""

#age = input("How old are you?")
#height = input("How tall are you?")
#weight = input("How much do you weigh?")

#print("So you're %r years old, %r metres tall and %r kilos" %(age, height, weight))

c.C2F()
c.countdown(10)
c.countdown(-10)

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet) #another way to format strings
    return greeting

print(greet('World'))
print(greet('Donnell'))


