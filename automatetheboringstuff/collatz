# Collatz Sequence
def collatz(number):
    result = ''

    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    return result


def inputNum():
    while True:
        try:
            number = int(input('input a number greater than 1 \n'))
            if number == 0:
                print('wrong')
            else:
                return number
        except ValueError:
            print('Enter a valid number')

number = inputNum()
while True:
    if(number == 1):
        print('exit program')
        break

    number = collatz(number)
    print(number)



