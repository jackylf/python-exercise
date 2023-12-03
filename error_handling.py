def print_reciprocal(number):
    try:
        result = 1 / number
    except Exception as e:
        print(f'There is an error:{repr(e)}')
        result = "NA"
    else:
        print('No error')
    finally:
        print(f'The result is {result}')

print_reciprocal('q')
print_reciprocal(0)