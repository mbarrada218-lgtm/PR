from tkinter import *
from tkinter import ttk
import pandas as pd 
from tkinter import messagebox

color = "#FAFDFA"

def Client (root , clear , open_dashboard ) :
    clear()
    root.title("GESTION DES CLIENTS")
    root.config(bg=color)

    #======================= Information des clients ==============================
    titre_client = Label(root , text="INFORMATION DES CLIENTS " ,  bg=color , width=30 , font=("Bookman old style", 20, "bold"))
    titre_client.grid( pady= 30 , padx=350)

    frame_client = Frame(root , bg=color , relief="ridge")
    frame_client.place(x = 200 , y=100)

    Nom_cl = Label(frame_client , text=" 👥 NOM :" , font= ("Segoe UI", 13, "bold") , bg = color , )
    Nom_cl.grid(row=0 , column=0 , pady=10 )

    Nom_ent = Entry(frame_client , font=("Bookman old style", 12) , width=35)
    Nom_ent.grid(row=0 , column=3 , padx=200 , pady=10)

    Tell_cl = Label(frame_client , text=" 📞 TELEPHONE :" , font= ("Segoe UI", 13, "bold") , bg = color , )
    Tell_cl.grid(row=1 , column=0 , pady=10)

    Tell_cl = Entry(frame_client , font=("Bookman old style", 12) , width=35)
    Tell_cl.grid(row=1 , column=3 , padx=10 , pady=10)

    Adres_cl = Label(frame_client , text=" 📍 ADRESSE :" , font= ("Segoe UI", 13, "bold") , bg = color , )
    Adres_cl.grid(row=2 , column=0 , pady=10 )

    Adres_cl = Entry(frame_client , font=("Bookman old style", 12) , width=35)
    Adres_cl.grid(row=2 , column=3 , pady=10)

    # ================== CREE BUTTONS ==========================
    
    Buttons = Frame(root , bg=color)
    Buttons.place(x=200 , y=260)

    ajout = Button(Buttons, text=" ✚ Ajouter ", width=15 , font=("Segoe UI", 12, "bold") 
                             , height=1 , bg="#459C3B" , fg="#FCFCFC" )
    ajout.grid(row=0 , column=1 , pady=10, padx=20)
    
    modif = Button(Buttons, text="✏️Modifier ", width=15 , font=("Segoe UI", 12, "bold")
                              , height=1 , bg="#5852F5" , fg="#FCFCFC" )
    modif.grid(row=0 , column=2 , pady=10 , padx=20)

    suprimer = Button(Buttons, text="🗑️ Suprimer ", width=15 , font=("Segoe UI", 12, "bold")
                              , height=1 , bg="#CE5B5B" , fg="#FCFCFC" )
    suprimer.grid(row=0 , column=3 , pady=10 , padx=20)

    enregistre = Button(Buttons, text="✔️ Enregistre ", 
                                width=15 , font=("Segoe UI", 12, "bold") , height=1 , 
                                bg="#C4F0E7"  , fg="#016954" )
    enregistre.grid(row=0 , column=4 , pady=10 , padx=20)

    retour = Button(root, text="⬅ Retour ", width=10 , font=("Segoe UI", 12, "bold") , height=1 , bg="#BEBFC1" , fg="#000000" , command= open_dashboard)
    retour.place(x =50 , y = 600)

    info = Label(root, text="LISTE DES CLIENTS :" , 
                 font=("Bookman old style", 12, "bold") , fg="#016954" , bg=color)
    info.place(x= 200 , y=335)

    # ======================= TABLEAU DES INFORMATION =====================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",
                        font=("Segoe UI", 12, "bold"),
                        background="#DAE8D9")
        
        

    style.configure("Treeview",
                        font=("Bookman old style", 12),
                        background="#F7F7EC" )
        


    tableau = ttk.Treeview(root, columns=(1,2,3,4),
                            height=10, show="headings", style="Treeview" )
        
    sc = ttk.Scrollbar(root, orient="vertical" , command=tableau.yview)
    sc.place(x=1030, y=370 , height=235)
    tableau.config(yscrollcommand=sc.set)

    tableau.heading(1, text="✅ ID ")
    tableau.heading(2, text="👥 NOM")
    tableau.heading(3, text="📞 TELEPHONE")
    tableau.heading(4, text="📍 ADRESSE")

    tableau.column(1, width=100)
    tableau.column(2, width=245)
    tableau.column(3, width=245)
    tableau.column(4, width=245)

    tableau.place(x=190, y=370)


