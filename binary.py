def count_bits(n):
    binary=format(n, 'b')
    print (binary)
    ans=binary.count("1")
    print(ans)

x=int(input("Enter a integer: "))
count_bits(x)