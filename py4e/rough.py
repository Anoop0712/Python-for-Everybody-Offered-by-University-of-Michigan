# Write your code here
def min_num(x):
    value=sum(x)
    lar=max(x)
    for i in range(lar+1):
    	for j in range(len(x)):
    		x[j]=i
    	if sum(x)>value:
    	    req=i
    	    break	
    return req


N=int(input("enter number"))
arr=[int(x) for x in input("enter array").split()]
print(min_num(arr))
