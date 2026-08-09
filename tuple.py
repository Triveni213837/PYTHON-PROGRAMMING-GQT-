#Tuple unpacking
t = 10,20,30,49
print(t)


a,b,c,d = t
print(a)
print(b)
print(c)
print(d)


#creating tuple using tuple() function:
#Eg -1 create list and convertin into tuple
l = [10,20,30,40,50,10,20,30]
print(l)
print(type(l))

print()
t = tuple(l)
print(t)
print(type(t))

#eg-2 create tuple using range() function
t = tuple(range(10,0,-2))
print(t)

#Accessing tuple elements using index
t = (10,2030,40,50)
print(t)
print(t[2])
print(t[-4])

#accessing tuple elements using slice operator
t = 10,20,30,40,50
#acccesing all elements left to right
print(t[:])
#access all elements left to right
print(t[: :])
#accessing all elements from right to left
print(t[: :-1])
#from index-2 to index-4,skip 2 elements
print(t[2:5:2])
#access allelements from right to left by skipping 3 elements
print(t[: :-3])


#eg:
t = ('Ramu',10,20,True,5.56,20,10,False)
print(t)

#important functions present in tuple:
t = (100,50,150,25,75,125,175)
print(t)
print(sorted(t))
#desending order sorted
print(sorted(t,reverse = True))

#min() and max():
t = (100,50,150,25,75,125,175)
print(t)
print(min(t))
print(max(t))

#Eg:
t = (X*X for X in range(5,11))
print(t)
print(type(t))
for X in t:
    print(X,end = '')

#applying concatenation operator ('+') on the tuple
t1 =('apple','orange')
print('t1 = ',t1)
t2 =('onion','potato')
print('t2 = ',t2)
print()
t3 = t1+t2
print('t1+t2 =',t3)

#applying multiplication opertaor ('*') on the tuple:
t1 = 'dosa',
print(t1)
t2 = t1*5
print(t2)

#converting list into tuple:
l1 =[10,20,30,40]
print('l1 =',l1,'\t type =',type(l1))
t1 = tuple(l1)
print('t1 =',t1,'\t type =',type(t1))

#converting tuple into list:
t1 =('a','b','c','d')
print('t1 =',t1,'\t type =',type(t1))
l1 = list(t1)
print('l1 =',l1,'\t type =',type(l1))






