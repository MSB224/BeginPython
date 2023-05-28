from tkinter import*
from gtts import gTTS

import os

root = Tk()

root.geometry('750x450')
root.title('Convertiseur de texte en vocale')

Frame1 =Frame(root,bg='#7b68ee',
              height='200')
Frame1.pack(fill=X)

label = Label(Frame1,
              text='CONVERTISSEZ VOS TEXTE EN AUDIO(VOCAL)',
              font='Calibri 20',
              bg='cyan')
label.place(x=190,y=70)

frame2 = Frame(root,bg='cyan',height='700')
frame2.pack(fill=X)

entry = Entry(frame2,width=60,
              bd=10,font=20)
entry.place(x=120, y=52)
entry.insert(0, "")

def  play():
    language = 'en'

    myobj = gTTS(text=entry.get(),
                lang= language,
                slow=False)
    myobj.save("convert.mp3")
    os.system("convert.mp3")

# les boutons

btnl = Button(frame2,text="LIRE",width="15",pady=10,
              font='Calibri 15',bg='#00ff00',command=play)
btnl.place(x=250, y=130)

Button(frame2,text="FERMER",
       width="15",pady=10,
       font='Calibri 15',
       bg="#00ff00",
       command=lambda:root.destroy()).place(x=450, y=1)

root.mainloop()
