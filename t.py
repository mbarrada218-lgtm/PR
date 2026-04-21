from tkinter import*


root = Tk()
root.title("PROJET S1-DEV - MIAGE")
root.geometry("1200x1090")

Nom_User = "admin"
Num_password = "1234"

#=================== TITRE DE PROJET =========================
lbl = Label(root, text="GESTION D'UNE PHARMACIE" , font=("Bookman old style", 20, "bold"), pady=20 )
lbl.pack(pady= 50 , padx=50)

#===================== VERIFICATION LOGINE ===================
def login():
    inpt_user = user.get()
    inpt_password = password.get()
    if Nom_User == inpt_user and Num_password == inpt_password:
        #hna khass iwarina kifash nhalo page akhra 
        #code hna mazal na9ass ghady i3ti error



#================== LOGINE ===================================
lbl_user = Label(root, text="USER" , font=("Bookman old style", 10 ), pady=20 )
lbl_user.pack()
user = Entry(root ,  font=("Bookman old style", 10 ) ,width=30  )
user.pack(pady=5 , padx=5)
lbl_password = Label(root, text="PASSWORD" , font=("Bookman old style", 10 ), pady=20 )
lbl_password.pack()
password = Entry(root , text="PASSWORD" , font=("Bookman old style", 10 ) , width=30 )
password.pack(pady=10 , padx=10)

btn_login = Button(root , text="LOGIN" , font=("Bookman old style",10), pady=10 , padx=20 , bg="red", command=lambda:login())
btn_login.pack(pady=20)







root.mainloop()