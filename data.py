# Data 
# Two type -> Numerical [2,9,66,77,78] and String ["Hello", "Gayatri", "gggg...@gmail.com"]
# numerical -> number(1,2,3) and float(decimal) [2.3, 45.6, 09.4]
#Boolean data type -> True/false, Yes/No 

a = 10 #integer
b = 2.33 #float
c = "Gayatri" #String
n = False #Boolean

print(type(a))
print(type(b))
print(type(c))
print(type(n))


# Data Input

a = 4
b = 33
c = 83

addition_result = a + b + c
print(addition_result)

product_result = a * b * c
print(product_result)

result = a / b / c
print(result)

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))

sum = a + b + c
print(sum)



a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))

#Convert the input(int) to float(Decimal)
x = float(a)
y = float(b)
z = float(c)

# printing the data type of x, y, z
print(type(x))
print(type(y))
print(type(z))

sum = x + y + z
print(sum)
