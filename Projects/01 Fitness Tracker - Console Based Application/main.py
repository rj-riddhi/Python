import mysql.connector
from enum import Enum

class User(Enum):
    CREATE_USER = 1
    EDIT_USER = 2
    VIEW_USER = 3
    DELETE_USER = 4

# db connection
mydb = mysql.connector.connect(host="localhost", user="python_user", passwd="Password@123",auth_plugin="mysql_native_password", database="radhika_python_db")

if mydb:
    mycursor = mydb.cursor()
    # mycursor.execute("Create table Users(name varchar(200), email varchar(200), age int(20))")

    # User Choice input
    print("")
    choice = int(input("Enter...\n 1 for Create User\n 2 for Edit User \n 3 for View User \n 4 for Delete User \n"))
    print(f"You have Entered {choice}")
    print("")

    if choice < 1 or choice > 4:
        print("You have entered wrong inpute, please selecte from 1,2,3,4") 
    else:
        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            mycursor.execute("Insert into Users(name,email,age) values({name},{email},{age})")
            mycursor.commit()
            mycursor.execute("Select * from Users")
            for i in mycursor:
                print(i)
else:
    print("Not connected")