import random

def get_lower_limit():
    while True:
        try:
            lower_limit = int(input('Enter the lower limit of a number range: '))
        except ValueError:
            print('You should enter an integer!')
            continue
        else:
            break
    return lower_limit

def get_upper_limit():
    while True:
        try:
            upper_limit = int(input('Enter the upper limit of a number range: '))
        except ValueError:
            print('You should enter an integer!')
            continue
        else:
            break
    return upper_limit    

def get_number_range():
    lower_limit = get_lower_limit()
    upper_limit = get_upper_limit()
    
# Check the validity of the upper limit and the lower limit    
    while upper_limit <= lower_limit:
        print('Upper limit shoud larger than the lower limit!')
        upper_limit = get_upper_limit()

    return (lower_limit, upper_limit)

def guess_number(number_range):
    lower_limit = number_range[0]
    upper_limit = number_range[1]
    secret_num = random.randint(lower_limit, upper_limit)
    guessed_times = 0

    while True:
        try:
            guessed_num = int(input(f'guess the secret number that is between {lower_limit} and {upper_limit}: '))
        except ValueError:
            print('you should input numbers')
            continue

        if guessed_num < secret_num:
            if guessed_num < lower_limit:
                print('Your guess is out of the number range')
                guessed_times += 1
                continue
            else:
                print('Your guess is smaller, try again')
                guessed_times += 1
                continue
        elif guessed_num > secret_num:
            if guessed_num > upper_limit:
                print('Your guess is out of the number range')
                guessed_times += 1
                continue
            else:
                print('Your guess is larger, try again')
                guessed_times += 1
                continue
        else:
            guessed_times += 1
            print(f'You got it in {guessed_times} times!')
            break

number_range = get_number_range()
guess_number(number_range)