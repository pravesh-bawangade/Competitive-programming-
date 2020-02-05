if __name__ == "__main__":
    n = list(map(int, input().split()))
    N = n[0]
    M = n[1]
    welcome = "WELCOME"
    dash = "-"
    dot = ".|."
    mid = ((N//2)+1)
    for i in range(1,N+1):
        if i < mid:
            d_n = int( ((M-3)/2)-(3 *(i-1))  ) 
            print((dash * d_n) + (dot*int(i-1)) +dot+ (dot*int(i-1))+ (dash * d_n) )
        elif i == mid:
            print(    (dash*int((M-7)/2)) + welcome +  (dash*int((M-7)/2))   )
        elif i > mid:
            dot_n = int( ((N-3)/2)-((i+1)%6) )
            d_n = int((M- (((dot_n*2)*3)+3))/2  ) 
            print((dash * d_n) + (dot* dot_n)+dot+(dot*dot_n) + (dash * d_n))