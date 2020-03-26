#include<iostream>
#include<algorithm>
using namespace std;

int N, D;
int L[1000];



int main(){
    
    cin >> N >> D;
    for(int j=1;j<=N;j++){
        cin>>L[j];
    }
    sort(L+1, L+N+1);
    int count=0;
    int i =1;
    while(i<N){
        if (abs(L[i] - L[i+1]) <= D)  {
            count++;        
            i += 2;
        }
        else i++;
    }  
    cout<<count<<endl;
    return 0;
}