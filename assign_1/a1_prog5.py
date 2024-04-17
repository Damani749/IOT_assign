s1 = int(input("Enter s1 marks :"))
s2 = int(input("Enter s2 marks :"))
s3 = int(input("Enter s3 marks :"))

def grade_fun(s1, s2, s3):
    avg = (s1+s2+s3)/3
    if (avg<60):
        print(f"Grade F")
    elif (59<avg<70):
        print(f"Grade D")
    elif (69<avg<80):
        print(f"Grade C")
    elif (79<avg<90):
        print(f"Grade B")
    else:
        print(f"Grade A")

grade_fun(s1, s2, s3)

