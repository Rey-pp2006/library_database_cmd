"""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
"""

import sqlite3
import random
import UPDATE_USERS_TABLE

mydb= sqlite3.connect("library.db")
mycursor=mydb.cursor()


def add_new_staff(new_ID, stff_name,stffl_name,stffcontact,stf_email,stf_address,stf_password,stf_type):
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO USERS VALUES (:staff_ID,:stffname,:stfflname,:stffcontactnumber,:stfemail,:stfaddress,:stfpassword,:stftype)",
            {
                'staff_ID': new_ID ,
                'stffname':stff_name,
                'stfflname': stffl_name,
                'stffcontactnumber':stffcontact,
                'stfemail':stf_email,
                'stfaddress': stf_address,
                'stfpassword':stf_password,
                'stftype':stf_type
            })
        print("Data added successfully ... ")
        mycursor.execute("SELECT * FROM USERS WHERE staff_ID=(?)",(new_ID,))
        print("NOW YOU ARE REGISTERERD WITH THE FALLOWING INFORMATION\n")
        print("--------------------------------------------")
        STAFF_information = mycursor.fetchall()
        headigs=("ID             ","FIRST NAME     ","LAST NAME      ","CONTACT NUMBER ","EMAIL ADRESS   ", "ADRESS         " ,"PASSWORD       ","DISCREAPTION   " )
        for info in STAFF_information:
            info_dict = (dict(zip(headigs,info)))
        for key,value in info_dict.items():
            print(f"{key}: {value}")
        print("--------------------------------------------")
        print(f"\n< {new_ID} > IS YOUR ID ! PLEASE KEEP IT .... ")

        #TODO update things

        Edit_or_fine= input ("DO YOU NEED TO EDIT ANYTHING ? (YES/NO) ")
        if Edit_or_fine.replace(" ","").upper() == "YES":
            mydb.commit()
            mydb.close()
            return UPDATE_USERS_TABLE.SURE()
        elif Edit_or_fine.replace(" ","").upper() == "NO":
            mydb.commit()
            mydb.close()
            print(f"ALRIGHT ! JUST DON'T FORGET YOUR ID :{new_ID}")
            return UPDATE_USERS_TABLE.quit_OR_home()
        else:
            mydb.commit()
            mydb.close()
            print("WRONG INPUT!")
            return UPDATE_USERS_TABLE.quit_OR_home()
            
    except Exception as e:
        print(e)
        print("Ooops! Sorry Something Went Wrong ... user ")
        return 
        mydb.commit()
        mydb.close()


def check_info(new_ID):
    stff_name=input("ENTER YOUR FIRST NAME:- ")
    print("/n-----------------------------------------------------")

    stffl_name=input("ENTER YOUR LAST NAME- ")
    print("/n-----------------------------------------------------")

    stffcontact=input("ENTER YOUR CONTACT NUMBER:- ")
    print("/n-----------------------------------------------------")

    stf_email=input("ENTER YOUR EMAIL_ID:- ")
    print("/n-----------------------------------------------------")

    stf_address=input("ENTER YOUR HOME ADDRESS:- ")
    print("/n-----------------------------------------------------")

    stf_password=input("ENTER YOUR PASSWORD FOR THE NEW ACCOUNT:-")
    print("/n-----------------------------------------------------")

    stf_type=input("Any extra descreaption about yourself:- ")
    print("/n-----------------------------------------------------")

    def digit_check():
        if stffcontact.replace(" ","").isdigit():
            if "@" in stf_email.replace(" ","").lower() :
                if len(stf_password) >= 7:
                    return add_new_staff(new_ID, stff_name,stffl_name,stffcontact,stf_email,stf_address,stf_password,stf_type)
                else:
                    print("\nPASSWORD IS NOT STRONG ENOUGH ")
                    return check_info()
            else:
                print("\nINVALID EMAIL ADRESS ... ")
                return check_info(new_ID)
        else:
            print("\nINVALID TELEPHONE NUMBER ... ")
            return check_info(new_ID)
           

    if stff_name.isalpha() and stffl_name.isalpha() :
        return digit_check()
    else:
        print("\nFIRST NAME AND LAST NAME ARE REQUIRED AND CAN'T CONTAIN NUMBER")
        return check_info(new_ID)




  
def check_ID (new_ID) :
    mydb=sqlite3.connect("library.db")
    mycursor=mydb.cursor()
    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))


    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))

    all_IDs=[]

    for staff_id in staff_ids:
        all_IDs.append(staff_id[0])
    for student_id in student_ids:
        all_IDs.append(student_id[0])
    if str(new_ID) in all_IDs:
        #id has already taken 
        mydb.commit()
        mydb.close()
        return generate_new_ID()
    else:
        mydb.commit()
        mydb.close()
        return check_info(new_ID)

def generate_new_ID():
    one_t0_five=[1,2,3,4,5,6]
    null_to_nine=["0","1","2","3","4","5","6","7","8","9"]
    ID=[]
    digit_num=random.choice(one_t0_five)
    while digit_num != 0 : 
        ID.append(random.choice(null_to_nine))
        digit_num -= 1
    final_ID="".join(ID)
    return check_ID(final_ID)

generate_new_ID()
 
mydb.commit()
mydb.close()