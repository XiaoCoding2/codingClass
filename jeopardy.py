
#All questions and Answers
questions = {

    'Math': {
        '100': {"What type of triangle works with the Pythagorean theorem ": 'right'},
        '200': {"What is the area of a circle with the radius of 5 to 2 decimal points ": '78.53'},
        '300': {"Solve for x: 2x+6=3x-1 ": '7'}
    },

    'Science': {
        '100': {"What do all life need? ": 'water'},
        '200': {"The leaves of a cactus plant are what? ": 'spikes'},
        '300': {"Starch is turned into what inside your body? ": 'suger'}
    },
    'English': {
        '100': {"What does lax mean? ": 'not strict'},
        '200': {"How many wizarding schools are shown in Harry Potter? ": '3'},
        '300': {"What does the word salary come from? ": 'latin for salt'}
    }

}

questions = {
        'Math': {
        '100': {"What type of triangle works with the Pythagorean theorem ": 'right'}

    }
}

def print_subj():
    #prints the subjects
    print('--------')
    for topics, all_ in questions.items():
        print(topics)
    print('--------')

def remove_subj():
    #remove math
    if 'Math' not in questions:
        return 0
    if len(questions.get('Math', {})) == 0:
        questions.pop('Math')
    #remove english
    if 'English' not in questions:
        return 0
    if len(questions.get('English', {})) == 0:
        questions.pop('English')
    #remove science
    if 'Science' not in questions:
        return 0
    if len(questions.get('Science', {})) == 0:
        questions.pop('Science')

def check_win():
    #checks for win
    if len(questions) == 0:
        return True
    return False

#Main code
def selection_main(corrects):
    #removes
    remove_subj()
    #check win
    if check_win():
        print(f'You got {corrects} out of 1800.')
        return
    #prints
    print_subj()
    #selection of topics
    selection = input("Which one? ").lower()
    #If math is selected
    if selection == 'math':
        q_m = questions['Math']
        #prints points
        for points, q_a in q_m.items():
            print(points)
        selection2 = input("Which one? ") #selection of points
        #If 100 math is selected
        if selection2 == '100':
            if '100' in q_m:
                qm_1 = q_m['100']
                #question and answer
                for q_1_m, a_1_m in qm_1.items():
                    print(q_1_m)
                    selection3 = input("Answer? ").lower() #ask for answer (.lower function makes it all lowercase)
                    #if correct
                    if selection3 == a_1_m:
                        corrects += 100
                        q_m.pop('100')
                        print("Correct!")
                        selection_main(corrects) #reruns code
                    #if wrong
                    print('Wrong')
                    selection_main(corrects)
            print('Not an option')
            selection_main(corrects)
        #If 200 math is selected
        elif selection2 == '200':
            qm_2 = q_m['200']
            #question and answer
            for q_2_m, a_2_m in qm_2.items():
                print(q_2_m)
                selection3 = input("Answer? ").lower() #ask for answer
                #if correct
                if selection3 == a_2_m:
                    corrects += 200
                    q_m.pop('200')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                print('Wrong')
                selection_main(corrects)
        #If 300 math is selected
        elif selection2 == '300':
            qm_3 = q_m['300']
            #question and answer
            for q_3_m, a_3_m in qm_3.items():
                print(q_3_m)
                selection3 = input("Answer? ").lower() #ask for answer
                #if correct
                if selection3 == a_3_m:
                    corrects += 300
                    q_m.pop('300')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                print('Wrong')
                selection_main(corrects)
        #If other is selected
        else:
            print("!! Not an option !! | Select another")
            selection_main(corrects)
    #If science is selected
    elif selection == 'science':
        q_s = questions['Science']
        #prints points
        for points, q_a in q_s.items():
            print(points)
        selection2 = input("Which one? ") #selection of points
        #If 100 science is selected
        if selection2 == '100':
            qs_1 = q_s['100']
            #question and answer
            for q_1_s, a_1_s in qs_1.items():
                print(q_1_s)
                selection3 = input("Answer? ").lower() #ask for answer (.lower function makes it all lowercase)
                #if correct
                if selection3 == a_1_s:
                    corrects += 100
                    q_s.pop('100')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                #if wrong
                print('Wrong!')
                q_s.pop('100')
                selection_main(corrects) #reruns code
        #If 200 science is selected
        elif selection2 == '200':
            qs_2 = q_s['200']
            #question and answer
            for q_2_s, a_2_s in qs_2.items():
                print(q_2_s)
                selection3 = input("Answer? ").lower() #ask for answer
                #if correct
                if selection3 == a_2_s:
                    corrects += 200
                    q_s.pop('200')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                print('Wrong')
                q_s.pop('200')
                selection_main(corrects)
        #If 300 science is selected
        elif selection2 == '300':
            qs_3 = q_s['300']
            #question and answer
            for q_3_s, a_3_s in qs_3.items():
                print(q_3_s)
                selection3 = input("Answer? ").lower() #ask for answer
                #if correct
                if selection3 == a_3_s:
                    corrects += 300
                    q_s.pop('300')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                print('Wrong')
                q_s.pop('300')
                selection_main(corrects)
        #If other is selected
        else:
            print("!! Not an option !! | Select another")
    #if english is selected
    elif selection == 'english':
        q_e = questions['English']
        #prints points
        for points, q_a in q_e.items():
            print(points)
        selection2 = input("Which one? ") #selection of points
        #If 100 math is selected
        if selection2 == '100':
            qe_1 = q_e['100']
            #question and answer
            for q_1_e, a_1_e in qe_1.items():
                print(q_1_e)
                selection3 = input("Answer? ").lower() #ask for answer (.lower function makes it all lowercase)
                #if correct
                if selection3 == a_1_e:
                    corrects += 100
                    q_e.pop('100')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                #if wrong
                print('Wrong!')
                q_e.pop('100')
                selection_main(corrects) #reruns code
        #If 200 math is selected
        elif selection2 == '200':
            qe_2 = q_e['200']
            #question and answer
            for q_2_e, a_2_e in qe_2.items():
                print(q_2_e)
                selection3 = input("Answer? ").lower() #ask for answer
                #if correct
                if selection3 == a_2_e:
                    corrects += 200
                    q_e.pop('200')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                print('Wrong')
                q_e.pop('200')
                selection_main(corrects)
        #If 300 math is selected
        elif selection2 == '300':
            qe_3 = q_e['300']
            #question and answer
            for q_3_e, a_3_e in qe_3.items():
                print(q_3_e)
                selection3 = input("Answer? ").lower() #ask for answer
                #if correct
                if selection3 == a_3_e:
                    corrects += 300
                    q_e.pop('300')
                    print("Correct!")
                    selection_main(corrects) #reruns code
                print('wrong')
                q_e.pop('200')
                selection_main(corrects)
        #If other is selected
        else:
            print("!! Not an option !! | Select another")
    #if other subj is selected
    else:
        print("!! Not an option !! | Select another")
        selection_main(corrects)

selection_main(0)
