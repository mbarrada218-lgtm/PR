
        def ajouter ():
            Nom_entre.delete(0 , END )
            Adresse_entre.delete(0 , END)
            Telephone_entre.delete(0, END)
            Email_entre.delete(0 , END)

        def enregistrer():
    # 1. نجلب البيانات ونمسح الفراغات الزائدة
            N_ent = Nom_entre.get().strip()
            A_ent = Adresse_entre.get().strip()
            T_ent = Telephone_entre.get().strip()
            E_ent = Email_entre.get().strip()
            # تأكد أن الخانات ليست فارغة (اختياري ولكن مهم)
            if not N_ent:
                messagebox.showwarning("تنبيه", "يرجى إدخال الاسم على الأقل!")
                return

            try:
                # 2. نحاول قراءة الملف إذا كان موجوداً
                try:
                    df = pd.read_excel("g_f.xlsx")
                except FileNotFoundError:
                    # إذا لم يوجد الملف، ننشئ DataFrame فارغ بنفس الأعمدة
                    df = pd.DataFrame(columns=["NOM", "ADRESSE", "TELEPHONE", "EMAIL"])

                # 3. نجهز السطر الجديد (خلينا التليفون نص باش يبقى الصفر لي فاللول)
                new_row = pd.DataFrame({
                    "NOM": [N_ent],
                    "ADRESSE": [A_ent],
                    "TELEPHONE": [T_ent], 
                    "EMAIL": [E_ent]
                })

                # 4. ندمج السطر الجديد مع البيانات القديمة
                df = pd.concat([df, new_row], ignore_index=True)

                # 5. نحفظ الكل في ملف Excel
                df.to_excel("g_f.xlsx", index=False)
                
                messagebox.showinfo("نجاح", "تم تسجيل البيانات في ملف Excel بنجاح!")
                # كيعمر الجدول بمجرد ما تفتح الصفحة
                charger_donnees()
                ajouter ()# نخويو الخانات مورا ما نسجلو

            except Exception as e:
                messagebox.showerror("خطأ", f"وقع مشكل أثناء الحفظ: {e}")


        def charger_donnees():
            # 1. كنخويو الجدول من أي معلومات قديمة
            for row in tableau.get_children():
                tableau.delete(row)
            
            try:
                # 2. كنقرأو الملف
                df = pd.read_excel("g_f.xlsx")
                # 3. كنحطو كل سطر من Excel في الجدول
                for index, row in df.iterrows():
                    tableau.insert("", "end", values=(row["NOM"], row["ADRESSE"], row["TELEPHONE"], row["EMAIL"]))
            except FileNotFoundError:
                # يلا مكانش الملف، ما يدير والو
                pass

        def supprimer () :
            selection = tableau.selection()
            if not selection:
                messagebox.showwarning("Attention", "Veuillez sélectionner une ligne à supprimer")
                return

            item = selection[0]
            tableau.delete(item)

            # Vider les champs
            ajouter()


            if index is not None:
                data["conges"] = self.personnes[index]["conges"]
                self.personnes[index] = data
            else:
                self.personnes.append(data)
