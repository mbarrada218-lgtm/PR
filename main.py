from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk
import datetime 

root = Tk()
root.title("PROJET S1-DEV - MIAGE")
root.geometry("1200x1090")
color = "#FAFDFA"
root.config(bg=color)
icon = PhotoImage(file='pha.png')
root.iconphoto(True, icon)

Nom_User = ""
Num_password = ""

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
        #root.withdraw()
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

# =================== afficher new face ===================
def clear():
        for w in root.winfo_children():
            w.destroy()

# =================== afficher new face ===================
def open_dashboard():
    from fournisseur import Fournisseur
    from client import Client
    clear()
    root.title("TABLEAU DE GESTION DU STOCK PHARM")
    root.geometry("1200x1090")
    root.config(bg=color)

    lbl_dash = Label(root,text=" ✚ GESTION DE STOCK PHARMACIE",
                     font=("Bookman old style", 20, "bold") , fg="#014B01" , bg=color)
    lbl_dash.pack(pady=50)   

    F1 = Frame(root , bg=color )
    F1.place(x=100 , y=100 , width=180 , height=500 )

    Button(F1, text=" 💊 Produits", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#A5D2F5" , fg="#0C04FE").grid(row=0 , column=0 , pady=10)   
    
    Button(F1, text="🛒 Vente", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#D3F4D3" , fg="#014B01" ).grid(row=1 , column=0 , pady=10) 
    
    Button(F1, text="🚚 Fournisseurs", width=20 , font=("Segoe UI", 10, "bold") ,
                   height=2 , bg="#B5A3D3" , fg="#3E039C" , command=lambda:Fournisseur(root , clear , open_dashboard)).grid(row=2 , column=0 , pady=10)
    
    Button(F1, text="👥 Clients", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#E7D7B8"  , 
           fg="#8F4903" , command=lambda:Client(root , clear , open_dashboard) ).grid(row=3 , column=0 , pady=10)
    
    Button(F1, text=" 📦 Stock", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#C4F0E7"  , fg="#016954").grid(row=4 , column=0 , pady=10)
    
    Button(F1, text="📈 Rapports", width=20 , font=("Segoe UI", 10, "bold") , height=2 , bg="#F19494"  , fg="#7D1111").grid(row=5 , column=0 , pady=10)
    
    Button(F1, text="🔒 Déconnexion",width=20, font=("Segoe UI", 10, "bold") , height=2 ,
                  bg="#9C9A9A"  , fg="#373636" ,command=exit).grid(row=6 , column=0 , pady=10)

    def update_clock():
    # كياخد الوقت الحالي
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
    # كيبدل النص في الـ Label الخاص بالساعة
        lbl_time.config(text=f"🕒 Heure : {current_time}")
    # كيعاود يخدم راسو كل ثانية (1000ms)
        lbl_time.after(1000, update_clock)

# --- الفريم f3 ---
    f3 = Frame(root, bg=color)
    f3.place(x=650, y=480)


    lbl_welcome =Label(f3, text=" BIENVENU DANS LE SYSTÈME \n DE GESTION DE VOTRE PHARMACIE ",
                       font=("Bookman old style", 9, "bold"), 
                       bg=color, fg="#014B01")
    lbl_welcome.grid()


    date_now = datetime.date.today().strftime("%d/%m/%Y")
    lbl_date = Label(f3, text=f"📅 Date : {date_now}",
                    font=("Bookman old style", 8, "bold"),
                    bg=color)
    lbl_date.grid(row=3, column=0,)

    lbl_time = Label(f3, text="",
                    font=("Bookman old style", 8, "bold"),
                    bg=color)
    lbl_time.grid(row=4, column=0,)

    update_clock()



    #==============================FRAME PHOTO===========================
    F2 = Frame(root  , bd=5 , relief="ridge",)
    F2.place(x=600 , y=115 , width=350 , height=350 )
    F2.pack_propagate(False)
    original_img = Image.open("img1.png")
    resize_original = original_img.resize((350 , 350))
    img_final = ImageTk.PhotoImage(resize_original)
    img_labal = Label(F2 , image=img_final)
    img_labal.image = img_final
    img_labal.pack(expand=True)
    



#============================== FOURNISSEUR =============================

    
    



root.mainloop()