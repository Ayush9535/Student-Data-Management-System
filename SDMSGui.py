from tkinter import *
from tkinter import messagebox as mg
import mysql.connector
import csv    

#--------------------------------------------------------------------------------------------------------------------------------------
#                                                          USER DEFINED FUNCTIONS
#--------------------------------------------------------------------------------------------------------------------------------------

def export():
    q = 'select * from stud_data_1'
    cursor.execute(q)
    data = cursor.fetchall()
    with open('Student Data.csv' , 'w' , newline='') as f:
        writer = csv.writer(f)
        list_1 = ['RollNo','StudentName' , 'Class' , 'Div' , 'DOB' , 'MotherName' , 'FatherName' , 'Address' , 'ContactNo' , 
        'Father_Occupation' , 'Nationality' , 'Religion']
        writer.writerow(list_1)
        for i in data:
            writer.writerow(i)
        mg.showinfo('Done' , 'Your Data is exported in excel file named STUDENT DATA. Kindly open it in Excel..!!')    

def update_2():
    res = mg.askyesno('Warning' , 'Are you sure you want to update the data..?')
    if res == True:
        q = "update stud_data_1 set StudentName = '{}' where RollNo = {}".format(E1.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set Class = {} where RollNo = {}".format(E2.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set Division = '{}' where RollNo = {}".format(E3.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set DOB = '{}' where RollNo = {}".format(E4.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set MotherName = '{}' where RollNo = {}".format(E5.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set FatherName = '{}' where RollNo = {}".format(E6.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set Address = '{}' where RollNo = {}".format(E7.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set ContactNo = '{}' where RollNo = {}".format(E8.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set Father_Occupation = '{}' where RollNo = {}".format(E9.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set Nationality = '{}' where RollNo = {}".format(E10.get() , rn)
        cursor.execute(q)
        q = "update stud_data_1 set Religion = '{}' where RollNo = {}".format(E11.get() , rn)
        cursor.execute(q)
        conn.commit()
        mg.showinfo('Success' , 'Data Updated Successfully..!!')

def Add():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11

    Query = "select * from stud_data_1"
    cursor.execute(Query)
    data = cursor.fetchall()
    if data == []:
        roll_no = 1
    else:
        a = 1
        leng = len(data)
        for i in data:   
            if a == leng:
                old_rollno = i[0]
                roll_no = old_rollno + 1    
            elif a != leng:
                a += 1

    Query = "Insert into stud_data_1 values ({} , '{}' , {} , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}')".format(roll_no,e1.get(),e2.get(),e3.get(),e4.get()
    ,e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get())
    try:
        cursor.execute(Query)
        conn.commit()
        e1.delete(0  , 'end')
        e2.delete(0  , 'end')
        e3.delete(0  , 'end')
        e4.delete(0  , 'end')
        e5.delete(0  , 'end')
        e6.delete(0  , 'end')
        e7.delete(0  , 'end')
        e8.delete(0  , 'end')
        e9.delete(0  , 'end')
        e10.delete(0  , 'end')
        e11.delete(0  , 'end')
        mg.showinfo('Successful' , f'Data added successfully as ROLL NO = {roll_no}')
    except:
        mg.showinfo('Error' , 'Please enter all details..!!')     

def Update():
    global E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,rn
    l1 = []
    q = 'select * from stud_data_1'
    cursor.execute(q)
    data = cursor.fetchall()
    for i in data:
        l1.append(i[0])    

    rn = up_2.get()
    if rn == '':
        mg.showinfo('error' , 'Please Enter Roll No..!!')
    elif int(rn) not in l1:
        mg.showinfo('Error' , 'Data related to this roll no not found..!!')
    else:
        a = l1.index(int(rn))    
        for widget in f3.winfo_children():
            widget.destroy()
        Label(f3 , text='Update Information' , font='Calibre 20 bold underline' , bg='gold').grid(padx=570, row=0 , column=0, columnspan=4)
        name_1 = Label(f3 , text='Student Name : ' , font='comicsans 16' , bg='gold') 
        name_1.grid(row = 1,pady=(60,30) , padx=(90,20))
        E1 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E1.grid(row=1 , column=1 , padx=(50,100),pady=(60,30))
        E1.insert(0 , data[a][1])

        class_1 = Label(f3 , text='Class : ' , font='comicsans 16' , bg='gold')
        class_1.grid(row=1 , column=2 , padx=20,pady=(60,30))
        E2 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E2.grid(row=1 , column=3,padx=(20,100),pady=(60,30))
        E2.insert(0 , data[a][2])
        
        div = Label(f3 , text='Div : ' , font='comicsans 16' , bg='gold')
        div.grid(row=2 , column=0 , pady=30 , padx=(90,20))
        E3 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E3.grid(row=2 , column=1 , padx=(50,100))
        E3.insert(0 , data[a][3])
        
        dob = Label(f3 , text='Date of Birth : ' , font='comicsans 16' , bg='gold')
        dob.grid(row=2 , column=2 , pady=30 , padx=20)
        E4 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E4.grid(row=2 , column=3,padx=(20,100))
        E4.insert(0 , data[a][4])
        
        mom_name = Label(f3 , text='Mothers Name : ' , font='comicsans 16' , bg='gold')
        mom_name.grid(row=3 , column=0 , pady=30 , padx=(90,20))
        E5 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E5.grid(row=3 , column=1 , padx=(50,100))
        E5.insert(0 , data[a][5])
        
        fat_name = Label(f3 , text='Fathers Name : ' , font='comicsans 16' , bg='gold')
        fat_name.grid(row=3 , column=2 , pady=30 , padx=20)
        E6 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E6.grid(row=3 , column=3,padx=(20,100))  
        E6.insert(0 , data[a][6])
        
        address = Label(f3 , text='Address : ' , font='comicsans 16' , bg='gold')
        address.grid(row=4 , column=0 , pady=30 , padx=(90,20))
        E7 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ',width=20)
        E7.grid(row=4 , column=1 ,columnspan=3,sticky='ew' , padx=(50,100))
        E7.insert(0 , data[a][7])
        
        con_no = Label(f3 , text='Contact No : ' , font='comicsans 16' , bg='gold')
        con_no.grid(row=5 , column=0 , pady=30 , padx=(90,20))
        E8 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E8.grid(row=5 , column=1 , padx=(50,100))
        E8.insert(0 , data[a][8])
        
        ten_std_per = Label(f3 , text='Father Occupation : ' , font='comicsans 16' , bg='gold')
        ten_std_per.grid(row=5 , column=2 , pady=30 , padx=20)
        E9 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E9.grid(row=5 , column=3,padx=(20,100))
        E9.insert(0 , data[a][9])
        
        board = Label(f3 , text='Nationality : ' , font='comicsans 16' , bg='gold')
        board.grid(row=6 , column=0 , pady=30 , padx=(90,20))
        E10= Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E10.grid(row=6 , column=1 , padx=(50,100))
        E10.insert(0 , data[a][10])
        
        stream = Label(f3 , text='Religion : ' , font='comicsans 16' , bg='gold')
        stream.grid(row=6 , column= 2, pady=30 , padx=20)
        E11= Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
        E11.grid(row=6 , column=3,padx=(20,100))
        E11.insert(0 , data[a][11])
        
        button_1 = Button(f3 , text = 'Update' , command=update_2 , width=25 , height=4 , bg='green' , activebackground='light green' , fg = 'white')
        button_1.grid(row=7 , column=3 , padx=(0 , 50))

def display_but():
    l=[]
    Query = "select * from stud_data_1"
    cursor.execute(Query)
    data = cursor.fetchall()
    for i in data:
        l.append(i[0])
        print(i)
    print(l)
    if wsearch_e.get() == '':
        mg.showinfo('Error' , 'Please Enter Roll No..!!')
    elif int(wsearch_e.get()) not in l:
        mg.showinfo('Error' , 'Data Related to this roll no is not found..!!')
    else:
        a = l.index(int(wsearch_e.get()))
        data2 = data[a]        
        Label(f3 , text='Roll No ' , font='Comicsans 16' , bg='gold').grid(row=3 , column=0)
        Label(f3 , text='Student Name ' , font='Comicsans 16' , bg='gold').grid(row=4 , column=0)
        Label(f3 , text='Class ' , font='Comicsans 16' , bg='gold').grid(row=5 , column=0)
        Label(f3 , text='Div ' , font='Comicsans 16' , bg='gold').grid(row=6 , column=0)
        Label(f3 , text='DOB ' , font='Comicsans 16' , bg='gold').grid(row=7 , column=0)
        Label(f3 , text="Mother's Name " , font='Comicsans 16' , bg='gold').grid(row=8 , column=0)
        Label(f3 , text="Father's Name " , font='Comicsans 16' , bg='gold').grid(row=9 , column=0)
        Label(f3 , text='Address ' , font='Comicsans 16' , bg='gold').grid(row=10 , column=0)
        Label(f3 , text='Contact No ' , font='Comicsans 16' , bg='gold').grid(row=11 , column=0)
        Label(f3 , text='Father Occupation ' , font='Comicsans 16' , bg='gold').grid(row=12 , column=0)
        Label(f3 , text='Nationality ' , font='Comicsans 16' , bg='gold').grid(row=13 , column=0)
        Label(f3 , text='Religion ' , font='Comicsans 16' , bg='gold').grid(row=14 , column=0)

        for j in range(1 , 13):
            Label(f3 , text=':' , font='Comicsans 16' , bg = 'gold').grid(row=j+2 , column=1 , padx = 50)
        for k in range(0 , 12):
            Label(f3 , text=data2[k] , font='Comicsans 16' , bg='gold', fg='green').grid(row=k+3, column=2)            
    conn.commit()

def del_but_1():
    l = []
    Q = 'select * from stud_data_1'
    cursor.execute(Q)
    Data = cursor.fetchall()
    for i in Data:
        l.append(i[0])

    roll_no = del_2.get()
    if roll_no == '':
        mg.showinfo('Error' , 'Please Enter Roll No..!!')
    elif int(roll_no) not in l:
        mg.showinfo('Error' , 'Data related to this Roll No not found..!!')
    else:        
        res = mg.askyesno('Warning' , 'Are you sure want to delete the data..?')
        if res == TRUE:
            query = 'delete from stud_data where RollNo = {}'.format(roll_no)
            cursor.execute(query)
            conn.commit()
            del_2.delete(0 , 'end')
            mg.showinfo('Done' , 'Data Deleted Successfully..!!')

def del_all():
    query = 'select * from stud_data_1'
    cursor.execute(query)
    data = cursor.fetchall()
    leng = len(data)
    if leng == 0:
        conn.commit()
        mg.showinfo('Done' , 'No Data Found..!! Table was empty..!!')
    else:
        res = mg.askyesno('Warning' , 'Are you sure you want to delete all data in your database..?')
        if res == True:
            for i in range(1 , leng+1):
                q2 = 'delete from stud_data_1 where RollNo = {}'.format(i)
                cursor.execute(q2)
            conn.commit()    
            mg.showinfo('Done' , 'Data Deleted Successfully..!!')

#-------------------------------------------------------------------------------------------------------------------------------------

def insert():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    for widget in f3.winfo_children():
        widget.destroy()
    Label(f3 , text='Insert Data' , font='Calibre 20 bold underline' , bg='gold').grid(row=0 , column=0, columnspan=4)

    name_1 = Label(f3 , text='Student Name : ' , font='comicsans 16' , bg='gold')
    name_1.grid(row = 1,pady=(60,30) , padx=(90,20))
    e1 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e1.grid(row=1 , column=1 , padx=(50,100),pady=(60,30))
    
    class_1 = Label(f3 , text='Class : ' , font='comicsans 16' , bg='gold')
    class_1.grid(row=1 , column=2 , padx=20,pady=(60,30))
    e2 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e2.grid(row=1 , column=3,padx=(20,100),pady=(60,30))

    div = Label(f3 , text='Div : ' , font='comicsans 16' , bg='gold')
    div.grid(row=2 , column=0 , pady=30 , padx=(90,20))
    e3 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e3.grid(row=2 , column=1 , padx=(50,100))
     
    dob = Label(f3 , text='Date of Birth : ' , font='comicsans 16' , bg='gold')
    dob.grid(row=2 , column=2 , pady=30 , padx=20)
    e4 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e4.grid(row=2 , column=3,padx=(20,100))

    mom_name = Label(f3 , text='Mothers Name : ' , font='comicsans 16' , bg='gold')
    mom_name.grid(row=3 , column=0 , pady=30 , padx=(90,20))
    e5 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e5.grid(row=3 , column=1 , padx=(50,100))

    fat_name = Label(f3 , text='Fathers Name : ' , font='comicsans 16' , bg='gold')
    fat_name.grid(row=3 , column=2 , pady=30 , padx=20)
    e6 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e6.grid(row=3 , column=3,padx=(20,100))  

    address = Label(f3 , text='Address : ' , font='comicsans 16' , bg='gold')
    address.grid(row=4 , column=0 , pady=30 , padx=(90,20))
    e7 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ',width=20)
    e7.grid(row=4 , column=1 ,columnspan=3,sticky='ew' , padx=(50,100))

    con_no = Label(f3 , text='Contact No : ' , font='comicsans 16' , bg='gold')
    con_no.grid(row=5 , column=0 , pady=30 , padx=(90,20))
    e8 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e8.grid(row=5 , column=1 , padx=(50,100))

    ten_std_per = Label(f3 , text='Father Occupation : ' , font='comicsans 16' , bg='gold')
    ten_std_per.grid(row=5 , column=2 , pady=30 , padx=20)
    e9 = Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e9.grid(row=5 , column=3,padx=(20,100))

    board = Label(f3 , text='Nationality : ' , font='comicsans 16' , bg='gold')
    board.grid(row=6 , column=0 , pady=30 , padx=(90,20))
    e10= Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e10.grid(row=6 , column=1 , padx=(50,100))

    stream = Label(f3 , text='Religion : ' , font='comicsans 16' , bg='gold')
    stream.grid(row=6 , column= 2, pady=30 , padx=20)
    e11= Entry(f3 , textvariable = StringVar, font = 'calibre 16 ')
    e11.grid(row=6 , column=3,padx=(20,100))

    button_1 = Button(f3 , text = 'Add' , command=Add , width=25 , height=4 , bg='green' , activebackground='light green' , fg='white')
    button_1.grid(row=7 , column=3 , padx=(0 , 50)) 

def display():
    global wsearch_e
    for widget in f3.winfo_children():
        widget.destroy()
    Label(f3 , text='Display Data' , font='Calibre 20 bold underline' , bg='gold').grid(row = 0 , column=0, columnspan=4 , padx=570)

    wsearch = Label(f3,  text='>> Enter the rollno of student whose data you want to see: ' , font='Comicsans 14' , bg='gold')
    wsearch.grid(row = 1, column = 0, columnspan=2 , padx= (200 , 0) , pady=(30 , 0))
    wsearch_e = Entry(f3 , textvariable=StringVar , font='Comicsans 14')
    wsearch_e.grid(row=1 , column=2 , pady=(30,0))
    but = Button(f3 , text='Display' , font='Comicsans 14' , command=display_but , bg='Blue' , activebackground='light blue' , fg='white')
    but.grid(row = 1 , column=3 , pady =(30,0))
    Label(f3 , text = 'DATA' , font='Calibre 20 bold underline' , bg = 'gold').grid(row = 2 , column=0, columnspan=4 , padx=570 , pady = 30)    

def update():
    global up_2
    for widget in f3.winfo_children():
        widget.destroy()
    Label(f3 , text='Update Information' , font='Calibre 20 bold underline' , bg='gold').grid(padx=570, row=0 , column=0, columnspan=4)    

    up_1 = Label(f3 , text='>> Enter rollno of student whose data you want to update :' , font='Comicsans 14' , bg='gold')
    up_1.grid(row = 1 , column=1 , columnspan=2,padx=150 , pady = (50,0))

    up_2 = Entry(f3 , textvariable=StringVar , font='Comicsans 14')
    up_2.grid(row = 2 , column = 1 , padx=100 , pady=(30,20))

    up_but = Button(f3 , text='Update' , font='Comicsans 14' , command=Update , bg='Blue' , activebackground='light blue' , fg='white')
    up_but.grid(row = 2 , column = 2)
    
def delete():
    global del_2
    for widget in f3.winfo_children():
        widget.destroy()
    Label(f3 , text='Delete Data' , font='Calibre 20 bold underline' , bg='gold').grid(row = 0 , column=0, columnspan=4 , padx=570)

    del_1 = Label(f3 , text='>> Enter rollno of student whose data you want to delete :' , font='Comicsans 14' , bg='gold')
    del_1.grid(row = 1 , column=1 , columnspan=2,padx=150 , pady = (50,0))

    del_2 = Entry(f3 , textvariable=StringVar , font='Comicsans 14')
    del_2.grid(row = 2 , column = 1 , padx=100 , pady=(30,20))

    del_but = Button(f3 , text='Delete' , font='Comicsans 14' , command=del_but_1 , bg='blue' , activebackground='light blue', fg = 'white')
    del_but.grid(row = 2 , column = 2)

    del_3 = Label(f3 , text='OR' , font='Comicsans 18' , bg='gold')
    del_3.grid(row = 3 , column=1 , padx=200 , pady = (50,130))

    del_but2 = Button(f3 , text='Delete All Data' , font='Comicsans 14' , command=del_all , bg='blue' , activebackground='light blue' ,fg = 'white')
    del_but2.grid(row = 4 , column = 1)

def dsub():
    for widget in f3.winfo_children():
        widget.destroy()
    Label(f3 , text='Display all Data' , font='Calibre 20 bold underline' , bg='gold').pack(side=TOP , anchor=N , padx=550)
    
    q = 'select * from stud_data_1'
    cursor.execute(q)
    data = cursor.fetchall()   
    for i in data:
        print(i)
        Label(f3 , text=i, font='Comicsans 16' , bg = 'gold' , fg = 'green').pack(side = TOP , anchor=N , pady=(30,0))

    Button(f3 , text='Export' , command=export , bg = 'Blue', fg = 'white' , activebackground='light blue', width=20 , height=2).pack(side=TOP , anchor='n' , pady=30)

def about():
    for widget in f3.winfo_children():
        widget.destroy()
    about_1 = Label(f3 , text = 'This is a Software made by a group of two begineer coders..!!' , font='comicsans 25' , bg='gold')
    about_1.pack(padx = (200,200) , pady = (100,50))
    about_2 = Label(f3 , text = 'Reason Behind making this self coded software was to complete our project..!!' , font='comicsans 25' , bg='gold')
    about_2.pack(padx = (100,100))
    about_3 = Label(f3 , text = 'This Software helps us to store data of new students\ntaking admission for jr college.' , font='comicsans 25' , bg='gold')
    about_3.pack(padx = (100,100) , pady = (50,50))
    about_4 = Label(f3 , text = 'Hope You love it..!!' , font='comicsans 25' , bg='gold')
    about_4.pack(padx = (200,200))

def Exit():
    res = mg.askyesno('Warning' , 'Are you sure you want to quit the application..??')
    if res == TRUE:
        root.destroy()    

def home():
    for widget in f3.winfo_children():
        widget.destroy()
    head_1 = Label(f3,text='Welcome\nto\n XYZ Jr. College',font='comicsans 35 bold underline' , bg='gold')
    head_1.pack(padx = 450,pady = (100,150))
    head_2 = Label(f3,text='Select different option from MenuBar to Proceed.',font='comicsans 25 bold',fg='red' , bg='gold')
    head_2.pack(padx=(275,250),pady = (0,30))
    db_info = Label(f3 , text=f'''Username : {u} \n Password : {p} \n Database : {d} \n Table : Stud_data_1''' , font='Comicsans 18' 
    , bg='gold')
    db_info.pack(padx=(275,250))

       
def hide():
    password_entry.config(show='*')
    show_but.config(text='Show')
    show_but.config(command=show)

def show():
    password_entry.config(show='')
    show_but.config(text='Hide')
    show_but.config(command=hide)

def select():
    global f2 , f3 , d
    d = v.get() 
    q = 'use {}'.format(d)
    cursor.execute(q)
    for widget in root.winfo_children():
        widget.destroy()
    root.state('zoomed')
    f1 = Frame(root , background='orange' , relief=SOLID , borderwidth=5)
    f1.pack(fill = X)
    l8 = Label(f1 , text='Student Data Records' , font='Comicsans 30 bold' , bg='orange')
    l8.pack(pady = 20)

    f2 = Frame(root , relief=SOLID , borderwidth=3 , bg='gold')
    f2.pack(fill = Y , side = LEFT,pady=25 , padx=10)
    b = Button(f2 , width = 25 , height = 5 , text = 'Home' , command = home , bg='cyan')
    b.pack(side = TOP)
    b1 = Button(f2 , width = 25 , height = 5 , text = 'Insert Data' , command = insert, bg='cyan')
    b1.pack(side = TOP)
    b2 = Button(f2 , width = 25 , height = 5 , text = 'Display Data' , command = display, bg='cyan')
    b2.pack(side = TOP)
    b3 = Button(f2 , width = 25 , height = 5 , text = 'Update Data' , command = update, bg='cyan')
    b3.pack(side = TOP)
    b4 = Button(f2 , width = 25 , height = 5 , text = 'Delete Data' , command = delete, bg='cyan')
    b4.pack(side = TOP)
    b5 = Button(f2 , width = 25 , height = 5 , text = 'Display All Data' , command = dsub, bg='cyan')
    b5.pack(side = TOP)
    b6 = Button(f2 , width = 25 , height = 5 , text = 'About' , command = about, bg='cyan')
    b6.pack(side = TOP)
    b7 = Button(f2 , width = 25 , height = 5 , text = 'Exit' , command = Exit, bg='cyan')
    b7.pack(side = TOP)

    f3 = Frame(root , bg='gold')
    f3.pack(side = LEFT , fill=BOTH)

    head_1 = Label(f3,text='Welcome\nto\n XYZ Jr. College',font='comicsans 35 bold underline', bg='gold')
    head_1.pack(padx = 450,pady = (100,150))
    head_2 = Label(f3,text='Select different option from MenuBar to Proceed.',font='comicsans 25 bold',fg='red' , bg='gold')
    head_2.pack(padx=(275,250),pady = (0,30))
    db_info = Label(f3 , text=f'''Username : {u} \n Password : {p} \n Database : {d} \n Table : Stud_data_1''' , font='Comicsans 18' 
    , bg='gold')
    db_info.pack(padx=(275,250))

def connect():
    global v , conn , cursor , u , p
    u = username_entry.get()
    p = password_entry.get()
    conn = mysql.connector.connect(username=f'{u}' , password=f'{p}')
    if conn.is_connected():
        cursor = conn.cursor()
        q0 = 'show databases'
        cursor.execute(q0)
        databases = cursor.fetchall()
        options=[]
        for i in databases:
            options.append(i[0])

        for widget in Home_2.winfo_children():
            widget.destroy()

        connect_to_db = Label(Home_2 , text='Connect To Database' , font='forte 20 underline' , bg='yellow')
        connect_to_db.grid(row=0 , column=0 , columnspan=3 , padx=200 , pady=(50,40))
        aise = Label(Home_2 , text='Choose database from the list : ' , font='Comicsans 14' , bg='yellow')
        aise.grid(row=1 , column=0)
        v = StringVar()
        v.set('Select Database')
        drop = OptionMenu(Home_2 , v , *options)
        drop.grid(row=1 , column=2 , columnspan=3)
        sel_but = Button(Home_2 , text='Select' , font='Comicsans 14' , command=select)    
        sel_but.grid(row=2 , column=1 , pady=(30,60))       
#--------------------------------------------------------------------------------------------------------------------------------------
#                                                              MAIN PROGRAM
#--------------------------------------------------------------------------------------------------------------------------------------

root = Tk()
root.title('CS Project')
root.geometry('700x500')
root.resizable(False , False)
root.config(bg='gold')

Home = Frame(root , bg='gold')
Home.pack()
home_label_1 = Label(Home , text='Student Data Management System' , font='forte 26 underline' , bg='gold')
home_label_1.grid(row=0 , column=0 , columnspan=3 , pady=(50,50) , padx=50)

Home_2 = Frame(root , bg='yellow')
Home_2.pack(fill='both')

connect_to_sql = Label(Home_2 , text='Connect To SQL Server' , font='forte 20 underline' , bg='yellow')
connect_to_sql.grid(row=1 , column=0 , columnspan=3 , padx=200 , pady=(50,0))

E_username = Label(Home_2 , text='Enter Username : ' , font='Comicsans 14' , bg='yellow')
E_username.grid(row=2 , column=0 , padx=(70,30) , pady=(50,30))
username_entry = Entry(Home_2 , textvariable=StringVar , font='Calibre 14')
username_entry.grid(row=2 , column=1 , pady=(50,30))

E_password = Label(Home_2 , text='Enter Password : ' , font='Comicsans 14' , bg='yellow')
E_password.grid(row=3 , column=0 , padx=(70,30))
password_entry = Entry(Home_2 , textvariable=StringVar , font='Calibre 14' , show='*')
password_entry.grid(row=3 , column=1)
show_but = Button(Home_2 , text='Show' , font='Comicsans 14' , command=show)
show_but.grid(row=3 , column=2 , padx=30)

connect_but = Button(Home_2 , text='Connect' , font='Comicsans 14' , command=connect)
connect_but.grid(row=4 , column=1 , pady=(30,60))

root.mainloop()
