from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        #variables

        self.var_dep=StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mobile = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


       #1st
        img_1=Image.open("img2.jpg")
        img_1=img_1.resize((540,160),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)


        self.btn_1=Button(self.root,image=self.photoimg_1,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

        # 2nd
        img_2 = Image.open("img6.jpg")
        img_2 = img_2.resize((500,160), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=500, y=0, width=500, height=160)

        # 3rd
        img_3 = Image.open("img4.jpg")
        img_3 = img_3.resize((540,180), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=900, y=0, width=540, height=160)



        # bg image
        img_4=Image.open("img9.jpg")
        img_4=img_4.resize((1400,600),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1400,height=600)


        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1400,height=30)

        #manage_frame

        manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=10,y=33,width=1345,height=497)


        #left frame
        DataLeftFrame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",10,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=5,y=10,width=570,height=480)

        #img left
        img_5 = Image.open("img10.jpg")
        img_5 = img_5.resize((550, 90), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        my_img = Label(DataLeftFrame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=560, height=85)

        #current course labelframe information
        std_lbl_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Current Course Information",font=("times new roman", 10, "bold"), fg="red", bg="white")
        std_lbl_info_frame.place(x=0, y=90, width=560, height=105)

        #labels and combobox
        #department
        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",10,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",10,"bold"),width=20,state="readonly")
        combo_dep['value']=("Select Department","CS","IT","CE","ME","EX","EC")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course

        course_std=Label(std_lbl_info_frame,font=("arial",10,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)

        com_txtcourse_std=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,state="readonly",font=("arial",10,"bold"),width=20)

        com_txtcourse_std['value']=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)

        #year

        current_year=Label(std_lbl_info_frame,font=("arial",10,"bold"),text="Year:",bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_txt_current_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,state="readonly",font=("arial",10,"bold"),width=20)

        com_txt_current_year['value']=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1,column=1,sticky=W,padx=2)

        #semester
        label_Semester=Label(std_lbl_info_frame,font=("arial",10,"bold"),text="Courses:",bg="white")
        label_Semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        comSemester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester,state="readonly",font=("arial",10,"bold"),width=20)

        comSemester['value']=("Select Course","Semester-1","Semester-2","semester-3","Semester-4")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)


        #Student class LableFrame Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=("times new roman", 10, "bold"), fg="red", bg="white")
        std_lbl_class_frame.place(x=0,y=200,width=560,height=220)

        #lables entry
        #id
        lbl_id=Label(std_lbl_class_frame,font=("arial",10,"bold"),text="Student ID:",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id,font=("arial",10,"bold"),width=20)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

         # Name
        lbl_name = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Student Name:", bg="white")
        lbl_name.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name, font=("arial", 10, "bold"), width=20)
        txt_name.grid(row=0, column=3, sticky=W, padx=2, pady=7)


        # Division
        lbl_div = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Class Division:", bg="white")
        lbl_div.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        com_txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,state="readonly",font=("arial",10,"bold"),width=18)
        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)

         #Roll
        lbl_roll = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Enrollment No.:", bg="white")
        lbl_roll.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_roll = ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll, font=("arial", 10, "bold"), width=20)
        txt_roll.grid(row=1, column=3, sticky=W, padx=2, pady=7)

        #gender
        lbl_gender = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Class Division:", bg="white")
        lbl_gender.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        com_txt_gender = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender, state="readonly", font=("arial", 10, "bold"), width=18)
        com_txt_gender['value'] = ("Male","Female")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        #DOB
        lbl_dob = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="DOB:", bg="white")
        lbl_dob.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_dob = ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob, font=("arial", 10, "bold"), width=20)
        txt_dob.grid(row=2, column=3, padx=2, pady=7)

        #email
        lbl_email = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Email:", bg="white")
        lbl_email.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_email = ttk.Entry(std_lbl_class_frame,textvariable=self.var_email, font=("arial", 10, "bold"), width=20)
        txt_email.grid(row=3, column=1, padx=2, pady=7)

        #mobile no,
        lbl_mobile = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Mobile No.:", bg="white")
        lbl_mobile.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_mobile = ttk.Entry(std_lbl_class_frame,textvariable=self.var_mobile, font=("arial", 10, "bold"), width=20)
        txt_mobile.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        #address
        lbl_address = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Address:", bg="white")
        lbl_address.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(std_lbl_class_frame,textvariable=self.var_address, font=("arial", 10, "bold"), width=20)
        txt_address.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        #teacher
        lbl_faculty = Label(std_lbl_class_frame, font=("arial", 10, "bold"), text="Faculty Name.:", bg="white")
        lbl_faculty.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_faculty = ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher, font=("arial", 10, "bold"), width=20)
        txt_faculty.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        #button frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=420,width=560,height=30)

        btn_Add=Button(btn_frame,text="Save",font=("aria",11,"bold"),width=15,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update = Button(btn_frame, text="Update", font=("aria", 11, "bold"), width=14, bg="blue", fg="white")
        btn_update.grid(row=0, column=1, padx=1)

        btn_Delete = Button(btn_frame, text="Delete", font=("aria", 11, "bold"), width=14, bg="blue", fg="white")
        btn_Delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=("aria", 11, "bold"), width=14, bg="blue", fg="white")
        btn_reset.grid(row=0, column=3, padx=1)


        #right frame
        DataRightFrame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Details",font=("times new roman", 10, "bold"), fg="red", bg="white")
        DataRightFrame.place(x=580, y=10, width=755, height=480)

        #img1
        img_6 = Image.open("img3.jpg")
        img_6 = img_6.resize((745, 170), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        my_img = Label(DataRightFrame, image=self.photoimg_6, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=745, height=170)

        #search frame
        search_Frame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Search Student Information",
                                    font=("times new roman", 10, "bold"), fg="red", bg="white")
        search_Frame.place(x=0, y=170, width=745, height=54)

        search_by = Label(search_Frame, font=("arial", 10, "bold"), text="Search by:",fg="red", bg="yellow")
        search_by.grid(row=0, column=0, sticky=W, padx=2, pady=4)

        com_txt_search = ttk.Combobox(search_Frame, state="readonly", font=("arial", 10, "bold"), width=22)
        com_txt_search['value'] = ("Select Option","Enrollment No.",'Mobile No.',"Student Id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        txt_search = ttk.Entry(search_Frame, font=("arial", 10, "bold"), width=22)
        txt_search.grid(row=0, column=2, sticky=W, padx=5)

        btn_search = Button(search_Frame, text="Search", font=("aria", 11, "bold"), width=14, bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=3)

        btn_showall = Button(search_Frame, text="Show All", font=("aria", 11, "bold"), width=14, bg="blue", fg="white")
        btn_showall.grid(row=0, column=4, padx=5)

       # =======================Student Table and scroll  bar========================#

        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=225,width=745,height=230)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","gender","email","dob","division","enroll","mobile","address","teacher",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("division", text="Division")
        self.student_table.heading("enroll", text="Enrollment Num")
        self.student_table.heading("mobile", text="Mobile Number")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("division", width=100)
        self.student_table.column("enroll", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)


        self.student_table.pack(fil=BOTH,expand=1)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
