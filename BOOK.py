"""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
mycursor=mydb.cursor()
"""
import random
import sqlite3

mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()





#TODO QUERY TO ADD THE book_ID INTO THE TABLE BOOK

def add_new_book (new_ID,YOUR_ID):
        
    bk_title=input("ENTER THE BOOK TITLE:- ")
    bk_edition=input("ENTER THE BOOK EDITION:- ")
    bk_author=input("ENTER THE NAME OF THE AUTHOR OF THE BOOK:- ")
    bk_pulisher=input("ENTER THE NAME OF THE NAME OF THE PUBLISHER OF THE BOOK:- ")
    bk_copies=int(input("ENTER THE NUMBER OF BOOK PRESENT:- "))
    bksource=input("ENTER THE SOURCE OF THE BOOK:- ")
    bkcost=int(input("ENTER THE COST OF THE BOOK:- "))
    bkremarks=input("ENTER ANY REMARKS YOU WANT TO ADD FOR THIS BOOK:- ")
    try:
        mydb=sqlite3.connect("library.db")
        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO BOOK VALUES (:book_ID , :bktitle , :bkedition, :bkauthor,:bkpublisher,:bkcopies,:bk_source,:bk_cost,:bk_remarks)",
                {
                    'book_ID' : new_ID,
                    'bktitle' : bk_title,
                    'bkedition' : bk_edition,
                    'bkauthor' : bk_author,
                    'bkpublisher': bk_pulisher,
                    'bkcopies' : bk_copies,
                    'bk_source': bksource,
                    'bk_cost':bkcost,
                    'bk_remarks':bkremarks
                })
        print("Data added successfully ... ")
        mydb.commit()
        mydb.close()
        try:
            import UsersMainMenu
            return UsersMainMenu.check_ID(YOUR_ID=str(YOUR_ID))
        except Exception as e:
            import main
            return main.Staff_Or_Student()
    except Exception as e :
        print(e)
        print("Ooops! Sorry Something Went Wrong ...")
        import UsersMainMenu
        return UsersMainMenu.check_ID(YOUR_ID=str(YOUR_ID))
        
 

def check_ID (new_ID,YOUR_ID) :
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    book_IDs =list(mycursor.execute("SELECT book_ID FROM BOOK"))
    all_book_IDs=[]
    for book_id in book_IDs:
        all_book_IDs.append(book_id[0])
 
    if new_ID in all_book_IDs:
        #id has already taken 
        mydb.commit()
        mydb.close()
        generate_new_ID(YOUR_ID)
    else:
        mydb.commit()
        mydb.close()
        add_new_book(new_ID,YOUR_ID)



def generate_new_ID(YOUR_ID):
    one_t0_five=[1,2,3,4,5,6]
    some_char=["0","1","2","3","4","5","6","7","8","9"]
    ID=[]
    digit_num=random.choice(one_t0_five)
    while digit_num != 0 : 
        ID.append(random.choice(some_char))
        digit_num -= 1
    final_ID="".join(ID)
    return check_ID(final_ID,YOUR_ID)
mydb.commit()
mydb.close()