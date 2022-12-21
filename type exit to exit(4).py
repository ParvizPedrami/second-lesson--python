list=[]
while true:
    num=int(input("enter your number: "))
    list.append(num)
    c=input("type EXIT to kill the programm")
    if c=="exit":
        break
a=sum(list)
print(a)
