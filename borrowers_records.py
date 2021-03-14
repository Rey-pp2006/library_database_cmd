"""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")

"""
import sqlite3
from datetime import date


mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()

#import main

def quit():
    return




def Borrow(BorrowersID ,bookID,bk_title ,today_date ,dueDATE,no_return_date_for_now):
    try:
        mydb=sqlite3.connect("library.db")
        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO BookBorrowReturnRecords VALUES(:Borrowers_ID,:book_ID,:bktitle,:releaseDate ,:duedate,:bkdatereturn)",{
        'Borrowers_ID' : BorrowersID,
        'book_ID' :bookID, 
        'bktitle' :bk_title,  
        'releaseDate' :date.today(), 
        'duedate':dueDATE, 
        'bkdatereturn': no_return_date_for_now
        })
        mydb.commit()
        mydb.close()
        print (f"Data added succesfully !\nYou can have book : {bk_title} till {dueDATE}...\n Make sure you keep it clean and return it like you borrow it  .... ")
        
        import MAIN_MENU
        return MAIN_MENU.student_main_menu()
    except Exception as e:
        print(e)
        print("Oooops ! Something Went wrong ....")
        mydb.commit()
        mydb.close()
        try:
            import MAIN_MENU
            return MAIN_MENU.student_main_menu()
        except Exception as e : 
            print(e)
            print("Ooops Something Went Wrong ")
            import MAIN_MENU
            return MAIN_MENU.student_main_menu()

#Borrow()


def check_ID (BorrowersID ,bookID,bk_title ,today_date,dueDATE ,no_return_date_for_now) :
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    all_IDs=[]

    

    book_ids = list(mycursor.execute("SELECT book_ID FROM BOOK"))
    bookIDs= [book_id[0] for book_id in book_ids]

    book_names = list(mycursor.execute("SELECT bktitle FROM BOOK"))
    BookNames= [book_name[0] for book_name in book_names]


    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))
    all_IDs=[student_id[0] for student_id in student_ids]
    
    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))
    for staff_id in staff_ids:
        all_IDs.append(staff_id[0])
    

   # print(all_IDs)
    if str(BorrowersID) in all_IDs:
        if bookID in bookIDs:
            #ID exist 
            mydb.commit()
            mydb.close()
            return Borrow(BorrowersID ,bookID,bk_title ,today_date ,dueDATE,no_return_date_for_now)
        else:
            print("THIS BOOK ID DOESN'T EXIST ! ")
            mydb.commit()
            mydb.close()
            try:
                import MAIN_MENU
                return MAIN_MENU.student_main_menu()
            except Exception as e :
                print(e)
                print("Ooops Something Went Wrong ! ")
                return
    else:
        print("Sorry ID doesn't exist")
        mydb.commit()
        mydb.close()
        try:
            import MAIN_MENU
            return MAIN_MENU.student_main_menu()
        except Exception as e :
            print(e)
            print("Ooops Something Went Wrong ! ")
            return




def questions():
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    BorrowersID=input("ENTER YOUR ID:- ")
    print("Here is the list of availablie books ... ")
    print("\n-------------------------------------------------------")
    mycursor.execute("SELECT book_ID,bktitle FROM BOOK ")
    id_name=mycursor.fetchall()
    dic_id_name={i[0]:i[1] for i in id_name}
    for key,value in dic_id_name.items():
        print(f"{key} : {value}")
    print("----------------------------------------------------------")

    bookID=input("ENTER THE BOOK'S ID:- ")

    bk_title=input("ENTER THE BOOK'S TITLE:- ")

    today_date= date.today()

    dueDATE=input("Please Enter the due date in the (yyyy-mm-dd) format")

    no_return_date_for_now=""
    mydb.commit()
    mydb.close()
    return check_ID (BorrowersID ,bookID,bk_title ,today_date,dueDATE ,no_return_date_for_now)

#questions()

#check_ID (BorrowersID)

mydb.commit()
mydb.close()