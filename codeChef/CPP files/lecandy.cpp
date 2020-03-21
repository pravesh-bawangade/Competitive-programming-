#include<iostream>

int main(){
    int cases;
    
    int count1=0, count2=0;
    std::cin >> cases;
    while(cases--){
        int sum=0;
        int E, C;
        std:: cin >> E >> C;
        while(E--){
            int a;
            std:: cin >> a;
            sum += a;
        }
        if(sum <= C){
            std::cout<<"Yes";
        }
        else std::cout<<"No";
    }
    return 0;
}