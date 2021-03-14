"""

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
"""

import sqlite3
from datetime import date 
#import main


today=str(date.today())


mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()



#mycursor.execute("UPDATE BookBorrowReturnRecords SET bkdatereturn = (?) ", (today,))



def BakOrQuit():
    backOrquit=input("\nDO YOU WANT TO GO BACK TO THE MAIN PAGE OR QUIT ? (QUIT/MAIN PAGE)")
    if backOrquit.replace(" ","").upper() == "QUIT":
        print("OK THANK YOU ! HAVE A NICE DAY ...")
        return 
    elif backOrquit.replace(" ","").upper() == "MAINPAGE" :
        #return main.student_main_menu
        import MAIN_MENU

        MAIN_MENU.student_main_menu()
         
    else:
        print("WRONG INPUT ! PLEASE CHEACK IT AGAIN ")
        BakOrQuit()



def Return_the_book():
    try:
        mydb=sqlite3.connect("library.db")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE BookBorrowReturnRecords SET bkdatereturn =(?) ", (today,))
        print("DATA UPDATED SUCCESSFULLY ? \nYou Returned the book ")
        BakOrQuit()
        
    except Exception as e:
        print(e)
        print("Oooops! SOMETHING WENT WRONG!")
    mydb.commit()
    mydb.close()
    import MAIN_MENU
    return MAIN_MENU.student_main_menu()

def is_return_date_after_the_duedate(BorrowersID):
    mydb=sqlite3.connect("library.db")
    mycursor = mydb.cursor()
    DUEDATE = str(mycursor.execute("SELECT duedate FROM BookBorrowReturnRecords WHERE Borrowers_ID =?", (BorrowersID,)))
    if today[0:4] <= DUEDATE[0:4] :
        if today[5] == "0" and  DUEDATE[5] == "0":
            if today[6] <= date[6]:
                
                if today[8] == "0" and  DUEDATE[8] == "0":
                    if today[9] <= DUEDATE[9]:
                        print("Thanks for returning on time ")
                        return Return_the_book()
                    else :
                        print("After The Due Date .... ")
                        return Return_the_book()

                        
                elif today[8] == "0" and DUEDATE[8] != "0":
                    print("Thanks for returning on time ")
                    return Return_the_book()
                elif  today[8] != "0" and DUEDATE[8] == "0":
                    print("After The Due Date .... ")
                    return Return_the_book()
                elif today[8] != "0" and DUEDATE[8] != "0":
                    if today[8:10] <= DUEDATE[8:10] :
                        print("Thanks for returning on time ")
                        return Return_the_book()
                    else:
                        print("After The Due Date .... ")
                        return Return_the_book()
            else :
                print("After The Due Date .... ")
                return Return_the_book()
        elif today[5] == "0" and  DUEDATE[5] != "0":
            print("Thanks for returning on time ")
            return Return_the_book()
        elif today[5] != "0" and DUEDATE[5] != "0":
            if today[5:7] <= DUEDATE[5:7] :
                print("Thanks for returning on time ")
                return Return_the_book()
            else:
                print("After The Due Date .... ")
                return Return_the_book()
    else:
        print("After The Due Date .... ")
    mydb.commit()
    mydb.close()
    return Return_the_book()

                
                

    





def Return(BorrowersID):
    #print(check_ID.BorrowersID())
    #print(check_ID().BorrowersID)
    ask_return=input("Do you want to Return the book ? (YES/NO)")

    if ask_return.replace(" ","").upper() == "YES":
        return is_return_date_after_the_duedate(BorrowersID)
       
    if ask_return.replace(" ","").upper() == "NO":
        return BakOrQuit()
    else : 
        print("Wrong INPUT ; PLEASE CHECK IT AGAIN ")
        return Return(BorrowersID)

    
        


def check_ID () :
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    BorrowersID = input("PLEASE ENTER YOUR ID .... ")
    all_IDs=[]
    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))
    for student_id in student_ids:
        all_IDs.append(student_id[0])
    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))
    for staff_id in staff_ids:
        all_IDs.append(staff_id[0])
    
    if str(BorrowersID) in all_IDs:
        #ID exist 
        return Return(BorrowersID)
    else:
        print("Sorry ID doesn't exist")
        return main.Staff_Or_Student()
        
    mydb.commit()
    mydb.close()



mydb.commit()
mydb.close()