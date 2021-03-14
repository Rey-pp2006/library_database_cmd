import sqlite3

mydb=sqlite3.connect("library.db")
mycursor = mydb.cursor()



def Student_info(ID):
    try:
        mydb=sqlite3.connect("library.db")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM STUDENTS WHERE stud_ID=(?)",(ID,))
        print("---------------------------------------")
        ST_information = mycursor.fetchall()
        headigs=("ID             ","FIRST NAME     ","LAST NAME      ","COURSE         ","ADMISSION YEAR ", "CONTACT NUMBER ","AGE            ","BIRTHDATE      ","GENDER         " )
        for info in ST_information:
            info_dict = (dict(zip(headigs,info)))
        for key,value in info_dict.items():
            print(f"{key}: {value}")
        print("----------------------------------------")
        mydb.commit()
        mydb.close()
        return student_main_menu()
    except Exception as e:

        print(e)#TODO DELETE IT LATER 
        print("Ooops! SORRY SOMETHING WENT WRONG ! ")
        mydb.commit()
        mydb.close()
        return student_main_menu()
    
    
    
def quit():
    return



def check_ID (ID) :
    
    mydb=sqlite3.connect("library.db")
    mycursor = mydb.cursor()
    
    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))

    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))

    all_IDs=[]

    for staff_id in staff_ids:
        all_IDs.append(staff_id[0])
    for student_id in student_ids:
        all_IDs.append(student_id[0])
    print(all_IDs)
    print(str(ID))
    if str(ID) in all_IDs:
        #so good that id exists
        return Student_info(ID)
    else:
        print("SEEMS LIKE THIS ID DOESN't EXIST")
        return student_main_menu()
    mydb.commit()
    mydb.close()

def student_main_menu():
    student_funcs=["BORROW ","RETURN","STUDENT INFO","QUIT"]
    studen_ablities=dict(enumerate(student_funcs))
    for key,value in studen_ablities.items():
        print(f"{key} -> {value}")
       
    do = input("PLEASE SELECT AN ITEM FROM MENU ABOVE ! (ENTER THE NUMBER)")


    if (do.replace(" ","").upper() == "0") or  (do.replace(" ","").upper() == "BORROW"):
        import borrowers_records
        return borrowers_records.questions()

    elif (do.replace(" ","").upper() == "1") or  (do.replace(" ","").upper() == "RETURN"):
        import return_records
        return return_records.check_ID()

    elif (do.replace(" ","").upper() == "2") or  (do.replace(" ","").upper() == "STUDENTINFO"):
        ID=input("PLEASE ENTER YOUR ID ... ")
        return check_ID(ID)
    elif (do.replace(" ","").upper() == "3") or  (do.replace(" ","").upper() == "QUIT"):
        print("THANK YOU FOR USING THIS PROGRAM !\nHAVE A BEAUTIFUL DAY ... ")
        return quit()

    else :
        print("WRONG INPUT ! PLEASE CHECK IT AGAIN ")
        return student_main_menu()

mydb.commit()
mydb.close()


