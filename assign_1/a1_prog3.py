n1 = float(input("Enter num1: "))
n2 = float(input("Enter num2: "))
n3 = float(input("Enter num3: "))

def avg_fun(n1, n2, n3):
    avg = (n1 + n2 + n3)/3
    print(round(avg,2))

avg_fun(n1, n2, n3)