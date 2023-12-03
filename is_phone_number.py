def is_phone_number(phone_number):
    if len(phone_number) != 12:
        return False
    if not phone_number[0:3].isdecimal():
        return False
    if phone_number[3] != '-':
        return False  
    if not phone_number[4:7].isdecimal():
        return False
    if phone_number[7] != '-':
        return False
    if not phone_number[8:12].isdecimal():
        return False
    return True


phone_number = '415-555-4242'
print(is_phone_number(phone_number))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    if is_phone_number(message[i:i+12]):
        print(message[i:i+12])
print('Done')

print(isinstance(2, int))
