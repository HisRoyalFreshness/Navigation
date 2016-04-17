import sqlite3
import re

def ValidateUser(values):
    """function that validates the user data, returns true or false
    depending on the validity, pass in a tuple of data containing
    the username,password,firstname,lastname,email in that order"""
    
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
    """function that validates the email to see if it's accurate
    and not already registered to another account, pass in a string
    containing the email
    """
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
    """Function that validates the first name, returning true or false
    depending on the validity of the name"""
    if 2<len(firstname)<20:
        return True
    else:
        print("first name not correct length (2-20 characters)")
        return False
    
def LastNameValidation(lastname):
    """Function that validates the last name, returning true or false
    depending on the validity of the name"""
    if 2<len(lastname)<20:
        return True
    else:
        print("last name not correct length (2-20 characters)")
        return False

def PasswordValidation(password):
    """Function that validates the password, returning true or false
    depending on the validity of the password"""
    if not any(char.isdigit() for char in password):
        print("Password does not contain a number!")
        return False
    if 6<len(password)<18:
        return True
    else:
        print("Password not correct length (6-8 characters)")
        return False
    
def UsernameValidation(username):
    """Function that validates the username, returning true or false
    depending on the validity of the name, it also checks the
    database to make sure that the username is not currently in use"""
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
    """Function that inserts a neww user into the database,
    pass in a tuple containing the data in the following order:
    username, password,firstname,lastname,email,none,none,none,none"""
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
    """A way to add a user without going through for the site, only for server technicians"""
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
    
