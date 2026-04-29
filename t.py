from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk

root = Tk()
root.title("PROJET S1-DEV - MIAGE")
root.geometry("1200x1090")
color = "#FAFDFA"
root.config(bg=color)

Nom_User = "a"
Num_password = "1"

# =================== TITRE ===================
lbl_titre_1 = Label(root, text="GESTION D'UNE PHARMACIE",
                    font=("Bookman old style", 22, "bold"),
                    height=6, fg="#014B01", bg=color)

lbl_titre_2 = Label(root, text=" ╰┈➤ BIENVENU SUR VOTRE APPLICATION",
                    font=("Bookman old style", 10, "bold"),
                    height=3, fg="#014B01", bg=color)

lbl_titre_1.pack()
lbl_titre_2.pack()

# =================== LOGIN FUNCTION ===================
def login():
    inpt_user = user.get()
    inpt_password = password.get()

    if Nom_User == inpt_user and Num_password == inpt_password:
        root.withdraw()
        open_dashboard()
    elif inpt_user == "" or inpt_password == "":
        messagebox.showwarning("Attention", "Remplir les champs")
    else:
        messagebox.showerror("Attention", "Entrée échouée")

# =================== LOGIN UI ===================
fram = Frame(root, bg=color)
fram.pack(pady=30)   

lbl_user = Label(fram, text="USER NAME",font=("Bookman old style", 10, "bold"),pady=20, bg=color, fg="#014B01")

user = Entry(fram, font=("Bookman old style", 10), width=30)

lbl_user.grid(row=0, column=0)
user.grid(row=0, column=1)

lbl_password = Label(fram, text="PASSWORD",
                     font=("Bookman old style", 10, "bold"),
                     pady=20, bg=color, fg="#014B01")

password = Entry(fram, font=("Bookman old style", 10),
                 width=30, show="*")

lbl_password.grid(row=1, column=0)
password.grid(row=1, column=1)

btn_login = Button(fram, text="LOGIN ✅",
                   font=("Bookman old style", 10),
                   width=10, bg="#149606",
                   command=lambda: login())

btn_exit = Button(fram, text="EXIT ➜]",
                  font=("Bookman old style", 10),
                  width=10, bg="#980707",
                  command=exit)

btn_login.grid(row=2, column=1)
btn_exit.grid(row=2, column=2)

# =================== DASHBOARD ===================
def open_dashboard():
    new_face = Toplevel(root)
    new_face.title("TABLEAU DE GESTION DU STOCK PHARM")
    new_face.geometry("1200x1090")
    new_face.config(bg=color)

    lbl_dash = Label(new_face,text=" ✚ GESTION DE STOCK PHARMACIE",
                     font=("Bookman old style", 20, "bold") , fg="#014B01" , bg=color)
    lbl_dash.pack(pady=50)   

    F1 = Frame(new_face , bg=color )
    F1.place(x=100 , y=100 , width=180 , height=500 )

    btn1 = Button(F1, text=" 💊 Produits", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#A5D2F5" , fg="#0C04FE")
    btn1.grid(row=0 , column=0 , pady=10)

    btn2 = Button(F1, text="🛒 Vente", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#D3F4D3" , fg="#014B01" )
    btn2.grid(row=1 , column=0 , pady=10)

    btn3 = Button(F1, text="🚚 Fournisseurs", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#B5A3D3" , fg="#3E039C" )
    btn3.grid(row=2 , column=0 , pady=10)

    btn4 = Button(F1, text="👥 Clients", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#E7D7B8"  , fg="#8F4903" )
    btn4.grid(row=3 , column=0 , pady=10)

    btn5 = Button(F1, text=" 📦 Stock", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#C4F0E7"  , fg="#016954")
    btn5.grid(row=4 , column=0 , pady=10)

    btn6 = Button(F1, text="📈 Rapports", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#F19494"  , fg="#7D1111")
    btn6.grid(row=5 , column=0 , pady=10)

    btn7 = Button(F1, text="🔒 Déconnexion",width=20, font=("Segoe UI", 10, "bold") , height=2 ,
                  bg="#9C9A9A"  , fg="#373636" ,command=new_face.destroy)
    btn7.grid(row=6 , column=0 , pady=10)


    #==============================FRAME PHOTO===========================
    F2 = Frame(new_face  , bd=5 , relief="ridge",)
    F2.place(x=600 , y=115 , width=350 , height=350 )
    F2.pack_propagate(False)
    original_img = Image.open("img1.png")
    resize_original = original_img.resize((350 , 350))
    img_final = ImageTk.PhotoImage(resize_original)
    img_labal = Label(F2 , image=img_final)
    img_labal.image = img_final
    img_labal.pack(expand=True)




    



root.mainloop()