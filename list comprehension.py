l = []
print(l)
for x in range(1,11):
    l.append(x)
    print(l)
#eg-2 creating list with squre of numbers from 1 to 5:
l1 = [x for x in range(1,6)]
print(l1)

l2 =[x*x for x in range(1,6)]
print(l2)

#creating list with cube of numbers from 5 to 1:
l1 = [x for x in range(5,0,-1)]
print(l1)

l2 =(x*x*x for x in range(5,0,-1))
print(l2)

#creating a list with odd numbers from1 to 20:
l = [x for x in range(1,21) if x%2==1]
print(l)

#creating a list with even numbers that are divisible by 4 form 50 to 20
l =[x for x in range(50,19,-1) if x%2==0 and x%4==0]
print(l)