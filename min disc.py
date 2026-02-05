n=int(input("no. of items"))
li=[]
minit={}
for i in range (n):
    z=input("write name,price and discount seprating with comma: ")
    sp=z.split(',')
    name=sp[0]
    price=int(sp[1])
    disc=int(sp[2])
    mini=price*(disc/100)

   
    minit.update({name:mini})

print(min(minit, key=minit.get))
print(minit)

