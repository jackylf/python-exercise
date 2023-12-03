def sentence_maker(sentence):
    first_word = ('what','when','where','how','why',)
    if sentence.startswith(first_word):
        sentence = "{}?".format(sentence)
    else:
        sentence = '{}.'.format(sentence)
    capitalized = sentence.capitalize()
    return capitalized

sentences = []
while True:
    sentence =  input('Say something: ')
    if sentence == '\end':
        break
    else:
        sentences.append(sentence_maker(sentence))

print(' '.join(sentences))