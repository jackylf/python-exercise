def input_sentences():
    sentences = []
    while True:
        sentence = input('Say something: ')
        if sentence.lower() != '\end':
            sentence = sentence[0].capitalize() + sentence[1:]
            sentences.append(sentence)
            continue
        else:
            break
    return sentences

def add_symbol(sentences):
    sentences_with_symbol = []
    for sentence in sentences:
        sentence = sentence.lower()
        if sentence.startswith('when') or \
            sentence.startswith('where') or \
                sentence.startswith('how') or \
                    sentence.startswith('why') or \
                        sentence.startswith('what'):
            sentence = f'{sentence}?'
        else:
            sentence = f'{sentence}.'
        sentences_with_symbol.append(sentence)
    return sentences_with_symbol

def print_out(sentences):
    joined_sentences = ' '.join(sentences)
    print(joined_sentences)

sentences = input_sentences()
sentences_with_symbol = add_symbol(sentences)
print_out(sentences_with_symbol)