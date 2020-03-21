#include<iostream>

int main(){
    int test_cases;
    int N, K;
    int count;
    std::cin >> test_cases;
    while(test_cases--){
        std::cin >> N >> K;
        while(N--){
            int c;
            std::cin >> c;
            if((c+K)%7 == 0) count++;
        }
    }
    std::cout << count << std::endl;
    return 0;
}