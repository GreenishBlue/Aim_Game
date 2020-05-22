import turtle #import turtle for main game
import tkinter #import tkinter for UI

def menuScreen():
    #create menu screen
    window = tkinter.Tk()
    window.title("Aim Game")
    window.geometry ("800x800")

    window.mainloop()

def mainGame() :
    #create main game screen
    wn = turtle.Screen()
    wn.title ("Aim Game")
    wn.bgcolor ("grey")
    wn.setup (width=800, height= 800)


    wn.mainloop()

#calls menu function
menuScreen()