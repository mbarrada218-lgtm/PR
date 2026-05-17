
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
              
