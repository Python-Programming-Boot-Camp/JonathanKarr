print("Enter 3 numbers to see what the largest number is")
num1 = float(input("What is the first number: "))
num2 = float(input("What is the second number: "))
num3 = float(input("What is the third number: "))
if (num1>=num2 and num1>=num3):
    print(str(num1)+ " is the largest value")
elif(num2>=num3 and num2>=num1):
    print(str(num2)+ " is the largest value")
else:
    print(str(num3)+ " is the largest value")