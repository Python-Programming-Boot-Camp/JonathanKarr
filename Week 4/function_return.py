def sum (a,b):
    return a+b
sum(3,4)
print(sum(3,4))
a = sum(5,6)
print(a)
def division_with_default_parameters(a,b=1):
    if(b==0):
        return "Cannot divide by 0"
    return a/b
print(division_with_default_parameters(2,0))
print(division_with_default_parameters(2,2))
print(division_with_default_parameters(3))
print(division_with_default_parameters())