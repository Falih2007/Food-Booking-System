import mysql.connector as mycon
import tkinter as tk
import ttkbootstrap as tb
import os
import sys
from tkinter import ttk
from tkinter import * # type: ignore
from datetime import datetime
from ttkbootstrap.constants import * #type: ignore
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap import Style
import winsound


# Set an attribute to Image.CUBIC for compatibility with PIL
from PIL import Image
Image.CUBIC = Image.BICUBIC # type: ignore


# Establish connection to MySQL database
con = mycon.connect(host='localhost', user='root', passwd='ghouse@1974', database='project')


# Check if connection is successful
if con.is_connected():
    print('Connected to MySQL')
    cursor = con.cursor()  # Create cursor object to interact with database
else:
    print('Error, connection not established')




# Create main window for the application
root = tk.Tk()
root.title("FOOD BOOKING")


# Create a Notebook (tabs container)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


# Create frames for each tab
customer_frame = ttk.Frame(notebook)
menu_frame=ttk.Frame(notebook)
employees_frame = ttk.Frame(notebook)
database_frame = ttk.Frame(notebook)


# Add frames to notebook with respective titles
notebook.add(customer_frame, text='Customer')
notebook.add(menu_frame, text='Menu')
notebook.add(employees_frame, text='Employees')
notebook.add(database_frame, text="Database")


def hide_label():
    placeorder_label.place_forget()  # This hides the label

def show_label():
    placeorder_label.place(x=60,y=100)  # This shows the label again

def clear_entries():
    c_name.delete(0,tk.END)
    c_address.delete(0,tk.END)
    c_phone_no.delete(0,tk.END)

def open_customer_entry():
    customername_label.grid(row=0, column=0, padx=10, pady=10)
    c_name.grid(row=0, column=1, padx=10, pady=10)
    customerphoneno_label.grid(row=1, column=0, padx=10, pady=10)
    c_phone_no.grid(row=1, column=1, padx=10, pady=10)
    customeraddress_label.grid(row=2, column=0, padx=10, pady=10)
    c_address.grid(row=2, column=1, padx=10, pady=10)
    confirm_button2.grid(row=6, column=0, columnspan=2)
    error_label.grid(row=5, column=0, columnspan=3)




def close_customer_entry():# TO CLOSE THE ENTRIES WHILE MENU IS OPENED
    c_name.grid_forget()
    c_phone_no.grid_forget()
    c_address.grid_forget()
    customername_label.grid_forget()
    customerphoneno_label.grid_forget()
    customeraddress_label.grid_forget()
    confirm_button2.grid_forget()
    error_label.grid_forget()


# Function to handle inserting customer details into the database
def get_customer_id():
    # Query the database for the latest customer_id
    cursor.execute('SELECT MAX(customer_id) FROM customers')
    result = cursor.fetchone()
    if result and result[0] is not None:#type:ignore
        return result[0]  #type:ignore
    else:
        return 1000  # Default value if no records exist
def customer_button():
    # Define SQL query to create customers table if not exists
    createquery = '''CREATE TABLE IF NOT EXISTS customers (
                        customer_id int(10),
                        customer_name VARCHAR(50),
                        address VARCHAR(100),
                        customer_phoneno INT(15),
                        date_of_order date,
                        time varchar(50),
                        BUTTER_CHICKEN FLOAT(5),
                        PIZZA FLOAT(5),
                        BURGER FLOAT(5),
                        GRILLED_CHICKEN_WRAP FLOAT(5),
                        TEA FLOAT(5),
                        COFFEE FLOAT(5),
                        CHOCOLATE_MILKSHAKE FLOAT(5),
                        WATERMELON_JUICE FLOAT(5),
                        ICE_CREAM FLOAT(5),
                        GULAB_JAMUN  FLOAT(5),
                        CHEESE_CAKE  FLOAT(5),
                        KUNAFA FLOAT(5)
                    )'''
    cursor.execute(createquery)  # Execute SQL query
   
    # Get customer details from entry widgets
    customer_name = c_name.get()
    address = c_address.get()
    cphone_no = c_phone_no.get()
   
    # Validate customer name, address, and phone number
    customer_name_check = len(customer_name) != 0 and customer_name.isalpha() and len(customer_name) > 2
    address_check = len(address) != 0 and (address.isalpha())
    cphone_no_check=len(cphone_no)!=0 and cphone_no.isdigit() and 9<=len(str(cphone_no)) <= 15
   
    # If all validations pass, proceed to insert customer details into the database
    if customer_name_check and address_check and cphone_no_check:
        close_customer_entry()


        ToastNotification(title='SUCCESS!!',message='WELCOME TO OUR RESTURANT!!',duration=4000,position=()).show_toast()


        check_query=f'''select * from customers'''
        cursor.execute(check_query)


        rs=cursor.fetchall()


        insertquery = f'''INSERT INTO customers(customer_id,customer_name, address, customer_phoneno) VALUES({get_customer_id()+1},'{customer_name}', '{address}', {int(cphone_no)})''' # type: ignore
        cursor.execute(insertquery)
        con.commit()  # Commit changes to the database
        confirm_button2.config(state=tk.DISABLED)
        menu_meter()  # Open confirmation window
        show_label()
    else:
        # Display specific error messages based on validation failures
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        if not customer_name_check:
            if len(customer_name) == 0:
                error_label.config(text='INVALID NAME: NO NAME DETECTED')
                ToolTip(confirm_button2, text='INVALID NAME: NO NAME DETECTED',bootstyle=(DANGER, INVERSE))
            elif not (len(customer_name) > 2):
                error_label.config(text='INVALID NAME: IMPROPER LENGTH')
                ToolTip(confirm_button2, text='INVALID NAME: IMPROPER LENGTH',bootstyle=(DANGER, INVERSE))
            elif not customer_name.isalpha():
                error_label.config(text='INVALID NAME: NUMBERS DETECTED')
                ToolTip(confirm_button2, text='INVALID NAME: NUMBERS DETECTED',bootstyle=(DANGER, INVERSE))
        elif not cphone_no_check:
            if len(cphone_no) == 0:
                error_label.config(text='INVALID PHONE NUMBER: NO NUMBERS DETECTED')
                ToolTip(confirm_button2, text='INVALID PHONE NUMBER: NO NUMBERS DETECTED',bootstyle=(DANGER, INVERSE))
            elif not(cphone_no.isdigit()):
                error_label.config(text='INVALID PHONE NUMBER: LETTERS DETECTED')
                ToolTip(confirm_button2,text='INVALID PHONE NUMBER: LETTERS DETECTED',bootstyle=(DANGER, INVERSE))
            elif not (9 <= len(str(cphone_no)) <= 15):
                error_label.config(text='INVALID PHONE NUMBER: IMPROPER NO OF DIGITS ')
                ToolTip(confirm_button2, text='INVALID PHONE NUMBER: IMPROPER NO OF DIGITS ',bootstyle=(DANGER, INVERSE))
        elif not address_check:
            if len(address) == 0:
                error_label.config(text='INVALID ADDRESS: NO ADDRESS DETECTED')
                ToolTip(confirm_button2, text='INVALID ADDRESS: NO ADDRESS DETECTED',bootstyle=(DANGER, INVERSE))
            elif not(address.isalpha()):
                error_label.config(text='INVALID ADDRESS: NUMBERS DETECTED')
                ToolTip(confirm_button2, text='INVALID ADDRESS: NUMBERS DETECTED',bootstyle=(DANGER, INVERSE))
        else:
            pass


# Label and Entry widgets for entering customer details
customername_label=tk.Label(customer_frame, text="NAME")
customername_label.grid(row=0, column=0, padx=10, pady=10)
c_name = ttk.Entry(customer_frame)
c_name.grid(row=0, column=1, padx=10, pady=10)


customerphoneno_label=tk.Label(customer_frame, text="PHONE")
customerphoneno_label.grid(row=1, column=0, padx=10, pady=10)
c_phone_no = ttk.Entry(customer_frame)
c_phone_no.grid(row=1, column=1, padx=10, pady=10)


customeraddress_label=tk.Label(customer_frame, text="ADDRESS")
customeraddress_label.grid(row=2, column=0, padx=10, pady=10)
c_address = ttk.Entry(customer_frame)
c_address.grid(row=2, column=1, padx=10, pady=10)


placeorder_label=tk.Label(customer_frame, text="PLACE YOUR ORDER",anchor=CENTER)
def set_default_values(a):
    # Set default values in Entry widgets
    a.delete(0, tk.END)  # Clear any existing text
    a.insert(0,'0')

# Function to display confirmation window with meter widgets
def int_check(a):
    if a=='' or a==' ':
        return 0
    else:
        return int(a)
    
def menu_meter():
    def order():
        def place_order():
            class ReceiptTab(tk.Frame):
                def __init__(self, parent):
                    super().__init__(parent)
                    self.parent = parent
                    self.style = Style(theme='minty')
                    self.create_widgets()

                def create_widgets(self):
                    self.grid(row=0, column=0, sticky="nsew")
                    self.parent.grid_rowconfigure(0, weight=1)
                    self.parent.grid_columnconfigure(0, weight=1)

                    # Creating a frame to hold the receipt information
                    receipt_frame = ttk.Frame(self)
                    receipt_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

                    # Creating a treeview widget to display receipt
                    self.tree = ttk.Treeview(receipt_frame, columns=('Item', 'Quantity','Size', 'Total Cost'), show='headings')
                    self.tree.heading('Item', text='Item')
                    self.tree.heading('Quantity', text='Quantity')
                    self.tree.heading('Size', text='Size')
                    self.tree.heading('Total Cost', text='Total Cost')
                    self.tree.column('Item', width=200)
                    self.tree.column('Quantity', width=100, anchor='center')
                    self.tree.column('Size', width=200,anchor='center')
                    self.tree.column('Total Cost', width=100, anchor='center')
                    self.tree.grid(row=0, column=0, sticky='nsew')

                    # Adding a scrollbar to the treeview
                    scrollbar = ttk.Scrollbar(receipt_frame, orient='vertical', command=self.tree.yview)
                    self.tree.configure(yscroll=scrollbar.set) # type: ignore
                    scrollbar.grid(row=0, column=1, sticky='ns')

                    

                    # Display total cost using a LabelFrame for better styling
                    self.total_frame = ttk.Label(self, text=" Total Cost: $0.00 ",relief='sunken', padding=(10, 5),font=('Arial', 12, 'bold'))
                    self.total_frame.grid(row=1, column=0, padx=10, pady=(10, 0),sticky='w')
                    # Button to generate receipt
                    generate_button = ttk.Button(self, text="Generate Receipt", command=self.generate_receipt)
                    generate_button.grid(row=2, column=0, pady=(20, 10))

                    # Configure grid weights for resizing
                    self.grid_rowconfigure(0, weight=1)
                    self.grid_columnconfigure(0, weight=1)

                def generate_receipt(self):
                    # Example data (you can replace with actual data or input mechanism)

                    items = [
                        {'item': 'Pizza', 'quantity':no_s_pizza,'size':'Small', 'total_cost': no_s_pizza*10.00},
                        {'item': 'Pizza', 'quantity':no_m_pizza,'size':'Medium', 'total_cost': no_m_pizza*15.00},
                        {'item': 'Pizza', 'quantity':no_l_pizza,'size':'Large', 'total_cost': no_l_pizza*20.00},


                        {'item': 'Burger', 'quantity':no_s_burger,'size':'Small', 'total_cost': no_s_burger*4.00},
                        {'item': 'Burger', 'quantity':no_m_burger,'size':'Medium', 'total_cost': no_m_burger*8.00},
                        {'item': 'Burger', 'quantity':no_l_burger,'size':'Large', 'total_cost': no_l_burger*12.00},

                        {'item': f'''Butter Chicken {s_butter}''', 'quantity':no_butter,'size':'N/A', 'total_cost': no_butter*14.00},

                        {'item': f'''Grilled Wrap{s_wrap}''', 'quantity':no_wrap,'size':'N/A', 'total_cost': no_wrap*5.00},

                        {'item': 'Karak', 'quantity':no_karak,'size':'N/A', 'total_cost': no_karak*1.50},
                        {'item': 'Green Tea', 'quantity':no_green,'size':'N/A', 'total_cost': no_green*1.00},
                        {'item': 'Black Tea', 'quantity':no_black,'size':'N/A', 'total_cost': no_black*0.50},

                        {'item': 'Latte', 'quantity':no_latte,'size':'N/A', 'total_cost': no_latte*2.00},
                        {'item': 'Cappuccino', 'quantity':no_cappuccino,'size':'N/A', 'total_cost': no_cappuccino*2.50},
                        {'item': 'Americano', 'quantity':no_americano,'size':'N/A', 'total_cost': no_americano*3.00},

                        {'item': 'Choclocate Milk', 'quantity':no_s_milk,'size':'Medium', 'total_cost': no_s_milk*7.50},
                        {'item': 'Choclocate Milk', 'quantity':no_m_milk,'size':'Medium', 'total_cost': no_m_milk*9.00},
                        {'item': 'Choclocate Milk', 'quantity':no_l_milk,'size':'Medium', 'total_cost': no_l_milk*12.00},

                        {'item': 'Watermelon Juice', 'quantity':no_s_melon,'size':'Medium', 'total_cost': no_s_melon*6.00},
                        {'item': 'Watermelon Juice', 'quantity':no_m_melon,'size':'Medium', 'total_cost': no_m_melon*7.50},
                        {'item': 'Watermelon Juice', 'quantity':no_l_melon,'size':'Medium', 'total_cost': no_l_melon*8.00},

                        {'item': 'Ice Cream', 'quantity':no_ice,'size':'N/A', 'total_cost': no_ice*1.00},
                        {'item': 'Gulab Jamun', 'quantity':no_gulab,'size':'N/A', 'total_cost': no_gulab*4.00},
                        {'item': 'Cheese Cake', 'quantity':no_cheese,'size':'N/A', 'total_cost': no_cheese*6.00},
                        {'item': 'Kunafa', 'quantity':no_kunafa,'size':'N/A', 'total_cost': no_kunafa*7.00},
                    ]




                    # Clear existing items in treeview
                    for item in self.tree.get_children():
                        self.tree.delete(item)

                    # Insert new data into the treeview
                    total_cost = 0.0
                    for item in items:
                        if not(item['quantity']):
                            pass
                        else:
                            self.tree.insert('', 'end', values=(item['item'], item['quantity'],item['size'],f"${item['total_cost']:.2f}"))
                            total_cost += item['total_cost']

                    # Update total cost label
                    self.total_frame.configure(text='Total Cost:'+f" ${total_cost:.2f} ",font=('Arial', 12, 'bold'))

                    def restart_program():
                        """Restarts the current program."""
                        hide_label()
                        open_customer_entry()
                        clear_entries()
                        receipt_tab.destroy()
                        
                        

                    
                    
                    next_customer=tk.Button(self,text="Next Customer",command=restart_program)
                    next_customer.grid(row=1,column=0, padx=10, pady=(10, 0))

            receipt_tab = ReceiptTab(customer_frame)
            order_toplevel.destroy()

        

            receipt_query=f'''SELECT 
                                c.customer_id,
                                COALESCE(p.s_pizza, 0) AS s_pizza,
                                COALESCE(p.m_pizza, 0) AS m_pizza,
                                COALESCE(p.l_pizza, 0) AS l_pizza,
                                COALESCE(b.s_burger, 0) AS s_burger,
                                COALESCE(b.m_burger, 0) AS m_burger,
                                COALESCE(b.l_burger, 0) AS l_burger,
                                COALESCE(c.BUTTER_CHICKEN, 0) AS BUTTER_CHICKEN,
                                COALESCE(c.GRILLED_CHICKEN_WRAP, 0) AS GRILLED_CHICKEN_WRAP,
                                COALESCE(t.t_spice, 1) AS t_spice,
                                COALESCE(w.w_spice, 1) AS w_spice,
                                COALESCE(te.karak, 0) AS karak,
                                COALESCE(te.black_tea, 0) AS black_tea,
                                COALESCE(te.green_tea, 0) AS green_tea,
                                COALESCE(co.latte, 0) AS latte,
                                COALESCE(co.cappuccino, 0) AS cappuccino,
                                COALESCE(co.americano, 0) AS americano,
                                COALESCE(ch.s_choco, 0) AS s_choco,
                                COALESCE(ch.m_choco, 0) AS m_choco,
                                COALESCE(ch.l_choco, 0) AS l_choco,
                                COALESCE(wa.s_watermelon, 0) AS s_watermelon,
                                COALESCE(wa.m_watermelon, 0) AS m_watermelon,
                                COALESCE(wa.l_watermelon, 0) AS l_watermelon,
                                COALESCE(c.ICE_CREAM, 0) AS ICE_CREAM,
                                COALESCE(c.GULAB_JAMUN, 0) AS GULAB_JAMUN,
                                COALESCE(c.CHEESE_CAKE, 0) AS CHEESE_CAKE,
                                COALESCE(c.kunafa, 0) AS kunafa      
                                    FROM customers c
                                    LEFT JOIN pizza p ON c.customer_id = p.customer_id
                                    LEFT JOIN burger b ON c.customer_id = b.customer_id
                                    LEFT JOIN tikka t ON c.customer_id = t.customer_id
                                    LEFT JOIN wrap w ON c.customer_id = w.customer_id
                                    LEFT JOIN tea te ON c.customer_id = te.customer_id
                                    LEFT JOIN coffee co ON c.customer_id = co.customer_id
                                    LEFT JOIN choco ch ON c.customer_id = ch.customer_id
                                    LEFT JOIN watermelon wa ON c.customer_id = wa.customer_id
                                    LEFT JOIN icecream ic ON c.customer_id = ic.customer_id
                                    LEFT JOIN gulabjamun gu ON c.customer_id = gu.customer_id
                                    LEFT JOIN cheesecake ce ON c.customer_id = ce.customer_id
                                    LEFT JOIN kunafa ku ON c.customer_id = ku.customer_id
                                    WHERE c.customer_id = {get_customer_id()};'''
            cursor.execute(receipt_query)


            rs=cursor.fetchall()


            for i in rs:
                no_s_pizza=int(i[1])# type: ignore
                no_m_pizza=int(i[2])# type: ignore
                no_l_pizza=int(i[3])# type: ignore

                no_s_burger=int(i[4])# type: ignore
                no_m_burger=int(i[5])# type: ignore
                no_l_burger=int(i[6])# type: ignore

                no_butter=int(i[7])# type: ignore
                no_wrap=int(i[8])# type: ignore
                s_butter=int(i[9])# type: ignore
                s_wrap=int(i[10])# type: ignore

                no_karak=int(i[11])# type: ignore
                no_green=int(i[12])# type: ignore
                no_black=int(i[13])# type: ignore

                no_latte=int(i[14])# type: ignore
                no_cappuccino=int(i[15])# type: ignore
                no_americano=int(i[16])# type: ignore

                no_s_milk=int(i[17])# type: ignore
                no_m_milk=int(i[18])# type: ignore
                no_l_milk=int(i[19])# type: ignore

                no_s_melon=int(i[20])# type: ignore
                no_m_melon=int(i[21])# type: ignore
                no_l_melon=int(i[22])# type: ignore

                no_ice=int(i[23])# type: ignore
                no_gulab=int(i[24])# type: ignore
                no_cheese=int(i[25])# type: ignore
                no_kunafa=int(i[26])# type: ignore
            



            receipt_tab.grid(row=0, column=0, columnspan=1)

        #FOOD
        chicken=ch_meter.amountusedvar.get()
        pizza=p_meter.amountusedvar.get()
        burger=b_meter.amountusedvar.get()
        grilled_chicken=gr_meter.amountusedvar.get()


        #JUICE
        tea=t_meter.amountusedvar.get()
        coffee=co_meter.amountusedvar.get()
        chocolate_milkshake=cho_meter.amountusedvar.get()
        watermelon_juice=w_meter.amountusedvar.get()


        #DESERT
        icecream=ice_meter.amountusedvar.get()
        gulab_jamun=g_meter.amountusedvar.get()
        cheese_cake=chs_meter.amountusedvar.get()
        kunafa=k_meter.amountusedvar.get()


        menu_meter.destroy()
        hide_label()
        confirm_button2.config(state=tk.NORMAL)


        insertfood_query=f'''insert into customers(customer_id,
                        customer_name,
                        address,
                        customer_phoneno,
                        BUTTER_CHICKEN,
                        PIZZA,
                        BURGER,
                        GRILLED_CHICKEN_WRAP,
                        TEA,
                        COFFEE,
                        CHOCOLATE_MILKSHAKE,
                        WATERMELON_JUICE,
                        ICE_CREAM,
                        GULAB_JAMUN,
                        CHEESE_CAKE,
                        KUNAFA)
                        values({get_customer_id()},'{c_name.get()}','{c_address.get()}',{int(c_phone_no.get())},{chicken},{pizza},{burger},{grilled_chicken},{tea},{coffee},{chocolate_milkshake},{watermelon_juice},{icecream},{gulab_jamun},{cheese_cake},{kunafa})'''
        insertfood_query1=f'''update customers set customer_name='{c_name.get()}',
                             address='{c_address.get()}',
                             customer_phoneno={int(c_phone_no.get())},
                             BUTTER_CHICKEN={chicken},
                             PIZZA={pizza},
                             BURGER={burger},
                             GRILLED_CHICKEN_WRAP={grilled_chicken},
                             TEA={tea},COFFEE={coffee},
                             CHOCOLATE_MILKSHAKE={chocolate_milkshake},
                             WATERMELON_JUICE={watermelon_juice},
                             ICE_CREAM={icecream},
                             GULAB_JAMUN={gulab_jamun},
                             CHEESE_CAKE={cheese_cake},
                             KUNAFA={kunafa} where customer_id={get_customer_id()}'''
        cursor.execute(insertfood_query1)
        con.commit()


        def details_confirm():


            createquery_pizza='''create table if not exists pizza(customer_id int(10),s_pizza int(3),m_pizza int(3),l_pizza int(3),s_cost float(3),m_cost float(3),l_cost float(3))'''
            createquery_burger='''create table if not exists burger(customer_id int(10),s_burger int(3),m_burger int(3),l_burger int(3),s_cost float(3),m_cost float(3),l_cost float(3))'''
            createquery_tikka='''create table if not exists tikka(customer_id int(10),t_spice int(2),t_cost float(3))'''
            createquery_wrap='''create table if not exists wrap(customer_id int(10),w_spice int(2),w_cost float(3))'''
            createquery_tea='''create table if not exists tea(customer_id int(10),karak int(3),black_tea int(3),green_tea int(3),k_cost float(3),b_cost float(3),g_cost float(3))'''
            createquery_coffee='''create table if not exists coffee(customer_id int(10),latte int(3),cappuccino int(3),americano int(3),l_cost float(3),c_cost float(3),a_cost float(3))'''
            createquery_choco='''create table if not exists choco(customer_id int(10),s_choco int(3),m_choco int(3),l_choco int(3),s_cost float(3),m_cost float(3),l_cost float(3))'''
            createquery_watermelon='''create table if not exists watermelon(customer_id int(10),s_watermelon int(3),m_watermelon int(3),l_watermelon int(3),s_cost float(3),m_cost float(3),l_cost float(3))'''
            createquery_icecream='''create table if not exists icecream(customer_id int(10),i_cost float(3))'''
            createquery_gulabjamun='''create table if not exists gulabjamun(customer_id int(10),g_cost float(3))'''
            createquery_cheesecake='''create table if not exists cheesecake(customer_id int(10),ch_cost float(3))'''
            createquery_kunafa='''create table if not exists kunafa(customer_id int(10),k_cost float(3))'''


            cursor.execute(createquery_pizza)
            cursor.execute(createquery_burger)
            cursor.execute(createquery_tikka)
            cursor.execute(createquery_wrap)
            cursor.execute(createquery_tea)
            cursor.execute(createquery_coffee)
            cursor.execute(createquery_choco)
            cursor.execute(createquery_watermelon)
            cursor.execute(createquery_icecream)
            cursor.execute(createquery_gulabjamun)
            cursor.execute(createquery_cheesecake)
            cursor.execute(createquery_kunafa)


            s_pizza=int_check(small_pizza_entry.get())
            m_pizza=int_check(medium_pizza_entry.get())
            l_pizza=int_check(large_pizza_entry.get())


            s_burger=int_check(small_burger_entry.get())
            m_burger=int_check(medium_burger_entry.get())
            l_burger=int_check(larger_burger_entry.get())


            s_butterchicken=int_check(butter_chicken_spice_level_entry.get())
            s_wrap=int_check(grilled_wrap_spice_level_entry.get())


            karak=int_check(karak_entry.get())
            black_tea=int_check(black_tea_entry.get())
            green_tea=int_check(green_tea_entry.get())


            latte=int_check(latte_entry.get())
            cappuccino=int_check(cappuccino_entry.get())
            americano=int_check(americano_entry.get())


            s_choco=int_check(small_milkshake_entry.get())
            m_choco=int_check(medium_milkshake_entry.get())
            l_choco=int_check(large_milkshake_entry.get())


            s_watermelon=int_check(small_watermelon_entry.get())
            m_watermelon=int_check(medium_watermelon_entry.get())
            l_watermelon=int_check(large_milkshake_entry.get())


            check_query=f'''select * from customers where customer_id={get_customer_id()}'''
            cursor.execute(check_query)


            rs=cursor.fetchall()

            print(s_pizza,m_pizza,l_pizza)
            print(s_burger,m_burger,l_burger)
            


            for i in rs:
                no_pizza=float(i[7]) # type: ignore
                no_burger=float(i[8])# type: ignore
                no_tea=float(i[10])# type: ignore
                no_coffee=float(i[11])# type: ignore
                no_choco=float(i[12])# type: ignore
                no_watermelon=float(i[13])# type: ignore

            pizza_check= burger_check=tea_check= coffee_check=choco_check=watermelon_check=True
            if no_pizza!=0:
                pizza_check= int(s_pizza+m_pizza+l_pizza)==no_pizza and str(s_pizza).isdigit() and str(m_pizza).isdigit() and str(l_pizza).isdigit()
            else:
                pass
            if no_burger!=0:
                burger_check=int(s_burger+m_burger+l_burger)==int(no_burger) and str(s_burger).isdigit() and str(m_burger).isdigit() and str(l_burger).isdigit()
            else:
                pass
            if no_tea!=0:
                tea_check=int(karak+black_tea+green_tea)==no_tea and  str(karak).isdigit() and str(black_tea).isdigit() and str(green_tea).isdigit()
            else:
                pass
            if no_coffee!=0:
                coffee_check=int(latte+cappuccino+americano)==no_coffee and str(latte).isdigit() and str(cappuccino).isdigit() and str(americano).isdigit()
            else:
                pass
            if no_choco!=0:
                choco_check=int(s_choco+m_choco+l_choco)==no_choco and str(s_choco).isdigit() and str(m_choco).isdigit() and str(l_choco).isdigit()
            else:
                pass
            if no_watermelon!=0:
                watermelon_check=int(s_watermelon+m_watermelon+l_watermelon)==no_watermelon and str(s_watermelon).isdigit() and str(m_watermelon).isdigit() and str(l_watermelon).isdigit()
            else:
                pass

            if pizza_check and burger_check and tea_check and coffee_check and choco_check and watermelon_check:
                insertquery_pizza=f'''insert into pizza values({get_customer_id()},{s_pizza},{m_pizza},{l_pizza},10,15,20)'''
                insertquery_burger=f'''insert into burger values({get_customer_id()},{s_burger},{m_burger},{l_burger},4,8,12)'''
                insertquery_tikka=f'''insert into tikka values({get_customer_id()},{s_butterchicken},14)'''
                insertquery_wrap=f'''insert into wrap values({get_customer_id()},{s_wrap},5)'''
                insertquery_tea=f'''insert into tea values({get_customer_id()},{karak},{black_tea},{green_tea},1.50,0.50,1)'''
                insertquery_coffee=f'''insert into coffee values({get_customer_id()},{latte},{cappuccino},{americano},2,2.50,3)'''
                insertquery_choco=f'''insert into choco values({get_customer_id()},{s_choco},{m_choco},{l_choco},7.50,9,12)'''
                insertquery_watermelon=f'''insert into watermelon values({get_customer_id()},{s_watermelon},{m_watermelon},{l_watermelon},6,7.5,8)'''
                insertquery_icecream=f'''insert into icecream values({get_customer_id()},1)'''
                insertquery_gulabjamun=f'''insert into gulabjamun values({get_customer_id()},4)'''
                insertquery_cheesecake=f'''insert into cheesecake values({get_customer_id()},6)'''
                insertquery_kunafa=f'''insert into kunafa values({get_customer_id()},7)'''

                cursor.execute(insertquery_pizza)
                cursor.execute(insertquery_burger)
                cursor.execute(insertquery_tikka)
                cursor.execute(insertquery_wrap)
                cursor.execute(insertquery_tea)
                cursor.execute(insertquery_coffee)
                cursor.execute(insertquery_choco)
                cursor.execute(insertquery_watermelon)
                cursor.execute(insertquery_icecream)
                cursor.execute(insertquery_gulabjamun)
                cursor.execute(insertquery_cheesecake)
                cursor.execute(insertquery_kunafa)


                insertquery_date=f'''update customers set date_of_order='{datetime.now().date().strftime("%Y-%m-%d")}' where customer_id={get_customer_id()}'''
                insertquery_time=f'''update customers set time='{datetime.now().time().strftime("%H:%M:%S")}' where customer_id={get_customer_id()}'''
                cursor.execute(insertquery_date)
                cursor.execute(insertquery_time)


                con.commit()
                place_order()
            else:
                if not(pizza_check):
                    print('ERROR!!:  PIZZA COUNT NOT MATCHED')
                elif not(burger_check):
                    print('ERROR!!: BURGER COUNT NOT MATCHED')    
                elif not(tea_check):
                    print('ERROR!!: TEA COUNT NOT MATCHED')
                elif not(coffee_check):
                    print('ERROR!!: COFFEE COUNT NOT MATCHED')
                elif not(choco_check):
                    print('ERROR!!: MILKSHAKE COUNT NOT MATCHED')
                elif not(watermelon_check):
                    print('ERROR!!: WATERMELON COUNT NOT MATCHED')
                else:
                    pass

            




        style = Style(theme="flatly")


        order_toplevel=Toplevel()


        # Create notebook (tabbed interface)
        notebook = ttk.Notebook(order_toplevel)
        notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


        # Create tabs for Pizza, Burger, Tea, Coffee, and Spice Level
        pizza_tab = ttk.Frame(notebook)
        burger_tab = ttk.Frame(notebook)
        tea_tab = ttk.Frame(notebook)
        coffee_tab = ttk.Frame(notebook)
        spice_tab = ttk.Frame(notebook)
        chocolate_milkshake_tab=ttk.Frame(notebook)
        watermelon_juice_tab=ttk.Frame(notebook)


        notebook.add(pizza_tab, text='Pizza')
        notebook.add(burger_tab, text='Burger')
        notebook.add(tea_tab, text='Tea')
        notebook.add(coffee_tab, text='Coffee')
        notebook.add(spice_tab, text='Spice Level')
        notebook.add(chocolate_milkshake_tab,text='chocolate milkshake')
        notebook.add(watermelon_juice_tab,text='watermelon Juice')

        def validate_input(char):
                """Validate if the input is a digit."""
                return char.isdigit() or char == ""


        validate_cmd = root.register(validate_input)


        # Pizza options
        pizza_size_label = ttk.Label(pizza_tab, text="Pizza Sizes and Quantities:")
        pizza_size_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


        small_pizza_label = ttk.Label(pizza_tab, text="Small:")
        small_pizza_label.grid(row=1, column=0, padx=10, pady=5)
        small_pizza_amount = tk.IntVar(value=0)
        small_pizza_entry =ttk.Entry(pizza_tab, textvariable=small_pizza_amount,validate="key", validatecommand=(validate_cmd, "%S")) # type: ignore
        small_pizza_entry.grid(row=1, column=1, padx=10, pady=5)


        medium_pizza_label = ttk.Label(pizza_tab, text="Medium:")
        medium_pizza_label.grid(row=2, column=0, padx=10, pady=5)
        medium_pizza_amount = tk.IntVar(value=0)
        medium_pizza_entry = ttk.Entry(pizza_tab, textvariable=medium_pizza_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        medium_pizza_entry.grid(row=2, column=1, padx=10, pady=5)


        large_pizza_label = ttk.Label(pizza_tab, text="Large:")
        large_pizza_label.grid(row=3, column=0, padx=10, pady=5)
        large_pizza_amount = tk.IntVar(value=0)
        large_pizza_entry = ttk.Entry(pizza_tab, textvariable=large_pizza_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        large_pizza_entry.grid(row=3, column=1, padx=10, pady=5)


        # Burger options
        burger_size_label = ttk.Label(burger_tab, text="Burger Sizes and Quantities:")
        burger_size_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


        small_burger_label = ttk.Label(burger_tab, text="Small:")
        small_burger_label.grid(row=1, column=0, padx=10, pady=5)
        small_burger_amount = tk.IntVar(value=0)
        small_burger_entry = ttk.Entry(burger_tab, textvariable=small_burger_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        small_burger_entry.grid(row=1, column=1, padx=10, pady=5)


        medium_burger_label = ttk.Label(burger_tab, text="Medium:")
        medium_burger_label.grid(row=2, column=0, padx=10, pady=5)
        medium_burger_amount = tk.IntVar(value=0)
        medium_burger_entry = ttk.Entry(burger_tab, textvariable=medium_burger_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        medium_burger_entry.grid(row=2, column=1, padx=10, pady=5)


        larger_burger_label = ttk.Label(burger_tab, text="Large:")
        larger_burger_label.grid(row=3, column=0, padx=10, pady=5)
        larger_burger_amount = tk.IntVar(value=0)
        larger_burger_entry = ttk.Entry(burger_tab, textvariable=larger_burger_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        larger_burger_entry.grid(row=3, column=1, padx=10, pady=5)


        # Tea options
        tea_type_label = ttk.Label(tea_tab, text="Tea Types, Sugar, and Quantities:")
        tea_type_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


        # Karak Tea
        karak_label = ttk.Label(tea_tab, text="Karak:")
        karak_label.grid(row=1, column=0, padx=10, pady=5)
        karak_amount = tk.IntVar(value=0)
        karak_entry = ttk.Entry(tea_tab, textvariable=karak_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        karak_entry.grid(row=1, column=1, padx=10, pady=5)


        karak_sugar_var = tk.BooleanVar()
        sugar_for_karak_checkbox = ttk.Checkbutton(tea_tab, text="Sugar", variable=karak_sugar_var)
        sugar_for_karak_checkbox.grid(row=1, column=2, padx=10, pady=5)


        # Green Tea
        green_tea_label = ttk.Label(tea_tab, text="Green:")
        green_tea_label.grid(row=2, column=0, padx=10, pady=5)
        green_tea_amount = tk.IntVar(value=0)
        green_tea_entry = ttk.Entry(tea_tab, textvariable=green_tea_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        green_tea_entry.grid(row=2, column=1, padx=10, pady=5)


        green_tea_sugar = tk.BooleanVar()
        green_tea_sugar_checkbox = ttk.Checkbutton(tea_tab, text="Sugar", variable=green_tea_sugar)
        green_tea_sugar_checkbox.grid(row=2, column=2, padx=10, pady=5)


        # Black Tea
        black_tea_label = ttk.Label(tea_tab, text="Black:")
        black_tea_label.grid(row=3, column=0, padx=10, pady=5)
        black_tea_amount = tk.IntVar(value=0)
        black_tea_entry = ttk.Entry(tea_tab, textvariable=black_tea_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        black_tea_entry.grid(row=3, column=1, padx=10, pady=5)


        black_tea_sugar_var = tk.BooleanVar()
        black_tea_sugar_checkbox = ttk.Checkbutton(tea_tab, text="Sugar", variable=black_tea_sugar_var)
        black_tea_sugar_checkbox.grid(row=3, column=2, padx=10, pady=5)


        # Coffee options
        coffee_type_label = ttk.Label(coffee_tab, text="Coffee Types, Sugar, and Quantities:")
        coffee_type_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


        # Cappuccino Coffee
        cappuccino_label = ttk.Label(coffee_tab, text="Cappuccino:")
        cappuccino_label.grid(row=1, column=0, padx=10, pady=5)
        cappuccino_amount = tk.IntVar(value=0)
        cappuccino_entry = ttk.Entry(coffee_tab, textvariable=cappuccino_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        cappuccino_entry.grid(row=1, column=1, padx=10, pady=5)


        cappuccino_sugar_var = tk.BooleanVar()
        cappuccino_sugar_checkbox = ttk.Checkbutton(coffee_tab, text="Sugar", variable=cappuccino_sugar_var)
        cappuccino_sugar_checkbox.grid(row=1, column=2, padx=10, pady=5)


        # Americano Coffee
        americano_label = ttk.Label(coffee_tab, text="Americano:")
        americano_label.grid(row=2, column=0, padx=10, pady=5)
        americano_amount = tk.IntVar(value=0)
        americano_entry = ttk.Entry(coffee_tab, textvariable=americano_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        americano_entry.grid(row=2, column=1, padx=10, pady=5)


        americano_sugar_var = tk.BooleanVar()
        americano_sugar_checkbox = ttk.Checkbutton(coffee_tab, text="Sugar", variable=americano_sugar_var)
        americano_sugar_checkbox.grid(row=2, column=2, padx=10, pady=5)


        # Latte Coffee
        latter_label = ttk.Label(coffee_tab, text="Latte:")
        latter_label.grid(row=3, column=0, padx=10, pady=5)
        latter_amount = tk.IntVar(value=0)
        latte_entry = ttk.Entry(coffee_tab, textvariable=latter_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        latte_entry.grid(row=3, column=1, padx=10, pady=5)


        latte_sugar_var = tk.BooleanVar()
        latte_sugar_checkbox = ttk.Checkbutton(coffee_tab, text="Sugar", variable=latte_sugar_var)
        latte_sugar_checkbox.grid(row=3, column=2, padx=10, pady=5)


        # Spice Level
        spice_level_label = ttk.Label(spice_tab, text="Spice Level for Grilled Wrap and Butter Chicken:")
        spice_level_label.grid(row=0, column=0, padx=10, pady=10)


        # Grilled Wrap options (spice level)
        grilled_wrap_spice_label = ttk.Label(spice_tab, text="Grilled Wrap Spice Level (1-5):")
        grilled_wrap_spice_label.grid(row=1, column=0, padx=10, pady=5)
        grilled_wrap_spice_level = tk.IntVar(value=1)
        grilled_wrap_spice_level_entry = ttk.Entry(spice_tab, textvariable=grilled_wrap_spice_level,validate="key", validatecommand=(validate_cmd, "%S"))
        grilled_wrap_spice_level_entry.grid(row=1, column=1, padx=10, pady=5)


        # Butter Chicken options (spice level)
        butter_chicken_spice_label = ttk.Label(spice_tab, text="Butter Chicken Spice Level (1-5):")
        butter_chicken_spice_label.grid(row=2, column=0, padx=10, pady=5)
        butter_chicken_spice_level = tk.IntVar(value=1)
        butter_chicken_spice_level_entry = ttk.Entry(spice_tab, textvariable=butter_chicken_spice_level,validate="key", validatecommand=(validate_cmd, "%S"))
        butter_chicken_spice_level_entry.grid(row=2, column=1, padx=10, pady=5)


         # MILKSHAKE options
        milkshake_size_label = ttk.Label(chocolate_milkshake_tab, text="Chocolate milkshake Sizes and Quantities:")
        milkshake_size_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


        small_milkshake_label = ttk.Label(chocolate_milkshake_tab, text="Small:")
        small_milkshake_label.grid(row=1, column=0, padx=10, pady=5)
        small_milkshake_amount = tk.IntVar(value=0)
        small_milkshake_entry =ttk.Entry(chocolate_milkshake_tab, textvariable=small_milkshake_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        small_milkshake_entry.grid(row=1, column=1, padx=10, pady=5)


        medium_milkshake_label = ttk.Label(chocolate_milkshake_tab, text="Medium:")
        medium_milkshake_label.grid(row=2, column=0, padx=10, pady=5)
        medium_milkshake_amount = tk.IntVar(value=0)
        medium_milkshake_entry = ttk.Entry(chocolate_milkshake_tab, textvariable=medium_milkshake_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        medium_milkshake_entry.grid(row=2, column=1, padx=10, pady=5)


        large_milkshake_label = ttk.Label(chocolate_milkshake_tab, text="Large:")
        large_milkshake_label.grid(row=3, column=0, padx=10, pady=5)
        large_milkshake_amount = tk.IntVar(value=0)
        large_milkshake_entry = ttk.Entry(chocolate_milkshake_tab, textvariable=large_milkshake_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        large_milkshake_entry.grid(row=3, column=1, padx=10, pady=5)


         # watermelon options
        watermelon_size_label = ttk.Label(watermelon_juice_tab, text="Watermelon melon Sizes and Quantities:")
        watermelon_size_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


        small_watermelon_label = ttk.Label(watermelon_juice_tab, text="Small:")
        small_watermelon_label.grid(row=1, column=0, padx=10, pady=5)
        small_watermelon_amount = tk.IntVar(value=0)
        small_watermelon_entry =ttk.Entry(watermelon_juice_tab, textvariable=small_watermelon_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        small_watermelon_entry.grid(row=1, column=1, padx=10, pady=5)


        medium_watermelon_label = ttk.Label(watermelon_juice_tab, text="Medium:")
        medium_watermelon_label.grid(row=2, column=0, padx=10, pady=5)
        medium_watermelon_amount = tk.IntVar(value=0)
        medium_watermelon_entry = ttk.Entry(watermelon_juice_tab, textvariable=medium_watermelon_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        medium_watermelon_entry.grid(row=2, column=1, padx=10, pady=5)


        large_watermelon_label = ttk.Label(watermelon_juice_tab, text="Large:")
        large_watermelon_label.grid(row=3, column=0, padx=10, pady=5)
        large_watermelon_amount = tk.IntVar(value=0)
        large_watermelon_entry = ttk.Entry(watermelon_juice_tab, textvariable=large_watermelon_amount,validate="key", validatecommand=(validate_cmd, "%S"))
        large_watermelon_entry.grid(row=3, column=1, padx=10, pady=5)

        default_values = {
            "Small Pizza": tk.StringVar(value="0"),
            "Medium Pizza": tk.StringVar(value="0"),
            "Large Pizza": tk.StringVar(value="0"),
            "Small Burger": tk.StringVar(value="0"),
            "Medium Burger": tk.StringVar(value="0"),
            "Large Burger": tk.StringVar(value="0"),
            "Karak Tea": tk.StringVar(value="0"),
            "Green Tea": tk.StringVar(value="0"),
            "Black Tea": tk.StringVar(value="0"),
            "Cappuccino": tk.StringVar(value="0"),
            "Americano": tk.StringVar(value="0"),
            "Latte": tk.StringVar(value="0"),
            "Grilled Wrap Spice Level": tk.StringVar(value="1"),
            "Butter Chicken Spice Level": tk.StringVar(value="1"),
            "Small Chocolate Milkshake": tk.StringVar(value="0"),
            "Medium Chocolate Milkshake": tk.StringVar(value="0"),
            "Large Chocolate Milkshake": tk.StringVar(value="0"),
            "Small Watermelon Juice": tk.StringVar(value="0"),
            "Medium Watermelon Juice": tk.StringVar(value="0"),
            "Large Watermelon Juice": tk.StringVar(value="0")
        }





        # Button to place order
        order_button = ttk.Button(order_toplevel, text="Place Order", command=details_confirm)
        order_button.pack(padx=10, pady=10)














    menu_meter = Toplevel()
   
    # Define Meter widgets for various food items
    #FOOD
    p_meter=tb.Meter(menu_meter,bootstyle='warning',
                   subtext="PIZZA",
                   interactive=TRUE,
                   stepsize=1
                   )
    p_meter.grid(row=1,column=0)


    b_meter=tb.Meter(menu_meter,bootstyle='warning',
                   subtext="BURGER",
                   interactive=TRUE,
                   stepsize=1
                   )
    b_meter.grid(row=1,column=1,padx=(0,40))


    ch_meter=tb.Meter(menu_meter,bootstyle='warning',
                   subtext="BUTTER CHICKEN",
                   interactive=TRUE,
                   stepsize=1
                   )
    ch_meter.grid(row=2,column=0)


    gr_meter=tb.Meter(menu_meter,bootstyle='warning',
                   subtext="GRILLED C.WRAP",
                   interactive=TRUE,
                   stepsize=1
                   )
    gr_meter.grid(row=2,column=1,padx=(0,40))
    #BEVERAGE
    t_meter=tb.Meter(menu_meter,bootstyle='info',
                   subtext="TEA",
                   interactive=TRUE,
                   stepsize=1
                   )
    t_meter.grid(row=1,column=2,padx=(40,0))


    co_meter=tb.Meter(menu_meter,bootstyle='info',
                   subtext="COFFEE",
                   interactive=TRUE,
                   stepsize=1
                   )
    co_meter.grid(row=1,column=3,padx=(0,40))


    cho_meter=tb.Meter(menu_meter,bootstyle='info',
                   subtext="CHOCO MILKSHAKE",
                   interactive=TRUE,
                   stepsize=1
                   )
    cho_meter.grid(row=2,column=2,padx=(40,0))


    w_meter=tb.Meter(menu_meter,bootstyle='info',
                   subtext="WATERMELON JUICE",
                   interactive=TRUE,
                   stepsize=1
                   )
    w_meter.grid(row=2,column=3,padx=(0,40))


    #DESERT


    ice_meter=tb.Meter(menu_meter,bootstyle='dark',
                   subtext="ICE CREAM",
                   interactive=TRUE,
                   stepsize=1
                   )
    ice_meter.grid(row=1,column=4)


    g_meter=tb.Meter(menu_meter,bootstyle='dark',
                   subtext="GULAB JAMUN",
                   interactive=TRUE,
                   stepsize=1
                   )
    g_meter.grid(row=1,column=5)


    chs_meter=tb.Meter(menu_meter,bootstyle='dark',
                   subtext="CHEESE CAKE",
                   interactive=TRUE,
                   stepsize=1
                   )
    chs_meter.grid(row=2,column=4)


    k_meter=tb.Meter(menu_meter,bootstyle='dark',
                   subtext="KUNAFA",
                   interactive=TRUE,
                   stepsize=1
                   )
    k_meter.grid(row=2,column=5)
    confirm_order=tk.Button(menu_meter,text="CONFIRM ORDER",command=order)
    confirm_order.grid(row=3,column=2,columnspan=2)

# Button to confirm customer details input
confirm_button2 = tk.Button(customer_frame, text="CONFIRM", command=customer_button)
confirm_button2.grid(row=6, column=0, columnspan=2)
ToolTip(confirm_button2, text='CLICK TO CONFIRM',bootstyle=(SUCCESS,INVERSE))


error_label = ttk.Label(customer_frame, text='')
error_label.grid(row=5, column=0, columnspan=3)

customer_id_label=ttk.Label(database_frame,text="ENTER CUSTOMER ID:")
customer_id_label.grid(row=0,column=0,padx=10,pady=10)

def validate_input(char):
                """Validate if the input is a digit."""
                return char.isdigit() or char == ""


validate_cmd = root.register(validate_input)

customer_id_entry=ttk.Entry(database_frame,validate="key", validatecommand=(validate_cmd, "%S"))
customer_id_entry.grid(row=0,column=1,padx=10,pady=10)

def get_receipt():
    try:
        datababse_customerid=int(customer_id_entry.get())
    except ValueError:
        ToolTip(receipt_button,text='INVALID CUSTOMER ID',bootstyle=(DANGER,INVERSE))
    else:
        receipt_toplevel=Toplevel()
        class ReceiptTab(tk.Frame):
                def __init__(self, parent):
                    super().__init__(parent)
                    self.parent = parent
                    self.style = Style(theme='minty')
                    self.create_widgets()

                def create_widgets(self):
                    self.grid(row=0, column=0, sticky="nsew")
                    self.parent.grid_rowconfigure(0, weight=1)
                    self.parent.grid_columnconfigure(0, weight=1)

                    # Creating a frame to hold the receipt information
                    receipt_frame = ttk.Frame(self)
                    receipt_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

                    # Creating a treeview widget to display receipt
                    self.tree = ttk.Treeview(receipt_frame, columns=('Item', 'Quantity','Size', 'Total Cost'), show='headings')
                    self.tree.heading('Item', text='Item')
                    self.tree.heading('Quantity', text='Quantity')
                    self.tree.heading('Size', text='Size')
                    self.tree.heading('Total Cost', text='Total Cost')
                    self.tree.column('Item', width=200)
                    self.tree.column('Quantity', width=100, anchor='center')
                    self.tree.column('Size', width=200,anchor='center')
                    self.tree.column('Total Cost', width=100, anchor='center')
                    self.tree.grid(row=0, column=0, sticky='nsew')

                    # Adding a scrollbar to the treeview
                    scrollbar = ttk.Scrollbar(receipt_frame, orient='vertical', command=self.tree.yview)
                    self.tree.configure(yscroll=scrollbar.set) # type: ignore
                    scrollbar.grid(row=0, column=1, sticky='ns')

                    

                    # Display total cost using a LabelFrame for better styling
                    self.total_frame = ttk.Label(self, text=" Total Cost: $0.00 ",relief='sunken', padding=(10, 5),font=('Arial', 12, 'bold'))
                    self.total_frame.grid(row=1, column=0, padx=10, pady=(10, 0),sticky='w')

                    #Display date and time
                    self.date_time_label= ttk.Label(self, text=f'''DATE : {date} , TIME : {time}''' ,relief='sunken', padding=(10, 5),font=('Arial', 12, 'bold'))
                    self.date_time_label.grid(row=1, column=0, padx=10, pady=(10, 0))

                    self.generate_receipt()

                    # Configure grid weights for resizing
                    self.grid_rowconfigure(0, weight=1)
                    self.grid_columnconfigure(0, weight=1)

                def generate_receipt(self):
                    # Example data (you can replace with actual data or input mechanism)

                    items = [
                        {'item': 'Pizza', 'quantity':no_s_pizza,'size':'Small', 'total_cost': no_s_pizza*10.00},
                        {'item': 'Pizza', 'quantity':no_m_pizza,'size':'Medium', 'total_cost': no_m_pizza*15.00},
                        {'item': 'Pizza', 'quantity':no_l_pizza,'size':'Large', 'total_cost': no_l_pizza*20.00},


                        {'item': 'Burger', 'quantity':no_s_burger,'size':'Small', 'total_cost': no_s_burger*4.00},
                        {'item': 'Burger', 'quantity':no_m_burger,'size':'Medium', 'total_cost': no_m_burger*8.00},
                        {'item': 'Burger', 'quantity':no_l_burger,'size':'Large', 'total_cost': no_l_burger*12.00},

                        {'item': f'''Butter Chicken {s_butter}''', 'quantity':no_butter,'size':'N/A', 'total_cost': no_butter*14.00},

                        {'item': f'''Grilled Wrap{s_wrap}''', 'quantity':no_wrap,'size':'N/A', 'total_cost': no_wrap*5.00},

                        {'item': 'Karak', 'quantity':no_karak,'size':'N/A', 'total_cost': no_karak*1.50},
                        {'item': 'Green Tea', 'quantity':no_green,'size':'N/A', 'total_cost': no_green*1.00},
                        {'item': 'Black Tea', 'quantity':no_black,'size':'N/A', 'total_cost': no_black*0.50},

                        {'item': 'Latte', 'quantity':no_latte,'size':'N/A', 'total_cost': no_latte*2.00},
                        {'item': 'Cappuccino', 'quantity':no_cappuccino,'size':'N/A', 'total_cost': no_cappuccino*2.50},
                        {'item': 'Americano', 'quantity':no_americano,'size':'N/A', 'total_cost': no_americano*3.00},

                        {'item': 'Choclocate Milk', 'quantity':no_s_milk,'size':'Medium', 'total_cost': no_s_milk*7.50},
                        {'item': 'Choclocate Milk', 'quantity':no_m_milk,'size':'Medium', 'total_cost': no_m_milk*9.00},
                        {'item': 'Choclocate Milk', 'quantity':no_l_milk,'size':'Medium', 'total_cost': no_l_milk*12.00},

                        {'item': 'Watermelon Juice', 'quantity':no_s_melon,'size':'Medium', 'total_cost': no_s_melon*6.00},
                        {'item': 'Watermelon Juice', 'quantity':no_m_melon,'size':'Medium', 'total_cost': no_m_melon*7.50},
                        {'item': 'Watermelon Juice', 'quantity':no_l_melon,'size':'Medium', 'total_cost': no_l_melon*8.00},

                        {'item': 'Ice Cream', 'quantity':no_ice,'size':'N/A', 'total_cost': no_ice*1.00},
                        {'item': 'Gulab Jamun', 'quantity':no_gulab,'size':'N/A', 'total_cost': no_gulab*4.00},
                        {'item': 'Cheese Cake', 'quantity':no_cheese,'size':'N/A', 'total_cost': no_cheese*6.00},
                        {'item': 'Kunafa', 'quantity':no_kunafa,'size':'N/A', 'total_cost': no_kunafa*7.00},
                    ]




                    # Clear existing items in treeview
                    for item in self.tree.get_children():
                        self.tree.delete(item)

                    # Insert new data into the treeview
                    total_cost = 0.0
                    for item in items:
                        if not(item['quantity']):
                            pass
                        else:
                            self.tree.insert('', 'end', values=(item['item'], item['quantity'],item['size'],f"${item['total_cost']:.2f}"))
                            total_cost += item['total_cost']

                    # Update total cost label
                    self.total_frame.configure(text='Total Cost:'+f" ${total_cost:.2f} ",font=('Arial', 12, 'bold'))
        receipt_query1=f'''SELECT 
                                c.customer_id,
                                COALESCE(p.s_pizza, 0) AS s_pizza,
                                COALESCE(p.m_pizza, 0) AS m_pizza,
                                COALESCE(p.l_pizza, 0) AS l_pizza,
                                COALESCE(b.s_burger, 0) AS s_burger,
                                COALESCE(b.m_burger, 0) AS m_burger,
                                COALESCE(b.l_burger, 0) AS l_burger,
                                COALESCE(c.BUTTER_CHICKEN, 0) AS BUTTER_CHICKEN,
                                COALESCE(c.GRILLED_CHICKEN_WRAP, 0) AS GRILLED_CHICKEN_WRAP,
                                COALESCE(t.t_spice, 1) AS t_spice,
                                COALESCE(w.w_spice, 1) AS w_spice,
                                COALESCE(te.karak, 0) AS karak,
                                COALESCE(te.black_tea, 0) AS black_tea,
                                COALESCE(te.green_tea, 0) AS green_tea,
                                COALESCE(co.latte, 0) AS latte,
                                COALESCE(co.cappuccino, 0) AS cappuccino,
                                COALESCE(co.americano, 0) AS americano,
                                COALESCE(ch.s_choco, 0) AS s_choco,
                                COALESCE(ch.m_choco, 0) AS m_choco,
                                COALESCE(ch.l_choco, 0) AS l_choco,
                                COALESCE(wa.s_watermelon, 0) AS s_watermelon,
                                COALESCE(wa.m_watermelon, 0) AS m_watermelon,
                                COALESCE(wa.l_watermelon, 0) AS l_watermelon,
                                COALESCE(c.ICE_CREAM, 0) AS ICE_CREAM,
                                COALESCE(c.GULAB_JAMUN, 0) AS GULAB_JAMUN,
                                COALESCE(c.CHEESE_CAKE, 0) AS CHEESE_CAKE,
                                COALESCE(c.kunafa, 0) AS kunafa,  
                                c.date_of_order,c.time    
                                    FROM customers c
                                    LEFT JOIN pizza p ON c.customer_id = p.customer_id
                                    LEFT JOIN burger b ON c.customer_id = b.customer_id
                                    LEFT JOIN tikka t ON c.customer_id = t.customer_id
                                    LEFT JOIN wrap w ON c.customer_id = w.customer_id
                                    LEFT JOIN tea te ON c.customer_id = te.customer_id
                                    LEFT JOIN coffee co ON c.customer_id = co.customer_id
                                    LEFT JOIN choco ch ON c.customer_id = ch.customer_id
                                    LEFT JOIN watermelon wa ON c.customer_id = wa.customer_id
                                    LEFT JOIN icecream ic ON c.customer_id = ic.customer_id
                                    LEFT JOIN gulabjamun gu ON c.customer_id = gu.customer_id
                                    LEFT JOIN cheesecake ce ON c.customer_id = ce.customer_id
                                    LEFT JOIN kunafa ku ON c.customer_id = ku.customer_id
                            WHERE c.customer_id = {datababse_customerid};'''
        cursor.execute(receipt_query1)


        rs=cursor.fetchall()


        for i in rs:
            no_s_pizza=int(i[1])# type: ignore
            no_m_pizza=int(i[2])# type: ignore
            no_l_pizza=int(i[3])# type: ignore

            no_s_burger=int(i[4])# type: ignore
            no_m_burger=int(i[5])# type: ignore
            no_l_burger=int(i[6])# type: ignore

            no_butter=int(i[7])# type: ignore
            no_wrap=int(i[8])# type: ignore
            s_butter=int(i[9])# type: ignore
            s_wrap=int(i[10])# type: ignore

            no_karak=int(i[11])# type: ignore
            no_green=int(i[12])# type: ignore
            no_black=int(i[13])# type: ignore

            no_latte=int(i[14])# type: ignore
            no_cappuccino=int(i[15])# type: ignore
            no_americano=int(i[16])# type: ignore

            no_s_milk=int(i[17])# type: ignore
            no_m_milk=int(i[18])# type: ignore
            no_l_milk=int(i[19])# type: ignore

            no_s_melon=int(i[20])# type: ignore
            no_m_melon=int(i[21])# type: ignore
            no_l_melon=int(i[22])# type: ignore

            no_ice=int(i[23])# type: ignore
            no_gulab=int(i[24])# type: ignore
            no_cheese=int(i[25])# type: ignore
            no_kunafa=int(i[26])# type: ignore

            date=i[27]# type: ignore
            time=i[28]# type: ignore


        receipt_tab = ReceiptTab(receipt_toplevel)
        receipt_tab.grid(row=0, column=0, columnspan=1)



receipt_button=tk.Button(database_frame,text="GET RECEIPT",command=get_receipt,relief='sunken')
receipt_button.grid(row=1,column=0)







root.mainloop()  # Start the main event loop
