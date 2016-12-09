import os
import cmd
import json
import time
import errno

from shutil import copy2

from tests.qstructure import Qstructure



def all_quizzes():

    '''Lists all json files in other folders other than the questions/ folder'''
    
    quizb = local_quizzes()
    quizc= library_quizzes()
    try:
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname.endswith(".json"):
                    Display = fname.replace('.json', '') 
                          
                    return Display
    except IOError:
        print 'No such files'
    return [Display, quizb, quizb]


def local_quizzes():  
    try:
       for file in os.listdir('Json/'):
            if file.endswith(".json"):        
                Display = file.replace('.json', '')
                print Display
    except IOError:
        print 'No such files'
   


def library_quizzes():  
    try:
       for file in os.listdir('library/'):
            if file.endswith(".json"):        
                Display = file.replace('.json', '')
                print Display
    except IOError:
        print 'No such files'
    
def import_quizzes(quizopen):
    a = os.listdir('library/')  
    libquiz = [file.replace('.json', '')for file in a]

    b = os.listdir('Json/')  
    localquiz = [file.replace('.json', '') for file in b]

    src = os.path.join(os.path.abspath('.'), 'library/')
    dst = os.path.join(os.path.abspath('.'), 'Json/')

    try:
        for file in os.listdir('library/'):
            if file.endswith(".Json"): 
                if file not in os.listdir('json/'): # check if the file in the lib that you want to import exists in the json
                    print "Import successful, attempt quiz"
                else:
                     print "The file already there"
    except IOError: 
         print 'No such files'
    return libquiz, localquiz


def quiz_content(quizie):
    path = 'Json/'+ quizie + '.json'
    for quizname in path:
        quizopen = open(path, 'r').read()
        quizfile=json.loads(quizopen)
        time = int(quizfile["time"])
        new_list=[]        
        for question_object in quizfile["quiz"]:
            question = question_object['questions']
            choices = question_object['options']  
            answer= question_object['answer']

            qstructure=Qstructure(question, choices, answer)

            new_list.append (qstructure)
        
        return {"time":time, "quiz":new_list} 

def take_quiz(quizie):
    try: 

        if quizie == "":
            print "No such file"
    except IOError:
        print "File does not exist"

    count_rightanswer = 0
    count_wronganswer = 0

    quizcontent = quiz_content(quizie)
    questions = quizcontent['quiz']
    timelimit = quizcontent['time']
    answers_to_questions = []
    start = time.time()
    you_cant_continue = False

    for question in questions:
        print question
        if (time.time()-start)>time:
            you_cant_continue = True

        print question.display_questions_and_choices()

        usersanswer = str(raw_input("Give your answer "))
        print "your answr is: " + usersanswer

        answers_to_questions.append(question.correct_answer(usersanswer))

        if answers_to_questions[-1] is True:
            count_rightanswer = count_rightanswer + 1
            print "Right answer"
            
        else:
            count_wronganswer = count_wronganswer + 1
            print "Wrong answer"
            

    if len(answers_to_questions) == len (questions):
        end = time.time() - start

    if you_cant_continue:
        print "Time ran out"

    results = (float(count_rightanswer) / len(questions) * 100)
    score_board = [ {"Time to complete the test": time},
                    {"Time taken to complete":end},
                    {"Questions done":len(answers_to_questions)},
                    {"What is your score":results},
                    {"Answers you got right":count_rightanswer},
                    {"Answers you got wrong":count_wronganswer},

                    ]
    return score_board

#print take_quiz('python')















      










