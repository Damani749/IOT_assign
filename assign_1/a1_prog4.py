n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n3 = int(input("Enter num3: "))

def max_fun(n1, n2, n3):
    if n1 > n2 > n3:
        print(f"The max number is : {n1}")
    elif n1 > n3 > n2:
        print(f"The max number is : {n1}")
    elif n2 > n1 > n3:
        print(f"The max number is : {n2}")
    elif n2 > n3 > n1:
        print(f"The max number is : {n2}")
    elif n3 > n2 > n1:
        print(f"The max number is : {n3}")
    else:
        print(f"The max number is : {n3}")

max_fun(n1, n2, n3)
    
