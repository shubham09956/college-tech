n=int(input())
arr=list(map(int,input().split()))
max=0
for i in range(0,len(arr)):
    if(arr[i]%2==0):
        k=2*arr[i]
        if(max<k):
            max=k
print(max)
