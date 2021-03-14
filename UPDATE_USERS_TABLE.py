import sqlite3
import logging
#import MAIN_MENU
mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()

def quit():
    return


def quit_OR_home():
    QuitOrHome=input("\nOK DO YOU WANT TO QUIT OR GO BACK TO THE HOME PAGE ? (QUIT/HOME PAGE) ")
    if QuitOrHome.replace(" ","").upper() == "QUIT":
        print("\nOK THANK YOU ! HAVE A NICE DAY ... ")
        return quit()
    elif QuitOrHome.replace(" ","").upper() == "HOMEPAGE":
        import UsersMainMenu
        return UsersMainMenu.check_ID()
    else :
        print("WRONT INPUT ! PLEASE CHECK IT AGAIN ; IT CAN BE WRONG SPELLING OR SOMETHING ELSE ... ")
        return quit_OR_home()


    
   
def UPDATE(second_Staff,stff_name,stffl_name,stffcontact,stf_email,stf_address,stf_password,stf_type):
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("""UPDATE USERS SET
                    stffname=(?),
                    stfflname=(?),
                    stffcontactnumber=(?),
                    stfemail=(?),
                    stfaddress=(?),
                    stfpassword=(?),
                    stftype=(?)
                    WHERE staff_ID =(?)""",
                    (
                        stff_name,
                        stffl_name,
                        stffcontact,
                        stf_email,
                        stf_address,
                        stf_password,
                        stf_type,
                        second_Staff
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

def DELETE(second_Staff):
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("DELETE FROM USERS WHERE staff_ID = " + second_Staff)
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
    
    
    
    
    
    

def check_info(second_Staff):
    stff_name=input("ENTER THE NEW FIRST NAME:- ")
    print("\n---------------------------------------------")

    stffl_name=input("ENTER THE NEW LAST NAME- ")
    print("\n---------------------------------------------")

    stffcontact=input("ENTER THE NEW CONTACT NUMBER:- ")
    print("\n---------------------------------------------")

    stf_email=input("ENTER THE NEW EMAIL_ID:- ")
    print("\n---------------------------------------------")

    stf_address=input("ENTER THE NEW HOME ADDRESS:- ")
    print("\n---------------------------------------------")

    stf_password=input("ENTER THE PASSWORD FOR THE NEW ACCOUNT:- ")
    print("\n---------------------------------------------")

    stf_type=input("Any extra descreaption :- ")
    print("\n---------------------------------------------")

    def digit_check():
        if stffcontact.replace(" ","").isdigit():
            if "@" in stf_email.replace(" ","").lower() :
                if len(stf_password) >= 7:
                    return UPDATE(second_Staff,stff_name,stffl_name,stffcontact,stf_email,stf_address,stf_password,stf_type)
                else:
                    print("\nPASSWORD IS NOT STRONG ENOUGH ")
                    return check_info(second_Staff)
            else:
                print("\INVALID EMAIL ADRESS ... ")
                return check_info(second_Staff)
        else:
           # print("INVALID TELEPHONE NUMBER ... ")
            print("\nINVALID TELEPHONE NUMBER ...")
            return check_info(second_Staff)
           

    if stff_name.isalpha() and stffl_name.isalpha() :
        return digit_check()
    else:
        print("\nFIRST NAME AND LAST NAME ARE REQUIRED AND CAN'T CONTAIN NUMBER")
        return check_info(second_Staff)


    
def EDITorDELETE(all_staff_IDs):
    Edit_or_delete=input("DO YOU WANT TO EDIT OR DELETE A RECORD ? (DELETE/EDIT) ")
    if Edit_or_delete.replace(" ","").upper()=="EDIT":
        second_Staff=input("PLEASE ENTER THE STAFF's ID THAT YOU ARE GOING TO EDIT... ")
        if second_Staff in all_staff_IDs :
            print("GREAT ! PLEASE ENTER NEW DATA ... ")
            return check_info(second_Staff) #TODO 
        else:
            print("THIS STAFF ID DOESN'T EXIST ... ")
            return quit_OR_home()#
    elif Edit_or_delete.replace(" ","").upper()=="DELETE":
        second_Staff=input("PLEASE ENTER THE STAFF's ID THAT YOU ARE GOING TO DELETE...  ")
        if second_Staff in all_staff_IDs :
            sure_delete=input("GOOD ! ARE YOU SURE YOU WANT TO DLETE THIS RECORD ?\nONCE YOU DELETE IT YOU WON'T BEABLE TO RESTORE IT AGAIN !\n(YES/NO)")
            if sure_delete.replace(" ","").upper() == "YES":
                return DELETE(second_Staff)#
            elif sure_delete.replace(" ","").upper() == "NO":
                print("ALRIGHT :-) ")
                return quit_OR_home()#
            else:
                print("WRONG INPUT!")
                return quit_OR_home()#
        else:
            print("THIS STUDENT ID DOESN'T EXIST ... ")
            return quit_OR_home()#
    else:
        print("WRONG INPUT !  ")
        quit_OR_home()#



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
    #print(all_staff_IDs) #delete then 

    if YOUR_ID in all_staff_IDs:
        #GOOD ... ID EXIST #TODO IT WOULD BE MUCH BETTER TO ADD A PASSWORD CHECKER HERTE 
        print("WELCOME DEAR STAFF ... ")
        mydb.commit()
        mydb.close()
        return EDITorDELETE(all_staff_IDs)
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