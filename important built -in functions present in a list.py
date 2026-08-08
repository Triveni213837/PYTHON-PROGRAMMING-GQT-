l = [10,20,10,30,40,10]
#len() function
print(len(l))

#count()
print(l.count(10))
print(l.count(40))

#index()
print(l.index(30))
print(l.index(10))

#append()
l.append(10)
print(l)
l.append(20)
l.append(30)
l.append('A')
print(l)

#insert()
l.insert(1,555)
print(l)

l.insert(3,888)
print(l)

#extend()
l1 = [100,200,300]
l2 = [400,500,600]
print(l1)
print(l2)

l1.extend(l2)
print(l1)

l2.extend(l1)
print(l2)

#remove()
a = [10,20,30,40,50]
print(a)
a.remove(30)
print(a)
a.remove(50)
print(a)

#pop()
b = [10,20,30,40,50]
print(b)
print(b.pop())
print(b)
print(b.pop(3))
print(b)

#clear()
l = ['a',b,'c','d']
print(l)
l.clear()
print(l)

#reverse()
l = ['a','b','c','d']
print(l)
l.reverse()
print(l)

#sort()
l = [30,10,40,20]
print(l)
l.sort()
print(l)

#sort program
l1 =[100,50,150,25,75,125,175]
print(l1)
l1.sort()
print(l1)

l2 = ['banana','apple','mango','grapes']
print(l2)
l2.sort()
print(l2)

#sort program in reverse order
l1 =[100,50,150,25,75,125,175]
print(l1)
l1.sort(reverse=True)
print(l1)

l2 = ['banana','apple','mango','grapes']
print(l2)
l2.sort(reverse=True)
print(l2)
