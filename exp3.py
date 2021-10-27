# Name: Neeraj Nair
# Roll no.: CEB438
# Aim: Write a program to demonstrate exception handling using try,multiple except and finally. 

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        n = int(input("Enter a number: "))
        if n < number:
            raise ValueTooSmallError("This value is too small")
        elif n > number:
            raise ValueTooLargeError("This value is too large")
        break
    
    except ValueTooSmallError as se:
        print(se)
        
    except ValueTooLargeError as le:
        print(le)
        
    finally:
        print("Try again!")
        
print("Congratulations! You guessed it correctly.")