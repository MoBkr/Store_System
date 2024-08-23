from prettytable import PrettyTable
from tkinter import *
import random

Enn = None
Enn2 = None
def log_in():
    global Enn
    global Enn2
    for widget in root.winfo_children():
        widget.destroy()
    
    
    lb = Label(root, text="Log in", font=("bold", 50), pady=20)
    lbfr = Frame(root, bd=2, relief="solid", width=400, height=500)
    lbb = Label(lbfr, text="UserName: ")
    Enn = Entry(lbfr, bg="light gray", relief="raised")
    lbb2 = Label(lbfr, text="Password: ")
    Enn2 = Entry(lbfr, bg="light gray", relief="raised", show='*')
    btn = Button(root, text="Submit", font=("Arial", 20), padx=40, command=check_correct)
    
    lb.pack()
    lbfr.pack()
    lbb.grid(column=1, row=1)
    Enn.grid(column=2, row=1)
    lbb2.grid(column=1, row=2)
    Enn2.grid(column=2, row=2)
    btn.pack()    

    

products = [
    {"Name": "Water", "Price": 80.0, "Quantity": 1200},
    {"Name": "Soda", "Price": 130.0, "Quantity": 1200},
    {"Name": "Chips", "Price": 75.0, "Quantity": 1200},
    {"Name": "Bread", "Price": 45.0, "Quantity": 1200},
    {"Name": "Eggs", "Price": 65.0, "Quantity": 1200}
]
get_table=None
table = PrettyTable()
def create_table():
    global get_table
    # Add columns
    table.field_names = [i for i in products[0].keys()]
    for dic in products:
        table.add_row(dic.values())
    get_table = table.get_string()

    # Create a Label with a fixed-width font
    lab = Label(lbfr, text=get_table, font=("Courier", 10), justify="left", bg="white")
    lab.pack(pady=10)



verfication_code=None
vrf=None
code=None

        
def check_correct():
    global verification_code, code,ch_verf_Entry
    
    defu_user="Mohamed"
    defu_password="123"
    user = Enn.get()
    password = Enn2.get()
    if user!=defu_user or password!=defu_password:
        Wrong=Label(root,text="Wrong User Name Or Password! \n Plese Enter them Again", fg="red",font=20)
        Wrong.pack()
    else :
        code=str(random.randint(10000 , 1000000))
        Verf=Toplevel(root)
        vrf=Label(Verf,text=f"Your Verfication Code is {code}")
        vrf.pack()
        
        lbfr2 = Frame(root, bd=2, relief="solid", width=400, height=200)
        ch_verf_label=Label(lbfr2,text="Enter Your Verfication Code:")
        ch_verf_Entry=Entry(lbfr2, bg="light gray", relief="raised")
        Verf_btn=Button(lbfr2,text="Verify",command=verf_validate)
        lbfr2.pack(padx=10, pady=10)
        ch_verf_label.grid(column=1,row=1)
        ch_verf_Entry.grid(column=2,row=1)
        Verf_btn.grid(row=2,columnspan=3)
        
        
def verf_validate():
    global verfication_code,code,ch_verf_Entry
    verfication_code = ch_verf_Entry.get()
    if verfication_code ==code:
            for widget in root.winfo_children():
                       widget.destroy()
            
        
            success=Label(root,text="You Have LogIN Successfully", fg="Green",font=('bold',80))
            success.pack(pady=20, padx=20, anchor="center")
            purchase()
    else:
        error=Label(root,text="Wrong Code", fg="Red",font=50)
        error.pack()
        

            

        
        
                    


products = [
    {"Name": "Water", "Price": 80.0, "Quantity": 1200},
    {"Name": "Soda", "Price": 130.0, "Quantity": 1200},
    {"Name": "Chips", "Price": 75.0, "Quantity": 1200},
    {"Name": "Bread", "Price": 45.0, "Quantity": 1200},
    {"Name": "Eggs", "Price": 65.0, "Quantity": 1200}
]
product_name=[]
shopping_cart=[]
askpurch_en=None
ask_quntity=None
total=0
discount=0
def purchase():
       global askpurch_en,ask_frame,ask_quntity
        
       ask_frame=Frame(root, pady=20)
       


    # Create a Label with a fixed-width font
       lab = Label(ask_frame, text=get_table, font=("Courier", 10), justify="left", bg="white")
       
       
       ask_purch=Label(ask_frame,text="What Do You Want to Buy ?",font=("bold",20),fg="red" )
       ask_quntity_label=Label(ask_frame,text= 'Dont Forget to Enter the quntity of the product !',font=30,fg="red")
       askpurch_en=Entry(ask_frame,bg="light gray", relief="raised")
       ask_quntity=Entry(ask_frame,bg="light gray", relief="raised") 
       buy =Button(ask_frame,text="BUY",command=confirmation_exist)
       ask_frame.pack()
       lab.grid(pady=10)
       ask_purch.grid(column=1,row=1)
       askpurch_en.grid(column=2,row=1) 
       ask_quntity_label.grid(column=1,row=2)
       ask_quntity.grid(column=2,row=2) 
       buy.grid(columnspan=2,row=3)
        
        
def confirmation_exist():
    global total
    product_name = [dic["Name"] for dic in products]
    
    if askpurch_en.get() not in product_name:
        Not_exist = Label(ask_frame, text="We do not have this product.", font=30, fg="red")
        Not_exist.grid(row=4, column=2)
        return
    
    for dic in products:
        if askpurch_en.get() == dic["Name"]:
            if int(ask_quntity.get()) > dic["Quantity"]:
                sold_out = Label(ask_frame, text=f"This quantity is not available. ", font=30, fg="red")
                sold_out.grid(row=5, column=2)
                return
            
            # Calculate discount
            quantity = int(ask_quntity.get())
            discount = min((quantity // 250) * 5, 25)
            
            # Calculate total price
            total_price = quantity * dic["Price"]
            discounted_price = total_price * (100 - discount) / 100
            total += discounted_price
            
            # Display discount and total
            disc_label = Label(ask_frame, text=f"You've got a {discount}% discount\nTotal After Discount is {total:.2f} USD", font=("Bold", 30))
            disc_label.grid(row=6, column=1)
            
            # Update product quantity
            dic["Quantity"] -= quantity
            
            break
    
    # Update table display
    tablee = PrettyTable()
    tablee.field_names = [i for i in products[0].keys()]
    for dic in products:
        tablee.add_row(dic.values())
    
    get_tablee = tablee.get_string()
    lab = Label(ask_frame, text=get_tablee, font=("Courier", 10), justify="left", bg="white")
    lab.grid(pady=10)
    
    Again = Label(ask_frame, text="Do you want to add another item?", font=20, fg="red")
    Yes_Again = Button(ask_frame, text="YES", command=Add_Items)
    No_Again = Button(ask_frame, text="NO",command=new_store_or_delivery)
    Again.grid(column=1, row=7)
    Yes_Again.grid(column=2, row=7)
    No_Again.grid(column=3, row=7)
Add=None
add_product=None
add_product_Entry=None
add_quantity=None
add_quantity_En=None
def Add_Items() :
    global Add,add_product,add_product_Entry,add_quantity,add_quantity_En,total
    Add=Toplevel(root)
    add_product=Label(Add,text="What Do You Want To Add",font=30,fg="red")
    add_product_Entry=Entry(Add,bg="light gray", relief="raised")
    add_quantity=Label(Add,text= 'Dont Forget to Enter the quntity of the product !',font=30,fg="red")
    add_quantity_En=Entry(Add,bg="light gray", relief="raised")
    Add_Button=Button(Add,text="Add",command=preforme_Add_items)
    add_product.grid(column=1,row=1,pady=10)
    add_product_Entry.grid(column=2,row=1,pady=10)
    add_quantity.grid(column=1,row=2,pady=10)
    add_quantity_En.grid(column=2,row=2,pady=10)
    Add_Button.grid(columnspan=3,row=3)
def preforme_Add_items():
    global total
    product_name = [dic["Name"] for dic in products]
    
    if add_product_Entry.get() not in product_name:
        Not_exist = Label(Add, text="We do not have this product.", font=30, fg="red")
        Not_exist.grid(row=4, column=2)
        return
    
    for dic in products:
        if add_product_Entry.get() == dic["Name"]:
            if int(add_quantity_En.get()) > dic["Quantity"]:
                sold_out = Label(Add, text=f"This quantity is not available. ", font=30, fg="red")
                sold_out.grid(row=5, column=2)
                return
            
            # Calculate discount
            quantity = int(add_quantity_En.get())
            discount = min((quantity // 250) * 5, 25)
            
            # Calculate total price
            total_price = quantity * dic["Price"]
            discounted_price = total_price * (100 - discount) / 100
            total += discounted_price
            
            # Display discount and total
            disc_label = Label(Add, text=f"You've got a {discount}% discount\nTotal After Discount and add Items {total:.2f} USD", font=("Bold", 30))
            disc_label.grid(row=6, column=1)
            
            # Update product quantity
            dic["Quantity"] -= quantity
            
            break
    
    # Update table display
    tablee = PrettyTable()
    tablee.field_names = [i for i in products[0].keys()]
    for dic in products:
        tablee.add_row(dic.values())
    
    get_tablee = tablee.get_string()
    lab = Label(Add, text=get_tablee, font=("Courier", 10), justify="left", bg="white")
    lab.grid(pady=10)
    

# Visit=None
def new_store_or_delivery():
    global Visit
    Visit=Toplevel(root)
    visit_ask=Label(Visit,text="Do You Want To Visit Our New Staionary Store    ",font=30, fg="red")
    visit_Yes=Button(Visit,text="Yes",command=new_store)
    visit_No=Button(Visit,text="No",command=selcetDelivery)
    
    visit_ask.grid(column=1,row=1,pady=10)
    visit_Yes.grid(column=2,row=1,pady=10,padx=10)
    visit_No.grid(column=3,row=1,pady=10,padx=10)
def new_store():
    global stationary_products,askstore_en,ask_storequntitiy_en
    stationary_products = [  
                    {"Name": "Notebook", "Price": 50.0, "Quantity": 500},
                    {"Name": "Pen", "Price": 10.0, "Quantity": 1000},
                    {"Name": "Pencil", "Price": 5.0, "Quantity": 1500},
                    {"Name": "Eraser", "Price": 3.0, "Quantity": 800},
                    {"Name": "Ruler", "Price": 20.0, "Quantity": 300}]
    table = PrettyTable()
    table.field_names = [i for i in stationary_products[0].keys()]
    for dic in stationary_products:
        table.add_row(dic.values())
    get_table = table.get_string()

    # Create a Label with a fixed-width font
    lab = Label(Visit, text=get_table, font=("Courier", 10), justify="right", bg="white")
    lab.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
    
    # Configure grid weights to center the Label
    Visit.grid_columnconfigure(0, weight=1)
    Visit.grid_columnconfigure(1, weight=1)
    Visit.grid_columnconfigure(2, weight=1)
    Visit.grid_columnconfigure(3, weight=1)
    ask_store=Label(Visit,text="What Do You Want to Buy ?",font=("bold",20),fg="red" )
    ask_quntity_store=Label(Visit,text= 'Dont Forget to Enter the quntity of the product !',font=30,fg="red")
    askstore_en=Entry(Visit,bg="light gray", relief="raised")
    ask_storequntitiy_en=Entry(Visit,bg="light gray", relief="raised") 
    buy_store =Button(Visit,text="BUY",command=purch_story)
    ask_store.grid(column=1,row=3)
    askstore_en.grid(column=2,row=3) 
    ask_quntity_store.grid(column=1,row=4)
    ask_storequntitiy_en.grid(column=2,row=4) 
    buy_store.grid(columnspan=2,row=5)
def purch_story():    
    global total
    product_name_store = [dic["Name"] for dic in stationary_products]
    
    if askstore_en.get() not in product_name_store:
        Not_exist = Label(Visit, text="We do not have this product.", font=30, fg="red")
        Not_exist.grid(row=5, column=2)
        return
    
    for dic in stationary_products:
        if askstore_en.get() == dic["Name"]:
            if int(ask_storequntitiy_en.get()) > dic["Quantity"]:
                sold_out = Label(Visit, text=f"This quantity is not available. ", font=30, fg="red")
                sold_out.grid(row=5, column=2)
                return
            
            # Calculate discount
            quantity = int(ask_storequntitiy_en.get())
            discount = (quantity // 50) * 2
            
            # Calculate total price
            total_price = quantity * dic["Price"]
            discounted_price = total_price * (100 - discount) / 100
            total += discounted_price
            
            # Display discount and total
            disc_label = Label(Visit, text=f"You've got a {discount}% discount\nTotal After Discount and add Items {total:.2f} USD", font=("Bold", 30))
            disc_label.grid(row=6, column=1)
            
            # Update product quantity
            dic["Quantity"] -= quantity
            
            break
    
    # Update table display
    tablee = PrettyTable()
    tablee.field_names = [i for i in stationary_products[0].keys()]
    for dic in stationary_products:
        tablee.add_row(dic.values())
    
    get_tablee = tablee.get_string()
    lab = Label(Visit, text=get_tablee, font=("Courier", 10), justify="left", bg="white")
    lab.grid(pady=10)
    Again = Label(Visit, text="Do you want to add another item?", font=20, fg="red")
    Yes_Again = Button(Visit, text="YES", command=Add_Items_store)
    No_Again = Button(Visit, text="NO",command=selcetDelivery)
    Again.grid(column=1, row=7)
    Yes_Again.grid(column=2, row=7)
    No_Again.grid(column=3, row=7)
store_add = None
ask_store_add = None
ask_quntity_store_add = None
askstore_en_add = None
ask_storequntitiy_en_add = None  # Changed from '0' to None

def Add_Items_store():
    global store_add, askstore_en_add, ask_quntity_store_add, askstore_en_add, ask_storequntitiy_en_add, total
    # Create a new Toplevel window for adding items
    store_add = Toplevel(root)

    # Labels and Entry widgets for item name and quantity
    ask_store_add = Label(store_add, text="What Do You Want To Add", font=30, fg="red")
    askstore_en_add = Entry(store_add, bg="light gray", relief="raised")
    ask_quntity_store_add = Label(store_add, text='Don\'t Forget to Enter the quantity of the product!', font=30, fg="red")
    ask_storequntitiy_en_add = Entry(store_add, bg="light gray", relief="raised")  # Ensure this is an Entry widget

    # Button to add the item
    Add_Button_store = Button(store_add, text="Add", command=preforme_Add_items_store)

    # Layout the widgets in the window
    ask_store_add.grid(column=1, row=1, pady=10)
    askstore_en_add.grid(column=2, row=1, pady=10)
    ask_quntity_store_add.grid(column=1, row=2, pady=10)
    ask_storequntitiy_en_add.grid(column=2, row=2, pady=10)  # Ensure this is Entry widget
    Add_Button_store.grid(columnspan=3, row=3)

def preforme_Add_items_store():
    global total
    product_name_store = [dic["Name"] for dic in stationary_products]

    # Check if the entered product exists
    if askstore_en_add.get() not in product_name_store:
        Not_exist = Label(store_add, text="We do not have this product.", font=30, fg="red")
        Not_exist.grid(row=5, column=2)
        return

    # Check for available quantity and calculate total price with discount
    for dic in stationary_products:
        if askstore_en_add.get() == dic["Name"]:
            if int(ask_storequntitiy_en_add.get()) > dic["Quantity"]:
                sold_out = Label(store_add, text=f"This quantity is not available.", font=30, fg="red")
                sold_out.grid(row=5, column=2)
                return
            
            # Calculate discount
            quantity = int(ask_storequntitiy_en_add.get())
            discount = (quantity // 50) * 2
            
            # Calculate total price after discount
            total_price = quantity * dic["Price"]
            discounted_price = total_price * (100 - discount) / 100
            total += discounted_price
            
            # Display the discount and total price
            disc_label = Label(store_add, text=f"You've got a {discount}% discount\nTotal After Discount and add Items {total:.2f} USD", font=("Bold", 30))
            disc_label.grid(row=6, column=1)
            
            # Update the product quantity in inventory
            dic["Quantity"] -= quantity
            break
    lA_Deliv=Label(store_add,text="Choose your delivery method")
    delivery_charge_btn=Button(store_add,text="delivery_charge ",command=delivery) 
    pickup_charge_btn=Button(store_add,text="pickup_charge ",command=pickup_charge)
    lA_Deliv.grid()
    delivery_charge_btn.grid()
    pickup_charge_btn.grid()
    # Update table display with new quantities
    tablee = PrettyTable()
    tablee.field_names = [i for i in stationary_products[0].keys()]
    for dic in stationary_products:
        tablee.add_row(dic.values())
    get_tablee = tablee.get_string()
    lab = Label(store_add, text=get_tablee, font=("Courier", 10), justify="left", bg="white")
    lab.grid(pady=10)    
    # Optionally add more widgets here if needed to update the GUI with new data

    

    
    

def delivery():
    global total,Delivery_root,get_payment,payment_currency_En
    Delivery_root=Toplevel(root)
    Dekivery_LABEL=Label(Delivery_root,text="200 USD  will Be Adde as Delivery tax",font=40,pady=10)
    total+= 200
    payment_currency =Label(Delivery_root,text="Choose Your payment currency --> USD,EUR,EGP",font=30,pady=10)
    payment_currency_En=Entry(Delivery_root,bg="light gray", relief="raised")
    Selcet_btn=Button(Delivery_root,text="select",command=currency_convert)
    Dekivery_LABEL.grid()
    payment_currency.grid()
    payment_currency_En.grid()
    Selcet_btn.grid()
def pickup_charge ():
    global total,Delivery_root,get_payment,payment_currency_En
    Delivery_root=Toplevel(root)
    Dekivery_LABEL=Label(Delivery_root,text="50 USD  will Be Adde as Delivery tax",font=40,pady=10)
    total+= 50
    payment_currency =Label(Delivery_root,text="Choose Your payment currency --> USD,EUR,EGP",font=30,pady=10)
    payment_currency_En=Entry(Delivery_root,bg="light gray", relief="raised")
    Selcet_btn=Button(Delivery_root,text="select",command=currency_convert)
    Dekivery_LABEL.grid()
    payment_currency.grid()
    payment_currency_En.grid()
    Selcet_btn.grid()
    get_payment=payment_currency_En.get()
def currency_convert():
    global get_payment
    get_payment = payment_currency_En.get()
    if get_payment=="EUR":
        Finally=Label(Delivery_root,text=f"1 USD = .90 EUR\nYour Total In EUR is {total*.90}\nYour order is on the way",font=("bold",50))
        Finally.grid()
        
    elif get_payment=="EGP":
        Finally=Label(Delivery_root,text=f"1 USD = 48.78 EGP\nYour Total In EGP is {total*48.78}\nYour order is on the way",font=("bold",50))
        Finally.grid() 
    else:
        Finally=Label(Delivery_root,text=f"Your Total In USD is {total}\nYour order is on the way",font=("bold",50))
        Finally.grid() 
def selcetDelivery():
    The_Last_Dance=Toplevel(root)
    lA_l=Label(The_Last_Dance,text="Choose your delivery method")
    delivery_charge_btnl=Button(The_Last_Dance,text="delivery_charge ",command=delivery) 
    pickup_charge_btnl=Button(The_Last_Dance,text="pickup_charge ",command=pickup_charge)
    lA_l.grid()
    delivery_charge_btnl.grid()
    pickup_charge_btnl.grid()
        
    
    

        
        
        

root = Tk()
root.title("Groceries Store")

lb1 = Label(root, text="Welcome To Our Store", font=("bold", 50), pady=20)
lbfr = Frame(root, bd=2, relief="solid", width=400, height=500)
lb2 = Label(lbfr, text="Explore Our Price Picks", font=("Arial", 20))
btn=Button(root,text="LogIn",pady=20,font=("Arial",20),padx=40,command=log_in)
lb1.pack()
lbfr.pack(padx=10, pady=10)
lb2.pack(pady=10)
create_table()
btn.pack()
root.mainloop()
