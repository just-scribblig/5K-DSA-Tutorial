n,k = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
 
if k==0:
    print(ls[0]-1 if ls[0] > 1 else -1)
elif k<n:
    print(-1 if ls[k-1] == ls[k] else ls[k-1])
else:
    print(ls[k-1])
