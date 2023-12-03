def foo(string_list):
    value_list = [float(number) for number in string_list]
    return sum(value_list)

added_value = foo(['1.2', '2.6', '3.3',])
print(added_value)