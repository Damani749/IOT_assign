# import mysql connector
import mysql.connector

# function to create a connection
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "dexter",
        password = "sunbeam",
        database = "iotdb"
    )

def update_employee(salary, empid):
    # get connection
    conn = get_connection()

    # form a query
    query = f"update employee SET salary = %s where empid = %s;"
    val = (salary, empid)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()

def update_record():
    num = int(input("Enter the Employee ID of a employee you want to delete the record."))
    sal = int(input("Enter the updated salary"))
    update_employee(sal, num)


#update_employee(194000, 904)