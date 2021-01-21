try:
    print("Enter 2 numbers to divide")
    num1 = float(input("What is the first number: "))
    num2 = float(input("What is the second number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("You cannot divide by 0")
except ValueError:
    print("You must enter a number")
except:
    print("There is some other type of error")
finally:
    print("This prints no matter what")