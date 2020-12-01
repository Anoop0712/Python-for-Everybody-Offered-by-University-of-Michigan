# Use words.txt as the file name
fname = input("Enter file data:")
fhand = open(fname)
fr=fhand.read()
up=fr.upper().rstrip()
print(up)
