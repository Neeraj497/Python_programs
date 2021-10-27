# Name: Neeraj Nair
# Roll no.: CEB438
# Aim: Write a python program to swap two numbers and check if the 
#      first number is positive or negative or zero.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def numChecker(a):
    if(a>0):
        return 'Positive'
    elif (a<0):
        return 'Negative'
    else:
        return 'Zero'

print('\nBefore swapping: ')
print('a = ',a)
print('b = ',b)

print('First number is {} before swapping'.format(numChecker(a)))

a,b = b,a

print('\nAfter swapping: ')
print('a = ',a)
print('b = ',b)

print('First number is {} after swapping'.format(numChecker(a)))