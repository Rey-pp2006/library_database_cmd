import sqlite3

mydb=sqlite3.connect("library.db")
mycursor=mydb.cursor()





mycursor.execute("""CREATE TABLE IF NOT EXISTS BOOK (
    book_ID VARCHAR,
    bktitle VARCHAR,
    bkedition VARCHAR, 
    bkauthor VARCHAR, 
    bkpublisher VARCHAR, 
    bkcopies INT, 
    bk_source VARCHAR, 
    bk_cost INT, 
    bk_remarks VARCHAR )""") 


mycursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
    staff_ID VARCHAR,
    stffname CHAR,
    stfflname CHAR,
    stffcontactnumber INT,
    stfemail VARCHAR,
    stfaddress VARCHAR, 
    stfpassword VARCHAR, 
    stftype VARCHAR )""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS BookBorrowReturnRecords(
     Borrowers_ID VARCHAR,
     book_ID VARCHAR, 
     bktitle VARCHAR,  
     releaseDate DATE, 
     duedate DATE, 
     bkdatereturn DATE )""")


mycursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS( 
    stud_ID VARCHAR PRIMARY KEY ,
    stfname VARCHAR,
    stlname VARCHAR,
    stcourse VARCHAR,
    styear VARCHAR,
    stcontact VARCHAR,
    stage VARCHAR,
    stbirthdate VARCHAR,
    stgender VARCHAR )""")


mydb.commit()
mycursor.close()

