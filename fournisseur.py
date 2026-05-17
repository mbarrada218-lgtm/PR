from tkinter import *
from tkinter import ttk
import pandas as pd 
import openpyxl 
from tkinter import messagebox

color = "#FAFDFA"


def Fournisseur (root , clear , open_dashboard):
        clear()
        root.title("GESTION DES FOURNISSEURS")
        root.config(bg=color)
        
        #=============== LABEL TITRE INFORMATION FOURNISSEUR =============================
        info = Label(root , text=" 📝 INFORMATION FOURNISSEUR" ,  bg=color , width=30 , font=("Bookman old style", 20, "bold"))
        info.grid( pady= 30 , padx=350)

        #=============== FRAME LES INFORMATIONS  =============================
        util_four = Frame(root , bg=color , relief="ridge")
        util_four.place(x = 80 , y=100)

        nom = Label (util_four, text=" 👥 Nom : " ,  font=("Segoe UI", 13, "bold")  , bg=color , width= 12 )
        nom.grid(row=1 , column=0 )

        Nom_entre = Entry(util_four ,font=("Bookman old style", 12), width=35 )
        Nom_entre.grid(row=1 , column=1 )

        adresse = Label (util_four, text="📍 Adresse : " ,  font=("Segoe UI", 13, "bold")  , bg= color , width= 12 )
        adresse.grid(row=2 , column=0 , pady=10 , padx=10 )

        Adresse_entre = Entry(util_four ,font=("Bookman old style", 12), width=35)
        Adresse_entre.grid(row=2 , column=1 , pady=10 , padx=10)

        telephone = Label (util_four, text=" 📞 Téléphone : " ,  font=("Segoe UI", 13, "bold")  , bg= color , width= 12 )
        telephone.grid(row=1 , column=3 , pady=10 , padx=10 )

        Telephone_entre = Entry(util_four ,font=("Bookman old style", 12), width=35)
        Telephone_entre.grid(row=1 , column=4 , pady=10 , padx=10)

        email = Label (util_four, text="📩 Email : " ,  font=("Segoe UI", 13, "bold")  , bg= color , width= 12 )
        email.grid(row=2 , column=3 , pady=10 , padx=10 )

        Email_entre = Entry(util_four ,font=("Bookman old style", 12), width=35)
        Email_entre.grid(row=2 , column=4 , pady=10 , padx=10)

        #=============== FRAME LES BUTTONS  =============================

        Buttons = Frame(root , bg=color)
        Buttons.place(x = 200 , y=210)

        retour = Button(root, text="⬅ Retour ", width=10 , font=("Segoe UI", 12, "bold") , height=1 , bg="#BEBFC1" , fg="#000000" , command= open_dashboard)
        retour.place(x =50 , y = 600)
        
        ajout = Button(Buttons, text=" ✚ Ajouter ", width=15 , font=("Segoe UI", 12, "bold") 
                             , height=1 , bg="#459C3B" , fg="#FCFCFC" , command=lambda:ajouter())
        ajout.grid(row=0 , column=1 , pady=10, padx=20)

        modif = Button(Buttons, text="✏️Modifier ", width=15 , font=("Segoe UI", 12, "bold")
                              , height=1 , bg="#5852F5" , fg="#FCFCFC" ,  command=lambda:modifier())
        modif.grid(row=0 , column=2 , pady=10 , padx=20)

        suprimer = Button(Buttons, text="🗑️ Suprimer ", width=15 , font=("Segoe UI", 12, "bold")
                              , height=1 , bg="#CE5B5B" , fg="#FCFCFC" , command=lambda:supprimer())
        suprimer.grid(row=0 , column=3 , pady=10 , padx=20)

        enregistre = Button(Buttons, text="✔️ Enregistre ", 
                                width=15 , font=("Segoe UI", 12, "bold") , height=1 , 
                                bg="#C4F0E7"  , fg="#016954" ,  command=lambda:enregistrer())
        enregistre.grid(row=0 , column=4 , pady=10 , padx=20)

        # =========================== TABLEAU DES DONNES ======================
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 12, "bold"),
                        background="#DAE8D9")

        style.configure("Treeview",
                        font=("Bookman old style", 12),
                        background="lightyellow")

        tableau = ttk.Treeview(root, columns=(1,2,3,4),
                            height=13, show="headings", style="Treeview")

        tableau.heading(1, text="👥 NOM")
        tableau.heading(2, text="📍 ADRESSE")
        tableau.heading(3, text="📞 TELEPHONE")
        tableau.heading(4, text="📩 EMAIL")

        tableau.column(1, width=245)
        tableau.column(2, width=245)
        tableau.column(3, width=245)
        tableau.column(4, width=245)

        tableau.place(x=120, y=280)

        # ================= CLEAR INPUTS =================
        selected_item = None
        def ajouter():

            nonlocal selected_item

            Nom_entre.delete(0, END)
            Adresse_entre.delete(0, END)
            Telephone_entre.delete(0, END)
            Email_entre.delete(0, END)

            selected_item = None
        # ================= LOAD DATA =================

        def charger_donnees():

            for row in tableau.get_children():
                tableau.delete(row)

            try:
                df = pd.read_excel("g_f.xlsx")

                for i, row in df.iterrows():

                    tableau.insert(
                        "",
                        "end",
                        values=(
                            row["NOM"],
                            row["ADRESSE"],
                            row["TELEPHONE"],
                            row["EMAIL"]
                        )
                    )

            except FileNotFoundError:
                pass


        # ================= SAVE / MODIFY =================

        def enregistrer():

            nonlocal selected_item

            N_ent = Nom_entre.get()
            A_ent = Adresse_entre.get()
            T_ent = Telephone_entre.get()
            E_ent = Email_entre.get()

            if not N_ent or not A_ent or not T_ent or not E_ent:
                messagebox.showwarning(
                    "Attention",
                    "Remplir tous les champs"
                )
                return

            # ===== MODIFY =====

            if selected_item:

                tableau.item(selected_item,values=(N_ent, A_ent, T_ent, E_ent))

            # ===== ADD =====

            else:

                tableau.insert("",END,values=(N_ent, A_ent, T_ent, E_ent))

            # ===== SAVE ALL TREEVIEW TO EXCEL =====

            data = []

            for row in tableau.get_children():

                values = tableau.item(row, "values")

                data.append({
                    "NOM": values[0],
                    "ADRESSE": values[1],
                    "TELEPHONE": values[2],
                    "EMAIL": values[3]
                })

            df = pd.DataFrame(data)

            df.to_excel("g_f.xlsx", index=False)

            # ===== RESET =====

            ajouter()


        # ================= MODIFY =================

        def modifier():

            nonlocal selected_item

            select = tableau.selection()

            if not select:
                messagebox.showwarning(
                    "Attention",
                    "Veuillez sélectionner une ligne"
                )
                return

            item = select[0]

            selected_item = item

            values = tableau.item(item, "values")

            Nom_entre.delete(0, END)
            Nom_entre.insert(0, values[0])

            Adresse_entre.delete(0, END)
            Adresse_entre.insert(0, values[1])

            Telephone_entre.delete(0, END)
            Telephone_entre.insert(0, values[2])

            Email_entre.delete(0, END)
            Email_entre.insert(0, values[3])


        # ================= DELETE =================

        def supprimer():

            selection = tableau.selection()

            if not selection:
                messagebox.showwarning(
                    "Attention",
                    "Veuillez sélectionner une ligne"
                )
                return

            item = selection[0]

            tableau.delete(item)

            # ===== SAVE AFTER DELETE =====

            data = []

            for row in tableau.get_children():

                values = tableau.item(row, "values")

                data.append({
                    "NOM": values[0],
                    "ADRESSE": values[1],
                    "TELEPHONE": values[2],
                    "EMAIL": values[3]
                })

            df = pd.DataFrame(data)

            df.to_excel("g_f.xlsx", index=False)

            ajouter()


        # ================= START =================

        charger_donnees()
              










