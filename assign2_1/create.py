# importing module of mysql connector
import mysql.connector
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "dexter",
        password = "sunbeam",
        database = "iotdb"
    )


# empid = int(input("Enter empid : "))
# name = input("Enter name : ")
# department = input("Enter department : ")
# email = input("Enter email :")
# salary = int(input("Enter salary : "))
# doj = input("Enter date of joining : ")

def create_employee(empid, name, department, email, salary, doj):
    # get connection
    conn = get_connection()

    # form a query
    query = f"insert into employee values({empid}, '{name}', '{department}', '{email}', {salary}, '{doj}');"

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()

#create_employee(empid, name, department, email, salary, doj)

def create_record():
    empid = int(input("Enter empid : "))
    name = input("Enter name : ")
    department = input("Enter department : ")
    email = input("Enter email :")
    salary = int(input("Enter salary : "))
    doj = input("Enter date of joining : ")
    create_employee(empid, name, department, email, salary, doj)


    