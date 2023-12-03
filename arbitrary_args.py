def mean(*args):
    return sum(args) / len(args)

def mean2(**kwargs):
    return kwargs

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

def foo2(**kwargs):
    return max(kwargs, key= kwargs.get)

print(foo2(a=1,b=2))
'''
print(mean(2,3,4,1))
print(mean2(a=1,b=2,c=3,d=4))
print(foo("snow", "glacier", "iceberg"))
'''
