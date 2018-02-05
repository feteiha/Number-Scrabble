v=0
g=[1,2,3,4,5,6,7,8,9]
p1=0
p2=0
x=1
y=1
s=0
print("Welcome To Number Scrabble")
s=input("Press ENTER to START...")
if s=="":
    while v==0:
            while True:
                print(g)
                x=int(input("PLAYER ONE; choose a number from above: "))
                if x in g:
                    g.remove(x)
                    p1=p1+x
                    print("PLAYER ONE; score:",p1)
                    break
                else:
                    print("Error, Number not available!")                   
            if p1==15:
                print("PLAYER ONE WINS!")
                v=1
                break
            if g==[]:
                print("Draw!")
                break
            if v==0:
                while True:
                    print (g)
                    y=int(input("PLAYER TWO; choose a number from above: "))
                    if y in g:
                        g.remove(y)
                        p2=p2+y
                        print("PLAYER TWO; score:",p2)
                        break
                    else:
                        print("Error, Number not available!")
                if p2==15:
                    print("PLAYER TWO WINS!")
                    v=1
                    break
                if g==[]:
                    print("Draw!")
                    break
