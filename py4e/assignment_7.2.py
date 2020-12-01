#average of all the float numbers of line as X-DSPAM-Confidence: 0.8475
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
s=0
s=float(s)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
        str1=line[20:26]
        s=s+float(str1)
print("Average spam confidence:",s/count)
