from Question import Question
print('----------------------------')
print('            QUIZ            ')
print('     Made By Aryan Gore     ')
print('----------------------------')
print('INSTRUCTIONS\n(1) Quiz consists of 5 questions.\n(2) Each question will have 4 options (a)(b)(c)(d)\n(3) You need to input the correct option below each question.')
print('(4) Each question carries 1 mark.\n(5) Multiple selection of option will not be considered.\n(6) ENTER yes AFTER READING ALL THE INSTRUCTIONS TO TAKE QUIZ\n ')
question_prompt = [
    "Q1) Who is founder of Python programming language ?\n (a) Guido Rangephiller \n (b) Guido van Rossum\n (c) Guido mark Rossum\n (d) JetBrains\n\n",
    "\nQ2) What is the longest river in world? \n  \n (a) Nile\n (b) Amazon\n (c) Ganga\n (d) Don't Know\n\n",
    "\nQ3) What is the smallest animal in world? \n  \n (a) Dog\n (b) Flea\n (c) Hodgehog\n (d) Kitti's hog-nosed bat\n\n",
    "\nQ4) Which is the Biggest Fish in world? (Currently) \n  \n (a) Megladon\n (b) Blue Whale\n (c) Whale Shark\n (d) None of the above\n\n",
    "\nQ5) Which Jelly Fish is Imortal?:\n (a) Jellyfish\n (b) Turritopsis dohrnii\n (c) box jellyfish\n (d) Bloodybelly Comb Jellyfish\n\n",
]
question=[
    Question(question_prompt[0],"b"),
    Question(question_prompt[1],"a"),
    Question(question_prompt[2],"d"),
    Question(question_prompt[3],"c"),
    Question(question_prompt[4],"b"),
]
def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        print('Your Response is ==> ', answer)
        if answer == question.answer:
            score+=1
    print("You got " + str(score) + " / " + str(len(questions)) + " correct")
    print("--------------")
    print("YOUR SCORE = ",score)
    print("--------------")
    if score <= 2:
        print("Try again,Keep yourself updated")
    elif score >2 and score <= 4:
        print("WELL DONE!!")   
    else:
        print("EXCELLENT!!")    

p= input("ARE U READY TO START??!!  ")
q=p.lower()
if q=="yes":
    print('Enter your name')
    name=input()
    print("Enter login ID")
    Id = input()

    run_test(question)            
    a=input("TYPE 'ex' to Exit ")
    b=a.lower()
    if b=="ex":
       print('THANKS FOR ATTENDING '+ name.upper())

else:
    print('Thanks for attending our Quiz')

