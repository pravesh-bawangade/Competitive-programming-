def mutateMinions(N, K, m):
    count = 0
    for i in [x+K for x in m ]:
        if i % 7 == 0:
            count += 1
    return count 


if __name__ == "__main__":
    test_cases = int(input())
    ans = list()
    for i in range(0, test_cases):
        N, K = map(int, input().split())
        m = list(map(int, input().split()))
        ans.append(str(mutateMinions(N, K, m)))

    print("\n".join(ans))