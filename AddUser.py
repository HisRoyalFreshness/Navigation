import sqlite3
import re

def ValidateUser(values):
    if UsernameValidation(values[0]):
        if PasswordValidation(values[1]):
            if FirstNameValidation(values[2]):
                if LastNameValidation(values[3]):
                    if EmailValidation(values[4]):
                        print("Passed Validation")
                        return True
    print("Failed Validation")
    return False

def EmailValidation(email):
    
    with sqlite3.connect("database.db") as db:
            cursor=db.cursor()
            sql="select Email from User"
            cursor.execute(sql)
            ExistingEmails=cursor.fetchall()
            if (email,) in ExistingEmails:
                print("Email in use!")
                return False
            
    if 6<len(email)<30:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Not a valid email")
            return False
    else:
        print("Email is not valid")
        return False
    
    return True

def FirstNameValidation(firstname):
    if 2<len(firstname)<20:
        return True
    else:
        print("first name not correct length (2-20 characters)")
        return False
    
def LastNameValidation(lastname):
    if 2<len(lastname)<20:
        return True
    else:
        print("last name not correct length (2-20 characters)")
        return False

def PasswordValidation(password):
    if not any(char.isdigit() for char in password):
        print("Password does not contain a number!")
        return False
    if 6<len(password)<18:
        return True
    else:
        print("Password not correct length (6-8 characters)")
        return False
    
def UsernameValidation(username):
    if 6<len(username)<18: 
        with sqlite3.connect("database.db") as db:
            cursor=db.cursor()
            sql="select UserName from User"
            cursor.execute(sql)
            ExistingUsernames=cursor.fetchall()
            if (username,) not in ExistingUsernames:
                return True
            else:
                print("Username in use!")
                return False
    else:
        print("Username not correct size!(6-18 characters)") 
        return False
    
def AddUserToDatabase(values):
    with sqlite3.connect("Database.db") as db:
        cursor=db.cursor()
        sql="""insert into User (
        UserName,
        Password,
        FirstName,
        LastName,
        Email,
        StartFavourite,
        FinishFavourite,
        StartLast,
        FinishLast
        )
        values (?,?,?,?,?,?,?,?,?)
        """
        cursor.execute(sql,values)
        db.commit()
        
def ManuallyAddUser():
    UserName=input("Please input username: ")
    Password=input("Please input password: ")
    FirstName=input("Please input first name: ")
    LastName=input("Please input last name: ")
    Email=input("Please input email: ")
    return (UserName,Password,FirstName,LastName,Email,"None","None","None","None")

def main():
    while 1:
        print("r - add user")
        print("w - test validation")
        print("e - manaully add user")
        print("q- exit")
        a=input("")
        if a=="r":
            User=("TotallyNotJiminy","19Christian","Jiminy","Haynes","jiminy@jjhaynes.co.uk","None","None","None","None")
            valid=ValidateUser(User)
            if valid:
                AddUserToDatabase(User)
                print("success")
        elif a=="w":
            valid=ValidateUser(("TotlyNotJiminy","19Christian","Jiminy","Haynes","jiminy@jjhaynes.co.uk","None","None","None","None"))
        elif a=="e":
            User=ManuallyAddUser()
            valid=ValidateUser(User)
            if valid:
                AddUserToDatabase(User)
                print("Success")
        elif a=="q":
            return

if __name__=="__main__":
        main()
    
