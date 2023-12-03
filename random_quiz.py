import random
import capitals
import os

for quiz_num in range(35):
    #generate 35 quizzes
    quiz_file_name = f'quiz{quiz_num + 1}.txt'
    quiz_folder_name = 'quiz_folder'
    #os.makedirs(quiz_folder_name)
    quiz_file_path = os.path.join(os.getcwd(), quiz_folder_name, quiz_file_name)
    answer_file_name = f'answer_{quiz_file_name}'
    answer_file_path = os.path.join(os.getcwd(), quiz_folder_name, answer_file_name)

    with open(quiz_file_path, 'w') as quiz_file:
        #quiz header
        quiz_file.write(f'Name:\n\n')
        quiz_file.write(f'Date:\n\n')
        quiz_file.write(f'Period:\n\n')
        #create 50 quiz questions for each quiz
        states = list(capitals.capitals.keys())
        random.shuffle(states)
        for question_num in range(50):
            #provide one correct option and 3 random wrong options
            #in random orders for each question
            quiz_file.write(f'{question_num + 1}. What\'s the capital of {states[question_num]}?\n')
            answers = list(capitals.capitals.values())
            correct_answer = capitals.capitals[states[question_num]]
            answers.remove(correct_answer)
            wrong_options = random.sample(answers, 3)
            options = wrong_options + [correct_answer]
            random.shuffle(options)
            opt_prefix = 'ABCD'
            for i in range(4):
                quiz_file.write(f'\t{opt_prefix[i]}.{options[i]}\n')
                
            #generate 35 quiz answer text files
            with open(answer_file_path,'a') as answer_file:
                answer_file.write(f'{question_num + 1}: {opt_prefix[options.index(correct_answer)]}\n')