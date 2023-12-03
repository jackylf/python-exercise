def foo1(mix_list):
    value_list = [value if value != 'no data' else 0 for value in mix_list ]
    return value_list

def foo2(mix_list):
    value_list = [value if isinstance(value, int) else 0 for value in mix_list ]
    return value_list

def foo3(mix_list):
    value_list = [0 if isinstance(value, str) else value for value in mix_list ]
    return value_list   

print(foo1([99, 'no data', 95, 94, 'no data']))
print(foo2([99, 'no data', 95, 94, 'no data']))
print(foo3([99, 'no data', 95, 94, 'no data']))