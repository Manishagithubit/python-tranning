number =int(input("Enter number "))
if number%2==0:
    print(f" {number} is Even Number")
else:
    print(f"{number} is Odd Number ") #another ways
    print(number,"is Odd number")   #primary or first ways


a=10
b=20

# beforeswapping
print(a)
print(b)

# after the swapping
a,b=b,a
print(a)
print(b)