def convert_list_to_string(values):
    final_string = ''
    for value in values:
        if values.index(value) != len(values)-1:
            final_string += f"{value}, "
        else:
            final_string += f"and {value}"
    print(final_string)

spam = ['apple','banana','toufu','cats','pineapple']
convert_list_to_string(spam)