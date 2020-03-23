#include<iostream>
#include<stack>
using namespace std;

int main(){
    int T;
    cin>>T;
    while(T--){
        stack <char> sk;
        int count =0;
        string s;
        cin>>s;
        for(int i=0; i<s.length();i++){
            if(s[i] == '<'){
                sk.push(s[i]);
            }
            else if (s[i] == '>'){
                if(!sk.empty()){
                    sk.pop();
                    count++;
                }
            }
        }
        cout<<(count==0? count:count*2)<<endl;
    }
    return 0;
}