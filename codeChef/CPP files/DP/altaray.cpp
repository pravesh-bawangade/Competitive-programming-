#include<iostream>
using namespace std;

int main(){
    int T;
    cin>>T;
    while(T--){
        int N;
        cin>>N;
        int a[1000];
        for(int i=0; i<N;i++) cin>>a[i];
        int len[N];
        len[N] = 1;
        for (int i = N - 1; i >= 1; i--) {
            if (a[i] * (long long) a[i + 1]< 0) {
                len[i] = len[i + 1] + 1;
            } else {
                len[i] = 1;
            }
        }
        for(int i=0; i<N;i++)cout<< len[i];
    }
}
