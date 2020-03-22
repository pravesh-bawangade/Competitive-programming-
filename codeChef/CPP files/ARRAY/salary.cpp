#include<iostream>
int main(){
    int T;
    std:: cin>>T;
    while(T--){
        int N;
        int sum=0, min=1000000; 
        int salary;
        std::cin>>N;
        for(int i=0; i<N; i++){
            std::cin>>salary;
            sum += salary;
            min = std::min(min, salary);
        }
        std::cout<<(sum - (N*min))<<std::endl;
    }
}