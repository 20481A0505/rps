from tkinter import *
from PIL import Image,ImageTk
from random import randint
#window
root= Tk()
root.title("rps")
root.configure(background="orange")
#PICS
player2_rock = ImageTk.PhotoImage(Image.open("rock2.png"))
player2_paper = ImageTk.PhotoImage(Image.open("paper2.png"))
player2_scissor = ImageTk.PhotoImage(Image.open("scissor2.png"))
player1_rock = ImageTk.PhotoImage(Image.open("rock1.png"))
player1_paper= ImageTk.PhotoImage(Image.open("paper1.png"))
player1_scissor= ImageTk.PhotoImage(Image.open("scissor1.png"))

#inserting 
player2=Label(root,image=player2_paper)
player1=Label(root,image=player1_paper)
player1.grid(row=1,column=0)
player2.grid(row=1,column=30)


#scores
p2score=Label(root,text=0,font=100,bg="orange",fg="black")
p1score=Label(root,text=0,font=100,bg="orange",fg="black")
p1score.grid(row=1,column=1)
p2score.grid(row=1,column=9)

#indicator
p2indicator=Label(root,font=50,text="player2",bg="orange",fg="white")
p1indicator=Label(root,font=50,text="player1",bg="orange",fg="white")
p2indicator.grid(row=0,column=6)
p1indicator.grid(row=0,column=0)

#messages
msg=Label(root,font=50,bg="orange",fg="red")
msg.grid(row=3,column=2)

#update messages
def updateMessage(x):
    msg['text']=x

#update p2score
def updateplayer2score():
    score=int(p2score["text"])
    score+=1
    p2score["text"]=str(score)
#update p1score
def updateplayer1score():
    score=int(p1score["text"])
    score+=1
    p1score["text"]=str(score)
#check winner
def checkwin(player1,player2):
    if player2==player1:
        updateMessage("its a tie")
    elif player2=="rock":
        if player1 =="paper":
            updateMessage("you loose")
            updateplayer1score()
        else:
            updateMessage("you win")
            updateplayer2score
    elif player2=="paper":
        if player1=="scissor":
            updateMessage("you loose")
            updateplayer1score()
        else:
            updateMessage("you win")
            updateplayer2score()
    elif player2=="scissor":
        if player1=="rock":
            updateMessage("you loose")
            updateplayer1score()
        else:
            updateMessage("you win")
            updateplayer2score()
    else:
        pass
#update choices
def updatechoice(x):
    if x == "rock":
        player1.configure(image=player1_rock)
    elif x =="paper":
        player1.configure(image=player1_paper)
    else:
        player1.configure(image=player1_scissor)
#for user
def updatechoice2(x):
    if x =="rock2":
        player2.configure(image=player2_rock)
    elif x =="paper2":
        player2.configure(image=player2_paper)
    else:
        player2.configure(image=player2_scissor)

#buttons
rock=Button(root,width=10,height=2,text="Rock",bg="red",command=lambda:updatechoice("rock")).grid(row=5,column=1)
paper=Button(root,width=10,height=2,text="paper",bg="yellow",command=lambda:updatechoice("paper")).grid(row=5,column=2)
scissor=Button(root,width=10,height=2,text="scissor",bg="skyblue",command=lambda:updatechoice("scissor")).grid(row=5,column=3)
rock2=Button(root,width=10,height=2,text="Rock",bg="red",command=lambda:updatechoice2("rock2")).grid(row=5,column=7)
paper2=Button(root,width=10,height=2,text="paper",bg="yellow",command=lambda:updatechoice2("paper2")).grid(row=5,column=8)
scissor2=Button(root,width=10,height=2,text="scissor",bg="skyblue",command=lambda:updatechoice2("scissor2")).grid(row=5,column=9)
root.mainloop()