from tkinter import *
import pyttsx3
w =Tk()
w.title("Text to Speech")
w.geometry("800x500")
w.config(bg="white")
def talk():
 e=pyttsx3.init()
 e.say(entry.get())
 e.runAndWait()
 entry.delete(0,END)

entry=Entry(w,font=("Times New Roman", 28), bg="red")
entry.pack(pady=20, padx=20 )

button=Button(w, text="Speak", command=talk)
button.pack()
w.mainloop()