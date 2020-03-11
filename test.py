count = 0
N=5
r = []
for i in range(1, N+1):
    l=[]
    for j in range(i):
        count+=1
        l.append(str(count))
    r.append(l)
    print("*".join(l))
for i in range(1,len(r)+1):
    print("*".join(r[len(r)-i]))

    
