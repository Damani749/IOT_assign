
#--------------------------------------------------------------------------------------#
num = int(input("Enter a 4 digit number: "))

def faceval_fun(num):
    while(num != 0):
        temp = num % 10
        print(f"The face value of num is: {temp}")
        num = num // 10

def placeval_fun(num):
    count = 1
    while(num != 0):
        temp = ((num %10) * count)
        print(f"The place value is: {temp}")
        num = num //10
        count = count * 10

def rev_fun(num):
    rev_str = ""

    while(num != 0):
        temp = num % 10
        rev_str += str(temp)
        num = num // 10

    print(f"The reversed digits of num are: {rev_str}\n")

def face_place_rev_fun():
    faceval_fun(num)
    print("\n")
    placeval_fun(num)
    print("\n")
    rev_fun(num)

face_place_rev_fun()
#--------------------------------------------------------------------------------------#
