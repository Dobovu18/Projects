import random as rnd
import numpy as np
import pylab as plt
import math as m

x = np.linspace(0, 2 * m.pi, 100)
y = np.sin(x)

plot = plt.plot(x,y)
plt.show()

#By default, open(filename) opens a reading version of the file

print("Opening the file...")
txt_r = open("textfile1.txt", 'r') #opens the file
print("Here's the file printed out: ")
old_txt = str(txt_r.read()) #I convert the file's text to a string so it can be saved here in the program and used even after the file is closed.
print(old_txt) #reads the text inside the file
txt_r.close()
txt_w = open("textfile1.txt", 'w')
#print(txt) #reads the "file object", which is like some meta-data about the file

#print("Clearing the file...")
#txt_w.truncate() #In order to truncate a file, I need to make it writeable, using open(filename, 'w')
#truncate() empties the file

print("I will now ask for three lines")

line1, line2, line3 = input("line 1: "), input("line 2: "), input("line 3: ")
print("Writing these lines to the file...")


#In order to write to files, I need to make the file writeable, using open(filename, 'w')
txt_w.write(old_txt)
#txt_w.write("\n")
txt_w.write(line1)
txt_w.write("\n")
txt_w.write(line2)
txt_w.write("\n")
txt_w.write(line3)
txt_w.write("\n")

txt_w.close() #careful where you open and close files, after a file is closed, it cannot be accessed (so the variables using it become useless)
txt_r = open("textfile1.txt", 'r')
print(txt_r.read())
print("Closing file...")
txt_r.close()




