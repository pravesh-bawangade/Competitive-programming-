def cnote(p,c,x,y,k):
    rem = x - y
    for i in range(len(c)):
        if (k >= c[i]) and (p[i] >= rem):
            return "LuckyChef"
    else:
        return "UnluckyChef"

if __name__ == "__main__":
    test_cases = int(input())
    ans = list()
    for i in range(0, test_cases):
        p = list()
        c = list()
        x , y, k, n = map(int, input().split())
        for j in range(0, n):
            a, b = map(int, input().split())
            p.append(a)
            c.append(b)
        ans.append(cnote(p, c, x, y, k))

    print("\n".join(ans))