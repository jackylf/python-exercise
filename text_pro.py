def input_messages():
    messages = []
    while True:
        message = input('Say something: ')
        if message.lower() != '\end':
            messages.append(message)
            continue
        else:
            break
    return messages

def output_formatted_messages(texts):
    messages = []
    for text in texts:
        text = text.lower()
        if text.startswith('when') or \
            text.startswith('where') or \
                text.startswith('how') or \
                    text.startswith('why') or \
                        text.startswith('what'):
            text = f'{text}?'
            #Capitalize the first letter 
            text = text[0].capitalize() + text[1:] 
        else:
            text = f'{text}.'
            #Capitalize the first letter 
            text = text[0].capitalize() + text[1:] 
        messages.append(text)

    formatted_message =  ' '.join(messages)
    return formatted_message


original_messages = input_messages()
print(original_messages)
formatted_messages = output_formatted_messages(original_messages)
print(formatted_messages)
