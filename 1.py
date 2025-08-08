#count how many digits are there in a number
n = int(input("Enter a number: "))
count = 0

while (n != 0):
    n = n//10
    count += 1

if count == 0:
    print("The number of digits is 1")
else: 
    print("The number of digits is:", count)
