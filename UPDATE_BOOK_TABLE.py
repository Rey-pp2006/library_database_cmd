import sqlite3
import logging
#import MAIN_MENU
mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()



def quit_OR_home():
    QuitOrHome=input("\nOK DO YOU WANT TO QUIT OR GO BACK TO THE HOME PAGE ? (QUIT/HOME PAGE) ")
    if QuitOrHome.replace(" ","").upper() == "QUIT":
        print("\nOK THANK YOU ! HAVE A NICE DAY ... ")
        return
    elif QuitOrHome.replace(" ","").upper() == "HOMEPAGE":
        import UsersMainMenu
        return UsersMainMenu.check_ID()
    else :
        print("WRONT INPUT ! PLEASE CHECK IT AGAIN ; IT CAN BE WRONG SPELLING OR SOMETHING ELSE ... ")
        return quit_OR_home()


def EDIT(Which_bookID,bk_title,adition,writer,publisher,presents,source,cost,remark):
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("""UPDATE BOOK SET
                    bktitle=(?),
                    bkedition=(?),
                    bkauthor=(?),
                    bkpublisher=(?),
                    bkcopies=(?),
                    bk_source=(?),
                    bk_cost=(?),
                    bk_remarks=(?)
                    WHERE book_ID =(?)""",
                    (
                        bk_title,
                        adition,
                        writer,
                        publisher,
                        presents,
                        source,
                        cost,
                        remark,
                        Which_bookID
                    ))
        mydb.commit()
        mydb.close()
        print("DATA UPDATED SUCCESSFULLY ... ")
        return quit_OR_home()
        
    except Exception as e : 
        print(e) #TODO I should delete this line later 
        print("Oooops! SORRY SOMETHING WENT WRONG ... ")
        return quit_OR_home()


    mydb.commit()
    mydb.close()

def DELETE(Which_bookID):
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("DELETE FROM BOOK WHERE book_ID =(?)" , (Which_bookID,))
        mydb.commit()
        mydb.close()
        print("RECORD DELTED SUCCESSFULLY !")
        return quit_OR_home()
    except Exception as e:
        print(e) #TODO I should delete this line later 
        print("Oooops SOMETHING WENT WRONG")
        mydb.commit()
        mydb.close()
        return quit_OR_home()
    
    
    
    
    
    

def check_info(Which_bookID):
    bk_title=input("ENTER THE NEW BOOK TITLE:- :- ")
    print("\n---------------------------------------------")

    adition=input("ENTER THE BOOK EDITION:- ")
    print("\n---------------------------------------------")

    writer=input("ENTER THE NAME OF THE AUTHOR OF THE BOOK:- ")
    print("\n---------------------------------------------")

    publisher=input("ENTER THE NAME OF THE NAME OF THE PUBLISHER OF THE BOOK:- ")
    print("\n---------------------------------------------")

    presents=input("ENTER THE NUMBER OF BOOK PRESENT:-")
    print("\n---------------------------------------------")

    source=input("ENTER THE SOURCE OF THE BOOK:- ")
    print("\n---------------------------------------------")

    cost=input("ENTER THE COST OF THE BOOK:- ")
    print("\n---------------------------------------------")

    remark=input("ENTER ANY REMARKS YOU WANT TO ADD FOR THIS BOOK:- ")
    print("\n---------------------------------------------")

    def digit_check():
        if cost.replace(" ","").isdigit():
            if presents.replace(" ","").isdigit():
                return EDIT(Which_bookID,bk_title,adition,writer,publisher,presents,source,cost,remark)
            else:
                print("\nPRESENT BOOKS NUMBER CAN*T CONTAIN LETTTERS ")
                return check_info(Which_bookID)
        else:
            print("\nINVALID PRICE , IT CAN'T CONTAIN ANY LETTERs ...")
            return check_info(Which_bookID)
           

    if writer.isalpha() and publisher.isalpha()   :
        return digit_check()
    else:
        print("\nINVALID INPUT ... ")
        return check_info(Which_bookID)


    
def EDITorDELETE():
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    Book_IDs=list(mycursor.execute("SELECT book_ID FROM BOOK"))
    ALL_BOOK_IDs=[]
    for book_id in Book_IDs:
        ALL_BOOK_IDs.append(book_id[0])

    Edit_or_delete=input("DO YOU WANT TO EDIT OR DELETE A RECORD ? (DELETE/EDIT) ")

    if Edit_or_delete.replace(" ","").upper()=="EDIT":
        Which_bookID=input("PLEASE ENTER THE BOOK ID THAT YOU WANT TO EDIT ? ")
        if Which_bookID in ALL_BOOK_IDs :
            print("GREAT ! PLEASE ENTER NEW DATA ... ")
            mydb.commit()
            mydb.close()
            return check_info(Which_bookID) #TODO 
        else:
            print("THIS BOOK ID DOESN'T EXIST ... ")
            mydb.commit()
            mydb.close()
            return quit_OR_home()
    elif Edit_or_delete.replace(" ","").upper()=="DELETE":
        #TODO 
        print("Here is the list of availablie books ... ")
        print("\n-------------------------------------------------------")
        mycursor.execute("SELECT book_ID,bktitle FROM BOOK ")
        id_name=mycursor.fetchall()
        dic_id_name={i[0]:i[1] for i in id_name}
        for key,value in dic_id_name.items():
            print(f"{key} : {value}")
        print("----------------------------------------------------------")
        Which_bookID=input("PLEASE ENTER THE BOOK ID THAT YOU WANT TO DELTE? ")
        print(Which_bookID , ALL_BOOK_IDs)
        if Which_bookID in ALL_BOOK_IDs :
            sure_delete=input("GOOD ! ARE YOU SURE YOU WANT TO DLETE THIS RECORD ?\nONCE YOU DELETE IT YOU WON'T BEABLE TO RESTORE IT AGAIN !\n(YES/NO)")
            if sure_delete.replace(" ","").upper() == "YES":
                mydb.commit()
                mydb.close()
                return DELETE(Which_bookID)#
            elif sure_delete.replace(" ","").upper() == "NO":
                print("ALRIGHT :-) ")
                mydb.commit()
                mydb.close()
                return quit_OR_home()#
            else:
                print("WRONG INPUT!")
                mydb.commit()
                mydb.close()
                return quit_OR_home()#
        else:
            print("THIS BOOK ID DOESN'T EXIST ... ")
            mydb.commit()
            mydb.close()
            return quit_OR_home()#
    else:
        print("WRONG INPUT !  ")
        mydb.commit()
        mydb.close()
        return quit_OR_home()#



def check_ID (YOUR_ID) :
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()

    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))
    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))    
    all_staff_IDs=[]
    all_student_IDs=[]
    for staff_id in staff_ids:
        all_staff_IDs.append(staff_id[0])
    for student_id in student_ids:
        all_student_IDs.append(student_id[0])
    print(all_staff_IDs) #delete then 

    if YOUR_ID in all_staff_IDs:
        #GOOD ... ID EXIST #TODO IT WOULD BE MUCH BETTER TO ADD A PASSWORD CHECKER HERTE 
        print("WELCOME DEAR STAFF ... ")
        mydb.commit()
        mydb.close()
        return EDITorDELETE()
    elif YOUR_ID in all_student_IDs:
        print("OH SEEMS LIKE YOU ARE A STUDENT ! SORRY BUT YOU DON'T HAVE PERMISSON TO UPDATE THE TABLES ")
        mydb.commit()
        mydb.close()
        return quit_OR_home()
    else:
        print("Ooops ! THIS ID DOESN'T EXIST")
        mydb.commit()
        mydb.close()
        return quit_OR_home()


def SURE():
    sure=input("ARE YOU SURE YOU WANT TO CHANGE THE TABLE ? (YES/NO)")
    if sure.replace(" ","").upper() == "YES":
        YOUR_ID=input("ENTER YOUR OWN ID PLEASE :- ").replace(" ","")
        return check_ID(YOUR_ID) #TODO
        
    elif sure.replace(" ","").upper() == "NO":
        return quit_OR_home()
    else:
        print("WRONG INPUT ! PLEASE CHECK IT AGAIN ")
        return SURE()

mydb.commit()
mydb.close()