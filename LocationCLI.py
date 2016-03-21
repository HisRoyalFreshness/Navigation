import sqlite3

def AddLocation():
    LocationName=input("Please enter the name of the location: ")
    
    while 1:
        try:
            Latitude=float(input("Please enter the latitude of the location: "))
            break
        except:
            print("Not a valid latitude!")
            
    while 1:
        try:
            Longitude=float(input("Please enter the longitude of the location: "))
            break
        except:
            print("Not a valid longitude!")

    Link=input("Please enter the link for the location: ")
    sql="select LocationID from Location"
    cursor.execute(sql)
    total=cursor.fetchall()
    LocationID=1
    for each in total:
        LocationID+=1
    Location=[LocationID,LocationName,Latitude,Longitude,Link]
    Valid=ValidateLocation(Location)
    if Valid:
        AddLocationToDatabase(Location)
        print()
        print("Added Successfully!")

def ValidateLocation(Loc):
    if 3<len(Loc[0])<30:
        if -90<=Loc[1]<=90:
            if -180<=Loc[2]<=180:
                if 4<=len(Loc[3])<=75:
                    return True
    print("Failed - Values did not meet specifications!")
    return False

def AddLocationToDatabase(values):
    
    with sqlite3.connect("Database.db") as db:
        cursor=db.cursor()
        sql="""insert into Location (
        LocationID,
        LocationName,
        Latitude,
        Longitude,
        Link
        )
        values (?,?,?,?,?)
        """
        cursor.execute(sql,values)
        db.commit()
        
def EditLocation():
    pass

def DeleteLocation():
    pass

def ViewLocation():
    with sqlite3.connect("database.db") as db:
        cursor=db.cursor()
        sql="select * from Location"
        cursor.execute(sql)
        Users=cursor.fetchall()
        for each in Users:
            print("Location {0} - ".format(each[0]))
            print("Name - {0}".format(each[1]))
            print("Longitude - {0}".format(each[2]))
            print("Latitude - {0}".format(each[3]))
            print("Link - {0}".format(each[4]))
            
def DisplayMainMenu():
    print()
    print("{0}Welcome to Location CLI{0}".format(("="*10)))
    print("What do you wish to do?")
    print("1. Add New Location")
    print("2. Edit Existing Location")
    print("3. Delete Existing Location")
    print("4. View All Existing Locations")
    print("9. Quit CLI")
    print()
    
def main():
    while 1:
        DisplayMainMenu()
        choice=input(": ")
        if choice=="1":
            AddLocation()
            
        elif choice=="2":
            EditLocation()
            
        elif choice=="3":
            DeleteLocation()
            
        elif choice=="4":
            ViewLocation()
            
        elif choice=="9":
            print("Goodbye")
            return
        
        else:
            print("That's not a valid input (1-9)")
    
if __name__=="__main__":
    main()
    
