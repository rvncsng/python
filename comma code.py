# List practice
# Comma code
def commaFunc(someList: list):
    result = ''
    length = len(someList)

    if length > 2:
        for index, item in enumerate(someList):
            if someList[index] == someList[-1]:
                result += 'and ' + str(item)
            else:
                result += str(item) + ', '
    elif length == 2:
        result = someList[0] + ' and ' + someList[1]
    elif length == 1:
        result = someList[0]
    else:
        result = 'no items'

    return result

listOne = ['a', 'b', 'c', 'd', 'e']
print(commaFunc(listOne)) # prints "a, b, c, d, and e"
listTwo = ['a', 'b']
print(commaFunc(listTwo)) # prints "a and b"
listThree = ['a']
print(commaFunc(listThree)) # prints "a"
listFour= []
print(commaFunc(listFour)) # prints "no items"
