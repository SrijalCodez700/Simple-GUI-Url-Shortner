#Imports
from tkinter import *
import pyshorteners

#Functions
def getShortUrl(long_Url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_Url)

def short():
    longUrl = Entry1.get()
    shortUrl = getShortUrl(longUrl)
    Label2.configure(text=f"Your short url is: {shortUrl}")

#Define the main screen
screen = Tk()

#Customizing the screen
screen.title("Url Shortner")
screen.geometry("800x500")
screen.configure(bg="blue", border="50")

#GUI Stuff

Label1 = Label(screen, text="Please enter your url below.", background="lightblue", font=("Times New Roman", 18))
Label1.place(x=20, y=20)

Entry1 = Entry(screen, background="lightblue", font=("Times New Roman", 18))
Entry1.place(x=20, y=60)

Button1 = Button(screen, text="Ok", background="lightblue", font=("Times New Roman", 18), command=short)
Button1.place(x=20,y=100)

Label2 = Label(screen, text="Your short url will appear here as soon as you create one!", background="lightblue", font=("Times New Roman", 18))
Label2.place(x=20,y=160)

#Start the Screen mainloop
screen.mainloop()