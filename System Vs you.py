p1=0
p2=0

for i in range (1,6):
    print("Round       :",i)
    P1=input("Select any one :-Rock,Paper,Scissor  ")
    P2=input("Select any one :-Rock,Paper,Scissor  ")

    if P1=="Rock":
        if P1=="Rock" and  P2=="Scissor":
            print("P1 Wins")
            print("*"*100)
            p1=p1+1
        elif P1=="Rock" and  P2=="Rock":
            print("Draw")
            print("*"*100)
        elif P1=="Rock" and  P2=="Paper":
            print("P2 Wins")
            print("*"*100)
            p2=p2+1
        else:
            print("error")
            print("*"*100)
    
        
    elif P1=="Paper":
        if P1=="Paper" and  P2=="Scissor":
            print("P2 Wins")
            print("*"*100)
            p2=p2+1
        elif P1=="Paper" and  P2=="Rock":
            print("P1 wins")
            print("*"*100)
            p1=p1+1
        elif P1=="Paper" and  P2=="Paper":
            print("Draw")
            print("*"*100)
        else:
            print("error")
            
    elif P1=="Scissor":
        if P1=="Scissor" and  P2=="Scissor":
            print("Draw")
            print("*"*100)
        elif P1=="Scissor" and  P2=="Rock":
            print("P2 wins")
            print("*"*100)
            p2=p2+1
        elif P1=="Scissor" and  P2=="Paper":
            print("P1 Wins")
            print("*"*100)
            p1=p1+1
        else:
            print("error")
            print("*"*100)

    else:
        print("error")
        print("*"*100)

if p1>p2:
    print("P1!! Winner Winner Chicken Dinner")
elif p2>p1:
    print("P2!! Winner Winner Chicken Dinner")
else:
    print("Draw!!")
    
    
            
