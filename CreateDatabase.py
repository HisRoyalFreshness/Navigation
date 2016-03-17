import sqlite3


def main():
    with sqlite3.connect("Database.db") as db:
        cursor=db.cursor()
        sql="""create table User
                (UserName text,
                Password text,
                FirstName text,
                LastName text,
                Email text,
                StartFavourite text,
                FinishFavourite text,
                StartLast text,
                FinishLast text,
                primary key(UserName))
                """
        cursor.execute(sql)
        
        sql="""create table Location
                (LocationID interger,
                LocationName text,
                Latitude text,
                Longitude text,
                Link text,
                primary key(LocationID))
                """
        cursor.execute(sql)
        db.commit()
    
if __name__=="__main__":
    choice=input("do you wish to make a new database? (y/n)").lower()
    if choice =="y":
        main()
