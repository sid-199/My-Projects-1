def Fibonacci(n):
    if n<=0:
        print([])
    elif n<=1:
        print([0])
    elif n<=2:
        print([0,1])

    elif n>2:
        fib_ser=[0,1]

        for i in range (2,n):
            fib=fib_ser[i-1]+fib_ser[i-2]
            fib_ser.append(fib)

        print(fib_ser)


Fibonacci(int(input()))