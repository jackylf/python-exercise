import os
import random as r
from capitals import capitals


def single_QA_maker(question_num, shuffled_states):
    '''制作单个“问题 + 4选项”
    '''
    #1.问题
    question = f'{question_num + 1}.What is the capital of {shuffled_states[question_num]}?'
    #2. 选项
    #2.1 选项内容
    options = []
    right_option = capitals[shuffled_states[question_num]]
    options.append(right_option)
    wrong_options = list(capitals.values())  #这两句的写法可参考
    wrong_options.remove(right_option)       #《automate the boring stuff with python》P114
    options += r.sample(wrong_options, 3)
    #shuffle the order of the options
    r.shuffle(options)
    #2.2 combine the option letter with the contents
    for i in range(4):
        options[i] = ' '*4 +'ABCD'[i] + '. ' + options[i]
    #3. store the data
    single_QA = {} #single_QA{'question':[options]}
    single_QA[question] = options
    return single_QA

def single_quiz_answers_maker():
    '''制作单张测试卷
    '''
    #make info
    info = 'Name:\n\nDate:\n\nPeriod:\n\n'
    #make QAs & correct answers
    QAs = {} #QAs{question_num: single_QA}
    correct_answers = {} #correct_answers{question_num: correct_answer}
    for question_num in range(50):
        #randomize
        states = list(capitals.keys())
        r.shuffle(states)
        #make QAs
        single_QA = single_QA_maker(question_num, states) #single_QA{'question': [options]}
        QAs[question_num] = single_QA
        #make correct answers
        correct_state = capitals[states[question_num]]
        options = list(single_QA.values())
        for i in range(4):
            option = options[0][i]
            if correct_state in option:
                correct_answers[question_num] = option[0]
                 
    single_quiz = [info, QAs, correct_answers]
    return single_quiz

def print_1_quiz_answers():
    '''print one quiz and its answers in CLI
    '''
    quiz = single_quiz_answers_maker() 
    #quzi['info', {QAs}, {correct_answers}]
    #QAs{question_num: single_QA}
    #single_QA{'question': [options]}
    #correct_answers{question_num: correct_answer}

    #print info
    info = quiz[0]
    print(info)
    #print questions and options: 
    QAs = list(quiz[1].values()) 

    for question_num in range(len(QAs)):
        single_QA = QAs[question_num] 
        for question, options in single_QA.items():
            print(question)
            for option in options:
                print(option)

    #print correct answers 
    print('Answers are:')
    correct_answers = quiz[2].items() 
    for question_num, correct_answer in correct_answers:
        print(f'{question_num + 1}. {correct_answer.title()}')

def quiz_file_path(num):
    file_name = f'quiz{num}.txt'
    folder = 'quiz_folder1'
    return os.path.join('.', folder, file_name)

def answer_file_path(num):
    file_name = f'answer_quiz{num}.txt'
    folder = 'quiz_folder1'
    return os.path.join('.', folder, file_name)

def get_contents():
    quiz = single_quiz_answers_maker() 
    #quzi['info', {QAs}, {correct_answers}]
    #QAs{question_num: single_QA}
    #single_QA{'question': [options]}
    #correct_answers{question_num: correct_answer}

    #info
    contents = f'{quiz[0]}\n'
    #questions and options: 
    QAs = list(quiz[1].values()) 

    for question_num in range(len(QAs)):
        single_QA = QAs[question_num] 
        for question, options in single_QA.items():
            contents += f'{question}\n'
            for option in options:
                contents += f'{option}\n'

    return contents

def write_1_quiz_file(num):
    quiz_path = quiz_file_path(num)
    contents = get_contents()
    with open(quiz_path, 'w') as file_object:
        quiz_file = file_object.write(contents)


for num in range(35):
    write_1_quiz_file(num + 1)
