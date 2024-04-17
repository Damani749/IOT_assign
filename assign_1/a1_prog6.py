num = int(input("Enter the number you want to find the factorial.\n"))

def fun_fact(num):
    count = 1;
    fact = 1;
    while (count <= num):
        fact = fact * count
        count = count + 1
    print(f"Factorial = {fact}")

fun_fact(num)