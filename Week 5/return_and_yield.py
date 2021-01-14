def sum(a,b):
    return a+ b
    print("This won't print")
def loop(num):
    for i in range (num):
        #return i
        yield i
        print("test")
#print(sum(3,2))
print(list(loop(3)))
count = loop(3)
print(next(count))
print(next(count))
print(next(count))
#print(next(count))