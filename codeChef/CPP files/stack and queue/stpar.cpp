#include<iostream>
#include<stack>
using namespace std;
int main(){
    while(1){
        int N;
        cin>>N;
        if(N == 0){
            break;
        }
        int arr[1000];
        stack <int> s;
        for(int i=0;i<N;i++){
            cin>>arr[i];   
        }
        int k=0, j=0;
        while(j<N){
            while(s.size() && s.top()==k+1) k++, s.pop();
            if (arr[j] != k + 1) s.push(arr[j]);
            else k++;
            j++;
        }
        while (s.size() && s.top() == k + 1) k++, s.pop();
        if(k==N)cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
}