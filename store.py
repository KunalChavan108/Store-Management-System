from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Store:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Management System")
        self.root.geometry("1580x800+0+0")

        self.Nameofunit = StringVar()
        self.numberofunits = StringVar()
        self.buyingprice = StringVar()
        self.sellingprice = StringVar()
        self.profit = StringVar()
        
        
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="STORE MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        

        #==============DataFrame=============
        Dataframe = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("Arial", 12, "bold"), text="Units Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("Arial", 12, "bold"), text="Sales Information")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        #=================ButtonsFrame===========================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        #=================DetailsFrame==========================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        #=================DataframeLeft=========================
        lblNametablet = Label(DataframeLeft, text="Name of Unit", font=("times new roman", 16, "bold"), padx=2, pady=6)
        lblNametablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameofunit, state="readonly", font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"] = ("Sugar", "Rice", "Wheat", "Dal", "Oil")
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Number of Unit:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.numberofunits, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Buying price:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.buyingprice, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="Selling price:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.sellingprice, width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Profit:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.profit, width=35)
        txtLot.grid(row=4, column=1)

        

        #===================DataframeRight============================
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #====================Buttons====================================
        btnPresciption = Button(Buttonframe, command=self.iPrescription, text="Sales Data", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnPresciption.grid(row=0, column=0)

        btnPresciptionData = Button(Buttonframe, command=self.iPrescriptionData,text="Save", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6, )
        btnPresciptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,command=self.update_data,text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,command=self.idelete, text="Delete", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,command=self.clear, text="Clear", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        
        btnExit = Button(Buttonframe,command=self.iExit,text="Exit", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        btngraph = Button(Buttonframe, command=self.storedata, text="Analyse Profit", bg="blue", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btngraph.grid(row=0, column=6)

        
        #========================Table============================
        #========================Scrollbar========================

        

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("nameofunit", "numberofunit", "buyingprice", "sellingprice", "profit"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        
        self.hospital_table.heading("nameofunit", text="Name of Unit")
        self.hospital_table.heading("numberofunit", text="Number of Unit")
        self.hospital_table.heading("buyingprice", text="Buying Price")
        self.hospital_table.heading("sellingprice", text="Selling Price")
        self.hospital_table.heading("profit", text="Profit")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        # Adjusting column widths based on content
        self.hospital_table.column("nameofunit", width=100, anchor=CENTER, stretch=YES)
        self.hospital_table.column("numberofunit", width=100, anchor=CENTER, stretch=YES)
        self.hospital_table.column("buyingprice", width=100, anchor=CENTER, stretch=YES)
        self.hospital_table.column("sellingprice", width=100, anchor=CENTER, stretch=YES)
        self.hospital_table.column("profit", width=100, anchor=CENTER, stretch=YES)

        # Fetch and display data
        self.fetch_data()

        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        
    #=========================Functionality Declaration=====================
    def iPrescriptionData(self):
        if self.Nameofunit.get() == "" or self.numberofunits.get() == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Oneeyedeagle@21", database="store")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO store (Nameofunit, numberofunits, buyingprice, sellingprice, profit) VALUES (%s, %s, %s, %s, %s)", (
                                                                                                                self.Nameofunit.get(),
                                                                                                                self.numberofunits.get(),
                                                                                                                self.buyingprice.get(),
                                                                                                                self.sellingprice.get(),
                                                                                                                self.profit.get()
                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record inserted")

    def update_data(self):
        if self.Nameofunit.get() == "":
            messagebox.showerror("Error", "Name of Unit is required for updating")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Oneeyedeagle@21", database="store")
            my_cursor = conn.cursor()
            
            sql_update_query = """UPDATE store SET 
                numberofunits = %s,
                buyingprice = %s,
                sellingprice = %s,
                profit = %s
                WHERE Nameofunit = %s"""
            
            data_tuple = (
                self.numberofunits.get(),
                self.buyingprice.get(),
                self.sellingprice.get(),
                self.profit.get(),
                self.Nameofunit.get()
            )

            my_cursor.execute(sql_update_query, data_tuple)
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Record has been updated")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Oneeyedeagle@21", database="store")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM store")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                self.hospital_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
    
        if row is not None:
            self.Nameofunit.set(row[0])
            self.numberofunits.set(row[1])
            self.buyingprice.set(row[2])
            self.sellingprice.set(row[3])
            self.profit.set(row[4])

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Units:\t\t\t" + self.Nameofunit.get() + "\n")
        self.txtPrescription.insert(END, "Number of Units:\t\t\t" + self.numberofunits.get() + "\n")
        self.txtPrescription.insert(END, "Buying price:\t\t\t" + self.buyingprice.get() + "\n")
        self.txtPrescription.insert(END, "Selling price:\t\t\t" + self.sellingprice.get() + "\n")
        self.txtPrescription.insert(END, "Profit:\t\t\t" + self.profit.get() + "\n")
    
    def idelete(self):
        if self.Nameofunit.get() == "":
            messagebox.showerror("Error", "Name of Unit is required for deletion")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Oneeyedeagle@21", database="store")
            my_cursor = conn.cursor()
            query = "DELETE FROM store WHERE Nameofunit = %s"
            value = (self.Nameofunit.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Delete", "Record has been deleted successfully")

    def clear(self):
        self.Nameofunit.set("")
        self.numberofunits.set("")
        self.buyingprice.set("")
        self.sellingprice.set("")
        self.profit.set("")
        
        self.txtPrescription.delete("1.0", END)
        
    def iExit(self):
        iExit = messagebox.askyesno("Store Management System", "Confirm you want to exit")
        if iExit > 0:
            root.destroy()

    def storedata(self):
        import storedata


root = Tk()
ob = Store(root)
root.mainloop()
