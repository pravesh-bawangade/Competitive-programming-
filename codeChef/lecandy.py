def lecandy(candies, list_candies):
    if candies >= sum(list_candies):
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    test_cases = int(input())
    ans = list()
    for i in range(test_cases):
        elephants , candies = map(int, input().split())
        list_candies = list(map(int, input().split()))
        ans.append(lecandy(candies, list_candies))
    print("\n".join(ans))


    


    