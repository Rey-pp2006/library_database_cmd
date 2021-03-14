import random
#import main 
import sqlite3
#import UPDATE_STUDENT_TABLE

#mydb_students = sqlite3.connect("STUDENT")
#CREATE TABLE IF NOT EXISTS some_table (id INTEGER PRIMARY KEY AUTOINCREMENT, ...);


mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()

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
    



def add_new_student (new_ID , stf_name , stl_name ,st_course,st_year,st_contact,st_age,st_birthdate,st_gender):

    try:
        mydb=sqlite3.connect("library.db")
        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO STUDENTS VALUES (:stud_ID , :stfname ,:stlname ,:stcourse, :styear,:stcontact,:stage,:stbirthdate,:stgender)",
                {
                    'stud_ID': new_ID,
                    'stfname' : stf_name,
                    'stlname' : stl_name,
                    'stcourse' : st_course,
                    'styear': st_year,
                    'stcontact' : st_contact,
                    'stage': st_age,
                    'stbirthdate':st_birthdate,
                    'stgender':st_gender
                })
        mydb.commit()

        print("Data added successfully ... ")
        mycursor.execute("SELECT * FROM STUDENTS WHERE stud_ID=(?)",(new_ID,))
        print("NOW YOU ARE REGISTERERD WITH THE FALLOWING INFORMATION\n")
        print("--------------------------------------")
        ST_information = mycursor.fetchall()
        headigs=("ID             ","FIRST NAME     ","LAST NAME      ","COURSE         ","ADMISSION YEAR ", "CONTACT NUMBER ","AGE            ","BIRTHDATE      ","GENDER         " )
        for info in ST_information:
            info_dict = (dict(zip(headigs,info)))
        for key,value in info_dict.items():
            print(f"{key}: {value}")
        print("--------------------------------------")
        print(f"\n{new_ID} IS YOUR ID ! PLEASE KEEP IT .... ")
        
        try:
            mydb.commit()
            mydb.close()
            import MAIN_MENU
            return MAIN_MENU.student_main_menu()
            
        except Exception as e :
            print(e)
            print("SOMETHING WENT WRONG ! ")
            mydb.commit()
            mydb.close()
            return 

    except Exception as e:
        print(e)
        print("Ooops! Sorry Something Went Wrong ...")
        import UPDATE_STUDENT_TABLE
        return UPDATE_STUDENT_TABLE.quit_OR_home()

   
    
        

"""
        Edit_or_fine= input ("DO YOU NEED TO EDIT ANYTHING ? (YES/NO) ")
        if Edit_or_fine.replace(" ","").upper() == "YES":
            return UPDATE_STUDENT_TABLE.SURE()
        elif Edit_or_fine.replace(" ","").upper() == "NO":
            print(f"ALRIGHT ! JUST DON'T FORGET YOUR ID :{new_ID}")
            return UPDATE_STUDENT_TABLE.quit_OR_home()
        else:
            print("WRONG INPUT!")
            return UPDATE_STUDENT_TABLE.quit_OR_home()
"""
    


def check_info(new_ID):
    print("\n------------------------------------------------------------")
    stf_name=input("ENTER YOUR FIRST NAME:- ")
    print("\n------------------------------------------------------------")

    stl_name=input("ENTER YOUR LAST NAME:- ")
    print("\n------------------------------------------------------------")

    st_course=input("ENTER YOUR COURSE:- ")
    print("\n------------------------------------------------------------")

    st_year=input("ENTER THE YEAR YOU GOT ADMISSION IN:- ")
    print("\n------------------------------------------------------------")

    st_contact=input("ENTER YOUR CONTACT NUMBER:-")
    print("\n------------------------------------------------------------")

    st_age=input("ENTER YOUR AGE:-")
    print("\n------------------------------------------------------------")

    st_birthdate=input("ENTER YOUR BIRTH DATE IN (YYYY-MM-DD) FORMAT:- ")
    print("\n------------------------------------------------------------")

    st_gender=input("ENTER YOUR GENDER (FEMALE / MALE / OTHER ) :-")
    print("\n------------------------------------------------------------")

    def gender_check():
        if ( st_gender.replace(" ","").upper() == "FEMALE" ) or ( st_gender.replace(" ","").upper() == "MALE" ) or ( st_gender.replace(" ","").upper() == "OTHER" ) :
            return add_new_student (new_ID , stf_name , stl_name ,st_course,st_year,st_contact,st_age,st_birthdate,st_gender)
        else:
            print("INVALID GENDER ! YOU MUST CHOOSE BETWEEN (FEMALE / MALE / OTHER)")
            return check_info(new_ID)
    def date_check():
        if len(st_birthdate.replace(" ","")) == 10 and st_birthdate.replace(" ","")[0:4].isdigit() and st_birthdate.replace(" ","")[5:7].isdigit() and st_birthdate.replace(" ","")[8:10].isdigit():
            return gender_check()
        else:
            print("INVALID DATE ! IT MUST BE IN THIS FORM (yyyy-mm-dd)")
            return check_info(new_ID)
    def digit_check():
        if len(st_year.replace(" ","")) == 4 and st_year.replace(" ","").isdigit():
            if str(st_contact).replace(" ","").isdigit():
                if len(str(st_age).replace(" ","")) <= 2 and str(st_age).replace(" ","").isdigit():
                    return date_check()
                else :
                    print("INVALID AGE ... ")
                    return check_info(new_ID)
            else:
                print("INVALID TELEPHONE NUMBER ... ")
                return check_info(new_ID)
        else:
            print("INVALID SUBMISSION YEAR , IT SHOULD BE 4-DIGIT NUMBER ...")
            return check_info(new_ID)
            


    if stf_name.replace(" ","").isalpha() and stl_name.replace(" ","").isalpha() :
        return digit_check()
    else:
        print("FIRST NAME AND LAST NAME ARE REQUIRED AND CAN'T CONTAIN NUMBER")
        return check_info(new_ID)




def check_ID (new_ID) :
    mydb=sqlite3.connect('library.db')
    mycursor=mydb.cursor()

    student_ids =list(mycursor.execute("SELECT stud_ID FROM STUDENTS"))


    staff_ids =list(mycursor.execute("SELECT staff_ID FROM USERS"))

    all_IDs=[]

    for staff_id in staff_ids:
        all_IDs.append(staff_id[0])
    for student_id in student_ids:
        all_IDs.append(student_id[0])
    if new_ID in all_IDs:
        #id has already taken 
        mydb.commit()
        mydb.close()
        return generate_new_ID()
    else:
        mydb.commit()
        mydb.close()
        return check_info(new_ID)


mydb.commit()
mydb.close()
#check_ID (new_ID)


#add_new_student()

#TODO don't forget to call 

#generate_new_ID()


#FINISH 