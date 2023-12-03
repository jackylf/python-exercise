import random as r
from capitals import capitals

for quiz_num in range(35):
    #write quiz files and answer key files 
    quiz_file =  open(f'.\\quiz_folder2\\quiz{quiz_num + 1}.txt', 'w')
    answer_key_file = open(f'.\\quiz_folder2\\answer_quiz{quiz_num + 1}.txt', 'w')

    #make headers
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + f'State Captital Form({quiz_num + 1})\n\n')

    #shuffle the order of the states
    states = list(capitals.keys())
    r.shuffle(states)

    #loop through all 50 states, making a question for each.
    for question_num in range(50):
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
        
        right_option = capitals[states[question_num]]
        wrong_options = list(capitals.values())
        wrong_options.remove(right_option)
        wrong_options = r.sample(wrong_options,3)
        options = [right_option] + wrong_options
        r.shuffle(options)
        for i in range(4):
            quiz_file.write((' '*4) + ('ABCD'[i]) + f'.{options[i]}')
        quiz_file.write('\n')
        
        answer_key_file.write(f'{question_num+1}.' + 'ABCD'[options.index(right_option)] + '\n')
    quiz_file.close()
    answer_key_file.close()
        
