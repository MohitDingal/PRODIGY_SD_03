
from tkinter import *
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as tkMessageBox


def Database():
    global conn,cursor
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, EMAIL TEXT, CONTACT TEXT)")

def register():
    Database()
    fname1 = fname.get()
    lname1 = lname.get()
    email1 = email.get()
    contact1 = contact.get()
    # applying empty validation
    if fname1 == '' or lname1 == '' or email1 == '' or contact1 == '':
        tkMessageBox.showinfo("Warning", "Cannot accept empty fields")
    else:
        # execute query
        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,EMAIL,CONTACT) \
                 VALUES (?,?,?,?)', (fname1, lname1,email1, contact1));
        conn.commit()
        tkMessageBox.showinfo("Message", "Contact has been stored")
        # refresh table data
        conn.close()
def createpage():
    fname.set("")
    lname.set("")
    email.set("")
    contact.set("")
    create_contact = Frame(main_body)
    Label(create_contact,text = "Please add the Contact details",font =("Arial",20,"bold"),fg = "black").grid(row = 0,column=0,columnspan =2,sticky = "news",padx = 10,pady = 10)
    Label(create_contact, text="First Name  ", font=("Arial", 12,"bold"),  fg="black").grid(row =1,column=0,padx=10,pady=10,sticky = "news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=fname).grid(row = 1,column =1,padx=10,pady=10,sticky = "news")
    Label(create_contact, text="Last Name ", font=("Arial", 12,"bold"),  fg="black").grid(row = 2,column =0,padx=10,pady=10,sticky = "news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=lname).grid(row = 2,column =1,padx=10,pady=10,sticky = "news")
    Label(create_contact, text="Email ", font=("Arial", 12,"bold"),  fg="black").grid(row = 3,column =0,padx=10,pady=10,sticky = "news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=email).grid(row = 3,column =1,padx=10,pady=10,sticky = "news")
    Label(create_contact, text="Contact ", font=("Arial", 12,"bold"), fg="black").grid(row = 4,column =0,padx=10,pady=10,sticky = "news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=contact).grid(row = 4,column =1,padx=10,pady=10,sticky = "news")
    Button(create_contact, text="Submit", font=("Arial", 12, "bold"), command=register, bg="blue", fg="white").grid(row = 5,column =0,columnspan =2,padx=10,pady=10,sticky = "news")
    create_contact.pack()
def DisplayData():
    scrollbarx = Scrollbar(main_body, orient=HORIZONTAL)
    scrollbary = Scrollbar(main_body, orient=VERTICAL)
    tree = ttk.Treeview(main_body, columns=("Student Id", "First Name", "Last Name", "Email", "Contact"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # setting headings for the columns
    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('First Name', text="FirstName", anchor=W)
    tree.heading('Last Name', text="LastName", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    # setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    # open database
    Database()
    # clear current data
    tree.delete(*tree.get_children())
    # select query
    cursor = conn.execute("SELECT * FROM REGISTRATION")
    # fetch all data from database
    fetch = cursor.fetchall()
    # loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))

    cursor.close()
    conn.close()



def updatepage():
    create_contact = Frame(main_body)
    Label(create_contact, text="First Name  ", font=("Arial", 12, "bold"), fg="black").grid(row=0, column=0, padx=10,
                                                                                            pady=10, sticky="news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=fname).grid(row=0, column=1, padx=10, pady=10,
                                                                               sticky="news")
    Label(create_contact, text="Last Name ", font=("Arial", 12, "bold"), fg="black").grid(row=1, column=0, padx=10,
                                                                                          pady=10, sticky="news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=lname).grid(row=1, column=1, padx=10, pady=10,
                                                                               sticky="news")
    Label(create_contact, text="Email ", font=("Arial", 12, "bold"), fg="black").grid(row=2, column=0, padx=10, pady=10,
                                                                                      sticky="news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=email).grid(row=2, column=1, padx=10, pady=10,
                                                                               sticky="news")
    Label(create_contact, text="Contact ", font=("Arial", 12, "bold"), fg="black").grid(row=3, column=0, padx=10,
                                                                                        pady=10, sticky="news")
    Entry(create_contact, font=("Arial", 12, "bold"), textvariable=contact).grid(row=3, column=1, padx=10, pady=10,
                                                                                 sticky="news")
    Button(create_contact, text="Update", font=("Arial", 12, "bold"), command=lambda:update(tree), bg="blue", fg="white").grid(
        row=4, column=0, columnspan=2, padx=10, pady=10, sticky="news")

    selectitem = Button(create_contact,text = "Select item",font=("Arial", 12, "bold"),command = lambda:selector(tree),bg="red", fg="white")
    selectitem.grid(row=5,column=0,columnspan = 2,padx=10,pady=10,sticky = "news")
    create_contact.pack()
    fname.set("")
    lname.set("")
    email.set("")
    contact.set("")
    show_date = Frame(main_body)
    scrollbarx = Scrollbar(show_date, orient=HORIZONTAL)
    scrollbary = Scrollbar(show_date, orient=VERTICAL)
    tree = ttk.Treeview(show_date, columns=("Student Id", "First Name", "Last Name", "Email", "Contact"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # setting headings for the columns
    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('First Name', text="FirstName", anchor=W)
    tree.heading('Last Name', text="LastName", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    # setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()

    # open database
    Database()
    # clear current data
    tree.delete(*tree.get_children())
    # select query
    cursor = conn.execute("SELECT * FROM REGISTRATION")
    # fetch all data from database
    fetch = cursor.fetchall()
    # loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))

    show_date.pack()
    cursor.close()
    conn.close()

def selector(tree):
    selected_item = tree.focus()
    details = tree.item(selected_item)
    contacts = details['values']
    fname.set(contacts[1])
    lname.set(contacts[2])
    email.set(contacts[3])
    contact.set(contacts[4])
def update(tree):
    Database()
    # getting form data
    fname1 = fname.get()
    lname1 = lname.get()

    email1 = email.get()
    contact1 = contact.get()
    # applying empty validation
    if fname1 == '' or lname1 == ''  or email1 == '' or contact1 == '':
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:
        # getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        # update query
        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,EMAIL=?,CONTACT=? WHERE RID = ?',
                     (fname1, lname1, email1, contact1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message", "Updated successfully")
        # reset form
        # refresh table data
        conn.close()
def deletepage():
    create_contact = Frame(main_body)
    create_contact.pack(fill=BOTH, expand=True)
    selectitem = Button(create_contact, text="Delete Selected Item", command=lambda: deletor(tree),fg = "white",bg = "blue",font = ("Arial bold",12))
    selectitem.pack(padx=10,pady =10)
    scrollbarx = Scrollbar(create_contact, orient=HORIZONTAL)
    scrollbary = Scrollbar(create_contact, orient=VERTICAL)
    tree = ttk.Treeview(create_contact, columns=("Student Id", "First Name", "Last Name", "Email", "Contact"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # setting headings for the columns
    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('First Name', text="FirstName", anchor=W)
    tree.heading('Last Name', text="LastName", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    # setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()

    # open database
    Database()
    # clear current data
    tree.delete(*tree.get_children())
    # select query
    cursor = conn.execute("SELECT * FROM REGISTRATION")
    # fetch all data from database
    fetch = cursor.fetchall()
    # loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))

    cursor.close()
    conn.close()

def deletor(tree):
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
def switch(indicator,page):
    for child in menu_slider.winfo_children():
        if isinstance(child,Label):
            child["bg"] = "SystemButtonFace"
    indicator["bg"] = "red"

    for x in main_body.winfo_children():
        x.destroy()
        # root.update()
    page()




def master():
    global root

    global SEARCH
    global fname, lname, email, contact
    root = Tk()
    root.geometry("1000x600")
    root.title("Contact Manager")
    global menu_slider
    menu_slider = Frame(root)
    menu_slider.pack(padx = 5,pady = 5)
    menu_slider.pack_propagate(False)
    menu_slider.configure(height=45,width=1000)


    create_contact_indicator = Label(menu_slider,bg = "red")
    create_contact_indicator.place(y = 40,x=10,width =230,height = 2)
    create_contact_button = Button(menu_slider,text = "Create",font = ("Arial",13,"bold"),bd = 0, fg ="red",activebackground="red",command = lambda: switch(indicator = create_contact_indicator,page = createpage))
    create_contact_button.place(y = 0,x=0,width = 250, height = 40)

    all_button = Button(menu_slider,text = "All",font = ("Arial",13,"bold"),bd = 0, fg ="red",activebackground="red",command = lambda: switch(indicator = all_indicator,page = DisplayData))
    all_button.place(y = 0,x=250,width = 250, height = 40)
    all_indicator = Label(menu_slider)
    all_indicator.place(y = 40,x=260,width =230,height = 2)

    edit_button = Button(menu_slider,text = "Edit",font = ("Arial",13,"bold"),bd = 0, fg ="red",activebackground="red",command = lambda: switch(indicator = edit_indicator,page = updatepage))
    edit_button.place(y = 0,x=500,width = 250, height = 40)
    edit_indicator = Label(menu_slider)
    edit_indicator.place(y = 40,x=510,width =230,height = 2)

    delete_button = Button(menu_slider,text = "Delete",font = ("Arial",13,"bold"),bd = 0, fg ="red",activebackground="red",command = lambda: switch(indicator = delete_indicator,page = deletepage))
    delete_button.place(y = 0,x=750,width = 250, height = 40)
    delete_indicator = Label(menu_slider)
    delete_indicator.place(y = 40,x=760,width =230,height = 2)
    global main_body
    main_body = Frame(root,bg = "grey")

    main_body.pack(fill = BOTH,expand = True,padx = 5,pady = 5)

    # SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    email = StringVar()
    contact = StringVar()




master()

if __name__=='__main__':
    mainloop()