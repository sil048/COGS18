"""A collection of functions for doing my project."""

import webbrowser as wb
import time
from colorama import Fore, Back, Style

T = 0.5

def Q1_function(start_quiz):
    """This is Q1, asking for an answer for Q1, and transitions to the next specific question depending on the answer.

    PARAMETERS
    ----------
    start_quiz : str
        Default "Yes" to continue the quiz, or "No" to end the quiz.

    RETURNS
    -------
    start_quiz : str
        Default "Yes" to continue the quiz; or, if did not type in the choices given, "No" to end the quiz.
    """
    
    Q1 = input(Fore.BLUE + "Are you good at meeting deadlines? (enter A, B, or C)\n"
                "A) I'll start working at the last minute\n"
                "B) I bury my head in the sand until it's too late\n"
                "C) Deadlines?! Panic Stations!")
    if Q1.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q21_function(start_quiz)

    elif Q1.upper().strip() == "B":
        time.sleep(T)
        start_quiz = Q3_function(start_quiz)

    elif Q1.upper().strip() == "C":
        time.sleep(T)
        start_quiz = Q22_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q21_function(start_quiz):
    Q21 = input(Fore.BLUE + "Do you work well under pressure? (enter A, or B)\n"
                "A) Sure - pressure makes diamonds after all\n"
                "B) I crumble like a wet biscuit")

    if Q21.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q41_function(start_quiz)

    elif Q21.upper().strip() == "B":
        time.sleep(T)
        start_quiz = Q3_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q22_function(start_quiz):
    Q22 = input(Fore.BLUE + "Do you ever cut corners? (enter A, or B)\n"
                "A) Whatever gets the job done\n"
                "B) I stick to the straight and narrow")
    if Q22.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q3_function(start_quiz)

    elif Q22.upper().strip()== "B":
        time.sleep(T)
        start_quiz = Q42_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q3_function(start_quiz):
    Q3 = input(Fore.BLUE + "What stops you from working? (enter A, or B)\n"
                "A) A to-do list as long as my arm\n"
                "B) Working? I can't even get started")
    if Q3.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q41_function(start_quiz)

    elif Q3.upper().strip() == "B":
        time.sleep(T)
        start_quiz = Q42_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q41_function(start_quiz):
    Q41 = input(Fore.BLUE + "Are you happy making important decisions? (enter A, or B)\n"
                "A) I'm a natural leader\n"
                "B) Too much drama - let someone else decide ")
    if Q41.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q61_function(start_quiz)

    elif Q41.upper().strip() == "B":
        time.sleep(T)
        start_quiz = Q5_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q42_function(start_quiz):
    Q42 = input(Fore.BLUE + "Are you serious about your work? (enter A, or B)\n"
                "A) I'd rather binge on Netflix\n"
                "B) As serious as a heart attack")
    if Q42.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q5_function(start_quiz)

    elif Q42.upper().strip() == "B":
        time.sleep(T)
        start_quiz = Q62_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q5_function(start_quiz):
    Q5 = input(Fore.BLUE + "Do you worry about what others think of you? (enter A, or B)\n"
                "A) Who cares? Sticks and stones...\n"
                "B) Oh no! What are they saying about me now?")
    if Q5.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q61_function(start_quiz)

    elif Q5.upper().strip() == "B":
        time.sleep(T)
        start_quiz = Q62_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q61_function(start_quiz):
    """This is Q61, asking for an answer for Q61, and either transitions to the next specific question,
    or tells the user their procrastinator type, depending on the answer.

    PARAMETERS
    ----------
    start_quiz : str
        Default "Yes" to continue the quiz, or "No" to end the quiz.

    RETURNS
    -------
    start_quiz : str
        Default "Yes" to continue the quiz; or, if did not type in the choices given, "No" to end the quiz.
    """
    
    Q61 = input(Fore.BLUE + "Are you bothered about the quality of your work? (enter A, or B)\n"
                "A) It's fine - so long as it gets done\n"
                "B) It needs to be something I'm proud of")

    if Q61.upper().strip() == "A":   
        d_answer1 = input(Back.MAGENTA + "You are a Daredevil😈! Do you want to learn more about Daredevil? (enter Yes, or No)")
        if d_answer1.upper().strip() == 'YES':
            time.sleep(T)
            print()
            print(Back.CYAN + "You like to live dangerously, only starting work when the deadline is looming.")
            time.sleep(T)
            print()
            print("You think you show grace under pressure, but the end result is rushed work that's full of errors.\n"
                    "note: this is just an interpretation, do not treat it too seriously!")
            time.sleep(T)
            print()

            d_answer2 = input(Back.MAGENTA + "Would you want some tips for dealing with procrastination? (enter Yes, or No)")
            if d_answer2.upper().strip() == "YES":
                time.sleep(T)
                print()
                print(Back.YELLOW + "GET ORGANIZED: Set yourself tighter deadlines and use the adrenaline rush productively\n"
                        "while managing your team - self-regulate with panalties for not meeting these targets.\n"
                        "note: this is just a suggestion, do not treat it too seriously!")
                time.sleep(T)
                print(Style.RESET_ALL)
                print()

                d_answer3 = input(Back.MAGENTA + "Would you want to get a Daredevil profile? (enter Yes, or No)")
                if d_answer3.upper().strip() == "YES":
                    wb.open("https://i.postimg.cc/RFJJNJx0/Daredevil-Profile.png")
                    print("Hope you enjoyed taking the quiz! See you around!")
                    start_quiz = input("Do you want to start over? (enter Yes, or No, strictly)")

                else:
                    time.sleep(T)
                    print("No problem, hope you enjoyed taking the quiz! See you around!")
                    start_quiz = "No"

            else:
                time.sleep(T)
                print("No problem, hope you enjoyed taking the quiz! See you around!")
                start_quiz = "No"

        else:
            time.sleep(T)
            print("No problem, hope you enjoyed taking the quiz! See you around!")
            start_quiz = "No"

    elif Q61.upper().strip() == "B":
        time.sleep(T)
        start_quiz = Q71_function(start_quiz)

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q62_function(start_quiz):
    Q62 = input(Fore.BLUE + "Are you ever happy with your work? (enter A, or B)\n"
                "A) I think I do a pretty good job\n"
                "B) Nothing less than perfection will do")

    if Q62.upper().strip() == "A":
        time.sleep(T)
        start_quiz = Q72_function(start_quiz)

    elif Q62.upper().strip() == "B":       
        p_answer1 = input(Back.MAGENTA + "You are a Perfectionist🧐! Do you want to learn more about Perfectionist? (enter Yes, or No)")
        if p_answer1.upper().strip() == 'YES':
            time.sleep(T)
            print()
            print(Back.CYAN + "You'll settle for nothing less than perfection - which is essentially impossible.")
            time.sleep(T)
            print()
            print("You're ruled by what others think of you,\n"
                    "delaying work until you can be sure other people won't criticise it.\n"
                    "note: this is just an interpretation, do not treat it too seriously!")
            time.sleep(T)
            print()

            p_answer2 = input(Back.MAGENTA + "Would you want some tips for dealing with procrastination? (enter Yes, or No)")
            if p_answer2.upper().strip() == "YES":
                time.sleep(T)
                print()
                print(Back.YELLOW + "KEEP IT REAL: Set yourself reasonable targets that you know you can manage\n" 
                        "and do your best to meet them. Perfection is impossible, but you can learn from mistakes.\n"
                        "note: this is just a suggestion, do not treat it too seriously!")
                time.sleep(T)
                print(Style.RESET_ALL)
                print()

                p_answer3 = input(Back.MAGENTA + "Would you want to get a Perfectionist profile? (enter Yes, or No)")
                if p_answer3.upper().strip() == "YES":
                    wb.open("https://i.postimg.cc/05c1bWZb/Perfectionist-Profile.png")
                    print("Hope you enjoyed taking the quiz! See you around!")
                    start_quiz = input("Do you want to start over? (enter Yes, or No, strictly)")

                else:
                    time.sleep(T)
                    print("No problem, hope you enjoyed taking the quiz! See you around!")
                    start_quiz = "No"

            else:
                time.sleep(T)
                print("No problem, hope you enjoyed taking the quiz! See you around!")
                start_quiz = "No"

        else:
            time.sleep(T)
            print("No problem, hope you enjoyed taking the quiz! See you around!")
            start_quiz = "No"

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q71_function(start_quiz):
    Q71 = input(Fore.BLUE + "How do you handle stress? (enter A, or B)\n"
                "A) I'm as cool as the Fresh Prince\n"
                "B) Smoke starts coming out of my ears")

    if Q71.upper().strip() == "A":
        s_answer1 = input(Back.MAGENTA + "You are a Self-Saboteur🤐! Do you want to learn more about Self-Saboteur? (enter Yes, or No)")
        if s_answer1.upper().strip() == 'YES':
            time.sleep(T)
            print()
            print(Back.CYAN + "You're your own worst enemy, putting obstacles in your path to stop yourself working.")
            time.sleep(T)
            print()
            print("That way, you can say it's not your fault - rewarding yourself for a job left undone.\n"
                    "note: this is just an interpretation, do not treat it too seriously!")
            time.sleep(T)
            print()

            s_answer2 = input(Back.MAGENTA + "Would you want some tips for dealing with procrastination? (enter Yes, or No)")
            if s_answer2.upper().strip() == "YES":
                time.sleep(T)
                print()
                print(Back.YELLOW + "PLAN FOR OBSTACLES: List potential obstacles to getting things done ahead of time,\n"
                        "and plan countermeasures, e.g., 'Whenever I check Facebook, I take a short break.'\n"
                        "note: this is just a suggestion, do not treat it too seriously!")
                time.sleep(T)
                print(Style.RESET_ALL)
                print()

                s_answer3 = input(Back.MAGENTA + "Would you want to get a Self-Saboteur profile? (enter Yes, or No)")
                if s_answer3.upper().strip() == "YES":
                    wb.open("https://i.postimg.cc/rsNxdkX0/Self-Saboteur-Profile.png")
                    print("Hope you enjoyed taking the quiz! See you around!")
                    start_quiz = input("Do you want to start over? (enter Yes, or No, strictly)")
 
                else:
                    time.sleep(T)
                    print("No problem, hope you enjoyed taking the quiz! See you around!")
                    start_quiz = "No"

            else:
                time.sleep(T)
                print("No problem, hope you enjoyed taking the quiz! See you around!")
                start_quiz = "No"

    elif Q71.upper().strip() == "B":
        o_answer1 = input(Back.MAGENTA + "You are an Ostrich😶! Do you want to learn more about Ostrich? (enter Yes, or No)")
        if o_answer1.upper().strip() == 'YES':
            time.sleep(T)
            print()
            print(Back.CYAN + "You like to stick your head in the sand and ignore the tasks at hand -\n"
                    "avoiding having to make decisions.")
            time.sleep(T)
            print()
            print("If you don't make a decision, then you don't risk failing or being judged.\n"
                    "note: this is just an interpretation, do not treat it too seriously!")
            time.sleep(T)
            print()

            o_answer2 = input(Back.MAGENTA + "Would you want some tips for dealing with procrastination? (enter Yes, or No)")
            if o_answer2.upper().strip() == "YES":
                time.sleep(T)
                print()
                print(Back.YELLOW + "SELF-TALK CONFIDENTLY: Notice how you are talking to yourself when procrastinating.\n"
                        "Think positively - instead of 'I can't', say 'I will'.\n"
                        "note: this is just a suggestion, do not treat it too seriously!")
                time.sleep(T)
                print(Style.RESET_ALL)
                print()

                o_answer3 = input(Back.MAGENTA + "Would you want to get an Ostrich profile? (enter Yes, or No)")
                if o_answer3.upper().strip() == "YES":
                    wb.open("https://i.postimg.cc/yNC1GSSK/Ostrich-Profile.png")
                    print("Hope you enjoyed taking the quiz! See you around!")
                    start_quiz = input("Do you want to start over? (enter Yes, or No, strictly)")

                else:
                    time.sleep(T)
                    print("No problem, hope you enjoyed taking the quiz! See you around!")
                    start_quiz = "No"

            else:
                time.sleep(T)
                print("No problem, hope you enjoyed taking the quiz! See you around!")
                start_quiz = "No"

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


def Q72_function(start_quiz):
    Q72 = input(Fore.BLUE + "Are you afraid of failure? (enter A, or B)\n"
                "A) Of course! I don't want to feel useless\n"
                "B) I let other people take the heat")

    if Q72.upper().strip() == "A":
        o_answer1 = input(Back.MAGENTA + "You are an Ostrich😶! Do you want to learn more about Ostrich? (enter Yes, or No)")
        if o_answer1.upper().strip() == 'YES':
            time.sleep(T)
            print()
            print(Back.CYAN + "You like to stick your head in the sand and ignore the tasks at hand -\n"
                    "avoiding having to make decisions.")
            time.sleep(T)
            print()
            print("If you don't make a decision, then you don't risk failing or being judged.\n"
                    "note: this is just an interpretation, do not treat it too seriously!")
            time.sleep(T)
            print()

            o_answer2 = input(Back.MAGENTA + "Would you want some tips for dealing with procrastination? (enter Yes, or No)")
            if o_answer2.upper().strip() == "YES":
                time.sleep(T)
                print()
                print(Back.YELLOW + "SELF-TALK CONFIDENTLY: Notice how you are talking to yourself when procrastinating.\n"
                        "Think positively - instead of 'I can't', say 'I will'.\n"
                        "note: this is just a suggestion, do not treat it too seriously!")
                time.sleep(T)
                print(Style.RESET_ALL)
                print()

                o_answer3 = input(Back.MAGENTA + "Would you want to get an Ostrich profile? (enter Yes, or No)")
                if o_answer3.upper().strip() == "YES":
                    wb.open("https://i.postimg.cc/yNC1GSSK/Ostrich-Profile.png")
                    print("Hope you enjoyed taking the quiz! See you around!")
                    start_quiz = input("Do you want to start over? (enter Yes, or No, strictly)")

                else:
                    time.sleep(T)
                    print("No problem, hope you enjoyed taking the quiz! See you around!")
                    start_quiz = "No"

            else:
                time.sleep(T)
                print("No problem, hope you enjoyed taking the quiz! See you around!")
                start_quiz = "No"

    elif Q72.upper().strip() == "B":
        c_answer1 = input(Back.MAGENTA + "You are a Chicken🐓! Do you want to learn more about Chicken? (enter Yes, or No)")
        if c_answer1.upper().strip() == 'YES':
            time.sleep(T)
            print()
            print(Back.CYAN + "With so many choices, how are you supposed to decide?\n"
                    "By the time you've made up your mind, it's too late.")
            time.sleep(T)
            print()
            print("You feel like you may as well put it off and let someone else choose.\n"
                    "note: this is just an interpretation, do not treat it too seriously!")
            time.sleep(T)
            print()

            c_answer2 = input(Back.MAGENTA + "Would you want some tips for dealing with procrastination? (enter Yes, or No)")
            if c_answer2.upper().strip() == "YES":
                time.sleep(T)
                print()
                print(Back.YELLOW + "SWISS-CHEESE THE BIG TASKS: Handle the biggest tasks first by breaking them\n"
                        "down into smaller manageable ones. Devote small amounts of time and achieve\n"
                        "as much as you can in each to boost your momentum.")
                time.sleep(T)
                print(Style.RESET_ALL)
                print()

                c_answer3 = input(Back.MAGENTA + "Would you want to get a Chicken profile? (enter Yes, or No)")
                if c_answer3.upper().strip() == "YES":
                    wb.open("https://i.postimg.cc/J48SScpP/Chicken-Profile.png")
                    print("Hope you enjoyed taking the quiz! See you around!")
                    start_quiz = input("Do you want to start over? (enter Yes, or No, strictly)")
     
                else:
                    time.sleep(T)
                    print("No problem, hope you enjoyed taking the quiz! See you around!")
                    start_quiz = "No"

            else:
                time.sleep(T)
                print("No problem, hope you enjoyed taking the quiz! See you around!")
                start_quiz = "No"

    else:
        time.sleep(T)
        print("Quitting now?! Alright, hope to see you again!")
        start_quiz = "No"
    
    return start_quiz


### MAIN FUNCTION
def start():
    """This is the 'What type of procrastinator'are you?' quiz introduction. Inputs include name, and answer to Q0.
    The user will be automatically directed to Q1 following the instructions, or else the quiz will end.

    PARAMETERS
    ----------
    none

    RETURNS
    -------
    none
    """
    
    start_quiz = "Yes"

    while start_quiz == "Yes":
        print()
        print()
        print(Fore.BLUE + " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print(Fore.CYAN + "  _______________________________________ ")
        print(" /______________________________________/|")
        print(" |                                      ||")
        print(" | WHAT TYPE OF PROCRASTINATOR ARE YOU? ||")
        print(" |______________________________________|/")
        print()
        print(Fore.BLUE + " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print()
        print(Fore.RED + "Are you a  😈  or  🧐  or  🤐  or  😶  or  🐓?")
        print()
        print()
        print(Fore.MAGENTA + "🐑🐬🐋                ---- by Sny L  ʕ•́ᴥ•̀ʔっ♡")
        print()
        print()
        print(Style.RESET_ALL)
        
        time.sleep(T)
        name = input(Fore.MAGENTA + "What's your name?")
        time.sleep(T)
        print("Hi " + name + "! Are you interested in knowing yourself more? Do you know why you procrastinate in work?\n"
            "In this quiz, you will be answering a series of simple but fun questions\n"
            "that will eventually tell you what type of procrastinator you are.")
        wb.open("https://www.youtube.com/watch?v=8YGlzSl6cxU")

        Q0 = input(Fore.CYAN + "Earphones on! You may listen to Kahoot the entire time while answering the quiz!\n"
                    "Are you ready? (enter Yes, or No)")
        if Q0.upper().strip() == "NO":
            time.sleep(T)
            print("Well, you are not ready :( So why don't we end here?")
            print()
            start_quiz = "No"

        elif Q0.upper().strip() == "YES":
            time.sleep(T)
            print("In order for us to evaluate you accurately, you may type in the answer instructed in the question\n" 
                "(any case or spacing is fine! unless specifically told to write 'strictly')\n"
                "If you wanna end the quiz, type anything other than the choices given.")   
            start_quiz = Q1_function(start_quiz)
        
        else:
            print("Oh no! You need to type either Yes or No for this question, or else this quiz will end!")
            start_quiz = "No"
            
