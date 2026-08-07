#identity operator
a = 10
b = 20
print(a is b)
print(a is not b)


a = 10
b = 10
print( a is b)
print(a is not b)

#membership operator
s = 'Rama killed Ravana'
print('i' in s)
print('Rava' in s)
print('Mama' in s)
print('sita' not in s)

#adding two numbers
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = a + b
print('The sum is:', c)

#eval() function
#program -1
exp = eval('10+20*2+5')
print('Result = ',exp)

#program -2
exp= input('Enter the expression: ')
print('Result = ',eval(exp))


