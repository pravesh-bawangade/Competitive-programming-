def rainbowArray(K, m):
    if K % 2 == 0:
        return "no"
    else:
        for i in range((K//2)):
            if not ((m[i] == m[K-(i+1)]) and (not ((m[i] - m[i+1]) >1))):
                return "no"
        if m[(K//2)] == 7:
            return "yes"
        else:
            return "no"
        
        

if __name__ == "__main__":
    test_cases = int(input())
    ans = list()
    for i in range(0, test_cases):
        K = int(input())
        m = list(map(int, input().split()))
        ans.append(str(rainbowArray(K, m)))

    print("\n".join(ans))