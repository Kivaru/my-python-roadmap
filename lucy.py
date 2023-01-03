n=int(input("Enter the number of terms: "))
sum=0

if n < 0:
   print("Please enter a positive number")
else:
    sum=0
    while(n > 0):
        sum = sum + (n/(1+n))
        n -= 1
print("The sum of series is",round(sum,6))