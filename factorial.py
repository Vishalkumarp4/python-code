def factorial(num):
     product = 1
     for i in range (num):
        product = product*(i+1)
     return product
f= factorial(4)
print(f)    