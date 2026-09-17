def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci (merged):", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci(10)


print("\nFibonacci (original):", end=" ")
a = 0
b = 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b 




print("hello toqnoq")    