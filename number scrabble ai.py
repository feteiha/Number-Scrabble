win=0
sum1=[]
sum2=[]
choose=[1,2,3,4,5,6,7,8,9]
p=0
c1=0
c2=0
import random
print("                            WELCOME TO NUMBER SCRABBLE!")
while True:
    while True:
        try:
            p=input("Press 1 for ONE PLAYER and 2 for TWO PLAYERS or 3 to Exit: ")
            p=int(p)
            break
        except ValueError:
            print("No Valid Number, Please try again.")       
    if p==2:
        for i in range (3):
            while True:
                while True:
                    try:
                        print("                     ",choose)
                        c1=input("Player 1: Choose a number from above: ")
                        c1=int(c1)
                        break
                    except ValueError:
                        print("No Valid Number, Please try again.")
                if c1 in choose:
                    sum1.append(c1)
                    choose.remove(c1)
                    print("                                                Player 1 numbers:", sum1)
                    break
                else:
                    print("Error, number choosen isn't available!")
            if i==2:
                if sum1[0]+sum1[1]+sum1[2]==15:
                    print("PLAYER 1 WINS!!")
                    win=1
                    break
            if win==0:
                while True:
                    while True:
                        try:
                            print("                     ",choose)
                            c2=input("Player 2: Choose a number from above: ")
                            c2=int(c2)
                            break
                        except ValueError:
                            print("No Valid Number, Please try again.")
                    if c2 in choose:
                        sum2.append(c2)
                        choose.remove(c2)
                        print("                                                Player 2 numbers:", sum2)
                        break
                    else:
                        print("Error, number choosen isn't available!")
        if win ==0:                    
            if sum2[0]+sum2[1]+sum2[2]==15:
                print("PLAYER 2 WINS!!")
                win=1
        if win==0:
            while True:
                while True:
                    try:
                        print("                     ",choose)
                        c1=input("Player 1: Choose a number from above: ")
                        c1=int(c1)
                        break
                    except ValueError:
                        print("No Valid Number, Please try again.")
                if c1 in choose:
                    sum1.append(c1)
                    choose.remove(c1)
                    print("                                                Player 1 numbers:", sum1)
                    break
                else:
                    print("Error, number choosen isn't available!")
        if win==0:
            if sum1[1]+sum1[2]+sum1[3]==15 or sum1[0]+sum1[2]+sum1[3]==15 or sum1[0]+sum1[1]+sum1[3]==15:
                print("PLAYER 1 WINS!!")
                win=1
        if win==0:
            while True:
                while True:
                    try:
                        print("                     ",choose)
                        c2=input("Player 2: Choose a number from above: ")
                        c2=int(c2)
                        break
                    except ValueError:
                        print("No Valid Number, Please try again.")
                if c2 in choose:
                    sum2.append(c2)
                    choose.remove(c2)
                    print("                                                Player 2 numbers:", sum2)
                    break
                else:
                    print("Error, number choosen isn't available!")
        if win==0:    
            if sum2[1]+sum2[2]+sum2[3]==15 or sum2[0]+sum2[2]+sum2[3]==15 or sum2[0]+sum2[1]+sum2[3]==15:
                print("PLAYER 2 WINS!!")
                win=1
        if win==0:
            while True:
                while True:
                    try:
                        print("                     ",choose)
                        c1=input("Player 1: Choose a number from above: ")
                        c1=int(c1)
                        break
                    except ValueError:
                        print("No Valid Number, Please try again.")
                if c1 in choose:
                    sum1.append(c1)
                    choose.remove(c1)
                    print("                                                Player 1 numbers:", sum1)
                    break
                else:
                    print("Error, number choosen isn't available!")
        if win==0:
            if sum1[1]+sum1[2]+sum1[4]==15 or sum1[0]+sum1[1]+sum1[4]==15 or sum1[2]+sum1[3]+sum1[4]==15 or sum1[0]+sum1[2]+sum1[4]==15 or sum1[0]+sum1[3]+sum1[4]==15 or sum1[1]+sum1[3]+sum1[4]==15:
                print("PLAYER 1 WINS!!")
                win=1
        if win==0:
            print("DRAW!")
    if p==1:
        for i in range(5):
            while True:
                while True:
                    try:
                        print("                     ",choose)
                        c1=input("Player 1: Choose a number from above: ")
                        c1=int(c1)
                        break
                    except ValueError:
                        print("No Valid Number, Please try again.")
                if c1 in choose:
                    sum1.append(c1)
                    choose.remove(c1)
                    print("                                                Player 1 numbers:", sum1)
                    break
                else:
                    print("Error, number choosen isn't available!")
            if i==2:
                   if sum1[0]+sum1[1]+sum1[2]==15:
                        print("PLAYER 1 WINS!!")
                        win=1
                        break
            if i==3:
                if sum1[1]+sum1[2]+sum1[3]==15 or sum1[0]+sum1[2]+sum1[3]==15 or sum1[0]+sum1[1]+sum1[3]==15:
                    print("PLAYER 1 WINS!!")
                    win=1
                    break
            if i==4:        
                 if sum1[1]+sum1[2]+sum1[4]==15 or sum1[0]+sum1[1]+sum1[4]==15 or sum1[2]+sum1[3]+sum1[4]==15 or sum1[0]+sum1[2]+sum1[4]==15 or sum1[0]+sum1[3]+sum1[4]==15 or sum1[1]+sum1[3]+sum1[4]==15:
                    print("PLAYER 1 WINS!!")
                    win=1

                    
            if i<4:
                c2=random.choice(choose)
                sum2.append(c2)
                choose.remove(c2)
                print("                                                Computer:", sum2)
                if i==2:
                   if sum1[0]+sum1[1]+sum1[2]==15:
                        print("COMPUTER WINS!!")
                        win=1
                        break
                if i==3:
                    if sum2[1]+sum2[2]+sum2[3]==15 or sum2[0]+sum2[2]+sum2[3]==15 or sum2[0]+sum2[1]+sum2[3]==15:
                        print("COMPUTER WINS!!")
                        win=1
                        break
            
        if win==0:
            print("DRAW!!")
    elif p==3:
        print("GoodBYE!")
        break
    else:
        print("Please enter a valid number.")


    
    
