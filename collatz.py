# Collatz Sequence
def collatz(number):
    result = ''

    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    return result


print('input a number greater than 0')
number = int(input())
while number!=1:
    number = collatz(number)
    print(number)

    if(number == 1):
        print('exit program')
