def salary(w):
    count = sum(w) - (len(w)*min(w))
    return count   


if __name__ == "__main__":
    test_cases = int(input())
    ans = list()
    for i in range(0, test_cases):
        N = int(input())
        w = list(map(int, input().split()))
        ans.append(str(salary(w)))

    print("\n".join(ans))