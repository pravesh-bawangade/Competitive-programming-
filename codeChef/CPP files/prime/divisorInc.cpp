#include<iostream>
#include<c++/v1/math.h>
using namespace std;
class DivisorInc
{
    public:
    int countOperations(int N, int M)
    {
        if(N == M) return 0;
        int used[200001];
        for(int i=0; i < 100001;++i) { used[i] = 333333; }

        used[N] = 0;
        for(int k=N; k <=(M);++k)
        {
            for(int i=2; i <= (sqrt(k)+1) ;++i)
            {
                if(k%i == 0)
                {
                    int t = k/i;
                    if(k+i <=M)
                    {
                        used[k+i] = min(used[k]+1, used[k+i]);
                    }
                    if(k+t <= M)
                        used[k+t] = min(used[k]+1, used[k+t]);
                }
            }
        }
        if(used[M]==333333) return -1;
        return used[M];
    }
};
int main()
{
    int n, m;
    cin>>n>>m;
    DivisorInc ob;
    cout<<ob.countOperations(n, m);

    return 0;
}