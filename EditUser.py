import sqlite3
from AddUser import *

def EditUserName(value):
    """function to edit username,
    pass in tuple that contains the
    new username and the old username in that order"""
    
    if UsernameValidation(value[0]):
        try:
            with sqlite3.connect("database.db") as db:
                cursor=db.cursor()
                sql="update User set UserName=? where UserName=?"
                cursor.execute(sql,value)
                db.commit()
                return True
        except:
            return False
    else:
        return False
    
def EditPassword(value):
    """function to edit username,
    pass in tuple that contains the
    new password and the username in that order"""
    
    if PasswordValidation(value[0]):
        try:
            with sqlite3.connect("database.db") as db:
                cursor=db.cursor()
                sql="update User set Password=? where UserName=?"
                cursor.execute(sql,value)
                db.commit()
                return True
        except:
            return False
    else:
        return False

def EditFirstName(value):
    """function to edit username,
    pass in tuple that contains the
    new first name and the username in that order"""
    
    if FirstNameValidation(value[0]):
        try:
            with sqlite3.connect("database.db") as db:
                cursor=db.cursor()
                sql="update User set FirstName=? where UserName=?"
                cursor.execute(sql,value)
                db.commit()
                return True
        except:
            return False
    else:
        return False

def EditLastName(value):
    """function to edit username,
    pass in tuple that contains the
    new last name and the username in that order"""
    
    if LastNameValidation(value[0]):
        try:
            with sqlite3.connect("database.db") as db:
                cursor=db.cursor()
                sql="update User set LastName=? where UserName=?"
                cursor.execute(sql,value)
                db.commit()
                return True
        except:
            return False
    else:
        return False

def EditEmail(value):
    """function to edit username,
    pass in tuple that contains the
    new email and the username in that order"""
    
    if EmailValidation(value[0]):
        try:
            with sqlite3.connect("database.db") as db:
                cursor=db.cursor()
                sql="update User set Email=? where UserName=?"
                cursor.execute(sql,value)
                db.commit()
                return True
        except:
            return False
    else:
        return False

def EditStartFavourite(value):
    """function to edit username,
    pass in tuple that contains the
    new start favourite and the username in that order"""

    with sqlite3.connect("database.db") as db:
        cursor=db.cursor()
        sql="update User set StartFavourite=? where UserName=?"
        cursor.execute(sql,value)
        db.commit()
        return True

def EditFinishFavourite(value):
    """function to edit username,
    pass in tuple that contains the
    new finish favourite and the username in that order"""

    with sqlite3.connect("database.db") as db:
        cursor=db.cursor()
        sql="update User set FinishFavourite=? where UserName=?"
        cursor.execute(sql,value)
        db.commit()
        return True

def EditStartLast(value):
    """function to edit username,
    pass in tuple that contains the
    new start last and the username in that order"""

    with sqlite3.connect("database.db") as db:
        cursor=db.cursor()
        sql="update User set StartLast=? where UserName=?"
        cursor.execute(sql,value)
        db.commit()
        return True

def EditFinishLast(value):
    """function to edit username,
    pass in tuple that contains the
    new finish last and the username in that order"""

    with sqlite3.connect("database.db") as db:
        cursor=db.cursor()
        sql="update User set FinishLast=? where UserName=?"
        cursor.execute(sql,value)
        db.commit()
        return True

def main():
    a=EditUsername(("TotallyNotAwesome","TotallyNotJiminy"))
    with sqlite3.connect("database.db") as db:
        cursor=db.cursor()
        sql="select * from User where UserName=?"
        cursor.execute(sql,("TotallyNotAwesome",))
        print(cursor.fetchall())
        
if __name__=="__main__":
    main()
