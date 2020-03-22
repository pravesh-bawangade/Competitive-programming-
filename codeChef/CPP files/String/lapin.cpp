#include<iostream>
#include<algorithm>
using namespace std;

int main() {
    int ntest;
    cin >> ntest;

    while (ntest--) {
        string s;
        cin >> s;
        int len = s.size();

        string a = s.substr(0, (len + 1) / 2);
        string b = s.substr(len - (len + 1)/2, (len + 1) / 2);
        
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        if (a == b) cout<<"YES\n";
        else cout<<"NO\n";
    }
    return 0;
}