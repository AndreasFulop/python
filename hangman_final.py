# clear screen in every os
import os
import sys
import random


def cls():
    your_os = os.name
    if your_os == "posix":
        os.system('clear')
    else:
        os.system('cls')


cls()

# menu to selecting levels
level = ""


def menu():
    levelcheck = False
    level = input(
        "Let's play! What level do you chose? Easy(e), Medium(m) or Hard(h)?")
    while levelcheck is False:
        if (level == "e" or level == "m" or level == "h"):
            levelcheck = True
        else:
            level = input(
                "Invalid parameter(s)! What level do you chose? Easy(e), Medium(m) or Hard(h)?")
            levelcheck = False

    if level == "e":
        return 4
    elif level == "m":
        return 6
    elif level == "h":
        return 8


lives = menu()
cclevel = ""
# get random word from the txt file
# def txt():
if lives == 4:
    cclevel = "countriesEasy.txt"
elif lives == 6:
    cclevel = "countriesMedium.txt"
elif lives == 8:
    cclevel = "countriesHard.txt"

# def random


def get_cc():
    f = open(cclevel)
    words = f.read().splitlines()
    word = random.choice(words)
    return word


country = get_cc()

# def capital or country


def capORcou(num):
    x = country.split(" | ")
    return x[num]


Coolcode = capORcou(0)
Codecool = capORcou(1).lower()
# ascii function


def get_ascii(n):
    g = open("hangmanrajz.py")
    pic = g.read().splitlines()
    return pic[n]


def play(word, lives):
    # make opening screen
    i = 0
    guessword = ""
    solution = ""
    while i < len(word):
        guessword += "_ "
        solution += "_"
        i += 1
# display the underlines
    print("Try to guess which capital is this:\n", guessword)
    setguess = set()
    while lives > 0:
        # put the guess in the set
        print("\nYou have ", lives, "tries.")
        letter = input("Write me your guess!").lower()
# exit by gamer
        if letter == "quit":
            sys.exit("Your a coward gamer. Bye!")
# repeat checking
        lettercheck = False
        setlist = list(setguess)
        if setlist != []:
            while lettercheck is False:
                if letter == "quit":
                    sys.exit("Your a coward gamer. Bye!")
                else:
                    for q in setlist:
                        if letter == q:
                            letter = input(
                                "Sorry, but you have already guessed this letter. Try a new one!").lower()
                            lettercheck = False
                            break
                        else:
                            lettercheck = True
# attempts
        setguess.add(letter)
        printset = ""
        printset += ", ".join(setguess)
# succesful guess
        j = 0
        j2 = 0
        lifesteal = False
        cls()
        for w in word:
            if w == letter:
                tmp = list(guessword)
                tmp.insert(j, w)
                tmp.pop(j+1)
                guessword = "".join(tmp)
                tmp = list(solution)
                tmp.insert(j2, w)
                tmp.pop(j2+1)
                solution = "".join(tmp)
                lifesteal = True
            guessword2 = guessword.capitalize()
            j += 2
            j2 += 1
        if word != solution:
            print(guessword2)
# won the game
        else:
            print(guessword2)
            sys.exit("Nice game, you won!")
# lives-counting
        if lifesteal is False:
            lives -= 1
            print("\nBad luck!")
        else:
            print("\nBravo, go on!")
# ascii graphs
        if cclevel == "countriesEasy.txt":
            a = 2
            b = 10
            i = lives*11
        if cclevel == "countriesMedium.txt":
            a = 60
            b = 67
            i = lives*11
        if cclevel == "countriesHard.txt":
            a = 139
            b = 147
            i = lives*12
        x = range(a+i, b+i)
        for n in x:
            y = get_ascii(n)
            print(y)

        print("\nYour attempts: ", printset)
    print("GAME OVER")
    print("The capital was:", word.capitalize() +
          ", the capital of " + Coolcode + ".")


# ascii art for menu
x = range(46, 54)
for n in x:
    y = get_ascii(n)
    print(y)
# call the game
play(Codecool, lives)
