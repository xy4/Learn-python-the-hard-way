from sys import argv # import argument from system by input	

script, filename = argv # the script refers to this python script
# filename should be the file we want to open
# that is ex15_sample.txt here

txt = open(filename) # open the txt

print "Here is your file %r:" % filename
print txt.read() # read the result
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()