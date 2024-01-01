import random as r
l=["ROCK","PAPER","SCISSOR"]
while True:
    g=int(input("""
Do you want to Start the Game:
1.Yes
2.No
"""))
    if g==1:
        usercount=0
        computercount=0
        drawcount=0
        for i in range(1,6):
            print('''
1.ROCK
2.PAPER
3.SCISSOR
''')    
            cc=r.choice(l)
            userchoice=int(input("Choose Choice "))
            uc=""
            if userchoice==1:
                uc="ROCK"
            if userchoice==2:
                uc="PAPER"
            if userchoice==3:
                uc="SCISSOR"

            

            if uc==cc:
                print("User Coice ",uc)
                print("Computer Coice ",cc)
                print("Round Draw") 
                drawcount +=1
            elif uc=="ROCK" and cc=="SCISSOR" or uc=="SCISSOR" and cc=="PAPER" or uc=="PAPER" and cc=="ROCK":
                print("User Coice ",uc)
                print("Computer Coice ",cc)  
                print("You Win")
                usercount +=1
            elif cc=="ROCK" and uc=="SCISSOR" or cc=="SCISSOR" and uc=="PAPER" or cc=="PAPER" and uc=="ROCK":
                print("User Coice ",uc)
                print("Computer Coice ",cc)  
                print("Computer Win")
                computercount +=1
        print()
        if usercount>computercount:
            print("User Total Win =",usercount)
            print("Computer Total Win =",computercount)
            print("Draw=",drawcount)
            print("User Win")
        elif usercount<computercount:
            print("User Total Win =",usercount)
            print("Computer Total Win =",computercount)
            print("Draw=",drawcount)
            print("Computer Win")
        elif drawcount>=3:
            print("User Total Win =",usercount)
            print("Computer Total Win =",computercount)
            print("Draw=",drawcount)
            
    if g==2:
        break