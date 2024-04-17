num = 0
def fun_fact(num):
    count = 1;
    fact = 1;
    while (count <= num):
        fact = fact * count
        count = count + 1
    print(f"Factorial of {num} = {fact}")

while(num <= 10):
    fun_fact(num)
    num = num + 1