n=int(input("enter the range's first number: "))
m=int(input("enter the range's last number: "))
even_count=0
odd_count=0
for i in range(n,m+1):
    if (i%2)==0:
        even_count+=1
    else:
        odd_count+=1
print("no of even numbers: ",even_count)
print("no of odd nuumbers: ",odd_count)
