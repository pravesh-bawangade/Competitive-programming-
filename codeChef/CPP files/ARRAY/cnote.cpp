#include<iostream>
/*
x - pages long poetry
y - pages left
k - money left to use
n - number of notebooks
p[i] - pages in notebook
c[i] - cost of notebooks
inputs:
T
x, y, k, n
n[i]- p[i], c[i]
*/
int main(){
    int T;
    std::cin>> T;
    while(T--){
        int x,k,y,n;
        int flag=0;
        int p[1000000],c[1000000];
        std::cin>>x>>y>>k>>n;
        for(int i=0; i<n; i++){
            std::cin>>p[i]>>c[i];
            if((p[i]>=(x-y)) && (c[i]<=k)) {
                flag=1;
            }
        }
        if(flag == 1) std::cout<<"LuckyChef"<<std::endl;
        else std::cout<<"UnluckyChef"<<std::endl;
    }
}
