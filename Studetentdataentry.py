#Packages importing area
from importlib.resources import contents
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from tkcalendar import DateEntry
from datetime import date
import babel.numbers
import sqlite3 

#Class definition area
class register():

    def __init__(self,log_root):
        self.log_root = log_root
        self.log_root.title("Student Database Management")
        self.log_root.geometry("1300x690+0+0")
        self.log_root.config(bg="#EEF2FF")
        self.log_root.resizable(0,0)
        self.log_root.iconbitmap("Images/logo.ico")
        
        #---------backgroung Image---------
        self.bg = ImageTk.PhotoImage(file="Images/bg.jpg")
        bg_lab = Label(self.log_root,image=self.bg)
        bg_lab.pack()

        #---------Login Lables---------
        user_lab = Label(self.log_root, text="User name", font=('consolas',14,'bold'), fg="#C449C2", bg='white')
        user_lab.place(x=60,y=205)

        pass_lab = Label(self.log_root, text="Password", font=('consolas',14,'bold'), fg="#C449C2", bg='white')
        pass_lab.place(x=60,y=294)

        '''or_lab = Label(self.log_root, text="or", font=('consolas',14,'bold'), fg="black", bg='white')
        or_lab.place(x=230,y=536)'''

        #---------Login Entry---------
        self.username = StringVar
        self.password = StringVar
        
        Frame(self.log_root, height=2,bg="#c44984").place(x=60,y=275, width=270) 
        Frame(self.log_root, height=2,bg="#c44984").place(x=60,y=364, width=270)

        self.user_ent = Entry(self.log_root,textvariable=self.username, font=('consolas',18,'bold'), fg="#867AE9", bg='white', bd=0)
        self.user_ent.place(x=60,y=245)

        self.pass_ent = Entry(self.log_root,textvariable=self.password, font=('consolas',18,'bold'), fg="#867AE9", bg='white',show='*', bd=0)
        self.pass_ent.place(x=60,y=334)   

        #---------Login & signup btn---------  
        log_btn = Button(self.log_root, text="Login", bg="#867AE9", fg="#FFF5AB",font=('consolas',14,'bold'), bd=0, command=self.call, cursor="hand2")
        log_btn.place(x=165,y=486,width=150, height=40,)

        '''sign_btn = Button(self.log_root, text="Sign Up", bg="white", fg="#C449C2",font=('consolas',14,'bold'), bd=0, command=self.signup, cursor="hand2")
        sign_btn.place(x=165,y=568,width=150, height=40,)'''

    def call(self):# function for call a dataentry class & login page
        if self.user_ent.get()!="admin" or self.pass_ent.get()!="admin@123":
                messagebox.showerror("Login error", "Please enter your valid userid and password")
                                    
        else:
                messagebox.showinfo("Login info", "Login Sucessfull")
                root = Tk()
                self.log_root.destroy()
                ob = dataentry(root)
                root.mainloop() 
                     
    '''def signup(self):# function for Signup page
            #---------background image for signup page----------
        self.sign_bg = ImageTk.PhotoImage(file="Images/bg1.jpg")
        sign_bg_lab = Label(self.log_root,image=self.sign_bg)
        sign_bg_lab.place(x=0,y=0,width=1300, height=690)

        #---------Signup Lables---------
        sign_email_lab = Label(self.log_root, text="Email ID", font=('consolas',14,'bold'), fg="#C449C2", bg='white')
        sign_email_lab.place(x=877,y=172)

        sign_username_lab = Label(self.log_root, text="User name", font=('consolas',14,'bold'), fg="#C449C2", bg='white')
        sign_username_lab.place(x=877,y=260.5)

        sign_pass_lab = Label(self.log_root, text="Password", font=('consolas',14,'bold'), fg="#c449c2", bg='white')
        sign_pass_lab.place(x=877,y=349)

        sign_conpass_lab = Label(self.log_root, text="Confirm Password", font=('consolas',14,'bold'), fg="#c449c2", bg='white')
        sign_conpass_lab.place(x=877,y=437.5)
                
        #----------Signup entry boxes----------
        self.email = StringVar
        self.user = StringVar
        self.passwrd = StringVar
        self.conpass = StringVar
        
        self.email_ent = Entry(self.log_root,textvariable=self.email, font=('consolas',18,'bold'), fg="#867AE9", bg='white', bd=0)
        self.email_ent.place(x=877,y=210)
        Frame(self.log_root, height=2,bg="#c44984").place(x=877,y=240, width=270)

        self.pass_ent = Entry(self.log_root,textvariable=self.user, font=('consolas',18,'bold'), fg="#867AE9", bg='white', bd=0)
        self.pass_ent.place(x=877,y=300)
        Frame(self.log_root, height=2,bg="#c44984").place(x=877,y=330, width=270)
        
        self.passwrd_ent = Entry(self.log_root,textvariable=self.passwrd, font=('consolas',18,'bold'), fg="#867AE9", bg='white',show='*', bd=0)
        self.passwrd_ent.place(x=877,y=390)
        Frame(self.log_root, height=2,bg="#c44984").place(x=877,y=420, width=270)

        self.conpass_ent = Entry(self.log_root,textvariable=self.conpass, font=('consolas',18,'bold'), fg="#867AE9", bg='white',show='*', bd=0)
        self.conpass_ent.place(x=877,y=475)
        Frame(self.log_root, height=2,bg="#c44984").place(x=877,y=505, width=270)      

        #---------Login & signup btn---------   
        signin_btn = Button(self.log_root, text="Sign in", bg="#867AE9", fg="#FFF5AB",font=('consolas',14,'bold'), bd=0, command=self.call, cursor="hand2")
        signin_btn.place(x=980,y=577,width=150, height=40,)'''

class dataentry():

    def __init__(self,root):
        self.root = root
        self.root.title("Student Database Management")
        self.root.geometry("1300x690+0+0")
        self.root.config(bg="#EEF2FF")
        self.root.resizable(0,0)
        self.root.iconbitmap("Images/logo.ico")
        
        #------- Header frame ---------
        hrd_fr = Frame(self.root, bg="#6d8ae7")
        hrd_fr.pack(fill=X, side=TOP)

        hrd_lab = Label(hrd_fr, text="Student Database Mangement System", bg="#6d8ae7", fg="#eef2ff", font=("consolas", 42))
        hrd_lab.pack()

        #------- Left frame ---------
        lft_fr = Frame(self.root, bg="#a0b3f0")
        lft_fr.place(x=20, y=100, width=450, height=560)

        tit_lab = Label(lft_fr, text="Student-Info", bg="#a0b3f0", fg="#3b3c3f", font=("consolas",24,'bold'))
        tit_lab.grid(row=0, columnspan=2, padx=70, pady=20)

                #------- Information labels ---------       
        reg_lab = Label(lft_fr, text="Register No", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        reg_lab.grid(row=1, padx=20, pady=5, sticky='w')

        name_lab = Label(lft_fr, text="Name", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        name_lab.grid(row=2, padx=20, pady=8, sticky='w')

        gen_lab = Label(lft_fr, text="Gender", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        gen_lab.grid(row=3, padx=20, pady=8, sticky='w')

        con_lab = Label(lft_fr, text="Contact No", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        con_lab.grid(row=4, padx=20, pady=8, sticky='w')
        
        aadh_lab = Label(lft_fr, text="AADHAAR No", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        aadh_lab.grid(row=5, padx=20, pady=8, sticky='w')

        email_lab = Label(lft_fr, text="Email ID", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        email_lab.grid(row=6, padx=20, pady=8, sticky='w')

        dept_lab = Label(lft_fr, text="Department", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        dept_lab.grid(row=7, padx=20, pady=8, sticky='w')
        
        date_lab = Label(lft_fr, text="D.O.B", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        date_lab.grid(row=8, padx=20, pady=8, sticky='w')

        address_lab = Label(lft_fr, text="Address", bg="#a0b3f0", fg="#171819", font=("minion pro", 12))
        address_lab.grid(row=9, padx=20, pady=8, sticky='w')
        
            #------- Information labels & button ---------
        self.reg = StringVar
        self.name = StringVar
        self.aadhaar = StringVar
        self.contact = StringVar
        self.email = StringVar
        self.gender = StringVar
        self.date = StringVar
        self.dept = StringVar
        self.aadh = StringVar

                #------- Information Entry & combo boxes ---------  
        self.reg_ent = Entry(lft_fr, textvariable=self.reg,  font=("minion pro", 14), fg="#000822", highlightcolor="#0038ee", highlightthickness=1)
        self.reg_ent.grid(row=1, column=1, padx=10, sticky='w')

        self.name_ent = Entry(lft_fr, textvariable=self.name,  font=("minion pro", 14), fg="#000822", highlightcolor="#0038ee", highlightthickness=1)
        self.name_ent.grid(row=2,  column=1, padx=10, sticky='w')

        self.gend_ent = ttk.Combobox(lft_fr,textvariable=self.gender, state="readonly",font=("minion pro", 13), width=23)
        self.gend_ent['values']=['--- Select ---','Male', 'Female', 'Other']
        self.gend_ent.current(0)
        self.gend_ent.grid(row=3,column=1,padx=10,sticky='w')

        self.con_ent = Entry(lft_fr, textvariable=self.contact,  font=("minion pro", 14), fg="#000822", highlightcolor="#0038ee", highlightthickness=1)
        self.con_ent.grid(row=4,  column=1, padx=10, sticky='w')       

        self.aadh_ent = Entry(lft_fr, textvariable=self.aadhaar,  font=("minion pro", 14), fg="#000822", highlightcolor="#0038ee", highlightthickness=1)
        self.aadh_ent.grid(row=5,  column=1, padx=10, sticky='w')       

        self.email_ent = Entry(lft_fr, textvariable=self.email,  font=("minion pro", 14), fg="#000822", highlightcolor="#0038ee", highlightthickness=1)
        self.email_ent.grid(row=6,  column=1, padx=10, sticky='w')

        self.dept_ent = ttk.Combobox(lft_fr, textvariable=self.dept, state="readonly", width=23,font=("minion pro", 13))
        self.dept_ent['values']=['--- Select ---','CSE','IT','AUTO','MECH','FT','ECE','EEE','EIE','AGRI','CHEMICAL','MCT','CIVIL','BME','AERO','AI & ML']
        self.dept_ent.current(0)
        self.dept_ent.grid(row=7,  column=1, padx=10,sticky='w')  

        self.dob = DateEntry(lft_fr, font=("minion pro", 12), width=18)
        self.dob.grid(row=8, column=1, padx=10,sticky='w')
 
        self.address_ent = Text(lft_fr,font=("minion pro", 14), fg="#000822", highlightcolor="#0038ee", highlightthickness=1, width=20,height=2.5)
        self.address_ent.grid(row=9,  column=1, padx=10,pady=5,sticky='w')  

                #------- Information buttons ---------
        btn_fr = Frame(lft_fr, bg="#a0b3f0") 
        btn_fr.grid(row=10, columnspan=4,padx=30, pady=30)

                #------- Details management ----------            
        add_btn = Button(btn_fr, text="ADD", bg="#001a6f", fg="#eef2ff", width=8,height=1, font=("consolas", 12, 'bold'), command=self.add_detail)
        add_btn.grid(row=0,column=0, padx=5)

        update_btn = Button(btn_fr, text="UPDATE", bg="#0038ee", fg="#eef2ff", width=8,height=1, font=("consolas", 12, 'bold'), command=self.update_detail)
        update_btn.grid(row=0, column=1, padx=5)

        clear_btn = Button(btn_fr, text="CLEAR", bg="#001a6f", fg="#eef2ff", width=8,height=1, font=("consolas", 12, 'bold'), command = self.clear_details)
        clear_btn.grid(row=0, column=2, padx=5)

        del_btn = Button(btn_fr, text="DELETE", bg="#0038ee", fg="#eef2ff", width=8,height=1, font=("consolas", 12, 'bold'), command=self.delete_detail)
        del_btn.grid(row=0, column=3,padx=5)

        #------- Right frame ---------
        rgt_fr = Frame(self.root, bg="#a0b3f0")
        rgt_fr.place(x=550, y=100, width=700, height=560)

                #------- search frame --------
        srh_fr = Frame(rgt_fr,bg="#a0b3f0")
        srh_fr.grid(row=1,columnspan=4, padx=10, pady=10)

                #------- Labels ---------
        search_lab = Label(srh_fr, text="Search By", bg="#a0b3f0", fg="#0038ee", font=("consolas",14,'bold'))
        search_lab.grid(row=0,column=0,sticky='w',padx=10)

        srh_opt = ttk.Combobox(srh_fr, state='readonly', font=('minion pro',12), justify=CENTER)
        srh_opt['values']=['Register No']
        srh_opt.current(0)
        srh_opt.grid(row=1,padx=5,sticky='w')

        self.srh_ent = Entry(srh_fr, fg="#000822", font=('consolas',12), highlightcolor="#0038ee", highlightthickness=1)
        self.srh_ent.grid(row=1,column=1, padx=5)

        srh_btn = Button(srh_fr, text="Show", bg="#0038ee", fg="#eef2ff", font=('consolas',12,'bold'),width=10, command = self.search)
        srh_btn.grid(row=1,column=2, padx=10)

        srh_all_btn = Button(srh_fr, text="Show All", bg="#0038ee", fg="#eef2ff", font=('consolas',12,'bold'),width=10, command=self.fech_data)
        srh_all_btn.grid(row=1,column=3, padx=10)
        
        #============Treeview frame ======================
        table_fr = Frame(rgt_fr, bg="white")
        table_fr.place(x=20, y=100, height=450, width=660)
        
        scroll_x = Scrollbar(table_fr, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_fr, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_fr, columns=("Reg.no","Name","Gender","Contact","AADHAAR","Email","Dept","D.O.B","Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Reg.no",text="Reg.no")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("AADHAAR",text="AADHAAR")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Dept",text="Dept")
        self.student_table.heading("D.O.B",text="D.O.B")
        self.student_table.heading("Address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("Reg.no",width=100)
        self.student_table.column("Name",width=200)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("AADHAAR",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Dept",width=100)
        self.student_table.column("D.O.B",width=100)
        self.student_table.column("Address",width=350)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cur)
        
        # Connecting to the Database where all information will be stored
        self.connector = sqlite3.connect('Studentdatabase.db')
        self.cursor = self.connector.cursor()
        
        self.connector.execute(
        "CREATE TABLE IF NOT EXISTS STUDENT (REGISTER_NO TEXT PRIMARY KEY, NAME_ST TEXT, GENDER TEXT, PHONE_NO TEXT, AADHAAR TEXT,EMAIL TEXT,DEPT TEXT, DOB TEXT, _ADDRESS TEXT)"
        )
        self.fech_data()
        
        #-----------function for add a details in database----------------
    def add_detail(self):
        
        self.Reg = self.reg_ent.get()
        self.Name = self.name_ent.get()
        self.Gender = self.gend_ent.get()
        self.Contact = self.con_ent.get()
        self.Aadhaar = self.aadh_ent.get()
        self.Email = self.email_ent.get()
        self.Dept = self.dept_ent.get()
        self.Dob = self.dob.get_date()
        self.Address = self.address_ent.get("1.0","end")
        
        if self.reg_ent.get()=='':
                messagebox.showerror("ERROR", "Register number is mantatory")
        else:
                try:
                        self.connector.execute(
                        'INSERT INTO STUDENT (REGISTER_NO, NAME_ST, GENDER, PHONE_NO, AADHAAR, EMAIL, DEPT, DOB, _ADDRESS) VALUES (?,?,?,?,?,?,?,?,?)', 
                        (self.Reg, self.Name, self.Gender,self.Contact, self.Aadhaar, self.Email, self.Dept, self.Dob, self.Address)
                        )
                        self.fech_data()
                        self.clear_details()
                        self.connector.commit()
                except:
                        messagebox.showerror("ERROR !!!!","You May Enter Wrong Data")

        #-----------function for update a details in database----------------
    def update_detail(self):
            
        self.Reg = self.reg_ent.get()
        self.Name = self.name_ent.get()
        self.Gender = self.gend_ent.get()
        self.Contact = self.con_ent.get()
        self.Aadhaar = self.aadh_ent.get()
        self.Email = self.email_ent.get()
        self.Dept = self.dept_ent.get()
        self.Dob = self.dob.get_date()
        self.Address = self.address_ent.get("1.0","end")
        
        if self.reg_ent.get()=='':
                messagebox.showerror("ERROR", "Register number is mantatory")
        else:
                try:
                        self.connector.execute(
                        'UPDATE STUDENT SET NAME_ST=?, GENDER=?, PHONE_NO=?, AADHAAR=?, EMAIL=?, DEPT=?, DOB=?, _ADDRESS=? WHERE REGISTER_NO=?',
                        (self.Name, self.Gender,self.Contact, self.Aadhaar, self.Email, self.Dept, self.Dob, self.Address, self.Reg)
                        )
                        self.connector.commit()
                        self.fech_data()
                        self.clear_details()
                        messagebox.showinfo("Update","Data Update suscessful")
                except:
                        messagebox.showerror("ERROR !!!!","You May Enter Wrong Data")

        #-----------function for display a details in window----------------
    def fech_data(self):
             
        self.cursor.execute("SELECT * from STUDENT")
        self.row = self.cursor.fetchall()
             
        if len(self.row)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for rows in self.row:
                     self.student_table.insert('',END,values=rows)
                self.connector.commit()
        
        #-----------function for clear a details in entry boxes----------------
    def clear_details(self):
        
        today = date.today()
        opt = self.dept_ent['values']
        opt1 = self.gend_ent['values']
        self.reg_ent.delete(0,"end")
        self.name_ent.delete(0,"end")
        self.con_ent.delete(0,"end")
        self.aadh_ent.delete(0,"end")
        self.email_ent.delete(0,"end")
        self.address_ent.delete(1.0,END)
        self.dept_ent.set(opt[0])
        self.gend_ent.set(opt1[0])
        self.dob.set_date(today)

        #-----------function for select a details in window----------------
    def get_cur(self,ev):
        
        Cursor_row  = self.student_table.focus()
        contents = self.student_table.item(Cursor_row)
        row = contents['values']
        #Clear the entry filed before set
        self.reg_ent.delete(0,"end")
        self.name_ent.delete(0,"end")
        self.con_ent.delete(0,"end")
        self.aadh_ent.delete(0,"end")
        self.email_ent.delete(0,"end")
        self.address_ent.delete(1.0,END)
        
        #insert the values into entry filed
        self.reg_ent.insert(END, row[0])
        self.name_ent.insert(END, row[1])
        self.gend_ent.set(row[2])
        self.con_ent.insert(END, row[3])
        self.aadh_ent.insert(END, row[4])
        self.email_ent.insert(END, row[5])
        self.dept_ent.set(row[6])
        self.dob._set_text(row[7])
        self.address_ent.insert(END,row[8])
    
    #-----------function for delete a details in window----------------    
    def delete_detail(self):
        
        self.Reg = self.reg_ent.get()
        self.connector.execute('DELETE FROM STUDENT WHERE REGISTER_NO=?', (self.Reg,))
        self.connector.commit()
        self.fech_data()
        self.clear_details()
    
    #-----------function for search a details in window----------------    
    def search(self):

        self.cursor.execute("SELECT * from STUDENT WHERE REGISTER_NO=?", (self.srh_ent.get(),))
        self.row = self.cursor.fetchall()
             
        if len(self.row)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for rows in self.row:
                     self.student_table.insert('',END,values=rows)
                self.connector.commit()
        self.srh_ent.delete(0,END)
        
#Object and window define area
log_root = Tk()
obj = register(log_root)
log_root.mainloop()