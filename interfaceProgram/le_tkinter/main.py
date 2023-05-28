# les bibliotech
import tkinter

# definition de function

def update_label(*args):
    var_label.set(var_entry.get())
    
# creation et paramettrage de la fenetre
app = tkinter.Tk()
app.geometry("400x300")
app.title("First tkinter Menu")

# widgets

mainmenu = tkinter.Menu(app)

firstMenu = tkinter.Menu(mainmenu)
firstMenu.add_command(label="Gnie informatique")
firstMenu.add_command(label="Gnie mecanique")
firstMenu.add_command(label="Gnie orange")
firstMenu.add_command(label="Gnie Tomate")
# un sous menu

# end sous menu
secondMenu = tkinter.Menu(mainmenu)
secondMenu.add_command(label="Guinee")
secondMenu.add_command(label="senegale")
secondMenu.add_command(label="yaounde")
secondMenu.add_command(label="Mali")

mainmenu.add_cascade(label="Departement",menu=firstMenu)
mainmenu.add_cascade(label="CONTRY",menu=secondMenu)



# Boucle principale
app.config(menu=mainmenu)
app.mainloop()