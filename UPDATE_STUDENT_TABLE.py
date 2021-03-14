import sqlite3
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
        return UsersMainMenu.check_ID() #TODO need to get complete 
    else :
        print("WRONT INPUT ! PLEASE CHECK IT AGAIN ; IT CAN BE WRONG SPELLING OR SOMETHING ELSE ... ")
        return quit_OR_home()


   
def UPDATE(ST_ID,ST_FNAME,ST_LNAME,ST_COURSE,ST_SUBMISSION_YEAR,ST_CONTACT_NUMBER,ST_AGE,ST_BIRTHDATE,ST_GENDER):
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("""UPDATE STUDENTS SET 
                    stfname=(?),
                    stlname=(?),
                    stcourse=(?),
                    styear=(?),
                    stcontact=(?),
                    stage=(?),
                    stbirthdate=(?),
                    stgender=(?)
                    WHERE stud_ID =(?)""",
                    (
                        ST_FNAME,
                        ST_LNAME,
                        ST_COURSE,
                        ST_SUBMISSION_YEAR,
                        ST_CONTACT_NUMBER,
                        ST_AGE,
                        ST_BIRTHDATE,
                        ST_GENDER,
                        ST_ID
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

def DELETE(Student_ID):

    try:
        mydb=sqlite3.connect("library.db")
        mycursor=mydb.cursor()
        mycursor.execute("DELETE FROM STUDENTS WHERE stud_ID = " + str(Student_ID))
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
    

def check_info(ST_ID):
        ST_FNAME=input("ENTER YOUR FIRST NAME :-")
        ST_LNAME=input("ENTER YOUR LAST NAME :-")
        ST_COURSE=input("ENTER YOUR COURSE :- ")
        ST_SUBMISSION_YEAR=input("ENTER YOUR SUBMISSION YEAR :-")
        ST_CONTACT_NUMBER=input("ENTER YOUR CONTACT NUMBER :- ")
        ST_AGE=input("ENTER YOUR AGE :- ")
        ST_BIRTHDATE= input("ENTER YOUR BIRTHDATE in this form (yyyy-mm-dd):-")
        ST_GENDER=input("ENTER YOUR GENDER (FEMALE / MALE / OTHER ) :-")
        def gender_check():
            if ( ST_GENDER.replace(" ","").upper() == "FEMALE" ) or ( ST_GENDER.replace(" ","").upper() == "MALE" ) or ( ST_GENDER.replace(" ","").upper() == "OTHER" ) :
                return UPDATE(ST_ID,ST_FNAME,ST_LNAME,ST_COURSE,ST_SUBMISSION_YEAR,ST_CONTACT_NUMBER,ST_AGE,ST_BIRTHDATE,ST_GENDER)
            else:
                print("INVALID GENDER ! YOU MUST CHOOSE BETWEEN (FEMALE / MALE / OTHER)")
                return check_info(ST_ID)
        def date_check():
            if len(ST_BIRTHDATE.replace(" ","")) == 10 and ST_BIRTHDATE.replace(" ","")[0:4].isdigit() and ST_BIRTHDATE.replace(" ","")[5:7].isdigit() and ST_BIRTHDATE.replace(" ","")[8:10].isdigit():
                return gender_check()
            else:
                print("INVALID DATE ! IT MUST BE IN THIS FORM (yyyy-mm-dd)")
                return check_info(ST_ID)
        def digit_check():
            if len(ST_SUBMISSION_YEAR.replace(" ","")) == 4 and ST_SUBMISSION_YEAR.replace(" ","").isdigit():
                if ST_CONTACT_NUMBER.replace(" ","").isdigit():
                    if len(ST_AGE.replace(" ","")) <= 2 and ST_AGE.replace(" ","").isdigit():
                        return date_check()
                    else :
                        print("INVALID AGE ... ")
                        return check_info(ST_ID)
                else:
                    print("INVALID TELEPHONE NUMBER ... ")
                    return check_info(ST_ID)
            else:
                print("INVALID SUBMISSION YEAR , IT SHOULD BE 4-DIGIT NUMBER ...")
                return check_info(ST_ID)
            


        if ST_FNAME.isalpha() and ST_LNAME.isalpha() :
            return digit_check()
        else:
            print("FIRST NAME AND LAST NAME ARE REQUIRED AND CAN'T CONTAIN NUMBER")
            return check_info(ST_ID)



    
def EDITorDELETE(all_student_IDs):
    Edit_or_delete=input("DO YOU WANT TO EDIT OR DELETE A RECORD ? (DELETE/EDIT) ")
    if Edit_or_delete.replace(" ","").upper()=="EDIT":
        Student_ID=input("PLEASE ENTER THE STUDENT's ID ... ")
        if Student_ID in all_student_IDs :
            print("GREAT ! PLEASE ENTER NEW DATA ... ")
            return check_info(Student_ID)
        else:
            print("THIS STUDENT ID DOESN'T EXIST ... ")
            return quit_OR_home()
    elif Edit_or_delete.replace(" ","").upper()=="DELETE":
        Student_ID=input("PLEASE ENTER THE STUDENT's ID ... ")
        if str(Student_ID) in all_student_IDs :
            sure_delete=input("GOOD ! ARE YOU SURE YOU WANT TO DLETE THIS RECORD ?\nONCE YOU DELETE IT YOU WON'T BEABLE TO RESTORE IT AGAIN !\n(YES/NO)")
            if sure_delete.replace(" ","").upper() == "YES":
                return DELETE(Student_ID)
            elif sure_delete.replace(" ","").upper() == "NO":
                print("ALRIGHT :-) ")
                return quit_OR_home()
            else:
                print("WRONG INPUT!")
                return quit_OR_home()
        else:
            print("THIS STUDENT ID DOESN'T EXIST ... ")
            return quit_OR_home()
    else:
        print("WRONG INPUT  !  ")
        quit_OR_home()

        


        


def check_ID (YOUR_ID) :
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))
    #print(student_ids)
    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))   
    #print(staff_ids) 
    all_staff_IDs=[]
    all_student_IDs=[]
    for staff_id in staff_ids:
        all_staff_IDs.append(staff_id[0])
    for student_id in student_ids:
        all_student_IDs.append(student_id[0])
    print(all_student_IDs)
    if str(YOUR_ID) in all_staff_IDs:
        #GOOD ... ID EXIST #TODO IT WOULD BE MUCH BETTER TO ADD A PASSWORD CHECKER HERTE 
        print("WELCOME DEAR STAFF ... ")
        mydb.commit()
        mydb.close()
        return EDITorDELETE(all_student_IDs)
    elif str(YOUR_ID) in all_student_IDs:
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
        return check_ID(YOUR_ID)
        
    elif sure.replace(" ","").upper() == "NO":
        return quit_OR_home()
    else:
        print("WRONG INPUT ! PLEASE CHECK IT AGAIN ")
        return SURE()
    
            







mydb.commit()
mydb.close()