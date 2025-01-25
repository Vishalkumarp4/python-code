'''a=input("entre : ")
#b=a[::-1]
if a==a[::-1]:
    print("fibbonaccy")
else:
    print("not fibbonacy")'''
    
    
x=int(input("entre the no: "))  
a=0
b=1
c=0
for i in range (x):
    print(c, end="")
    a=b
    b=c
    c=a+b
 