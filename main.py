# + * / -
def soma(number1, number2):
    print(number1 + number2)


def minus(number1, number2):
    print(number1 - number2)


def times(number1, number2):
    print(number1 * number2)


def divide(number1, number2):
    if number1 or number2 == 0:
        print('its not possible divide by 0')
    else:
        print(number1 / number2)


def up(number1, number2):
    print(number1 ** number2)


def calculate(number1, number2):
    if signal == '*':
        times(number1, number2)
    elif signal == '-':
        minus(number1, number2)
    elif signal == '/':
        divide(number1, number2)
    elif signal == '+':
        soma(number1, number2)
    elif signal == '^':
        up(number1, number2)
    else:
        print(" ")
        print("This operation it's not possible")


end = 'no'
if end == 'no' or 'n':
    while True:
        number1 = int(input('tap a number: '))
        number2 = int(input('tap another number: '))
        signal = input('tap a math signal (+ - / * ^): ')
        calculate(number1, number2)
        end = input('du wanna calculate again? (yes/no): ')
        if end == 'yes' or end == 'y':
            print('good job')
            break