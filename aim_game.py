import turtle 
import tkinter 

def menu_screen():
  window = tkinter.Tk()
  window.title("Aim Game")
  window.geometry ("800x800")
  window.configure(bg="teal")
    
  tkinter.Label(window, text="AIM GAME", font="Impact 60", bg="Teal", 
                fg="brown").pack()
  tkinter.Button(window, text="PLAY!", width="100", font="20", bg="teal", 
                 fg="white", command=mainGame).pack()
  tkinter.Button(window, text="Settings", width="100", font="20", 
                 bg="teal", fg="white").pack()
  tkinter.Button(window, text="Exit Game", width="100", font="20", 
                 bg="teal", fg="white", command=window.destroy).pack()
  window.mainloop()

def main_game():
    wn = turtle.Screen()
    wn.title ("Aim Game")
    wn.bgcolor ("grey")
    wn.setup (width=800, height= 800)
    wn.mainloop()

menu_screen()
