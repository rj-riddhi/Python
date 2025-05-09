import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="python_user", passwd="Password@123", auth_plugin="mysql_native_password", database="radhika_python_db")

if mydb:
    print("Connection Successfull!!")
    mycursor = mydb.cursor()

    # Ceate DB
    mycursor.execute("Create database radhika_python_db")
    mycursor.execute("Show databases")
    for db in mycursor:
        print(db)

    # Create Table
    mycursor.execute("Create table user(name varchar(200), sal int(20))")
    mycursor.execute("Show tables")
    for tables in mycursor:
        print(tables)

    # Insert Data
    mycursor.execute("Insert into user(name,sal) values('Radhika','1234')")
    mydb.commit()

    # To insert many values at a time
    query = "Insert into user(name, sal) values(%s,%s)"
    mytuples = [("Ankit", 20000), ("Nikita", 30000), ("Monika", 40000)]
    mycursor.executemany(query,mytuples)
    mydb.commit()

    # Update the data
    mycursor.execute("Update user SET name='Ankita' WHERE name='Ankit'")
    mydb.commit()

    # Delete the data
    mycursor.execute("Delete from user WHERE name='Monika'")
    mydb.commit()

    # Fetch the data
    mycursor.execute("Select * from user")
    for records in mycursor:
        print(records)

else:
    print("Connection Unsuccessfull")