#include<iostream>
using namespace std; 
  
int fib(int n) 
{ 
    if (n <= 1) 
        return n; 
    return fib(n-1) + fib(n-2); 
} 
  
int main () 
{   int T;
    cin >> T;
    while(T--){
        int N, M;
        cin>>N>>M;
        cout << 2*fib(N)%M; 
    } 
    
    return 0; 
} 
  