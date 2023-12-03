def store_sentences():
    sentences = []
    while True:
        sentence = input('Say somthing: ')
        if sentence.lower() == '\end': break
        sentences.append(sentence)
    return sentences

def print_sentences(sentences):
    interrogatives = ['when', 'where', 'how', 'why', 'what']
    for sentence in sentences:
        first_word = sentence.split()[0] 
        if first_word in interrogatives:
            ending = '?'
        else:
            ending = '.'
        print(f'{sentence[0].capitalize()}{sentence[1:]}{ending} ', end='')

sentences = store_sentences()
print_sentences(sentences)
