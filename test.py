from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("PROJET S1-DEV - MIAGE")
root.geometry("1200x1090")
color = "#414241"
root.config(bg=color)

Nom_User = "admin"
Num_password = "1234"

# =================== TITRE ===================
lbl_titre_1 = Label(root, text="GESTION D'UNE PHARMACIE",
                    font=("Bookman old style", 22, "bold"),
                    height=6, fg="white", bg=color)

lbl_titre_2 = Label(root, text=" ╰┈➤ BIENVENU SUR VOTRE APPLICATION",
                    font=("Bookman old style", 10, "bold"),
                    height=3, fg="white", bg=color)

lbl_titre_1.pack()
lbl_titre_2.pack()

# =================== LOGIN FUNCTION ===================
def login():
    inpt_user = user.get()
    inpt_password = password.get()

    if Nom_User == inpt_user and Num_password == inpt_password:
        open_dashboard()
    elif inpt_user == "" or inpt_password == "":
        messagebox.showwarning("Attention", "Remplir les champs")
    else:
        messagebox.showerror("Attention", "Entrée échouée")

# =================== LOGIN UI ===================
fram = Frame(root, bg=color)
fram.pack(pady=30)   # ✔️ بدلنا grid بـ pack

lbl_user = Label(fram, text="USER NAME",
                 font=("Bookman old style", 10, "bold"),
                 pady=20, bg=color, fg="white")

user = Entry(fram, font=("Bookman old style", 10), width=30)

lbl_user.grid(row=0, column=0)
user.grid(row=0, column=1)

lbl_password = Label(fram, text="PASSWORD",
                     font=("Bookman old style", 10, "bold"),
                     pady=20, bg=color, fg="white")

password = Entry(fram, font=("Bookman old style", 10),
                 width=30, show="*")

lbl_password.grid(row=1, column=0)
password.grid(row=1, column=1)

btn_login = Button(fram, text="LOGIN ✅",
                   font=("Bookman old style", 10),
                   width=10, bg="#0D6803",
                   command=lambda: login())

btn_exit = Button(fram, text="EXIT ➜]",
                  font=("Bookman old style", 10),
                  width=10, bg="#730303",
                  command=exit)

btn_login.grid(row=2, column=1)
btn_exit.grid(row=2, column=2)

# =================== DASHBOARD ===================
def open_dashboard():
    new_face = Toplevel(root)
    new_face.title("TABLEAU DE GESTION DU STOCK PHARM")
    new_face.geometry("800x600")

    lbl_dash = Label(new_face,
                     text="bienvenue dans la partie de gestion",
                     font=("Arial Black", 18, "bold"))
    lbl_dash.pack(pady=50)   # ✔️ بدلنا grid بـ pack

    btn1 = Button(new_face, text="Ajouter produit!", width=20)
    btn1.pack(pady=10)

    btn2 = Button(new_face, text="Afficher produit!", width=20)
    btn2.pack(pady=10)

    btn3 = Button(new_face, text="Quitter",
                  width=20, command=new_face.destroy)
    btn3.pack(pady=10)

root.mainloop()



    F1 = Frame(new_face , bg="white")
    F1.place(x=500 , y=250 , width=200 , height=200)

    btn1 = Button(F1, text="Ajouter produit!", width=20 , font=("Bookman old style", 10, "bold")  )
    btn1.pack(pady=10)

    btn2 = Button(F1, text="Afficher produit!", width=20 , font=("Bookman old style", 10, "bold") )
    btn2.pack(pady=10)

    btn3 = Button(F1, text="Quitter",
                  width=20, font=("Bookman old style", 10, "bold") , command=new_face.destroy)
    btn3.pack(pady=10)
