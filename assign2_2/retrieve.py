# # import mysql connector
# import mysql.connector

# # create connection with mysql server
# connection = mysql.connector.connect(
#     host = "localhost",
#     port = 3306,
#     user = "dexter",
#     password = "sunbeam",
#     database = "iotdb"
# )

# # form a query
# query = "select * from employee;"
# query1 = "select * from employee where department = %s;"
# query2 = "select * from employee where salary = (select max(salary) from employee);"
# query3 = "select * from employee where salary = (select min(salary) from employee);"
# val1 = (department, )

# # create a cursor to execute query
# cursor = connection.cursor()

# # execute query using cursor
# cursor.execute(query)

# # executing query1 using cursor
# cursor.execute(query1, val1)

# print("Employee with the max salary.\n")

# # executing query2 using cursor
# cursor.execute(query2)

# print("Employee with the min salary.\n")

# # executing query3 using cursor
# cursor.execute(query3)

# # get data from cursor
# records = cursor.fetchall()                 #returns list of tuples

# print(records)

# # close the cursor
# cursor.close()

# # close the connection
# connection.close()

import mysql.connector

# Create connection with MySQL server
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="dexter",
    password="sunbeam",
    database="iotdb"
)

# Form queries
query = "SELECT * FROM employee;"
query1 = "SELECT * FROM employee WHERE department = %s;"
query2 = "SELECT * FROM employee WHERE salary = (SELECT MAX(salary) FROM employee);"
query3 = "SELECT * FROM employee WHERE salary = (SELECT MIN(salary) FROM employee);"
department = input("Enter the department you want to see the list of employees: ")

# Create a cursor to execute queries
with connection.cursor() as cursor:
    # Execute query
    cursor.execute(query)
    records = cursor.fetchall()
    print("All Employees:")
    for record in records:
        print(record)
    print("\n")


    # Execute query1
    cursor.execute(query1, (department,))
    records1 = cursor.fetchall()
    print(f"All employees in {department} are: ")
    for record in records1:
        print(record)

    # Execute query2
    cursor.execute(query2)
    record_max_salary = cursor.fetchone()
    print("\nEmployee with the max salary:")
    print(record_max_salary)

    # Execute query3
    cursor.execute(query3)
    record_min_salary = cursor.fetchone()
    print("\nEmployee with the min salary:")
    print(record_min_salary)

# close the cursor
cursor.close()

# close the connection
connection.close()
