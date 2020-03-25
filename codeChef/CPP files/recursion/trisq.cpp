#include<iostream>
using namespace std;

typedef long long int ll;

void trisq()
{
	ll N;
	cin>>N;
	N/=2;
	cout<<(N*(N-1))/2<<endl;
}

int main()
{
	int T;
	cin >> T;
	while(T--){
		trisq();
	}
	return 0;
}
