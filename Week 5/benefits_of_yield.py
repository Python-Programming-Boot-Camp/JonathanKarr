def squares (number):
    squared = []
    for i in range(len(number)):
        squared.append(number[i]**2)
    return squared
def squares_with_yield (number):
    for i in range(len(number)):
        yield number[i]**2
print(squares([3,2,5,8]))
print(list(squares_with_yield([3,2,5,8])))