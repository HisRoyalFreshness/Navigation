import sqlite3

def FetchUserData(Username):
    with sqlite3.connect("database.db") as db:
        cursor=db.cursor() 
        sql="select * from User where UserName = ?"
        cursor.execute(sql,(Username,))
        UserInfo=cursor.fetchall()
        return UserInfo

def main():
    user=FetchUserData("TotallyNotJiminy")
    for each in user:
        print(each)
        
if __name__=="__main__":
    main()
