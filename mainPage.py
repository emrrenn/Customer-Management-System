from tkinter import *
import customtkinter
from datetime import date
from tkinter import ttk
import sqlite3
import pyscreenshot
from PIL import Image


class mainPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1150x600")
        self.title("Odio-tek")

# ------------------------- Main Page title -------------------------
        # self.odio_tek = customtkinter.CTkLabel(self,text="Odio-Tek",font=("Helvetica",25,"bold"))
        # self.odio_tek.pack(pady=20)

# ------------------------- Treeview -------------------------
        self.style = ttk.Style()

        self.style.map("Treeview",background=[('selected', "#347083")])

        tree_frame = customtkinter.CTkFrame(self)
        tree_frame.pack(padx=10,pady=(20,10),fill=BOTH)

        tree_scroll = customtkinter.CTkScrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT,fill=Y)

        self.my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
        self.my_tree.pack(side="top",fill=BOTH,expand=True)

        tree_scroll.configure(command=self.my_tree.yview)

        self.my_tree["columns"] = ("ID", "First Name", "Last Name", "Birthday", "Phone", "Mail", "Job", "Record Date")

        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("ID",anchor="center",width=100)
        self.my_tree.column("First Name",anchor="center",width=140)
        self.my_tree.column("Last Name",anchor="center",width=140)
        self.my_tree.column("Birthday",anchor="center",width=140)
        self.my_tree.column("Phone",anchor="center",width=140)
        self.my_tree.column("Mail",anchor="center",width=140)
        self.my_tree.column("Job",anchor="center",width=140)
        self.my_tree.column("Record Date",anchor="center",width=140)

        self.my_tree.heading("#0",text="",anchor="w")
        self.my_tree.heading("ID",text="ID",anchor="center")
        self.my_tree.heading("First Name",text="İsim",anchor="center")
        self.my_tree.heading("Last Name",text="Soyisim",anchor="center")
        self.my_tree.heading("Birthday",text="Doğum Tarihi",anchor="center")
        self.my_tree.heading("Phone",text="Telefon",anchor="center")
        self.my_tree.heading("Mail",text="E-Mail",anchor="center")
        self.my_tree.heading("Job",text="Meslek",anchor="center")
        self.my_tree.heading("Record Date",text="Kayıt Tarihi",anchor="center")

        # Call function when row clicked
        self.my_tree.bind('<ButtonRelease-1>', self.get_treeview_data)

        # Get the data for treeview
        self.update_treeview()

# ------------------------- Customer Information Frame -------------------------
        self.info_frame = customtkinter.CTkFrame(self,border_width=1,border_color="black",corner_radius=10)
        self.info_frame.pack(padx=10,pady=(10,20),side=LEFT,fill="both")

        self.info_label = customtkinter.CTkLabel(self.info_frame,text="Hasta Bilgileri",font=("Helvetica",17,"bold","underline"))
        self.info_label.pack(padx=20,pady=10)

# ------------------------- ID / NAME / SURNAME -------------------------
        self.customer_info_frame = customtkinter.CTkFrame(self.info_frame,border_width=1,border_color="black")
        self.customer_info_frame.pack(padx=10,fill=BOTH)

        self.customer_id_label = customtkinter.CTkLabel(self.customer_info_frame,text="ID:",font=("Helvetica",13,"bold"))
        self.customer_id_label.pack(side=LEFT,padx=(50,0),pady=4)
        self.customer_id_entry = customtkinter.CTkEntry(self.customer_info_frame)
        self.customer_id_entry.pack(side=LEFT,padx=(40,10),pady=4)

        self.customer_name_label = customtkinter.CTkLabel(self.customer_info_frame,text="İsim:",font=("Helvetica",13,"bold"))
        self.customer_name_label.pack(side=LEFT,padx=10,pady=4)
        self.customer_name_entry = customtkinter.CTkEntry(self.customer_info_frame)
        self.customer_name_entry.pack(side=LEFT,padx=(0,20),pady=4)

        self.customer_surname_label = customtkinter.CTkLabel(self.customer_info_frame,text="Soyisim:",font=("Helvetica",13,"bold"))
        self.customer_surname_label.pack(side=LEFT,padx=10,pady=4)
        self.customer_surname_entry = customtkinter.CTkEntry(self.customer_info_frame)
        self.customer_surname_entry.pack(side=LEFT,padx=(0,10),pady=4)

# ------------------------- Hearing Aid Information -------------------------
        self.info_label = customtkinter.CTkLabel(self.info_frame,text="Cihaz Bilgileri",font=("Helvetica",17,"bold","underline"))
        self.info_label.pack(padx=20,pady=10)

        self.hearing_aid_info_frame = customtkinter.CTkFrame(self.info_frame,border_width=1,border_color="black")
        self.hearing_aid_info_frame.pack(padx=10,fill=BOTH)

        self.hearing_aid_brand_label = customtkinter.CTkLabel(self.hearing_aid_info_frame,text="Marka/Model:",font=("Helvetica",13,"bold"))
        self.hearing_aid_brand_label.pack(side=LEFT,padx=10,pady=4)
        self.hearing_aid_brand_entry = customtkinter.CTkEntry(self.hearing_aid_info_frame)
        self.hearing_aid_brand_entry.pack(side=LEFT,padx=(0,20),pady=4)

        self.hearing_aid_id_label = customtkinter.CTkLabel(self.hearing_aid_info_frame,text="ID:",font=("Helvetica",13,"bold"))
        self.hearing_aid_id_label.pack(side=LEFT,padx=(10,15),pady=4)
        self.hearing_aid_id_entry = customtkinter.CTkEntry(self.hearing_aid_info_frame)
        self.hearing_aid_id_entry.pack(side=LEFT,padx=(0,20),pady=4)

        self.hearing_aid_tube_label = customtkinter.CTkLabel(self.hearing_aid_info_frame,text="Tüp/Kalıp:",font=("Helvetica",13,"bold"))
        self.hearing_aid_tube_label.pack(side=LEFT,padx=(0,10),pady=4)
        self.hearing_aid_tube_entry = customtkinter.CTkEntry(self.hearing_aid_info_frame)
        self.hearing_aid_tube_entry.pack(side=LEFT,padx=(0,10),pady=4)


        self.hearing_aid_info2_frame = customtkinter.CTkFrame(self.info_frame,border_width=1,border_color="black")
        self.hearing_aid_info2_frame.pack(padx=10,fill=BOTH)

        self.hearing_aid_brand2_label = customtkinter.CTkLabel(self.hearing_aid_info2_frame,text="Marka/Model:",font=("Helvetica",13,"bold"))
        self.hearing_aid_brand2_label.pack(side=LEFT,padx=10,pady=4)
        self.hearing_aid_brand2_entry = customtkinter.CTkEntry(self.hearing_aid_info2_frame)
        self.hearing_aid_brand2_entry.pack(side=LEFT,padx=(0,20),pady=4)

        self.hearing_aid_id2_label = customtkinter.CTkLabel(self.hearing_aid_info2_frame,text="ID:",font=("Helvetica",13,"bold"))
        self.hearing_aid_id2_label.pack(side=LEFT,padx=(10,15),pady=4)
        self.hearing_aid_id2_entry = customtkinter.CTkEntry(self.hearing_aid_info2_frame)
        self.hearing_aid_id2_entry.pack(side=LEFT,padx=(0,20),pady=4)

        self.hearing_aid_tube2_label = customtkinter.CTkLabel(self.hearing_aid_info2_frame,text="Tüp/Kalıp:",font=("Helvetica",13,"bold"))
        self.hearing_aid_tube2_label.pack(side=LEFT,padx=(0,10),pady=4)
        self.hearing_aid_tube2_entry = customtkinter.CTkEntry(self.hearing_aid_info2_frame)
        self.hearing_aid_tube2_entry.pack(side=LEFT,padx=(0,10),pady=4)

# ------------------------- Update / Detail / Add-------------------------
        self.update_button = customtkinter.CTkButton(self.info_frame, text="Güncelle",command=self.update_patient)
        self.update_button.pack(side=LEFT,padx=10,expand=True)

        self.detail_button = customtkinter.CTkButton(self.info_frame, text="Detay...",command=self.get_form)
        self.detail_button.pack(side=LEFT,padx=10,expand=True)

        self.main_add_button = customtkinter.CTkButton(self.info_frame, text="Yeni Hasta Ekle", command=self.customerForm)
        self.main_add_button.pack(side=LEFT,padx=10,expand=True)

# ------------------------- Search1 -------------------------
        self.search_frame = customtkinter.CTkFrame(self,border_width=1,border_color="black",corner_radius=10)
        self.search_frame.pack(padx=10,pady=(10,20),side=LEFT,fill="both",expand=True)

        self.total_patient_label = customtkinter.CTkLabel(self.search_frame,text="Toplam Hasta Sayısı",font=("Helvetica",17,"bold","underline"))
        self.total_patient_label.pack(padx=20,pady=(10,2))
 
        self.get_total_patient()
        self.total_patient_label = customtkinter.CTkLabel(self.search_frame,text=self.total,font=("Helvetica",17))
        self.total_patient_label.pack(padx=20,pady=(0,20))

        self.search1_button = customtkinter.CTkButton(self.search_frame, text="İsme göre hasta bul",command=self.name_search)
        self.search1_button.pack(padx=10,pady=(20,10))

        self.search1_button = customtkinter.CTkButton(self.search_frame, text="Kayıt Tarihi",command=self.date_search)
        self.search1_button.pack(padx=10,pady=20)


    def customerForm(self):
        self.form = customtkinter.CTkToplevel(self)
        self.form.title("Anamnez Formu")
        self.main_frame = customtkinter.CTkFrame(self.form)
        self.main_frame.pack(padx=10,pady=20)

# ------------------------- Heading -------------------------
        self.top_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.top_frame.pack(padx=1,pady=(1,0),fill="both")

        self.heading = customtkinter.CTkLabel(self.top_frame,text="Hasta Bilgileri",font=("Helvetica",20,"bold"))
        self.heading.pack(padx=5,pady=10)

# ------------------------- Name / Surname -------------------------
        self.name_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.name_frame.pack(padx=1,fill="both")

        self.name_label = customtkinter.CTkLabel(self.name_frame,text="Ad:",font=("Helvetica",13))
        self.name_label.pack(padx=(10,5),pady=5,side="left")
        self.name_entry = customtkinter.CTkEntry(self.name_frame,placeholder_text="Ad")
        self.name_entry.pack(padx=(5,5),pady=5,side="left",fill="both",expand=True)

        self.surname_label = customtkinter.CTkLabel(self.name_frame,text="Soyad:",font=("Helvetica",13))
        self.surname_label.pack(padx=(5,5),pady=5,side="left")
        self.surname_entry = customtkinter.CTkEntry(self.name_frame,placeholder_text="Soyad")
        self.surname_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Birthday / Job -------------------------
        self.birthday_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.birthday_frame.pack(padx=1,fill="both")

        self.birthday_label = customtkinter.CTkLabel(self.birthday_frame,text="Doğum Tarihi:",font=("Helvetica",13))
        self.birthday_label.pack(padx=(10,5),pady=5,side="left")
        self.birthday_entry = customtkinter.CTkEntry(self.birthday_frame,placeholder_text="DD/MM/YYYY")
        self.birthday_entry.pack(padx=(5,5),pady=5,side="left",fill="both",expand=True)

        self.job_label = customtkinter.CTkLabel(self.birthday_frame,text="Meslek:",font=("Helvetica",13))
        self.job_label.pack(padx=(5,5),pady=5,side="left")
        self.job_entry = customtkinter.CTkEntry(self.birthday_frame,placeholder_text="Meslek")
        self.job_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Complaint -------------------------
        self.complaint_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.complaint_frame.pack(padx=1,fill="both")

        self.complaint_label = customtkinter.CTkLabel(self.complaint_frame,text="Şikayet:",font=("Helvetica",13))
        self.complaint_label.pack(padx=(10,5),pady=5,side="left")
        self.complaint_entry = customtkinter.CTkEntry(self.complaint_frame,placeholder_text="Şikayet...")
        self.complaint_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Sex / Email -------------------------
        self.sex_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.sex_frame.pack(padx=1,fill="both")

        self.sex_label = customtkinter.CTkLabel(self.sex_frame,text="Cinsiyet:",font=("Helvetica",13))
        self.sex_label.pack(padx=(10,5),pady=5,side="left")

        self.male_button = customtkinter.CTkCheckBox(self.sex_frame,text="E",checkbox_width=13,checkbox_height=13,width=30)
        self.male_button.pack(padx=(5,5),pady=5,side="left")

        self.female_button = customtkinter.CTkCheckBox(self.sex_frame,text="K",checkbox_width=13,checkbox_height=13,width=50)
        self.female_button.pack(padx=(5,5),pady=5,side="left")


        self.mail_label = customtkinter.CTkLabel(self.sex_frame,text="E-mail:",font=("Helvetica",13))
        self.mail_label.pack(padx=(5,5),pady=5,side="left")
        self.mail_entry = customtkinter.CTkEntry(self.sex_frame,placeholder_text="Mail") 
        self.mail_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Address -------------------------
        self.address_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.address_frame.pack(padx=1,fill="both")

        self.address_label = customtkinter.CTkLabel(self.address_frame,text="Adres:",font=("Helvetica",13))
        self.address_label.pack(padx=(10,5),pady=5,side="left")
        self.address_entry = customtkinter.CTkEntry(self.address_frame,placeholder_text="Adres")
        self.address_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Phone / Patient Relation -------------------------
        self.phone_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.phone_frame.pack(padx=1,fill="both")

        self.phone_label = customtkinter.CTkLabel(self.phone_frame,text="Telefon No:",font=("Helvetica",13))
        self.phone_label.pack(padx=(10,5),pady=5,side="left")
        self.phone_entry = customtkinter.CTkEntry(self.phone_frame,placeholder_text="(xxx) xxx xx xx")
        self.phone_entry.pack(padx=(5,5),pady=5,side="left",fill="both",expand=True)

        self.patient_label = customtkinter.CTkLabel(self.phone_frame,text="Hasta Yakınlık Derecesi:",font=("Helvetica",13))
        self.patient_label.pack(padx=(5,5),pady=5,side="left")
        self.patient_entry = customtkinter.CTkEntry(self.phone_frame,placeholder_text="Yakınlık")
        self.patient_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Emergency Contact -------------------------
        self.emergency_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.emergency_frame.pack(padx=1,fill="both")

        self.emergency_label = customtkinter.CTkLabel(self.emergency_frame,text="Acil durum tel:",font=("Helvetica",13))
        self.emergency_label.pack(padx=(10,5),pady=5,side="left")
        self.emergency_entry = customtkinter.CTkEntry(self.emergency_frame,placeholder_text="(xxx) xxx xx xx")
        self.emergency_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Recomandation -------------------------
        self.recomandation_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.recomandation_frame.pack(padx=1,fill="both")

        self.recomandation_label = customtkinter.CTkLabel(self.recomandation_frame,text="Bize nasıl ulaştınız?",font=("Helvetica",13))
        self.recomandation_label.pack(padx=(10,5),pady=5,side="left")

        self.recomandation_checkbox = customtkinter.CTkCheckBox(self.recomandation_frame,text="Tavsiye",checkbox_width=13,checkbox_height=13,width=30)
        self.recomandation_checkbox.pack(padx=(5,5),pady=5,side="left")

        self.recomandation_checkbox2 = customtkinter.CTkCheckBox(self.recomandation_frame,text="Internet",checkbox_width=13,checkbox_height=13,width=30)
        self.recomandation_checkbox2.pack(padx=(5,5),pady=5,side="left")

        self.recomandation_checkbox3 = customtkinter.CTkCheckBox(self.recomandation_frame,text="Geçerken",checkbox_width=13,checkbox_height=13,width=30)
        self.recomandation_checkbox3.pack(padx=(5,5),pady=5,side="left")

        self.dr_checkbox = customtkinter.CTkCheckBox(self.recomandation_frame,text="Dr.",checkbox_width=13,checkbox_height=13,width=30)
        self.dr_checkbox.pack(padx=(30,5),pady=5,side="left")
        self.dr_entry = customtkinter.CTkEntry(self.recomandation_frame)
        self.dr_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# -------------------------Hearing Aid Heading -------------------------
        self.aid_heading_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.aid_heading_frame.pack(padx=1,fill="both")

        self.heading = customtkinter.CTkLabel(self.aid_heading_frame,text="Cihaz Bilgileri",font=("Helvetica",20,"bold"))
        self.heading.pack(padx=5,pady=10)

# ------------------------- Hearing Aid Brand/Model -------------------------

        self.brand_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.brand_frame.pack(padx=1,fill="both")

        self.brand_label = customtkinter.CTkLabel(self.brand_frame,text="Marka/Model:",font=("Helvetica",13))
        self.brand_label.pack(padx=(10,5),pady=5,side="left")
        self.brand_entry = customtkinter.CTkEntry(self.brand_frame)
        self.brand_entry.pack(padx=(5,5),pady=5,side="left",fill="both",expand=True)

        self.ID_label = customtkinter.CTkLabel(self.brand_frame,text="ID:",font=("Helvetica",13))
        self.ID_label.pack(padx=(5,5),pady=5,side="left")
        self.ID_entry = customtkinter.CTkEntry(self.brand_frame)
        self.ID_entry.pack(padx=(5,5),pady=5,side="left",fill="both",expand=True)

        self.tube_label = customtkinter.CTkLabel(self.brand_frame,text="Tüp/Kalıp:",font=("Helvetica",13))
        self.tube_label.pack(padx=(10,5),pady=5,side="left")
        self.tube_entry = customtkinter.CTkEntry(self.brand_frame)
        self.tube_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)


        self.brand_frame2 = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black")
        self.brand_frame2.pack(padx=1,fill="both")

        self.brand_label2 = customtkinter.CTkLabel(self.brand_frame2,text="Marka/Model:",font=("Helvetica",13))
        self.brand_label2.pack(padx=(10,5),pady=5,side="left")
        self.brand_entry2 = customtkinter.CTkEntry(self.brand_frame2)
        self.brand_entry2.pack(padx=(5,5),pady=5,side="left",fill="both",expand=True)

        self.ID_label2 = customtkinter.CTkLabel(self.brand_frame2,text="ID:",font=("Helvetica",13))
        self.ID_label2.pack(padx=(5,5),pady=5,side="left")
        self.ID_entry2 = customtkinter.CTkEntry(self.brand_frame2)
        self.ID_entry2.pack(padx=(5,5),pady=5,side="left",fill="both",expand=True)

        self.tube_label2 = customtkinter.CTkLabel(self.brand_frame2,text="Tüp/Kalıp:",font=("Helvetica",13))
        self.tube_label2.pack(padx=(10,5),pady=5,side="left")
        self.tube_entry2 = customtkinter.CTkEntry(self.brand_frame2)
        self.tube_entry2.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Audiological Examination / Health History -------------------------

        self.audiological_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.audiological_frame.pack(padx=1,fill="both")

        self.heading = customtkinter.CTkLabel(self.audiological_frame,text="Odyolojik İnceleme / Hastalık Geçmişi",font=("Helvetica",20,"bold"))
        self.heading.pack(padx=5,pady=10)

# ------------------------- Questions-1 -------------------------

        self.question1_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.question1_frame.pack(padx=1,fill="both")

        self.question1_label = customtkinter.CTkLabel(self.question1_frame,text="Daha önce işitme testi yaptırdınız mı?",font=("Helvetica",13))
        self.question1_label.pack(padx=(10,5),pady=5,side="left")

        self.question1_yes_button = customtkinter.CTkCheckBox(self.question1_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.question1_yes_button.pack(padx=(5,5),pady=5,side="left") 

        self.question1_no_button = customtkinter.CTkCheckBox(self.question1_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.question1_no_button.pack(padx=(5,5),pady=5,side="left")

        self.question1_label2 = customtkinter.CTkLabel(self.question1_frame,text="Evet ise, ne zaman ve nerede?",font=("Helvetica",13))
        self.question1_label2.pack(padx=(5,5),pady=5,side="left")
        self.question1_entry = customtkinter.CTkEntry(self.question1_frame)
        self.question1_entry.pack(padx=(5,10),pady=5,side="left",fill="both",expand=True)

# ------------------------- Questions-2 -------------------------

        self.question2_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.question2_frame.pack(padx=1,fill="both")

        self.question2_label = customtkinter.CTkLabel(self.question2_frame,text="Kulaklarınızdan operasyon geçirdiniz mi?",font=("Helvetica",13))
        self.question2_label.pack(padx=(10,5),pady=5,side="left")

        self.question2_yes_button = customtkinter.CTkCheckBox(self.question2_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.question2_yes_button.pack(padx=(5,5),pady=5,side="left") 

        self.question2_no_button = customtkinter.CTkCheckBox(self.question2_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.question2_no_button.pack(padx=(5,5),pady=5,side="left")

        self.question2_label2 = customtkinter.CTkLabel(self.question2_frame,text="Ailenizde işitme kaybı olan var mı?",font=("Helvetica",13))
        self.question2_label2.pack(padx=(47,5),pady=5,side="left")

        self.question2_yes_button2 = customtkinter.CTkCheckBox(self.question2_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.question2_yes_button2.pack(padx=(5,5),pady=5,side="left") 

        self.question2_no_button2 = customtkinter.CTkCheckBox(self.question2_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.question2_no_button2.pack(padx=(5,10),pady=5,side="left")

# ------------------------- Diseases -------------------------

        self.disease123_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.disease123_frame.pack(padx=1,fill="both")


        self.disease1_label = customtkinter.CTkLabel(self.disease123_frame,text="Kulak Enfeksiyonu",font=("Helvetica",13))
        self.disease1_label.pack(padx=(10,5),pady=5,side="left")

        self.disease1_yes_button = customtkinter.CTkCheckBox(self.disease123_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.disease1_yes_button.pack(padx=(5,5),pady=5,side="left") 

        self.disease1_no_button = customtkinter.CTkCheckBox(self.disease123_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.disease1_no_button.pack(padx=(5,5),pady=5,side="left")


        self.disease2_label = customtkinter.CTkLabel(self.disease123_frame,text="Vertigo",font=("Helvetica",13))
        self.disease2_label.pack(padx=(85,5),pady=5,side="left")

        self.disease2_yes_button = customtkinter.CTkCheckBox(self.disease123_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.disease2_yes_button.pack(padx=(5,5),pady=5,side="left") 

        self.disease2_no_button = customtkinter.CTkCheckBox(self.disease123_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.disease2_no_button.pack(padx=(5,5),pady=5,side="left")


        self.disease3_label = customtkinter.CTkLabel(self.disease123_frame,text="Baş Ağrısı",font=("Helvetica",13))
        self.disease3_label.pack(padx=(85,5),pady=5,side="left")

        self.disease3_yes_button = customtkinter.CTkCheckBox(self.disease123_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.disease3_yes_button.pack(padx=(5,5),pady=5,side="left") 

        self.disease3_no_button = customtkinter.CTkCheckBox(self.disease123_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.disease3_no_button.pack(padx=(5,5),pady=5,side="left")


        self.disease45_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.disease45_frame.pack(padx=1,fill="both")


        self.disease4_label = customtkinter.CTkLabel(self.disease45_frame,text="Tinnitus",font=("Helvetica",13))
        self.disease4_label.pack(padx=(150,5),pady=5,side="left")

        self.disease4_yes_button = customtkinter.CTkCheckBox(self.disease45_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.disease4_yes_button.pack(padx=(5,5),pady=5,side="left") 

        self.disease4_no_button = customtkinter.CTkCheckBox(self.disease45_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.disease4_no_button.pack(padx=(5,5),pady=5,side="left")

        self.disease5_label = customtkinter.CTkLabel(self.disease45_frame,text="Hiperakuzi",font=("Helvetica",13))
        self.disease5_label.pack(padx=(150,5),pady=5,side="left")

        self.disease5_yes_button = customtkinter.CTkCheckBox(self.disease45_frame,text="Evet",checkbox_width=13,checkbox_height=13,width=30)
        self.disease5_yes_button.pack(padx=(5,5),pady=5,side="left") 

        self.disease5_no_button = customtkinter.CTkCheckBox(self.disease45_frame,text="Hayır",checkbox_width=13,checkbox_height=13,width=30)
        self.disease5_no_button.pack(padx=(5,5),pady=5,side="left")

# ------------------------- Comment -------------------------

        self.comment_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="black",corner_radius=10)
        self.comment_frame.pack(padx=1,side="left",fill="both")

        self.comment_label = customtkinter.CTkLabel(self.comment_frame,text="Diğer/Yorum:",font=("Helvetica",13))
        self.comment_label.pack(padx=(10,5),pady=5,side="left")

        self.comment_box = customtkinter.CTkTextbox(self.comment_frame,border_width=1,border_color="black",width=400)
        self.comment_box.pack(padx=5,pady=5,side="left")

# ------------------------- Button -------------------------

        self.add_button = customtkinter.CTkButton(self.main_frame,text="Müşteri Ekle",command=self.add_customer)
        self.add_button.pack(side="left",expand=True)


# ------------------------- FUNCTIONS -------------------------


# ------------------------- UPDATE TREEVIEW -------------------------
    # Updates the treeview every time program runs or a new customer added
    def update_treeview(self):
        self.my_tree.tag_configure("oddrow",background='gray')
        self.my_tree.tag_configure("evenrow",background='black')

        # Add data to the treeview
        conn = sqlite3.connect("customers.db")
        cur = conn.cursor()
        cur.execute("select * from customers")
        records = cur.fetchall()
        conn.close()

        global count
        count = 0
        for record in records:
                if count % 2 == 0:
                        self.my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[13]), tags='evenrow')
                else:
                        self.my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[13]), tags='oddrow')
                count += 1


# ------------------------- ADD CUSTOMER-------------------------
    def add_customer(self):
        # get user inputs
        #Patient Information
        name = self.name_entry.get().capitalize().strip()
        surname = self.surname_entry.get().capitalize().strip()
        birthday = self.birthday_entry.get().strip()
        phone = self.phone_entry.get().strip()
        mail = self.mail_entry.get().strip()
        job = self.job_entry.get().strip()

        #Hearing aid Information (right) 
        right_model = self.brand_entry.get().strip()
        right_id = self.ID_entry.get().strip()
        right_tube = self.tube_entry.get().strip()

        #Hearing aid Information (left) 
        left_model = self.brand_entry2.get().strip()
        left_id = self.ID_entry2.get().strip()
        left_tube = self.tube_entry2.get().strip()

        record_date = date.today().strftime("%d/%m/%Y")

        # Data that will be save into database
        data = [name,surname,birthday,phone,mail,job,right_model,right_id,right_tube,left_model,left_id,left_tube,record_date]

        # Create / Connect to database
        conn = sqlite3.connect("customers.db")
        c = conn.cursor()

        # Create a table
        c.execute("""CREATE TABLE if not exists customers(
                ID INTEGER PRIMARY KEY,
                name text,
                surname text,
                birthday text,
                phone text,
                mail text,
                job text,
                right_model text,
                right_id text,
                right_tube text,
                left_model text,
                left_id text,
                left_tube text,
                record_date text
        )""")

        #  Add the entries to the table
        c.executemany(f"INSERT INTO customers(name,surname,birthday,phone,mail,job,right_model,right_id,right_tube,left_model,left_id,left_tube,record_date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",[data])
        # Commit Changes
        conn.commit()
        #Close connection
        conn.close()

        #Clear the treeview
        self.my_tree.delete(*self.my_tree.get_children())
        #Update the Treeview
        self.update_treeview()

        #Get screenshot of the form
        width = self.form.winfo_width()
        height = self.form.winfo_height()
        x = self.form.winfo_rootx()
        y = self.form.winfo_rooty()
        im = pyscreenshot.grab(bbox=(x,y,width+x,height+y))
        im.save(f"Formlar/{name+surname}.png")


# ------------------------- GET TREEVIEW DATA -------------------------
    def get_treeview_data(self,e):
        self.selected_patient = self.my_tree.focus() #gets the selected column ID

        #Clear the patient information entries
        self.customer_id_entry.delete(0,END)
        self.customer_name_entry.delete(0,END)
        self.customer_surname_entry.delete(0,END)
        self.hearing_aid_brand_entry.delete(0,END)
        self.hearing_aid_id_entry.delete(0,END)
        self.hearing_aid_tube_entry.delete(0,END)
        self.hearing_aid_brand2_entry.delete(0,END)
        self.hearing_aid_id2_entry.delete(0,END)
        self.hearing_aid_tube2_entry.delete(0,END)

        #Grab record values
        self.values = self.my_tree.item(self.selected_patient,"values")

        #Connect to database and get the desired values
        conn = sqlite3.connect("customers.db")
        cur = conn.cursor()
        cur.execute(f"select * from customers where ID = {self.values[0]}")
        self.data = cur.fetchone()
        conn.close()

        #Insert customer information to each entry
        self.customer_id_entry.insert(0,self.data[0])
        self.customer_name_entry.insert(0,self.data[1])
        self.customer_surname_entry.insert(0,self.data[2])
        self.hearing_aid_brand_entry.insert(0,self.data[7])
        self.hearing_aid_id_entry.insert(0,self.data[8])
        self.hearing_aid_tube_entry.insert(0,self.data[9])
        self.hearing_aid_brand2_entry.insert(0,self.data[10])
        self.hearing_aid_id2_entry.insert(0,self.data[11])
        self.hearing_aid_tube2_entry.insert(0,self.data[12])


# ------------------------- UPDATE PATIENT -------------------------
    def update_patient(self):
        self.selected_patient = self.my_tree.focus()
        self.values = self.my_tree.item(self.selected_patient,"values")

        conn = sqlite3.connect("customers.db")
        cur = conn.cursor()
        cur.execute(f"""UPDATE customers
                        SET name = '{self.customer_name_entry.get().strip()}', 
                            surname = '{self.customer_surname_entry.get().strip()}',
                            right_model = '{self.hearing_aid_brand_entry.get().strip()}',
                            right_id = '{self.hearing_aid_id_entry.get().strip()}',
                            right_tube = '{self.hearing_aid_tube_entry.get().strip()}',
                            left_model = '{self.hearing_aid_brand2_entry.get().strip()}',
                            left_id = '{self.hearing_aid_id2_entry.get().strip()}',
                            left_tube = '{self.hearing_aid_tube2_entry.get().strip()}'
                        WHERE ID = {self.values[0]}
                        """)
        conn.commit()
        conn.close()
        #Clear the treeview
        self.my_tree.delete(*self.my_tree.get_children())
        #Update the Treeview
        self.update_treeview()


# ------------------------- CLEAR TABLE -------------------------
    def clear_table(self):
        conn = sqlite3.connect("customers.db")
        c = conn.cursor()
        c.execute("drop table customers")
        conn.commit()
        conn.close()


# ------------------------- GET FORM -------------------------
    def get_form(self):
        self.selected_patient = self.my_tree.focus()
        self.values = self.my_tree.item(self.selected_patient,"values")
        im = Image.open(f"Formlar/{self.values[1]+self.values[2]}.png")
        im.show()


# ------------------------- GET TOTAL PATIENT -------------------------
    def get_total_patient(self):
        conn = sqlite3.connect("customers.db")
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM customers")
        self.total = c.fetchone()
        conn.commit()
        conn.close()


# ------------------------- NAME SEARCH -------------------------
    def name_search(self):
        self.search_page = customtkinter.CTkToplevel(self)
        self.search_page.title("Odio-Tek")

        self.main_frame = customtkinter.CTkFrame(self.search_page)
        self.main_frame.pack(padx=10,pady=20)

        self.search_title = customtkinter.CTkLabel(self.main_frame,text="Arama Bilgileri",font=("Helvetica",17,"bold"))
        self.search_title.pack()

        self.search_name_frame = customtkinter.CTkFrame(self.main_frame,corner_radius=5,border_color="black",border_width=1)
        self.search_name_frame.pack(padx=5,pady=5)

        self.search_name_label = customtkinter.CTkLabel(self.search_name_frame,text="İsim:",font=("Helvetica",13))
        self.search_name_label.pack(side=LEFT,padx=10,pady=10)
        self.search_name_entry = customtkinter.CTkEntry(self.search_name_frame)
        self.search_name_entry.pack(side=LEFT,padx=10,pady=10)

        self.search_surname_label = customtkinter.CTkLabel(self.search_name_frame,text="Soyisim:",font=("Helvetica",13))
        self.search_surname_label.pack(side=LEFT,padx=10,pady=10)
        self.search_surname_entry = customtkinter.CTkEntry(self.search_name_frame)
        self.search_surname_entry.pack(side=LEFT,padx=10,pady=10)

        self.search_name_button = customtkinter.CTkButton(self.main_frame,text="Ara",command=self.find_by_name)
        self.search_name_button.pack(padx=10,pady=10)

        self.patient_id_label = customtkinter.CTkLabel(self.main_frame,text=" ")
        self.patient_id_label.pack(padx=10,pady=10)


# ------------------------- FIND BY NAME -------------------------
    def find_by_name(self):
        name = self.search_name_entry.get().capitalize().strip()
        surname = self.search_surname_entry.get().capitalize().strip()
        
        conn = sqlite3.connect("customers.db")
        c = conn.cursor()
        c.execute(f"""SELECT * FROM customers
                WHERE
                        name = '{name}'
                        AND
                        surname = '{surname}'
                """)
        selected_patient = c.fetchall()
        patient_id = "ID:  " + str(selected_patient[0][0])
        conn.close()
        self.patient_id_label.configure(text=patient_id,font=("Helvetica",15,"bold"))


# ------------------------- DATE SEARCH -------------------------
    def date_search(self):
        self.date_search_page = customtkinter.CTkToplevel(self)
        self.date_search_page.title("Odio-Tek")

        self.main_frame = customtkinter.CTkFrame(self.date_search_page)
        self.main_frame.pack(padx=10,pady=20)

        self.date_search_title = customtkinter.CTkLabel(self.main_frame,text="Arama Bilgileri",font=("Helvetica",17,"bold"))
        self.date_search_title.pack()

        self.month_frame = customtkinter.CTkFrame(self.main_frame,corner_radius=5,border_color="black",border_width=1)
        self.month_frame.pack(padx=5,pady=5)

        self.month_label = customtkinter.CTkLabel(self.month_frame,text="Ay:",font=("Helvetica",13))
        self.month_label.pack(side=LEFT,padx=(10,5),pady=10)

        self.month_combobox = customtkinter.CTkComboBox(self.month_frame,values=["01","02","03","04","05","06","07","08","09","10","11","12"])
        self.month_combobox.pack(side=LEFT,padx=(5,10),pady=10)

        self.month_button = customtkinter.CTkButton(self.month_frame,text="Ara",command=self.find_by_month)
        self.month_button.pack(side=LEFT,padx=10,pady=10)

        self.month_result_label = customtkinter.CTkLabel(self.month_frame,text="",font=("Helvetica",13))
        self.month_result_label.pack(side=LEFT,padx=10,pady=10)


        self.year_frame = customtkinter.CTkFrame(self.main_frame,corner_radius=5,border_color="black",border_width=1)
        self.year_frame.pack(padx=5,pady=5)

        self.year_label = customtkinter.CTkLabel(self.year_frame,text="Yıl:",font=("Helvetica",13))
        self.year_label.pack(side=LEFT,padx=(10,5),pady=10)

        self.year_combobox = customtkinter.CTkComboBox(self.year_frame,values=["2023"])
        self.year_combobox.pack(side=LEFT,padx=(5,10),pady=10)

        self.year_button = customtkinter.CTkButton(self.year_frame,text="Ara",command=self.find_by_year)
        self.year_button.pack(side=LEFT,padx=10,pady=10)

        self.year_result_label = customtkinter.CTkLabel(self.year_frame,text="",font=("Helvetica",13))
        self.year_result_label.pack(side=LEFT,padx=10,pady=10)


# ------------------------- FIND BY MONTH -------------------------
    def find_by_month(self):
        month = self.month_combobox.get()

        month_names = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]

        conn = sqlite3.connect("customers.db")
        c = conn.cursor()
        c.execute(f"""SELECT * FROM customers
                WHERE record_date LIKE '%/{month}/%'
                """)
        selected_patient = c.fetchall()
        conn.close()
        result = f"{month_names[int(month)-1]} ayı hasta sayisi:  {len(selected_patient)}" 
        self.month_result_label.configure(text=result,font=("Helvetica",15,"bold"))


# ------------------------- FIND BY YEAR -------------------------
    def find_by_year(self):
        year = self.year_combobox.get()
        conn = sqlite3.connect("customers.db")
        c = conn.cursor()
        c.execute(f"""SELECT * FROM customers
                WHERE record_date LIKE '%/2023%'
                """)
        selected_patient = c.fetchall()
        conn.close()
        result = f"{year} yılı hasta sayisi:  {len(selected_patient)}"
        self.year_result_label.configure(text=result,font=("Helvetica",15,"bold"))