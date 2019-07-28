from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s" %(from_file, to_file))

in_file = open(from_file)
in_data = in_file.read()

print("The input file is %d bytes long" %len(in_data)) #len() gives the length of the string passed into it

print("Does this output file exist? %r" % exists(to_file)) #exists(file) checks whether "file" exists

print("Ready, hit RETURN to continue, CTRL-C to abort")
input()
out_file = open(to_file, 'w')
out_file.write(in_data)

print("Complete!")

out_file.close()
in_file.close()