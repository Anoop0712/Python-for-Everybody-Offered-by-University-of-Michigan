import re
file1 = input("Enter file name: ")
hand = open(file1)
num=[]
for line in hand:
    list1=re.findall('[0-9]+',line.strip())
    #print(list1)
    for i in list1:
    	i=int(i)
    	num.append(i)


print(sum(num))