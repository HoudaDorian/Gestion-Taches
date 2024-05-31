from tkinter import *

import pandas as p

import inscription 

import agenda

"""
data = ["USERNAME", "PASSWORD", "KEY"]
fichier = open('compte.csv', 'w')
write = csv.writer(fichier)
write.writerow(data)
"""
compte = p.read_csv("compte.csv", usecols=["NOM","PASSWORD"])

def execute_agenda():
    global E_nom
    agenda.fenetre_agenda(E_nom.get())
    fenetre.destroy()
    
def verif():
    compte = p.read_csv("compte.csv", usecols=["NOM","PASSWORD"])
    global E_nom, E_password
    for i in range(len(compte.NOM)):
        if compte.NOM[i]==E_nom.get() and str(compte.PASSWORD[i])==E_password.get():
            print("ok verif")
            execute_agenda()
            return 1
    return 0

def validation():
    if verif()==1:
        print("True")
        TEXT_verif["fg"]="green"
        TEXT_verif["text"]="Vous êtes bien connecté"
    else:
        TEXT_verif["fg"]="red"
        TEXT_verif["text"]="mot de passe ou nom d'utilisateur incorrect"

fenetre = Tk()
width = fenetre.winfo_screenwidth()
height = fenetre.winfo_screenheight()
width = width/2 - 300
height = height/2 - 200
fenetre.geometry("600x400+%d+%d" % (width, height))
fenetre.title("HODOTASK")
fenetre.resizable(width=False, height=False)
fenetre.iconbitmap("icone.ico")



T_bienvenue = Label(fenetre, text="Bienvenue sur Hodotask", font=("Impact", 35))
T_bienvenue.pack()

frame_login = Frame(fenetre, pady=30)


T_login = Label(frame_login, text="Se connecter", font=("Impact", 25), pady=10)
T_login.pack()
T_nom = Label(frame_login, text="Nom d'utilisateur", font=("Arial", 15))
T_password = Label(frame_login, text="password", font=("Arial", 15))
E_nom = Entry(frame_login)
E_password = Entry(frame_login, show="*")
Btn_valide = Button(frame_login, text = "VALIDER", command=validation)
T_nom.pack()
E_nom.pack()
T_password.pack()
E_password.pack()
Btn_valide.pack()
frame_login.pack()

TEXT_verif = Label(fenetre, text="", font=("Arial", 15), fg="green")
TEXT_verif.pack()
Btn_cree_compte = Button(fenetre, text="Crée un compte", command=inscription.login)
Btn_cree_compte.pack(side="bottom")
fenetre.mainloop()