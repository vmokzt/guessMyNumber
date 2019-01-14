import random
import sys

x = random.randint(0,101)
 
guess1 = int(input('I am thinking of a number from 0 to 100. What do you think it is? Please type numbers only. (Tries left: 5)\n'))

while x != guess1:
    print
    if guess1 < x:
        guess2 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess1) + " to 100 (Tries left: 4)\n"))
        
        while x != guess2:
            print
            if guess2 < x:
                    guess3 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess2) + " to 100 (Tries left: 3)\n"))
                    
                    while x != guess3:
                        print
                        if guess3 < x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to 100 (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to 100 (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        elif guess3 > x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess2) + " to " + str(guess3) + " (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to " + str(guess3) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess2) + " to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        else:
                            print("You got it on your third try!")
                            sys.exit()
                            
            elif guess2 > x:
                guess3 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess1) + " to " + str(guess2) + " (Tries left: 3)\n"))

                while x != guess3:
                        print
                        if guess3 < x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to " + str(guess2) + " (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to " + str(guess2) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        elif guess3 > x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: " + + str(guess1) + " to " + str(guess3) + " (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to " + str(guess3) + "(Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess1) + " to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        else:
                            print("You got it on your third try!")
                            sys.exit()
                                 
            else:
                print("You got it in two tries!")
                sys.exit()
                                 
    elif guess1 > x:
        guess2 = int(input("That is incorrect. Guess again! Here's a hint: 0 to " + str(guess1) + " (Tries left: 4)\n"))
        
        while x != guess2:
            print
            if guess2 < x:
                    guess3 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess2) + " to " + str(guess1) + " (Tries left: 3)\n"))
                    
                    while x != guess3:
                        print
                        if guess3 < x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to " + str(guess1) + " (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to " + str(guess1) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        elif guess3 > x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: " + + str(guess2) + " to " + str(guess3) + " (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to " + str(guess3) + "(Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess2) + " to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        else:
                            print("You got it on your third try!")
                            sys.exit()
                            
            elif guess2 > x:
                guess3 = int(input("That is incorrect. Guess again! Here's a hint: 0 to " + str(guess2) + " (Tries left: 3)\n"))

                while x != guess3:
                        print
                        if guess3 < x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to " + str(guess2) + " (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to " + str(guess2) + "(Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess3) + " to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        elif guess3 > x:
                            guess4 = int(input("That is incorrect. Guess again! Here's a hint: 0 to " + str(guess3) + " (Tries left: 2)\n"))

                            while x != guess4:
                                print
                                if guess4 < x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: " + str(guess4) + " to " + str(guess3) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()

                                elif guess4 > x:
                                    guess5 = int(input("That is incorrect. Guess again! Here's a hint: 0 to " + str(guess4) + " (Tries left: 1)\n"))

                                    if x != guess5:
                                        print("That is incorrect. You have run out of tries! I was thinking of the number " + str(x) + ".")
                                        sys.exit()
                                    else:
                                        print("You got it on your last try!")
                                        sys.exit()
                                else:
                                    print("You got it on your fourth try!")
                                    sys.exit()

                        else:
                            print("You got it on your third try!")
                            sys.exit()
                                 
            else:
                print("You got it in two tries!")
                sys.exit()
        
    else:
        print("Wow! Are you a psychic? You got it in one try!")
        sys.exit()

