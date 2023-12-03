def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number +1
        print(result)
        return result

while True:
    try:
        number =  int(input('Enter an integer: '))
    except ValueError:
        print('Please enter a number!')
        continue
    else:
        break

while True:
    result = collatz(number)

    if result == 1:
        break
    else:
        number = result
        continue