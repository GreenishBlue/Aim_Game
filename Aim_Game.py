import turtle 
import tkinter 

def menuScreen():
    window = tkinter.Tk()
    window.title("Aim Game")
    window.geometry ("800x800")
    window.configure(bg="teal")
    
    title = tkinter.Label(window, text="AIM GAME", font="Impact 60", bg="Teal", fg="brown")
    title.pack()

    playButton = tkinter.Button(window, text="PLAY!", width="100", font="20", bg="teal", fg="white", command=mainGame)
    playButton.pack()

    settingsButton = tkinter.Button(window, text="Settings", width="100", font="20", bg="teal", fg="white")
    settingsButton.pack()

    exitButton = tkinter.Button(window, text="Exit Game", width="100", font="20", bg="teal", fg="white", command=window.destroy)
    exitButton.pack()


    window.mainloop()

def mainGame() :

    wn = turtle.Screen()
    wn.title ("Aim Game")
    wn.bgcolor ("grey")
    wn.setup (width=800, height= 800)


    wn.mainloop()


menuScreen()