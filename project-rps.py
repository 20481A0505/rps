from tkinter import *
from PIL import Image,ImageTk
from random import randint
#window
root= Tk()
root.title("rps")
root.configure(background="orange")
#PICS
rock_img = ImageTk.PhotoImage(Image.open("rock2.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper2.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor2.png"))
rock_comp = ImageTk.PhotoImage(Image.open("rock1.png"))
paper_comp = ImageTk.PhotoImage(Image.open("paper1.png"))
scissor_comp = ImageTk.PhotoImage(Image.open("scissor1.png"))

#inserting 
user=Label(root,image=paper_img)
comp=Label(root,image=paper_comp)
comp.grid(row=1,column=0)
user.grid(row=1,column=30)


#scores
uscore=Label(root,text=0,font=100,bg="orange",fg="black")
compscore=Label(root,text=0,font=100,bg="orange",fg="black")
compscore.grid(row=1,column=1)
uscore.grid(row=1,column=3)

#indicator
uindicator=Label(root,font=50,text="user",bg="orange",fg="white")
compindicator=Label(root,font=50,text="computer",bg="orange",fg="white")
uindicator.grid(row=0,column=6)
compindicator.grid(row=0,column=0)

#messages
msg=Label(root,font=50,bg="orange",fg="red")
msg.grid(row=3,column=2)

#update messages
def updateMessage(x):
    msg['text']=x

#update userscore
def updateUserscore():
    score=int(uscore["text"])
    score+=1
    uscore["text"]=str(score)
#update compscore
def updatecompscore():
    score=int(compscore["text"])
    score+=1
    compscore["text"]=str(score)
#check winner
def checkwin(player,computer):
    if player==computer:
        updateMessage("its a tie")
    elif player=="rock":
        if computer =="paper":
            updateMessage("you loose")
            updatecompscore()
        else:
            updateMessage("you win")
            updateUserscore
    elif player=="paper":
        if computer=="scissor":
            updateMessage("you loose")
            updatecompscore()
        else:
            updateMessage("you win")
            updateUserscore()
    elif player=="scissor":
        if computer=="rock":
            updateMessage("you loose")
            updatecompscore()
        else:
            updateMessage("you win")
            updateUserscore()
    else:
        pass
#update choices
choices= ["rock","paper","scissor"]
def updatechoice(x):
    compchoice=choices[randint(0,2)]
    if compchoice == "rock":
        comp.configure(image=rock_comp)
    elif compchoice=="paper":
        comp.configure(image=paper_comp)
    else:
        comp.configure(image=scissor_comp)
#for user
    if x=="rock":
        user.configure(image=rock_img)
    elif x=="paper":
        user.configure(image=paper_img)
    else:
        user.configure(image=scissor_img)
    checkwin(x,compchoice)
#buttons
rock=Button(root,width=10,height=2,text="Rock",bg="red",command=lambda:updatechoice("rock")).grid(row=5,column=1)
paper=Button(root,width=10,height=2,text="paper",bg="yellow",command=lambda:updatechoice("paper")).grid(row=5,column=2)
scissor=Button(root,width=10,height=2,text="scissor",bg="skyblue",command=lambda:updatechoice("scissor")).grid(row=5,column=3)

root.mainloop()