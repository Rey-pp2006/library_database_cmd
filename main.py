#import UsersMainMenu
import sqlite3


#import BOOK
#import return_records

mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()

def register_as_new_staff():
    registerornot=input("DO YOU WANT TO REGISTER AS A NEW STAFF MEMBER OF THIS LIBRARY? (YES/NO)")
    if registerornot.replace(" ","").upper() == "YES":
        import USERS
        USERS.generate_new_ID()

    elif registerornot.replace(" ","").upper() == "NO":
        print("TRY TO NOT WASTE TIME OF OURS AND OTHERS, THANK YOU !!!")
        return quit()
    else:
        print("\nWRONG INPUT, CHECK THE DATA AGAIN.")
        return register_as_new_staff()



def quit():
    return 



def register_as_new_student():
    import STUDENTS
    registerornot=input("DO YOU WANT TO REGISTER YOUR RECORDS IN THIS LIBRARY?")
    if registerornot.upper() == "YES":
        return STUDENTS.generate_new_ID()
    elif registerornot.upper() == "NO":
        print("EITHER REGISTER YOURSELF INTO THE DATABASE OR YOU WON'T BE ABLE TO ACCESS THE LIBRARY")
        RegisterOrGo = input("ARE YOU SURE YOU DON'T WANT TO REGISTER ? (YES/NO)")
        if RegisterOrGo.replace(" ","").upper() == "YES":
            print("OK THANK YOU ! HAVE A NICE DAY .... ")
            return quit()
        elif RegisterOrGo.replace(" ","").upper() == "NO":
            print("SUCH A NICE DESICION ! ")
            return STUDENTS.generate_new_ID()
        else:
            print("WRONG INPUT PLEASE CHECK IT AGAIN ")
            return register_as_new_student()
    else:
        print("WRONG INPUT, CHECK IT AGAIN")
        return register_as_new_student()
            




def login_as_old_staff():
    mydb=sqlite3.connect("library.db")
    mycursor =mydb.cursor()
    
    import UsersMainMenu
    staffID=int(input("PLEASE ENTER YOUR STAFF_ID:- "))
    all_IDs= list(mycursor.execute("SELECT staff_ID FROM USERS "))
    IDs=[]
    for ID in all_IDs:
        IDs.append(int(ID[0]))

    if staffID in IDs:
        password_check = input("PLEASE ENTER YOUR PASSWORD ...")
        ID_Password = list(mycursor.execute("SELECT stfpassword FROM USERS WHERE staff_ID =?",(str(staffID),)))
        if password_check == ID_Password[0][0]:
                staff_name = list(mycursor.execute("SELECT stffname FROM USERS WHERE staff_ID = ?", (str(staffID),)))
                print(f"Hello {staff_name[0][0]} ! Welcome ... ")
                mydb.commit()
                mydb.close()
                return UsersMainMenu.check_ID(YOUR_ID= staffID , PASSWORD=password_check)
        else:
            print("Wrong Password .... ")
            mydb.commit()
            mydb.close()
            return Staff_Or_Student()
            #need to get complete
    else : 
        print("This ID doesn't exist ... ")
        mydb.commit()
        mydb.close()
        print("FILL THE FORM TO BECOME A STAFF ... ")

        return register_as_new_staff()


def login_as_old_student():
    mydb=sqlite3.connect("library.db")
    mycursor =mydb.cursor()
    import MAIN_MENU
    studID=str(input("KINDLY ENTER YOUR STUDENT_ID PLEASE:- "))
    all_IDs= list(mycursor.execute("SELECT stud_ID FROM STUDENTS "))
    IDs=[]
    for ID in all_IDs:
        IDs.append(ID[0])
    print(IDs)
    if studID in IDs:
        student_name = list(mycursor.execute("SELECT stfname FROM STUDENTS WHERE stud_ID = ?", (str(studID),)))
        print(f"Hello {student_name[0][0]} ! Welcome ... ")
        mydb.commit()
        mydb.close()
        return MAIN_MENU.student_main_menu() #TODO

    else:
        print("THIS ID DOESN'T EXSIST ... ")
        mydb.commit()
        mydb.close()
        return register_as_new_student()
       






def staff():
    print("YOU ARE WELCOME!!!")
    neworold=input("ARE YOU A REGISTERED STAFF MEMBER? (YES/NO)")
    if neworold.upper()=="YES":
        return login_as_old_staff()
    elif neworold.upper()=="NO":
        return register_as_new_staff()
    else:
        print("WRONG INPUT, CHECK AGAIN IF YOU HAVE SPELLT IT CORRECTLY AND IN THE UPPER CASE")
        return staff()

def student():
    print("WELCOME PRECIOUS FUTURE OF THIS EARTH :)")
    existingornot=input("ARE YOU A REGISTERED STUDENT? (YES/NO)")
    if existingornot.upper()=="YES":
        return login_as_old_student()
    elif existingornot.upper()=="NO":
        return register_as_new_student()
    else:
        print("WRONG INPUT CHECK AGAIN")
        return student()


    


def Staff_Or_Student():
    stforstud=input("ARE YOU A STAFF MEMBER OR A STUDENT? (STAFF/STUDENT)")
    if stforstud.upper()=="STAFF":
        return staff()
    elif stforstud.upper()=="STUDENT":
        return student()
    else:
        print("WRONG INPUT ! CHECK IT AGAIN PLEASE ... ")
        return 
        
    
        


mydb.commit()
mydb.close()