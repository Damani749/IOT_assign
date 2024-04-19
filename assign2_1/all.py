
import update
import create
import delete


print("------------------------------------------------------------")
print("0. Exit")
print("1. Add an Employee")
print("2. Update salary of an employee")
print("3. Delete the record of an employee")
print("------------------------------------------------------------")

choice = int(input("Enter the choice as per your requirement.\n"))

while choice != 0:
    if choice == 1:
        create.create_record()
    elif choice == 2:
        update.update_record()
    elif choice == 3:
        delete.delete_record()
    elif choice == 0:
        break
    else:
        print("Invalid choice. Please try again.")

    print("------------------------------------------------------------")
    print("0. Exit")
    print("1. Add an Employee")
    print("2. Update salary of an employee")
    print("3. Delete the record of an employee")
    print("------------------------------------------------------------")

    choice = int(input("Enter the choice as per your requirement.\n"))

print("Welcome!")


