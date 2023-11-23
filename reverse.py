def reverse(n):
    print(n[::-1])
a=[]
n=int(input("Enter number of element you want to enter:"))
for i in range(n):
    e=int(input("Enter element: "))
    a.append(e)
reverse(a)