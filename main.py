# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import sys


CORRECT = 0
WRONG = 0

LETTERS_DICTIONARY = {"a"	: "\u03B1",
                      "b"	: "\u03B2",
                      "g"	: "\u03B3",
                      "d"	: "\u03B4",
                      "e"	: "\u03B5",
                      "z"	: "\u03B6",
                      "h"	: "\u03B7",
                      "q"	: "\u03B8",
                      "i"	: "\u03B9",
                      "k"	: "\u03BA",
                      "l"	: "\u03BB",
                      "m"	: "\u03BC",
                      "n"	: "\u03BD",
                      "c"	: "\u03BE",
                      "o"	: "\u03BF",
                      "p"	: "\u03C0",
                      "r"	: "\u03C1",
                      "$"	: "\u03C2",
                      "s"	: "\u03C3",
                      "t"	: "\u03C4",
                      "u"	: "\u03C5",
                      "f"	: "\u03C6",
                      "x"	: "\u03C7",
                      "y"	: "\u03C8",
                      "w"	: "\u03C9",
                      "A"	: "\u0391",
                      "B"	: "\u0392",
                      "G"	: "\u0393",
                      "D"	: "\u0394",
                      "E"	: "\u0395",
                      "Z"	: "\u0396",
                      "H"	: "\u0397",
                      "Q"	: "\u0398",
                      "I"	: "\u0399",
                      "K"	: "\u039A",
                      "L"	: "\u039B",
                      "M"	: "\u039C",
                      "N"	: "\u039D",
                      "C"	: "\u039E",
                      "O"	: "\u039F",
                      "P"	: "\u03A0",
                      "R"	: "\u03A1",
                      "S"	: "\u03A3",
                      "T"	: "\u03A4",
                      "U"	: "\u03A5",
                      "F"	: "\u03A6",
                      "X"	: "\u03A7",
                      "Y"	: "\u03A8",
                      "W"	: "\u03A9",
                      "|"   : "\u03B7\u0345",
                      " "   : " "
                      }

TIME_DICTIONARY = {"1": "Present", "2": "Imperfectum", "3": "Aoristus",
                   "4": "Futurum", "5": "Perfectum"}
MODUS_DICTIONARY = {"1": "Indicativus", "2": "Coniunctivus", "3": "Optativus",
                    "4": "Imperativus", "5": "Infinitivus"}
ACTIVE_PASSIVE_CICTIONARY = {"1": "act.", "2": "med.", "3": "pass."}
PERSON_NUM_DICTIONARY ={"1": "1SG", "2": "2SG", "3": "3SG",
                        "4": "1PL", "5": "2PL", "6": "3PL"}

OPENING_MESSEGE = "Welcome to Ancient Greek inflections memorization tool!\n" \
                  "This is how it works:\n"\
                  "each time you will be given a verb. You will be required " \
                  "to analayze it according to the following categories:\n" \
                  "1. TIME\n" \
                  "2. MODUS\n" \
                  "3. ACTIV\MED\PASS\n" \
                  "4. PERSON + NUMBER\n"

TABLE = "Your answer should contain ONLY NUMBERS, without separator," \
         "according to the following table:\n" \
        " ----------------------------------------------------------------\n" \
         "|       TIME      |      MODUS      |  ACTIVE  | PERSON + NUMBER |\n" \
         "|----------------------------------------------------------------|\n" \
         "| 1 = PRESENT     | 1 = INDICATIVUS | 1 = ACT. |     1 = 1SG     |\n" \
         "| 2 = IMPERFECTUM | 2 = CONIUNCTIVUS| 2 = MED. |     2 = 2SG     |\n" \
         "| 3 = AORISTUS    | 3 = OPTATIVUS   | 3 = PASS.|     3 = 3SG     |\n" \
         "| 4 = FUTURUM     | 4 = IMPERATIVUS |          |     4 = 1PL     |\n" \
         "| 5 = PERFECTUM   | 5 = INFINITIVUS |          |     5 = 2PL     |\n" \
         "|                 |                 |          |     6 = 3PL     |\n" \
         " ----------------------------------------------------------------\n"

EXAMPLE = "For example, if given the word \u03C0\u03B1\u03B9\u03B4\u03B5\u03C5\u03C9," \
          " your answer should be as follows:\n" \
          "1111\n" \
          "because: time is present, modus is indicaticus, this is an active form, of 1sg\n"

INSTRUCTIONS = "When you press enter, your answer will be submitted ant checked.\n" \
            "At any point, you can type 'table' and then hit enter, to show the table.\n" \
            "When you are ready to begin, hit ENTER.\nGOOD LUCK!\n\n"

PRESENT = [# indicative
    [# act - 0
        ["paideuw", "paideueis", "paideuei", "paideuomen", "paideuete", "paideuousin"],
        # passive,
        ["paideuomai",  "paideu|", "paideuetai","paideuomeqa","paideuesqe","paideuontai"]],


    [ # conjunctive - 1
        ["paideuw",  "paideu|s", "paideu|" ,"paideuwmen","paideuhte", "paideuwsin"],
        ["paideuwmai", "paideu|", "paideuhtai", "paideuwmeqa", "paideuhsqe", "paideuwntai"]

    ],
    [
        # optative - 2
        ["paideuoimi", "paideouois", "paideuoi","paideuoimen",  "paideuoite",  "paideuoien"],
        ["paideuoimhn", "paideuoio", "paideuoito","paideuoimeqa", "paideuoisqe", "paideuointo"]
    ],
    [ #imperative - 3
        ["", "paideue", "paideuetw","", "paideuete", "paideuontwn"],
        ["", "paideuou", "paideuesqw","", "paideuesqe", "paideuesqwn"]],

    [ # infinitive - 4
        ["paideuein"],
        ["paideuesqai"]]
    ]

IMPERFECT =[    #INDICATIVE - 0
                [["epaideuon", "epaideues", "epaideuen", "epaideuomen",  "epaideuete", "epaideuon"],
                ["epaideuomhn", "epaideuou", "epaideueto","epaideuomeqa", "epaideuesqe", "epaideuonto"]
            ]]


AORIST = [# indicative
    [# act - 0
        ["epaideusa", "epaideusas", "epaideusen", "epaideusamen", "epaideusate", "epaideusan"],
        # med - 1
        ["epaideusamhn",  "epaideusw", "epaideusato","epaideusameqa","epaideusasqe","epaideusanto"],
        # pass - 2
        ["epaideuqhn", "epaideuqhs", "epaideuqh", "epaideuqhmen", "epaideuqhte", "epaideuqhsan"]
    ],


    [ # conjunctive - 1
        ["paideusw", "paideus|s", "paideus|", "paideuswmen", "paideushte", "paideuswsin"],
        # med - 1
        ["paideuswmai",  "paideus|", "paideushtai","paideuswmeqa","paideushsqe","paideuswntai"],
        # pass - 2
        ["paideuqw", "paideuq|s", "paideuq|", "paideuqwmen", "paideuqhte", "paideuqwsin"]
    ],
    [
        # optative - 2
        # act - 0
        ["paideusaimi", "paideusais", "paideusai","paideusaimen",  "paideusaite",  "paideusaien"],
        #med - 1
        ["paideusaimhn", "paideusaio", "paideusaito","paideusaimeqa",  "paideusaisqe",  "paideusainto"],
        # pass - 2
        ["paideuqeihn", "paideuqeihs", "paideuqeih","paideuqeihmen", "paideuqeihte", "paideuqeihsan"]
    ],
    [ #imperative - 3
        ["", "paideuson", "paideusatw","", "paideusate", "paideusantwn"],
        ["", "paideusai", "paideusasqw","", "paideusasqe", "paideusasqwn"],
        ["", "paideuqhti", "paideuqhtw", "", "paideuqhte", "paideuqentwn"]
    ],

    [ # infinitive - 4
        ["paideusai"],
        ["paideusasqai"],
        ["paideuqhnai"]
    ]
]

FUTURE = [# indicative
    [# act - 0
        ["paideusw", "paideuseis", "paideusei", "paideusomen", "paideusete", "paideusousin"],
        #med - 1
        ["paideusomai",  "paideus|", "paideusetai","paideusomeqa","paideusesqe","paideusontai"],
        # pass - 2
        ["paideuqhsomai", "paideuqhs|", "paideuqhsetai", "paideuqhsomeqa", "paideuqhsesqe", "paideuqhsontai"]
    ],


    [],
    [
        # optative - 2
        ["paideusoimi", "paideousois", "paideusoi","paideusoimen",  "paideusoite", "paideusoien"],
        ["paideusoimhn", "paideusoio", "paideusoito","paideusoimeqa", "paideusoisqe", "paideusointo"],
        # pass
        ["paideuqhsoimhn", "paideuqhsoio", "paideuqhsoito", "paideuqhsoimeqa", "paideuqhsoisqe", "paideuqhsointo"]
    ],
    [],

    [ # infinitive - 4
        ["paideusein"],
        ["paideusesqai"],
        ["paideuqhsesqai"]
    ]
]

PERFECT =  [# indicative
    [# act - 0
        ["pepaideuka", "pepaideukas", "pepaideuken", "pepaideukamen", "pepaideukate", "pepaideukasin"],
        # passive,
        ["pepaideumai",  "pepaideusai", "pepaideutai","pepaideumeqa","pepaideusqe","pepaideuntai"]],


    [ # conjunctive - 1
        ["pepaideukw",  "pepaideuk|s", "pepaideuk|" ,"pepaideukwmen","pepaideukhte", "pepaideukwsin"],
        ["pepaideumonos w", "pepaideumonos |s", "pepaideumonos |", "pepaideumonoi wmen", "pepaideumonoi hte", "pepaideumonoi wsin"]

    ],
    [
        # optative - 2
        ["pepaideukoimi", "pepaideukois", "pepaideukoi","pepaideukoimen",  "pepaideukoite",  "pepaideukoien"],
        ["pepaideumonos eihn", "pepaideumonos eihs", "pepaideumonos eih","pepaideumonoi eimen", "pepaideumonoi eite", "pepaideumonoi eien"]
    ],
    [ #imperative - 3
        ["", "pepaideuke", "pepaideuketw","", "pepaideukete", "pepaideukontwn"],
        ["", "pepaideuso", "pepaideusqw","", "pepaideusqe", "pepaideusqwn"]],

    [ # infinitive - 4
        ["pepaideukenai"],
        ["pepaideusqai"]]
]


def pick_imperfect(modus, act_pass, person):
    modus = 1
    if act_pass != 1:
        act_pass = 2
    correct_answer = "2" + str(modus) + str(act_pass) + str(person)
    return (IMPERFECT[modus - 1][act_pass - 1][person - 1], correct_answer)


def pick_present(modus, act_pass, person):
    if act_pass != 1:
        act_pass = 2 # present has one form for med-pass
    if modus == 5: #infinitive has no number
        correct_answer = "1" + str(modus) + str(act_pass)
        return (PRESENT[modus - 1][act_pass - 1][0], correct_answer)
    elif modus == 4 and (person == 1 or person == 4): # imperative
        person = random.choice([2,3,5,6])

    correct_answer = "1" + str(modus) + str(act_pass) + str(person)
    return (PRESENT[modus - 1][act_pass - 1][person - 1], #form,
            correct_answer)


def pick_aorist(modus, act_pass, person):
    if modus == 5: #infinitive has no number
        correct_answer = "3" + str(modus) + str(act_pass)
        return (AORIST[modus - 1][act_pass - 1][0], correct_answer)
    elif modus == 4 and (person == 1 or person == 4): # imperative
        person = random.choice([2,3,5,6])
    correct_answer = "3" + str(modus) + str(act_pass) + str(person)
    return (AORIST[modus - 1][act_pass - 1][person - 1], #form,
            correct_answer)


def pick_future(modus, act_pass, person):
    if modus == 2 or modus == 4:
        modus =random.choice([1,3,5]) # future has no form of conj. or imperative
    if modus == 5: #infinitive has no number
        correct_answer = "4" + str(modus) + str(act_pass)
        return (FUTURE[modus - 1][act_pass - 1][0], correct_answer)
    correct_answer = "4" + str(modus) + str(act_pass) + str(person)
    return (FUTURE[modus - 1][act_pass - 1][person - 1], #form,
            correct_answer)


def pick_perfect(modus, act_pass, person):
    if act_pass != 1:
        act_pass = 2 # present has one form for med-pass
    if modus == 5: #infinitive has no number
        correct_answer = "5" + str(modus) + str(act_pass)
        return (PERFECT[modus - 1][act_pass - 1][0], correct_answer)
    elif modus == 4 and (person == 1 or person == 4): # imperative
        person = random.choice([2,3,5,6])

    correct_answer = "5" + str(modus) + str(act_pass) + str(person)
    return (PERFECT[modus - 1][act_pass - 1][person - 1], #form,
            correct_answer)


def pickAform():
    time = random.randint(1,5)
    modus = random.randint(1,5)
    active = random.randint(1,3)
    person = random.randint(1,6)

    if time == 1:
        form, correct_answer = pick_present(modus, active, person)
    elif time == 2:
        form, correct_answer = pick_imperfect(modus, active, person)
    elif time == 3:
        form, correct_answer = pick_aorist(modus, active, person)
    elif time == 4:
        form, correct_answer = pick_future(modus, active, person)
    elif time == 5:
        form, correct_answer = pick_perfect(modus, active, person)
    return form, correct_answer


def print_full_answer(correct_answer):
    print("The correct answer is " + correct_answer + ":")
    verbal_answer = TIME_DICTIONARY[correct_answer[0]] + ", "
    verbal_answer += MODUS_DICTIONARY[correct_answer[1]] + ", "
    verbal_answer += ACTIVE_PASSIVE_CICTIONARY[correct_answer[2]]
    if len(correct_answer) > 3:
        verbal_answer += ", "
        verbal_answer += PERSON_NUM_DICTIONARY[correct_answer[3]] +"."
    print(verbal_answer)


def get_answer(form, correct_answer):
    printGreek(form)
    analysis = input("Please write your analysis:")
    while analysis.lower() == "table":
        print(TABLE)
        printGreek(form)
        analysis = input("Please write your analysis:")

    if analysis == correct_answer:
        global CORRECT
        CORRECT += 1
        print("you are correct!")

    else:
        global WRONG
        WRONG += 1
        print("Thats incorrect.")
    print("TOTAL CORRECT ANSWERS: " + str(CORRECT) + " | " + "TOTAL WRONG ANSWERS: " + str(WRONG))
    print_full_answer(correct_answer)


def printGreek(word):
    # Use a breakpoint in the code line below to debug your script.
    new_word = ""
    for letter in word:
        new_word += LETTERS_DICTIONARY[letter]
    print(new_word)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(OPENING_MESSEGE)
    print(TABLE)
    print(EXAMPLE)
    print(INSTRUCTIONS)
    play = True
    while play:
        form, correct_answer = pickAform()
        get_answer(form, correct_answer)
