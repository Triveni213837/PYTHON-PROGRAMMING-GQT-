s1 = 'Rama'
print('s1 id =', id(s1))

s2 = 'Raja'
print('s2 id =', id(s2))

#Aliasing of list
l1 = [10,20,30,40,50]
print('l1 = ',l1)
print('l1 id =', id(l1))

print()

l2 = l1
print('l2 = ',l2)
print('l2 id =', id(l2))


#cloning of list
#using slice    operator -1
l1 = [10,20,30,40,50]
print('l1 = ',l1)
print('l1 id =', id(l1))

print()

l2 = l1[:]
print('l2 = ',l2)
print('l2 id =', id(l2))

#using copy() method
l1 = [100,200,300,400,500]
print('l1 = ',l1)
print('l1 id =', id(l1))

print()

l2 = l1.copy()
print('l2 = ',l2)
print('l2 id =', id(l2))
