name = input("Enter file:")
handle = open(name)
counts=dict()
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        email=words[1]
        counts[email]=counts.get(email,0)+1
 
bigcount=None
bigemail=None
for email,count in counts.items():
    if bigcount is None or bigcount<count:
        bigcount=count
        bigemail=email
print(bigemail,bigcount)        