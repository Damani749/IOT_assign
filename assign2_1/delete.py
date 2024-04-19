import dbcon

def delete_employee(empid):
    # get connection
    conn = dbcon.get_connection()

    # form a query
    query = f"delete from employee where empid = %s;"
    val = (empid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()

def delete_record():
    num = int(input("Enter the Employee ID of a employee you want to delete the record."))
    delete_employee(num);



