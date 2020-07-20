#include <stdio.h>

int main(void) {
    // inputs
    int T;
	scanf("%d",&T);
	while(T--)
	{
	    int N, M;
	    scanf("%d", &N);
        scanf("%d", &M);
	    int N_array[N];
        int P_array[N];
        for(int i=0;i<N;i++){
            scanf("%d", &N_array[i]);
        }
        for(int i=0;i<N;i++){
            scanf("%d", &P_array[i]);
        }
        int arr[M];
	    for(int i=0; i<M; i++)
		{
	        arr[i]=-1;
	    }
	    
	    // main calculation
	    for(int i=0; i<N; i++)
	    {
	        if(arr[N_array[i]-1]==-1)
	        arr[N_array[i]-1]=0;
	        
	        arr[N_array[i]-1]+=P_array[i];
	    }
	    int min=10000;
	    for(int i=0; i<M; i++)
	    {
	        if(arr[i]!=-1)
	        {
	            if(arr[i]<min)
	            min=arr[i];
	        }
	    }
        printf("%d\n", min);
	}
	return 0;
}