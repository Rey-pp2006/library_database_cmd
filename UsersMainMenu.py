
import sqlite3

mydb = sqlite3.connect("library.db")
mycursor=mydb.cursor()

def show_table(WHICH_TABLE,YOUR_ID,password):
    try:
        from  tabulate import tabulate

        mydb=sqlite3.connect("library.db")
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT * FROM {WHICH_TABLE} ")

        Table = mycursor.fetchall()
        print("\n-------------------------------------------------------------------------------------------------------------------------")


        print (tabulate(Table, headers=["ID", "BOOK NAME", "ADITION", "WRITER" ,"PUBLISHER","QUANTITES" ,"BOOK SOURCE","PRICE","REMARK"]))

        print("-------------------------------------------------------------------------------------------------------------------------")

        mydb.commit()
        mydb.close()
        return users_main_menu(YOUR_ID,password)
    except Exception as e:
        print(e)
        print("Oooops Something Went Wrong !")
        return users_main_menu(YOUR_ID,password)

def quit():
    return 


def which_table(YOUR_ID,password):
    WHICH_TABLE=input("WHICH TABLE DO YOU WANT TO SEE ? (BOOK/STUDENTS/USERS) ")
    if WHICH_TABLE.replace(" ","").upper() == "BOOK":
        return show_table(WHICH_TABLE,YOUR_ID,password)
    elif WHICH_TABLE.replace(" ","").upper() == "STUDENTS":
        return show_table(WHICH_TABLE,YOUR_ID,password)
    elif WHICH_TABLE.replace(" ","").upper() == "USERS":
        return show_table(WHICH_TABLE,YOUR_ID,password)
    else : 
        print("WRONG INPUT ! PLEASE CHECK IT AGAIN ...")
        return which_table(YOUR_ID,password)
    


def QuitOrAgain(YOUR_ID):
    ask_quit_or_again=input("DO YOU WANT TO ENTER THE PASSWORD AGAIN OR QUIT ? (AGAIN/QUIT)")
    if ask_quit_or_again.replace(" ","").upper() == "QUIT":
        print("OK THANK YOU SO MUCH ! HAVE A NICE DAY")
        return 
    elif ask_quit_or_again.replace(" ","").upper() == "AGAIN":
        print("GREAT ... ")
        return check_password(YOUR_ID)
    else:
        print("WRONG INPUT PLEASE CHECK IT AGAIN ...")
        return QuitOrAgain()




def users_main_menu(YOUR_ID,password):
    users_funcs=["EDIT/DELETE THE STUDENT'S TABLE ","EDIT/DELETE THE USERS TABLE","EDIT/DELETE THE BOOKS TABLE","ADD NEW STUDENT","ADD NEW USER","ADD NEW BOOKS","SHOW TABLES","QUIT"]
    users_ablities=dict(enumerate(users_funcs))
    for key,value in users_ablities.items():
        print(f"{key} -> {value}")
       
    do = input("\nPLEASE SELECT AN ITEM FROM MENU ABOVE ! (ENTER THE NUMBER)")


    if (do.replace(" ","").upper() == "0") :
        import UPDATE_STUDENT_TABLE
        return UPDATE_STUDENT_TABLE.SURE()

    elif (do.replace(" ","").upper() == "1"):
        import UPDATE_USERS_TABLE
        return UPDATE_USERS_TABLE.SURE()

    elif (do.replace(" ","").upper() == "2"):
        import UPDATE_BOOK_TABLE
        return UPDATE_BOOK_TABLE.SURE()
    elif (do.replace(" ","").upper() == "3"):
        import STUDENTS
        return STUDENTS.generate_new_ID()
   

    elif (do.replace(" ","").upper() == "4"):
        import USERS
        return USERS.generate_new_ID()


    elif (do.replace(" ","").upper() == "5"):
        import BOOK
        return BOOK.generate_new_ID(YOUR_ID)

    elif (do.replace(" ","").upper() == "6"):
        return which_table(YOUR_ID,password)
    elif (do.replace(" ","").upper() == "7"):
        print("Thank YOU ! HAVE A NICE DAY ")
        return

    else :
        print("WRONG INPUT ! PLEASE CHECK IT AGAIN\n DON'T FORGET THAT YOU MUST ENTER THE NUMBER .... ")
        return users_main_menu(YOUR_ID,password) 


def check_password(YOUR_ID , PASSWORD):
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()

    mycursor.execute("SELECT stfpassword FROM USERS WHERE staff_ID=(?)",(YOUR_ID,))
    right_password=mycursor.fetchall()
    #print(right_password) #delete later

    if right_password[0][0]== PASSWORD:
        print("WELCOME DEAR STAFF")
        mydb.commit()
        mydb.close()
        return users_main_menu(YOUR_ID,PASSWORD)

    else:
        print("Oooops! WRONG PASSWORD")
        mydb.commit()
        mydb.close()
        return QuitOrAgain(YOUR_ID)
    





def check_ID (YOUR_ID="",PASSWORD="") :
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    if YOUR_ID =="":
        YOUR_ID=input("PLEASE ENTER YOUR ID :-")
    else:
        YOUR_ID = str(YOUR_ID)
    
    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))
    #print(student_ids)
    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))   
    #print(staff_ids) 
    all_staff_IDs=[]
    all_student_IDs=[]
    for staff_id in staff_ids:
        all_staff_IDs.append(staff_id[0])
    #print(all_staff_IDs)
    for student_id in student_ids:
        all_student_IDs.append(student_id[0])
    #print(all_student_IDs) #delete then 
    #print(YOUR_ID)
    if str(YOUR_ID) in all_staff_IDs:
        #GOOD ... ID EXIST 
        if PASSWORD =="":
            PASSWORD=input("ENTER YOUR PASSWORD PLEASE :-")
        else:
            PASSWORD=PASSWORD
        mydb.commit()
        mydb.close()
        return check_password(YOUR_ID,PASSWORD = PASSWORD)
        
    elif str(YOUR_ID) in all_student_IDs:
        print("OH SEEMS LIKE YOU ARE A STUDENT ! SORRY BUT YOU DON'T HAVE PERMISSON TO UPDATE THE TABLES ")
        mydb.commit()
        mydb.close()
        return UPDATE_STUDENT_TABLE.quit_OR_home()
    else:
        print("Ooops ! THIS ID DOESN'T EXIST")
        mydb.commit()
        mydb.close()
        import main
        return main.Staff_Or_Student()

#check_ID(YOUR_ID="9689")
mydb.commit()
mydb.close()