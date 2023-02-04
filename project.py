from tkinter import *
import customtkinter
from PIL import Image
from mainPage import mainPage
import re

def main():
    sign_in()

def sign_in():
    sign_in_page = customtkinter.CTk()
    sign_in_page.geometry("400x450")
    sign_in_page.title("Odio-tek")
    
    logo = customtkinter.CTkImage(dark_image=Image.open("pictures/logo.png"),size=(350,200))
    logo_label = customtkinter.CTkLabel(sign_in_page,image=logo,text="")
    logo_label.pack(pady=15)

    username_frame = customtkinter.CTkFrame(sign_in_page,border_width=1,border_color="black")
    username_frame.pack(padx=20,fill=BOTH)
    username_label = customtkinter.CTkLabel(username_frame,text="Kullanıcı Adı:",font=("Helvetica",13))
    username_label.pack(padx=(10,5),pady=5,side=LEFT)
    username_entry = customtkinter.CTkEntry(username_frame)
    username_entry.pack(padx=(5,5),pady=5,fill="both",expand=True)

    password_frame = customtkinter.CTkFrame(sign_in_page,border_width=1,border_color="black")
    password_frame.pack(padx=20,pady=10,fill=BOTH)
    password_label = customtkinter.CTkLabel(password_frame,text="Parola:",font=("Helvetica",13))
    password_label.pack(padx=(30,5),pady=5,side=LEFT)
    password_entry = customtkinter.CTkEntry(password_frame)
    password_entry.pack(padx=(22,5),pady=5,fill="both",expand=True)

    sign_in_button = customtkinter.CTkButton(sign_in_page,text="Giriş Yap",command= lambda: check_username_password(username_entry.get(),password_entry.get()))
    sign_in_button.pack(pady=10)

    sign_in_page.mainloop()

def check_username_password(username,password):

    check_username = re.search(r"^admin$",username)
    check_password = re.search(r"^12345$",password)

    if not(check_password):
        print(f"Parola hatalı, tekrar deneyiniz.")
        return False
    elif not(check_username):
        print(f"Kullanıcı Adı hatalı, tekrar deneyiniz.")
        return False
    else:
        print("Hoşgeldiniz.")
        window = mainPage()
        window.mainloop()
        return True




if __name__ == "__main__":
   main()
