
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))

def print_three(*args):
    arg1, arg2, arg3 = args
    print("arg1: %r, arg2: %r, arg3: %r" %(arg1, arg2, arg3))

print_two("Hello", "Donnell")
print_three("I", "am", "Coding!")

#The asterisk before the args, (*args) tells python to take all the 
#arguments to the function and put them in args as a list.

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
#seek() deals in bytes, seak(pos) takes you to the pos'th byte in the file
#so seek(0) takes you to the start of the file

def print_a_line(line_count, f):
    print(line_count, f.readline()),
#readline scans each byte until it finds the \n char then stops reading and returns what it has read
#the file f is responsible to maintaining the current position in the file after each 
#readline()
current_file = open("textfile1.txt")
print("Printing the whole file:\n")
print_all(current_file)

print("Now to rewind")
rewind(current_file)

print("Printing 10 lines")

current_line = 0

for i in range(11):
    current_line += 1
    print_a_line(current_line, current_file)
#readline() returns the \n at the end of the line being read
#add a comma at the end of print so it doesn't make it's own \n


#some lists
#We can also index lists from right to left using negative numbers
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
print("A test of indexing arrays from the right: ", fruits[-1]) #Prints apricots, the first entry from the right
#for loops can only iterate over a predefined set of objects
for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("These fruits are %s" % fruit)

for i in change:
    print("I got %r" % i)

elements = [] #elements is an empty list

#range(a,b) gives a list of integers n (in numerical order) satisfying a <= n < b 

for i in range(0, 6): 
    print("adding %d to the list" % i)
    elements.append(i) #adding i to the list

for i in elements:
    print(i)

#This next loop shows how we can access elements in lists
for i in range(0, len(fruits)):
    print("%d.\t%s" %(i + 1, fruits[i]))

#while loops iterate whilst a condition holds true


#Working with dictionaries
#First part of the entry (before the colon) is the label for the variable
#on the second side of the colon.

#e.g let list = ['Donnell', 'Obovu', '18/06/1999', 'DA16 3HP']
#to access my surname here, I need to use list[1]

#for a dictionary, this looks like:
#dict = {'forename' : 'Donnell', 'surname' : 'Obovu', 'DoB' : '18/06/1999', 'Postcode' : 'DA16 3HP'}
#to access my surname, I write dict['surname'].
#curly brackets for dictionaries
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Miami'
}

#adding more cities
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

print('-' * 10) #prints - 10 times for a nice line
print("NY State has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" %(state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" %(abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev]))

print('-' * 10)
#safely get an abbreviation for a state that might not be there
state = states.get('Texas', None)

if not state:
    print("Sorry, no texas in this dictionary")

city = cities.get('Texas', 'Does not exist')
print("The city for the state 'TX' is: %s" % city)

def username(*name):
    #generates a username given a forename and surname
    forename, surname = name
    return forename[0] + surname[:7]

print(username("Donnell", "Obovu"))

print(ord("a"), ord("A"), chr(97), chr(90), chr(960))

def txt2num(msg):
    numstr = ""
    for ch in msg:
        numstr += "%d"
        numstr %= ord(ch)
        numstr += " "
    return numstr

def num2txt(numstr):
    chars = []
    for num in numstr.split(): #Splits the string at every occurrance of a space
        #split(<char>) splits the string at every occurrance of char in the string.
        #split makes an array of substrings from the split strings
        chars.append(chr(int(num))) #using append and treating strings as lists is more efficient
    return "".join(chars)


convert_msg = input("Enter a string to be converted to a number: ")
print(txt2num(convert_msg))
print(num2txt(txt2num(convert_msg)))

#A list is an ordered list of items.
#A dictionary is for matching some items (called keys) with other items, called values.
#dict =  {key1 : value1, ..., keyN : valueN}
#Use dictionaries whenever you have to look up another value

#Many of the operations we do to strings, like concatenation, repeated addition, etc
#Can be done to lists.
#E.g:   [1, 2] + [3, 4] == [1, 2, 3, 4]
#       [1, 2] * 3 == [1, 2, 1, 2, 1, 2]
#       grades = ['A', 'B', 'C', 'D', 'E', 'F']
#       grades[0] == 'A'
#       grades[2: 4] == ['C', 'D']
#       len(grades) = 6
#So lists are more general than strings, and string a a specific type of list


s = "hello, I camE here For an ArguMent"

print(s.capitalize()) #Makes first letter capital, others in lower
print(s.lower()) #Makes all lower case
print(s.title()) #First letter of each word is upper case
print(s.upper()) # All caps
print(s.replace("I", "you"))#replaces first substring with a new string
print(s.center(30))
print(s.center(50))
print(s.count('e')) #counts the number of non-overlapping occurrances of this substring
print(s.find('s')) #finds the position of this substring
print(" ".join(["Number", "one,", "the", "Larch"]))
print("SPAM".join(["Number", "one,", "the", "Larch"]))

total = 1.5
print("The total value of your change is £{0:0.2f}".format(total))
#<template-string>.format(<values>)
name, surname, prize = "Donnell", "Obovu", 1000000.50
print("Hello {0} {1}, you have recieved {2:0.2f} notifications!".format(name, surname, prize))

print("left justification: {0:<5}".format("Hi!"))
print("right justification: {0:>5}".format("Hi!"))
print("centred: {0:^5}".format("Hi!"))

