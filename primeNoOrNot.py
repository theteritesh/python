n=int(input("Enter a number"))
for i in range(2,n+1):
  if(n%i)==0:
    break
if i==n:
     print(n,"is prime number")
else:
      print(n,"is not prime number")