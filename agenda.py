from tkinter import *
import csv
import pandas as p
from tkinter import messagebox


tab_val=["", "", [0,0]]
            
def fenetre_agenda(nom_compte):
    tab=[[],[],[],[],[],[],[]]

    nom_compte = nom_compte+'.csv'
    print("connecté au compte :" , nom_compte)
    donnee = p.read_csv(nom_compte)

    #########################################FONCTION UTILE###########################################################################

    def placement_horaire(hor):
        for i in range(25):
            l = Label(gauche, text=f"{i}h" , font=("Arial", 8), height=1)
            hor.append(l)
            hor[i].grid(column = 0, row = i, ipady = 1)

    def couleur_donne(ind):
        if (donnee[ind[0]][ind[1]][-1]=="1"):
            return "white"
        elif (donnee[ind[0]][ind[1]][-1]=="2"):
            return "gray"
        elif (donnee[ind[0]][ind[1]][-1]=="3"):
            return "light sky blue"
        elif (donnee[ind[0]][ind[1]][-1]=="4"):
            return "light goldenrod"
        elif (donnee[ind[0]][ind[1]][-1]=="5"):
            return "spring green"
        elif (donnee[ind[0]][ind[1]][-1]=="6"):
            return "SlateBlue1"
        elif (donnee[ind[0]][ind[1]][-1]=="7"):
            return "MediumPurple1"
        elif (donnee[ind[0]][ind[1]][-1]=="8"):
            return "coral1"
        elif (donnee[ind[0]][ind[1]][-1]=="9"):
            return "IndianRed1"
        elif (donnee[ind[0]][ind[1]][-1]=="0"):
            return "azure2"
        else : 
            return "white"
        
    def text_donne(ind):
        t =""
        for i in range(0, len(str(donnee[ind[0]][ind[1]]))-1):
            t = t + str(donnee[ind[0]][ind[1]][i])
        return t
              

    def recup_donnee(tab):
        var = -1
        for i in donnee.columns:
            var = var + 1
            for j in range(1, 25):
                if donnee[i][j] != "*":
                    tab[var][j-1]["text"] = text_donne([i, j])
                    tab[var][j-1]["bg"] = couleur_donne([i, j])
                else :
                    tab[var][j-1]["text"] = ""
                    tab[var][j-1]["bg"] = "gray"
    
    def Label_placement(tab):
        for j in range(7):
            for i in range(24):
                a = Label(Box, text="", font=("Arial", 10), width= 20, height = 1)
                tab[j].append(a)
                tab[j][i].grid(column = j, row = i+1)
        recup_donnee(tab)

    def remplacement_donne(tab, val, nom_compte, ind):
        #donnee[ind[0]][ind[1]] = val
        donnee.loc[ind[1]+1, ind[0]] = val
        donnee.to_csv(nom_compte, index=False)
        recup_donnee(tab)
    
    def supprimer_tous():
        global tab_val
        msgbox = messagebox.askokcancel(title="HODOTASKS", message="Voulez-vous vraiment tous supprimer ?", icon="warning")
        if msgbox==True:
            for i in donnee.columns:
                for j in range(24):
                    remplacement_donne(tab, "*", nom_compte, [i, j])
            messagebox.showinfo(title="HODOTASKS", message="Données supprimées avec succès")
    
    def deco():
        fenetre.destroy()


    ###########################################FENETRE DE CHOIX ###########################################################################################################################
    def fenetre_ajouter():
        global tab_val
        def val_j1(): global tab_val; tab_val[0] = "Lundi"
        def val_j2(): global tab_val; tab_val[0] = "Mardi"
        def val_j3(): global tab_val; tab_val[0] = "Mercredi"
        def val_j4(): global tab_val; tab_val[0] = "Jeudi"
        def val_j5(): global tab_val; tab_val[0] = "Vendredi"
        def val_j6(): global tab_val; tab_val[0] = "Samedi"
        def val_j7(): global tab_val; tab_val[0] = "Dimanche"

        def val_c1(): global tab_val; tab_val[1] = "1"
        def val_c2(): global tab_val; tab_val[1] = "2"
        def val_c3(): global tab_val; tab_val[1] = "3"
        def val_c4(): global tab_val; tab_val[1] = "4"
        def val_c5(): global tab_val; tab_val[1] = "5"
        def val_c6(): global tab_val; tab_val[1] = "6"
        def val_c7(): global tab_val; tab_val[1] = "7"
        def val_c8(): global tab_val; tab_val[1] = "8"
        def val_c9(): global tab_val; tab_val[1] = "9"
        def val_c0(): global tab_val; tab_val[1] = "0"

        def val_h(): global tab_val; tab_val[2][0] = int(h_depart.get()) ; tab_val[2][1] = int(h_fin.get())

        def erreur_heure():
            messagebox.showerror("ERREUR", "Les informations entrées sont invalides")   

        def verif_heure():
            depart = int(h_depart.get())
            fin = int(h_fin.get())
            if depart >=0 and fin>=1 and depart<=23 and fin<=24:
                if depart<fin and type(depart)==int and type(fin)==int:
                    val_h()
                    return 1
                else:
                    erreur_heure()
                    return 0
            else:
                erreur_heure()
                return 0
            
        def boucle():
            global tab_val
            for i in range(tab_val[2][0], tab_val[2][1]):
                remplacement_donne(tab, (entry_text.get())+str(tab_val[1]), nom_compte, [tab_val[0], i])
        
        def entree_donnee_tab():
            global tab_val
            if verif_heure()==1:
                boucle()





        fenetre_ajt = Tk()
        fenetre_ajt.title("HODOTASKS - AJOUT DANS LE PLANNING")
        fenetre_ajt.geometry("300x400")
        fenetre_ajt.attributes('-alpha', 0.9) 

        Frame_jour = Frame(fenetre_ajt)
        Frame_jour.pack()

        Frame_temps = Frame(fenetre_ajt)
        Frame_temps.pack()

        Frame_couleur = Frame(fenetre_ajt)
        Frame_couleur.pack()

        Frame_text = Frame(fenetre_ajt)
        Frame_text.pack()

        Text_1 = Label(Frame_jour, text ="Choisi le jour", font=("Arial", 15 ), borderwidth=2, relief="groove",)
        Text_2 = Label(Frame_temps, text ="Choisi le temps", font=("Arial", 15 ), borderwidth=2, relief="groove",)
        Text_3 = Label(Frame_couleur, text ="Choisi la couleur", font=("Arial", 15 ), borderwidth=2, relief="groove",)
        Text_4 = Label(Frame_text, text ="Entre le texte", font=("Arial", 15 ), borderwidth=2, relief="groove",)

        btn_blanc = Button(Frame_couleur, bg="white", width=2, command = val_c1)
        btn_gris = Button(Frame_couleur, bg="gray", width=2, command =val_c2)
        btn_bleu = Button(Frame_couleur, bg="light sky blue", width=2, command =val_c3)
        btn_jaune = Button(Frame_couleur, bg="light goldenrod", width=2, command =val_c4)
        btn_vert = Button(Frame_couleur, bg="spring green", width=2, command =val_c5)
        btn_violet = Button(Frame_couleur, bg="SlateBlue1", width=2, command =val_c6)
        btn_violetpale = Button(Frame_couleur, bg="MediumPurple1", width=2, command =val_c7)
        btn_rouge = Button(Frame_couleur, bg="coral1", width=2, command =val_c8)
        btn_rose = Button(Frame_couleur, bg="IndianRed1", width=2, command =val_c9)
        btn_bleuc = Button(Frame_couleur, bg="azure2", width=2, command =val_c0)

        btn_lundi = Button(Frame_jour, text = "Lun", command=val_j1)
        btn_mardi = Button(Frame_jour, text = "Mar", command=val_j2)
        btn_mercredi = Button(Frame_jour, text = "Mer", command=val_j3)
        btn_jeudi = Button(Frame_jour, text = "Jeu", command=val_j4)
        btn_vendredi = Button(Frame_jour, text = "Ven", command=val_j5)
        btn_samedi = Button(Frame_jour, text = "Sam", command=val_j6)
        btn_dimanche = Button(Frame_jour, text = "Dim", command=val_j7)


        def p():
            global tab_val
            print(tab_val[0], tab_val[1], tab_val[2][0])

        Btn_val = Button(fenetre_ajt, text = "VALIDER", font=("Arial", 15 ), command=entree_donnee_tab) #entree_donnee_tab


        h_depart = Entry(Frame_temps, width=10)
        h_fin = Entry(Frame_temps, width=10)

        entry_text = Entry(Frame_text)

        Text_1.grid(column=1, row=0, columnspan=4)
        btn_lundi.grid(column=0, row=1)
        btn_mardi.grid(column=1, row=1)
        btn_mercredi.grid(column=2, row=1)
        btn_jeudi.grid(column=3, row=1)
        btn_vendredi.grid(column=4, row=1)
        btn_samedi.grid(column=5, row=1)
        btn_dimanche.grid(column=6, row=1)

        Text_2.grid(column=0, row=0, columnspan=1)
        h_depart.grid(column=0, row=1)
        h_fin.grid(column=1, row=1)

        Text_3.grid(column=1, row=0, columnspan=4)
        btn_blanc.grid(column=0, row=1)
        btn_gris.grid(column=1, row=1)
        btn_bleu.grid(column=2, row=1)
        btn_jaune.grid(column=3, row=1)
        btn_vert.grid(column=4, row=1)
        btn_violet.grid(column=0, row=2)
        btn_violetpale.grid(column=1, row=2)
        btn_rouge.grid(column=2, row=2)
        btn_rose.grid(column=3, row=2)
        btn_bleuc.grid(column=4, row=2)

        Text_4.pack()
        entry_text.pack()

        Btn_val.pack()

        fenetre_ajt.mainloop()
################################################FENETRE SUPPRIMER##########################################################################################
    def fenetre_supprimer():
        global tab_val
        def val_j1(): global tab_val; tab_val[0] = "Lundi"
        def val_j2(): global tab_val; tab_val[0] = "Mardi"
        def val_j3(): global tab_val; tab_val[0] = "Mercredi"
        def val_j4(): global tab_val; tab_val[0] = "Jeudi"
        def val_j5(): global tab_val; tab_val[0] = "Vendredi"
        def val_j6(): global tab_val; tab_val[0] = "Samedi"
        def val_j7(): global tab_val; tab_val[0] = "Dimanche"

        def val_h2(): global tab_val; tab_val[2][0] = int(heure_depart.get()) ; tab_val[2][1] = int(heure_fin.get())
    
        def erreur_heure():
            messagebox.showerror("ERREUR", "Les informations entrées sont invalides")   

        def verif_heure2():
            depart = int(heure_depart.get())
            fin = int(heure_fin.get())
            if depart >=0 and fin>=1 and depart<=23 and fin<=24:
                if depart<fin and type(depart)==int and type(fin)==int:
                    val_h2()
                    return 1
                else:
                    erreur_heure()
                    return 0
            else:
                erreur_heure()
                return 0
            
        def boucle2():
            global tab_val
            for i in range(tab_val[2][0], tab_val[2][1]):
                remplacement_donne(tab, "*", nom_compte, [tab_val[0], i])
        
        def entree_donnee_tab2():
            global tab_val
            if verif_heure2()==1:
                boucle2()

        fenetre_sup = Tk()
        fenetre_sup.attributes("-alpha", 0.9)
        fenetre_sup.title("HODOTASKS - SUPPRESSION DANS LE PLANNING")

        text_jour = Label(fenetre_sup, text="JOUR")
        text_temps = Label(fenetre_sup, text="TEMPS")

        B_lun = Button(fenetre_sup, text = "Lun", command=val_j1)
        B_mar = Button(fenetre_sup, text = "mar", command=val_j2)
        B_mer = Button(fenetre_sup, text = "mer", command=val_j3)
        B_jeu = Button(fenetre_sup, text = "jeu", command=val_j4)
        B_ven = Button(fenetre_sup, text = "ven", command=val_j5)
        B_sam = Button(fenetre_sup, text = "sam", command=val_j6)
        B_dim = Button(fenetre_sup, text = "dim", command=val_j7)

        heure_depart = Entry(fenetre_sup, width=5)
        heure_fin = Entry(fenetre_sup, width=5)

        B_valider = Button(fenetre_sup, text = "VALIDER", command=entree_donnee_tab2)

        text_jour.grid(column=3, row=0)
        B_lun.grid(column=0, row=1)
        B_mar.grid(column=1, row=1)
        B_mer.grid(column=2, row=1)
        B_jeu.grid(column=3, row=1)
        B_ven.grid(column=4, row=1)
        B_sam.grid(column=5, row=1)
        B_dim.grid(column=6, row=1)

        text_temps.grid(column=3, row=3)
        text_heure_depart = Label(fenetre_sup, text="départ :")
        text_heure_fin = Label(fenetre_sup, text="fin :")
        text_heure_depart.grid(column=2, row=4, columnspan=3)
        text_heure_fin.grid(column=2,row=5, columnspan=3)
        heure_depart.grid(column=4, row=4 )
        heure_fin.grid(column=4, row=5 )

        B_valider.grid(column=3, row=6, columnspan=4)

############################################################################################################################################################   
    fenetre = Tk()
    fenetre.title("HODOTASKS")


    width = fenetre.winfo_screenwidth()
    height = fenetre.winfo_screenheight()
    width = width/2 - 650
    height = height/2 - 400
    fenetre.geometry("1300x800+%d+%d" % (width, height))
    fenetre.resizable(width=False, height=False)
    

    Box = Frame(fenetre)
    Box.pack()

    gauche = Frame(fenetre)
    gauche.place(x=0, y=15)


    label_lun = Label(Box,text="Lundi   ", font=("Arial", 15 ), borderwidth=2, relief="groove", width=6)
    label_lun.grid(column=0, row=0, ipadx=50)
    label_mar = Label(Box,text="Mardi   ", font=("Arial", 15 ), borderwidth=2, relief="groove", width=6)
    label_mar.grid(column=1, row=0, ipadx=50)
    label_mer = Label(Box,text="Mercredi", font=("Arial", 15 ), borderwidth=2, relief="groove", width=6)
    label_mer.grid(column=2, row=0, ipadx=50)
    label_jeu = Label(Box,text="Jeudi   ", font=("Arial", 15 ), borderwidth=2, relief="groove", width=6)
    label_jeu.grid(column=3, row=0, ipadx=50)
    label_ven = Label(Box,text="Vendredi", font=("Arial", 15 ), borderwidth=2, relief="groove", width=6)
    label_ven.grid(column=4, row=0, ipadx=50)
    label_sam = Label(Box,text="Samedi  ", font=("Arial", 15 ), borderwidth=2, relief="groove", width=6)
    label_sam.grid(column=5, row=0, ipadx=50)
    label_dim = Label(Box,text="Dimanche", font=("Arial", 15 ), borderwidth=2, relief="groove", width=6)
    label_dim.grid(column=6, row=0, ipadx=50)

    Btn_ajouter = Button(fenetre, text="ajouter/modifier", font=("Arial", 15 ), command=fenetre_ajouter, bg="green")
    Btn_ajouter.place(x = 200, y = 700)

    Btn_supprimer = Button(fenetre, text="supprimer tous", font=("Arial", 15 ), command=supprimer_tous, bg = "red")
    Btn_supprimer.place(x = 600, y = 700)

    Btn_supp = Button(fenetre, text="supprimer", font=("Arial", 15 ), command=fenetre_supprimer, bg = "yellow")
    Btn_supp.place(x=400, y=700)

    Btn_deconnexion = Button(fenetre, text="Se déconnecter", font=("Arial", 15 ), command=deco, bg = "white")
    Btn_deconnexion.place(x=10, y=700)
    """
    label_horaire = Label(gauche, text = "00h")
    label_horaire.grid(column=0, row=0)
    """
    
    hor = []
    print(tab)
    Label_placement(tab)
    placement_horaire(hor)


    





    


    

