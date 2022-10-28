import os
import random
from time import sleep
import mysql.connector
from rich.progress import track
from rich.console import Console
from prettytable import PrettyTable


console=Console()
dbTable = PrettyTable()
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="library"
)
mycursor=db.cursor()
no=random.randint(1000,9999)

def processing():
    for _ in track(range(100),description='[blue]Procesing'):
               sleep(0.03) 
# base = Style.parse("cyan")


def admin_login1(name1):
    try:
        name1=(name1,)
        sqlquery1="select username from admin_details"
        mycursor.execute(sqlquery1)
        result=mycursor.fetchall()
        for i in result:
            if name1==i:
                flag=1
                break
            else:
                flag=0
        return flag
    except:
        return 0

def admin_login2(id1):
    try:
        id1=int(id1)
        sqlquery1="select admin_id from admin_details"
        mycursor.execute(sqlquery1)
        result=mycursor.fetchall()
        for i in result:
            for j in i:
                if j==id1:
                    return 1            
                else:
                    flag=0
        return flag
    except:
        return 0


def admin_login3(username,pass1):
    flag=1
    username=[username,username]
    pass1=[(pass1,)]
    sqlquery1="select pass from admin_details where username=%s or admin_id=%s"
    mycursor.execute(sqlquery1,username)
    result=mycursor.fetchall()
    if result==pass1:
        return 1
    else:
        flag=0
    return flag

def cus_login1(name1):
    try:
        name1=(name1,)
        sqlquery1="select first_name from customer_details"
        mycursor.execute(sqlquery1)
        result=mycursor.fetchall()
        for i in result:
            if name1==i:
                return 1
            else:
                flag=0
        return flag
    except:
        return 0

def cus_login2(id1):
    try:
        id1=int(id1)
        sqlquery1="select cus_id from customer_details"
        mycursor.execute(sqlquery1)
        result=mycursor.fetchall()
        for i in result:
            for j in i:
                if id1==j:
                    return 1
                else:
                    flag=0
        return flag
    except:
        return 0

def cus_login3(username,pass1):
    flag=1
    username=[username,username]
    pass1=[(pass1,)]
    sqlquery1="select pass from customer_details where first_name=%s or cus_id=%s"
    mycursor.execute(sqlquery1,username)
    result=mycursor.fetchall()
    if result==pass1:
        return 1
    else:
        flag=0
    return flag

def profile(name,id):
    try:
        processing()
        query=[id,name]
        mycursor.execute("SELECT first_name, mid_name, last_name, ph_no, address, cus_id from customer_details where cus_id=%s or first_name=%s",query)
        dbTable.field_names = [ "First name", "Mid name","Last name","Contact no.", "Address","Id no."]
        for data in mycursor:
            dbTable.add_row(data)
        print(dbTable)
        dbTable.clear()
    except:
        print("error!!!")


def view_all():
    console.print("  -----------------------------------------Displaying All Books-----------------------------------",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details")
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    dbTable.clear()
    
#wrt type
def view_specific1(typ1):  
    typ1='%'+typ1+'%'
    typ1=(typ1,)
    console.print("Displaying Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details where book_type LIKE %s",typ1)
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    console.print("!. if table is empty, means book with following type is not present.",style="yellow")
    console.print("Done!!",style="bold cyan")
    dbTable.clear()
    

#wrt name
def view_specific2(name1):  
    name1='%'+name1+'%'
    name1=(name1,)
    console.print("Displaying Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details where book_name LIKE %s",name1)
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    console.print("!. if table is empty, means book with following name is not present.",style="yellow")
    console.print("Done!!",style="bold cyan")
    dbTable.clear()
    

#wrt author name
def view_specific3(typ1):  
    typ1='%'+typ1+'%'
    typ1=(typ1,)
    console.print("Displaying Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details where author_name LIKE %s",typ1)
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    console.print("!. if table is empty, means book with following author name is not present.",style="yellow")
    console.print("Done!!",style="bold cyan")
    dbTable.clear()
    

#wrt code
def view_specific4(name1):  
    name1='%'+name1+'%'
    name1=(name1,)
    console.print("Displaying Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details where book_code LIKE %s",name1)
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    console.print(dbTable)
    console.print("!. if table is empty, means book with following id is not present.",style="yellow")
    console.print("Done!!",style="bold cyan")
    dbTable.clear()
    

def withdrawal_book(code):
    try:
        int(code)
        code=(code,)    
        mycursor.execute("SELECT status from books_details where book_code=%s",code)    
        a1=mycursor.fetchall()     
        b1=[(1,)]
        mycursor.execute("select count(book_code) from books_details where book_code=%s",code)
        a=mycursor.fetchall()
        b=[(1,)]
        if a==b and a1==b1:
            console.print("withdrawaling Books...",style="bold cyan")
            processing()
            mycursor.execute("update books_details set status=0 where book_code=%s",code)
            db.commit()
            console.print("book successfully withdrawled!!!",style="green")
            console.print("Book deatils..",style="cyan")
            mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details where book_code=%s",code)
            dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
            for data in mycursor:
                dbTable.add_row(data)
            console.print(dbTable)
        elif a==b and a1!=b1:
            console.print(f"Book with {code} code is not available right now.",style="bold red")
            console.print("Book you want is already withrawled by someone.",style="blue")
            console.print("TRY: Enter another correct valid book code",style="green")
        else:
            console.print(f"Book with {code} code is not available right now.",style="bold red")
            console.print("Book you want does not exist in our database.",style="blue")
            console.print("TRY: Enter another correct valid book code",style="green")
    except:
        console.print("ERROR: Something error occured!!!",style="bold red")
        console.print("TRY: Enter valid book code",style="green") 
    dbTable.clear()

def return_book(code):
    try:
        int(code)
        code=(code,)    
        mycursor.execute("SELECT status from books_details where book_code=%s",code)    
        a1=mycursor.fetchall()     
        b1=[(0,)]
        mycursor.execute("select count(book_code) from books_details where book_code=%s",code)
        a=mycursor.fetchall()
        b=[(1,)]
        if a==b and a1==b1:
                console.print("returning Books...",style="bold cyan")
                processing()
                mycursor.execute("update books_details set status=1 where book_code=%s",code)
                db.commit()
                console.print("book successfully returned!!!",style="green")
                console.print("Book deatils..",style="cyan")
                mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details where book_code=%s",code)
                dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
                for data in mycursor:
                    dbTable.add_row(data)
                console.print(dbTable)
        elif a==b and a1!=b1:
            console.print("ERROR: ",style="yellow")
            console.print("Book you are returning already present in our database and was never withdrawled.",style="blue")
            console.print("TRY: Enter another correct valid book code",style="green") 
        else:
            console.print("ERROR: invalid code!!!",style="bold red")
            console.print("The book you are returning does'nt exist in our database.",style="blue")
            console.print("TRY: Enter another correct valid book code",style="green") 
    except:
        console.print("ERROR: Something error occured!!!",style="bold red")
        console.print("TRY: Enter valid book code",style="green") 
    dbTable.clear()

#sorting functions...
def sort_by_name():
    console.print("  Displaying All Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details order by book_name asc")
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    console.print("Print table order by book name.",style="blue")
    dbTable.clear()

def sort_by_price():
    console.print("  Displaying All Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details order by price asc")
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    console.print("Print table order by price.",style="blue")
    dbTable.clear()
    
def sort_by_author():
    console.print("  Displaying All Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details order by author_name asc")
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    console.print("Print table order by author names.",style="blue")
    dbTable.clear()
    
def sort_by_type():
    console.print("  Displaying All Books...",style="bold cyan")
    processing()
    mycursor.execute("SELECT book_name,book_code,author_name,book_type,status,price from books_details order by book_type asc")
    dbTable.field_names = [ "Books", "Book code","Author","Catagory", "Status","Price"]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    console.print("Print table order by type.",style="blue")
    dbTable.clear()
    
#       functions for admin......
def show_cus_details():
    console.print("  Displaying Customers Details...",style="bold cyan")
    processing()
    mycursor.execute("SELECT first_name,mid_name,last_name,ph_no,address,cus_id from customer_details")
    dbTable.field_names = [ "First name","Mid name","Last name","Contact no.","Address","Customer id."]
    for data in mycursor:
        dbTable.add_row(data)
    print(dbTable)
    dbTable.clear()

#update name1..
def edit_name1(name1,cus):
    cus=int(cus)
    val=(name1,cus)
    console.print("Updating Customers Details...",style="bold cyan")
    processing()
    mycursor.execute("update customer_details set first_name =%s where cus_id =%s",val)
    db.commit()

#update name2..
def edit_name2(name2,cus):
    cus=int(cus)
    val=(name2,cus)
    console.print("Updating Customers Details...",style="bold cyan")
    processing()
    mycursor.execute("update customer_details set mid_name =%s where cus_id =%s",val)
    db.commit()

#update name3..
def edit_name3(name3,cus):
    cus=int(cus)
    val=(name3,cus)
    console.print("Updating Customers Details...",style="bold cyan")
    processing()
    mycursor.execute("update customer_details set last_name =%s where cus_id =%s",val)
    db.commit()

#update contact no...
def edit_ph_no3(no,cus):
    try:
        no=int(no)
        if len(no)==10:
            cus=int(cus)
            val=(no,cus)
            console.print("Updating Customers Details...",style="bold cyan")
            processing()
            mycursor.execute("update customer_details set ph_no =%s where cus_id =%s",val)
            db.commit()
        else:
            console.print("ERROR: Invalid phone number",style="bold red")
    except:
        console.print("ERROR: Something error occured!!!",style="bold red")
        console.print("Invalid phone number",style="red")

#update address...
def edit_address(address,cus):      
    console.print("Updating Customers Details...",style="bold cyan")
    processing()
    val=(address,cus)
    mycursor.execute("update customer_details set ph_no =%s where cus_id =%s",val)
    db.commit()
    
 
#add new book
def add_book(b_name,author,b_type,price):
    try:
        b_code=(no,)
        mycursor.execute("select count(book_code) from books_details where book_code=%s",b_code)
        a=mycursor.fetchall()
        b=[(1,)]
        if a!=b:
            console.print("Adding new book in database...",style="bold cyan")
            processing()
            val=(b_name,no,author,b_type,1,price)
            mycursor.execute("INSERT into books_details values(%s,%s,%s,%s,%s,%s)",val)
            db.commit()
        else:
            console.print("ERROR: Redundant code generated!!!",style="bold red")
            console.print("TRY: Try again with same book details..",style="green")
    except:
        console.print("ERROR: Something error occured!!!",style="bold red")
        console.print("TRY: Try again",style="green")
    dbTable.clear()

#remove a book
def remove_book(b_code):
    try:
        int(b_code)
        b_code=(b_code,)    
        mycursor.execute("SELECT status from books_details where book_code=%s",b_code)    
        a1=mycursor.fetchall()     
        b1=[(1,)]
        mycursor.execute("select count(book_code) from books_details where book_code=%s",b_code)
        a=mycursor.fetchall()
        b=[(1,)]
        if a==b and a1==b1:
            console.print("Removing book from database...",style="bold cyan")
            processing()
            mycursor.execute("DELETE from books_details where book_code=%s",b_code)
            db.commit()
        elif a==b and a1!=b1:
            console.print(f"Book with {b_code} is currently unavailable.\nIt may be borrowed by any customer")
        else:
            console.print(f"No book with {b_code} found in our database...")
    except:
        console.print("ERROR: Something error occured!!!",style="bold red")
        console.print("TRY: Enter valid book code",style="green") 
    dbTable.clear()

#add new customer id
def add_customer(f_name,m_name,l_name,passwd='1234',ph_no=111,address='Maharashtra, India'):
    try:
        c_id=(no,)
        mycursor.execute("select count(cus_id) from customer_details where cus_id=%s",c_id)
        a=mycursor.fetchall()
        b=[(1,)]
        if a!=b:
            mycursor.execute("select ph_no from customer_details")
            a=mycursor.fetchall()
            for i in a:
                    for j in i:
                        #111 means customer hasnt given any ph no by himself
                        if ph_no!=111 and ph_no==j:
                            flag=0
                            break
                            #flag 0= not acceptable
                        elif ph_no==111:
                            flag=1
                            break
                        elif ph_no!=111 and ph_no!=j:
                            flag=1
                        else:
                            flag=1
            if flag==1:
                console.print("Adding new customer id in database...",style="bold cyan")
                processing()
                val=(f_name,m_name,l_name,ph_no,address,no,passwd)
                mycursor.execute("INSERT into customer_details values(%s,%s,%s,%s,%s,%s,%s)",val)
                db.commit()
            else:
                console.print("ERROR: Error in inserted data!!!",style="bold red")
                console.print("TRY: check details (phone no) Try again..",style="green")
        else:
            console.print("ERROR: Redundant customer id appeared!!!",style="bold red")
            console.print("TRY: Try again with same details..",style="green")
    except:
        console.print("ERROR: Something error occured!!!",style="bold red")
        console.print("TRY: Try again",style="green")
    dbTable.clear()


#remove a customer
def remove_customer(c_id):
    try:
        c_id=(c_id,)    
        mycursor.execute("select count(cus_id) from customer_details where cus_id=%s",c_id)
        a=mycursor.fetchall()
        b=[(1,)]
        if a==b:
            console.print("Removing customer login from database...",style="bold cyan")
            processing()
            mycursor.execute("DELETE from customer_details where cus_id=%s",c_id)
            db.commit()
        else:
            console.print(f"No customer with {c_id} id found in our database...")
    except:
        console.print("ERROR: Something error occured!!!",style="bold red")
        console.print("TRY: Enter valid customer id.",style="green") 
    dbTable.clear()


#customer login code....     
class cus_stuff:

    def cus_menu(self):
        while True:
            menu = ('''
                        [bold green]+--------------------------------------------------------+[/bold green ]
                        [bold green]|[/bold green][bold blue]                   Student's Menu                       [/bold blue][bold green]|[/bold green]
                        [bold green]+--------------+-----------------------------------------+[/bold green ]
                        [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]            Actions                      [/bold cyan][bold green]|[/bold green]
                        [bold green]+--------------+-----------------------------------------+[/bold green]
                        [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] View books in database.[/cyan]            [bold green]   |[/bold green]
                        [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] Search for any book.[/cyan]               [bold green]   |[/bold green]
                        [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] View your profile.[/cyan]                 [bold green]   |[/bold green]
                        [bold green]|[cyan]      4.      [/cyan]|[/bold green]  [cyan] Withdrawl book.[/cyan]                    [bold green]   |[/bold green]
                        [bold green]|[cyan]      5.      [/cyan]|[/bold green]  [cyan] Return book.[/cyan]                       [bold green]   |[/bold green]
                        [bold green]|[cyan]      6.      [/cyan]|[/bold green]  [cyan] Back.                                [/cyan][bold green] |[/bold green]
                        [bold green]+--------------+-----------------------------------------+[/bold green]''')
            console.print(menu)
            ch=input("\t\t~Enter short-key: ")
            if ch=='1':
                os.system("cls")
                menu1 = ('''        [bold green][bold blue]             Choice 1:View books in database.          [/bold blue][/bold green ]
                            [bold green]+--------------+--------------------------------------------------+[/bold green ]
                            [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]                 Actions                          [/bold cyan][bold green]|[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]
                            [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] View all books.[/cyan]                         [bold green]       |[/bold green]
                            [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] View books in sorted order(sort by book name).[/cyan][bold green] |[/bold green]
                            [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] View books (sort by price)[/cyan]                  [bold green]   |[/bold green]
                            [bold green]|[cyan]      4.      [/cyan]|[/bold green]  [cyan] View books (sort by type)[/cyan]                  [bold green]    |[/bold green]
                            [bold green]|[cyan]      5.      [/cyan]|[/bold green]  [cyan] View books (sort by author name)[/cyan]        [bold green]       |[/bold green]
                            [bold green]|[cyan]      6.      [/cyan]|[/bold green]  [cyan] Back.                                     [/cyan][bold green]     |[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]''')
                while True:
                    console.print(menu1)
                    ch1=input("\t\t~Enter short-key: ")
                    if ch1=='1':
                        os.system("cls")
                        view_all()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='2':
                        os.system("cls")
                        sort_by_name()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='3':
                        os.system("cls")
                        sort_by_price()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='4':
                        os.system("cls")
                        sort_by_type()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='5':
                        os.system("cls")
                        sort_by_author()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='6':
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                        os.system("pause")
                    os.system("cls")
            elif ch=='2':
                os.system("cls")
                menu2 = ('''        [bold green][bold blue]             Choice 1:Search for any book.          [/bold blue][/bold green ]
                            [bold green]+--------------+--------------------------------------------------+[/bold green ]
                            [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]                 Actions                          [/bold cyan][bold green]|[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]
                            [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] Search book by it's book name.[/cyan]          [bold green]       |[/bold green]
                            [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] Search book by it's type.[/cyan]                     [bold green] |[/bold green]
                            [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] Search book by it's book id.[/cyan]                [bold green]   |[/bold green]
                            [bold green]|[cyan]      4.      [/cyan]|[/bold green]  [cyan] Search book by it's author name.[/cyan]           [bold green]    |[/bold green]
                            [bold green]|[cyan]      5.      [/cyan]|[/bold green]  [cyan] Back.                                     [/cyan][bold green]     |[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]''')
                while True:
                    console.print(menu2)
                    ch2=input("\t\t~Enter short-key: ")
                    if ch2=='1':
                        os.system("cls")
                        name=input("\t\t~Enter book name: ")
                        view_specific2(name)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='2':
                        os.system("cls")
                        type=input("\t\t~Enter book type: ")
                        view_specific1(type)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='3':
                        os.system("cls")
                        b_id=input("\t\t~Enter book code: ")
                        view_specific4(b_id)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='4':
                        os.system("cls")
                        author=input("\t\t~Enter author name: ")
                        view_specific3(author)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='5':
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                        os.system("pause")
                    os.system("cls")
            elif ch=='3':
                menu3 = ('''[bold green][bold blue]             Choice 3:View your profile.          [/bold blue][/bold green ]''')
                os.system("cls")
                console.print(menu3)
                profile(cus_stuff.user,cus_stuff.user)
                os.system("pause")
                os.system("cls")
            elif ch=='4':
                menu3 = ('''[bold green][bold blue]             Choice 4:Withdrawl a book.          [/bold blue][/bold green ]''')
                os.system("cls")
                console.print(menu3)
                code=input("\t\t~Enter a valid book id/book code : ")
                withdrawal_book(code)
                os.system("pause")
                os.system("cls")
            elif ch=='5':
                menu3 = ('''[bold green][bold blue]             Choice 5:Return a book.          [/bold blue][/bold green ]''')
                os.system("cls")
                console.print(menu3)
                code=input("\t\t~Enter a valid book id/book code : ")
                return_book(code)
                os.system("pause")
                os.system("cls")
            elif ch=='6':
                os.system("cls")
                break
            else:
                os.system("cls")
                console.print("\t\t","[bold underline red]ERROR: Invalid choice. [/bold underline red]\n")
    def cus_login(self):
        while True:
            console.print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            console.print("\t\t[bold green]|[/bold green][bold cyan]                            Student Login                                  [/bold cyan][bold green]|[/bold green]")
            console.print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            console.print("\t\t[bold green]|[/bold green][bold cyan]            [ Please enter the Valid Username and password ]               [/bold cyan][bold green]|[/bold green]")
            console.print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            console.print("\t\t[bold red]!. Enter x in username to go back.. [/bold red]")
            cus_stuff.user =  input("\t\t~ Username or id: ")
            if cus_stuff.user!="x" and cus_stuff.user!="X":
                a=cus_login1(cus_stuff.user)
                b=cus_login2(cus_stuff.user)
                if a==1 or b==1:
                    passwd = input("\t\t~ Password: ")
                    c=cus_login3(cus_stuff.user,passwd)
                    if c==1:
                        os.system("cls")
                        console.print("\t\t[bold green]Success: Access Granted[/bold green]")
                        cus_stuff.cus_menu(self)
                        os.system("cls")
                    else:
                        os.system("cls")
                        console.print("\t\t[bold underline red]ERROR: INCORRECT PASSWORD [/bold underline red]\n")
                        return self.cus_login() 
                else:
                    os.system("cls")
                    console.print("\t\t","[bold underline red]ERROR: INCORRECT USERNAME OR ID [/bold underline red]\n")
            else:
                os.system("cls")
                break

#Admin login code....     
class admin_stuff:
    def admin_menu(self):
        while True:
            menu = ('''
                        [bold green]+--------------------------------------------------------+[/bold green ]
                        [bold green]|[/bold green][bold blue]                   Admin's Menu                         [/bold blue][bold green]|[/bold green]
                        [bold green]+--------------+-----------------------------------------+[/bold green ]
                        [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]            Actions                      [/bold cyan][bold green]|[/bold green]
                        [bold green]+--------------+-----------------------------------------+[/bold green]
                        [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] View books in database.[/cyan]            [bold green]   |[/bold green]
                        [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] Search for any book.[/cyan]               [bold green]   |[/bold green]
                        [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] View students details.[/cyan]             [bold green]   |[/bold green]
                        [bold green]|[cyan]      4.      [/cyan]|[/bold green]  [cyan] Edit students details.[/cyan]             [bold green]   |[/bold green]
                        [bold green]|[cyan]      5.      [/cyan]|[/bold green]  [cyan] Add/Remove book in database[/cyan]        [bold green]   |[/bold green]
                        [bold green]|[cyan]      6.      [/cyan]|[/bold green]  [cyan] Add/Remove any student id in database[/cyan][bold green] |[/bold green]
                        [bold green]|[cyan]      7.      [/cyan]|[/bold green]  [cyan] Back.                                [/cyan][bold green] |[/bold green]
                        [bold green]+--------------+-----------------------------------------+[/bold green]''')
            console.print(menu)
            ch=input("\t\t~Enter short-key: ")
            if ch=='1':
                os.system("cls")
                menu1 = ('''        [bold green][bold blue]             Choice 1:View books in database.          [/bold blue][/bold green ]
                            [bold green]+--------------+--------------------------------------------------+[/bold green ]
                            [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]                 Actions                          [/bold cyan][bold green]|[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]
                            [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] View all books.[/cyan]                         [bold green]       |[/bold green]
                            [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] View books in sorted order(sort by book name).[/cyan][bold green] |[/bold green]
                            [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] View books (sort by price)[/cyan]                  [bold green]   |[/bold green]
                            [bold green]|[cyan]      4.      [/cyan]|[/bold green]  [cyan] View books (sort by type)[/cyan]                  [bold green]    |[/bold green]
                            [bold green]|[cyan]      5.      [/cyan]|[/bold green]  [cyan] View books (sort by author name)[/cyan]        [bold green]       |[/bold green]
                            [bold green]|[cyan]      6.      [/cyan]|[/bold green]  [cyan] Back.                                     [/cyan][bold green]     |[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]''')
                while True:
                    console.print(menu1)
                    ch1=input("\t\t~Enter short-key: ")
                    if ch1=='1':
                        os.system("cls")
                        view_all()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='2':
                        os.system("cls")
                        sort_by_name()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='3':
                        os.system("cls")
                        sort_by_price()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='4':
                        os.system("cls")
                        sort_by_type()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='5':
                        os.system("cls")
                        sort_by_author()
                        os.system("pause")
                        os.system("cls")
                    elif ch1=='6':
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                        os.system("pause")
                    os.system("cls")
            elif ch=='2':
                os.system("cls")
                menu2 = ('''        [bold green][bold blue]             Choice 1:Search for any book.          [/bold blue][/bold green ]
                            [bold green]+--------------+--------------------------------------------------+[/bold green ]
                            [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]                 Actions                          [/bold cyan][bold green]|[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]
                            [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] Search book by it's book name.[/cyan]          [bold green]       |[/bold green]
                            [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] Search book by it's type.[/cyan]                     [bold green] |[/bold green]
                            [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] Search book by it's book id.[/cyan]                [bold green]   |[/bold green]
                            [bold green]|[cyan]      4.      [/cyan]|[/bold green]  [cyan] Search book by it's author name.[/cyan]           [bold green]    |[/bold green]
                            [bold green]|[cyan]      5.      [/cyan]|[/bold green]  [cyan] Back.                                     [/cyan][bold green]     |[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]''')
                while True:
                    console.print(menu2)
                    ch2=input("\t\t~Enter short-key: ")
                    if ch2=='1':
                        os.system("cls")
                        name=input("\t\t~Enter book name: ")
                        view_specific2(name)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='2':
                        os.system("cls")
                        type=input("\t\t~Enter book type: ")
                        view_specific1(type)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='3':
                        os.system("cls")
                        b_id=input("\t\t~Enter book code: ")
                        view_specific4(b_id)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='4':
                        os.system("cls")
                        author=input("\t\t~Enter author name: ")
                        view_specific3(author)
                        os.system("pause")
                        os.system("cls")
                    elif ch2=='5':
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                        os.system("pause")
                    os.system("cls")
            elif ch=='3':
                menu3 = ('''[bold green][bold blue]             Choice 3:View students details.          [/bold blue][/bold green ]''')
                os.system("cls")
                console.print(menu3)
                show_cus_details()
                os.system("pause")
                os.system("cls")
            elif ch=='4':
                os.system("cls")
                menu3 = ('''        [bold green][bold blue]             Choice 4:Edit student details.          [/bold blue][/bold green ]
                            [bold green]+--------------+--------------------------------------------------+[/bold green ]
                            [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]                 Actions                          [/bold cyan][bold green]|[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]
                            [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] Update first name.[/cyan]                      [bold green]       |[/bold green]
                            [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] Update mid name.[/cyan]                              [bold green] |[/bold green]
                            [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] Update last name.[/cyan]                           [bold green]   |[/bold green]
                            [bold green]|[cyan]      4.      [/cyan]|[/bold green]  [cyan] Update contact no.[/cyan]                         [bold green]    |[/bold green]
                            [bold green]|[cyan]      5.      [/cyan]|[/bold green]  [cyan] Update address.[/cyan]                         [bold green]       |[/bold green]
                            [bold green]|[cyan]      6.      [/cyan]|[/bold green]  [cyan] Check updated records.[/cyan]                  [bold green]       |[/bold green]
                            [bold green]|[cyan]      7.      [/cyan]|[/bold green]  [cyan] Back.                                     [/cyan][bold green]     |[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]''')
                while True:
                    console.print(menu3)
                    console.print("!. Before updating any record, make sure to enter correct student id or no records wil change.",style="yellow")
                    ch3=input("\t\t~Enter short-key: ")
                    if ch3=='1':
                        os.system("cls")
                        try:
                            id=input("\t\t~Enter student id: ")
                            f_name=input("\t\t~Enter new 'first name': ")
                            edit_name1(f_name,id)
                        except:
                            console.print("\t\t\t[red]ERROR: Something went wrong!!! [/red]")
                            console.print("\t\t\t[green]TRY: Changes haven't commited so try this activity again.[/green]")
                        os.system("pause")
                        os.system("cls")
                    elif ch3=='2':
                        os.system("cls")
                        try:
                            id=input("\t\t~Enter student id: ")
                            m_name=input("\t\t~Enter new 'mid name': ")
                            edit_name2(m_name,id)
                        except:
                            console.print("\t\t\t[red]ERROR: Something went wrong!!! [/red]")
                            console.print("\t\t\t[green]TRY: Changes haven't commited so try this activity again.[/green]")
                        os.system("pause")
                        os.system("cls")
                    elif ch3=='3':
                        os.system("cls")
                        try:
                            id=input("\t\t~Enter student id: ")
                            l_name=input("\t\t~Enter new 'last name': ")
                            edit_name3(l_name,id)
                        except:
                            console.print("\t\t\t[red]ERROR: Something went wrong!!! [/red]")
                            console.print("\t\t\t[green]TRY: Changes haven't commited so try this activity again.[/green]")
                        os.system("pause")
                        os.system("cls")
                    elif ch3=='4':
                        os.system("cls")
                        try:
                            id=input("\t\t~Enter student id: ")
                            no=input("\t\t~Enter new 'ph no.': ")
                            edit_ph_no3(no,id)
                        except:
                            console.print("\t\t\t[red]ERROR: Something went wrong!!! [/red]")
                            console.print("\t\t\t[green]TRY: Changes haven't commited so try this activity again.[/green]")
                        os.system("pause")
                        os.system("cls")
                    elif ch3=='5':
                        os.system("cls")
                        try:
                            id=input("\t\t~Enter student id: ")
                            address=input("\t\t~Enter new 'ph no.': ")
                            edit_address(address,id)
                        except:
                            console.print("\t\t\t[red]ERROR: Something went wrong!!! [/red]")
                            console.print("\t\t\t[green]TRY: Changes haven't commited so try this activity again.[/green]")
                        os.system("pause")
                        os.system("cls")
                    elif ch3=='6':
                        os.system("cls")
                        show_cus_details()
                        console.print("Here you can check all updated records.",style="blue")
                        os.system("pause")
                        os.system("cls")
                    elif ch3=='7':
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                        os.system("pause")
                    os.system("cls")
            elif ch=='5':
                menu5 = ('''        [bold green][bold blue]             Choice 5:Add/Remove book in database.          [/bold blue][/bold green ]
                            [bold green]+--------------+--------------------------------------------------+[/bold green ]
                            [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]                 Actions                          [/bold cyan][bold green]|[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]
                            [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] Add a new book in databse.[/cyan]              [bold green]       |[/bold green]
                            [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] Remove any existing book from databse..[/cyan]       [bold green] |[/bold green]
                            [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] Back.[/cyan]                                       [bold green]   |[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]''')
                os.system("cls")
                while True:
                    console.print(menu5)
                    ch4=input("\t\t~Enter short-key: ")
                    if ch4=='1':
                        os.system("cls")
                        console.print("!. Fill following book details carefully...\nOnce book is added, changes are not possible.",style="yellow")
                        b_name=input("\t\t~Enter book name: ")
                        author=input("\t\t~Enter author name: ")
                        b_type=input("\t\t~Enter book type-sub_type: ")
                        price=input("\t\t~Enter price of book: ")
                        add_book(b_name,author,b_type,price)
                        os.system("pause")
                        os.system("cls")
                    elif ch4=='2':
                        os.system("cls")
                        console.print("!. Enter correct book code or no book will be removed.",style="yellow")
                        b_code=input("\t\t~Enter book code/book id: ")
                        remove_book(b_code)
                        os.system("pause")
                        os.system("cls")
                    elif ch4=='3':
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                        os.system("pause")
                    os.system("cls")
            elif ch=='6':
                os.system("cls")
                menu6 = ('''        [bold green][bold blue]             Choice 6:Add/Remove any student id from database.          [/bold blue][/bold green ]
                            [bold green]+--------------+--------------------------------------------------+[/bold green ]
                            [bold green]|[bold cyan]Short keys    [/bold cyan]|[bold cyan]                 Actions                          [/bold cyan][bold green]|[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]
                            [bold green]|[cyan]      1.      [/cyan]|[/bold green]  [cyan] Add new student login id in databse.[/cyan]    [bold green]       |[/bold green]
                            [bold green]|[cyan]      2.      [/cyan]|[/bold green]  [cyan] Remove any existing student login id.[/cyan]         [bold green] |[/bold green]
                            [bold green]|[cyan]      3.      [/cyan]|[/bold green]  [cyan] Back.[/cyan]                                       [bold green]   |[/bold green]
                            [bold green]+--------------+--------------------------------------------------+[/bold green]''')
                while True:
                    console.print(menu6)
                    ch4=input("\t\t~Enter short-key: ")
                    if ch4=='1':
                        os.system("cls")
                        console.print("!. Enter '-' for optional fields, if you don't\n want to fill any specific optional information.",style="yellow")
                        f_name=input("\t\t~Enter first name: ")
                        m_name=input("\t\t~Enter middle name: ")
                        l_name=input("\t\t~Enter last name: ")
                        ph_n=input("\t\t~Enter contact no. name(optional): ")
                        addre=input("\t\t~Enter address(optional): ")
                        passwd=input("\t\t~Enter correct 6 digit password: ")
                        if len(passwd)==6:
                            if ph_n=='-' and addre=='-':
                                add_customer(f_name,m_name,l_name,passwd)
                            elif ph_n!='-' and addre=='-':
                                add_customer(f_name,m_name,l_name,passwd,ph_no=ph_n)
                            elif ph_n=='-' and addre!='-':
                                add_customer(f_name,m_name,l_name,passwd,address=addre)
                            elif ph_n!='-' and addre!='-':
                                add_customer(f_name,m_name,l_name,passwd,ph_n,addre)
                            else:
                                console.print("\t\t\t[bold red]ERROR: Something went wrong[/bold red]")
                                console.print("\t\t\t[green]ERROR: Try again.[/green]")
                        else:
                            console.print("ERROR: Make password with of 6 digits!.",style="red")
                        os.system("pause")
                        os.system("cls")
                    elif ch4=='2':
                        os.system("cls")
                        console.print("!. Enter correct student code or no student id will be removed.",style="yellow")
                        c_id=input("\t\t~Enter student code/student id: ")
                        remove_customer(c_id)
                        os.system("pause")
                        os.system("cls")
                    elif ch4=='3':
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                        os.system("pause")
                    os.system("cls")
            elif ch=='7':
                os.system("cls")
                break
            else:
                os.system("cls")
                console.print("\t\t\t[bold underline red]ERROR: INCORRECT CHOICE [/bold underline red]")
                return self.admin_menu()

    def admin_login(self):
        while True: 
            console.print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            console.print("\t\t[bold green]|[/bold green][bold cyan]                            Adiminstrator Login                            [/bold cyan][bold green]|[/bold green]")
            console.print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            console.print("\t\t[bold green]|[/bold green][bold cyan]            [ Please enter the Valid Username and password ]               [/bold cyan][bold green]|[/bold green]")
            console.print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            console.print("\t\t[bold red]!. Enter x in username to go back. [/bold red]")
            user=input("\t\t~ Username or id: ")
            if user != 'x' and user!='X':
                a=admin_login1(user)
                b=admin_login2(user)
                if a==1 or b==1:
                    passwd = input("\t\t~ Password: ")
                    c=admin_login3(user,passwd)
                    if c==1:
                        os.system("cls")
                        console.print("\t\t[bold green]Success: Access Granted[/bold green]")
                        os.system("pause")
                        os.system("cls")
                        admin_stuff.admin_menu(self)
                        os.system("cls")
                    else:
                        os.system("cls")
                        console.print("\t\t[bold underline red]ERROR: INCORRECT PASSWORD [/bold underline red]\n")
                        return self.admin_login() 
                else:
                    os.system("cls")
                    console.print("\t\t","[bold underline red]ERROR: INCORRECT USERNAME OR ID [/bold underline red]\n")
            else:
                os.system("cls")
                break

class start:
    def login(self):
        while True:
            try:
                console.print("\t\t\t\t\t\tLibraray Management System",style="yellow")
                console.print("\t\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
                console.print("\t\t\t[bold green]|                             [ LOGIN PAGE]                                 |[/bold green]")
                console.print("\t\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
                console.print("\t\t\t[bold green]|                                                                           |[/bold green]")
                console.print("\t\t\t[bold green]|[/bold green][bold cyan]                        1. Adiminstrator Login                            [/bold cyan] [bold green]|[/bold green]")
                console.print("\t\t\t[bold green]|[/bold green][bold cyan]                        2. Student Login                                  [/bold cyan] [bold green]|[/bold green]")
                console.print("\t\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
                console.print("\t\t[bold red]!. Enter x to quit. [/bold red]")
                ch = input("\t\t\t~ Enter: ")
                os.system("cls")
                if ch != 'x' and ch!='X':
                    ch=int(ch)
                    one = admin_stuff()
                    two=cus_stuff()
                    if ch == 1:
                        one.admin_login()
                    elif ch==2:
                        two.cus_login()                        
                    else:
                        os.system("cls")
                        console.print("\n\t[bold red]ERROR: Invalid Input!![/bold red]")
                else:
                    os.system("cls")
                    console.print("\t\t[yellow]Closing program...[/yellow]")
                    processing()
                    os.system("cls")
                    break
            except ValueError:
                os.system("cls")
                console.print("\n\t[bold red]ERROR: Invalid Input!![/bold red]")


a1=start()
a1.login()


# a1=cus_stuff()
# a1.cus_login()
