1.binary number to decimal


b=int(input("enter the binary number  "))
r=0
i=1
while True:
    if b>0:
        n=b%10
        r=r+n*(pow(2,i))
        b=b//10
        i=i+1
    else:
        break
print("decimal number  ",r)


2.fibonacci series


n=int(input("enter the number of fibonacci series numbers"))
f1=0
f2=1
if n==1:
    print("fibonacci series  ",f1)
elif n==2:
    print("fibonacci series  ",f1 ,f2)
else:
    print("fibonacci series",f1 ,f2  )
    while n-2>0:
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
        n=n-1


3.multiplication table of k


k=int(input("enter the value of k  "))
for i in range(1,11):
    print(k,"*",i ,"=",k*i)


4.GCF

x=int(input("enter the number1  "))
y=int(input("enter the number2   "))
if x > y:
    small= y 
else: 
    small= x 
    print(s)
    for i in range(1, small+1): 
        if  ((x % i == 0) and (y % i == 0)): 
            g= i 
            print(g)


5.reverse


def reverse(x):
     return x[::-1]

t = reverse("jupyter")

print(t)


6.even and odd numbers


l={1,2,3,4,5,6,7,8,84,9,93,99}
even=0
odd=0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("even numbers  :",even ,"odd numbers",odd)

