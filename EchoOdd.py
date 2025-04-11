n=int(input("enter the size of array List"))
arr=list(map(int,input().split()))
for _ in range(1,n,2):
    print(arr[_] ,end=" ")