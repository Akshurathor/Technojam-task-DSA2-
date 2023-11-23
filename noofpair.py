def pairs(a, K):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == K:
                count += 1
    return count
a=[]
n=int(input("Enter number of element you want to enter:"))
for i in range(n):
    e=int(input("Enter element: "))
    a.append(e)
k=int(input("Enter the value of k:"))
count=pairs(a,k)
print("Number of pairs are :",count)