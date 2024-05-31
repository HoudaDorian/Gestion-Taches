from tkinter import *
from tkinter import messagebox
import csv
import pandas as p

data = p.read_csv("compte.csv")
print(data)


def create_case(name):
    fichier_sauvegarde2 = open(name+'.csv', 'a')
    for i in range(40):
        data_case = ['*', '*', '*', '*', '*', '*', '*']
        write = csv.writer(fichier_sauvegarde2)
        write.writerow(data_case)

def create_bd_user(name):
    titre = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    fichier_sauvegarde = open(name+'.csv', 'w')
    write = csv.writer(fichier_sauvegarde)
    write.writerow(titre)
    create_case(name)

def verif_csv(entry1, entry2):
    global data
    var1 =0
    var2 =0
    for a in data["NOM"]:
        if a==entry1.get():
            return 0
    if entry1.get()=="" and entry2.get()=="":
        return 0
    else:
        for i in entry1.get():
            if i!=" ":
                var1 =1
        for j in entry2.get():
            if j!=" ":
                var2 =1
        if var1==1 and var2==1:
            create_bd_user(entry1.get())
            return 1
        else:
            return 0

def login():

    global entry_nom 
    global entry_mdp

    def mettre_csv():
        if verif_csv(entry_nom, entry_mdp)==1:
            data = [entry_nom.get(), entry_mdp.get()]
            fichier = open('compte.csv', 'a')
            write = csv.writer(fichier)
            write.writerow(data)
            messagebox.showinfo("VALIDE", "Les informations sont correctement enregistrées")
            fenetre.destroy() 
        else:
            messagebox.showerror("ERREUR", "Les informations entrées sont invalides")




    fenetre =Tk()
    width = fenetre.winfo_screenwidth()
    height = fenetre.winfo_screenheight()
    width = width/2 - 150
    height = height/2 - 200
    fenetre.geometry("300x400+%d+%d" % (width, height))
    fenetre.title("INSCRIPTION")
    fenetre.iconbitmap("icone.ico")

    text_inscrire = Label(fenetre, text="S'inscrire", font=("Impact", 25), pady = 0)
    text_nom = Label(fenetre, text="Nom d'utilisateur / pseudo", font=("Arial", 15))
    text_mdp = Label(fenetre, text="Mot de passe", font=("Arial", 15))
    entry_nom = Entry(fenetre, font=("Arial", 10))
    entry_mdp = Entry(fenetre, font=("Arial", 10))
    Btn_valider = Button(fenetre, text="VALIDER", font=("Arial", 10), command = mettre_csv)
    
    text_inscrire.pack()
    text_nom.pack()
    entry_nom.pack()
    text_mdp.pack()
    entry_mdp.pack()
    Btn_valider.pack()
    fenetre.mainloop()

