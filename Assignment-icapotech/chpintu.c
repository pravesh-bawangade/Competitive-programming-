/*
File_name : chpintu.c
Author : Pravesh Bawangade
*/

#include<stdio.h>

int main(){
    int T;
    scanf("%d", &T);
    while(T--){
        // take inputs
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

        // main calculations 
        int min = 1000000;
        int sum = 0;
        for(int i=1; i<=M; i++){
            for(int j=0; j<N; j++){
                if(N_array[j]==i){
                    sum = sum + P_array[j];
                }
            }
            if(sum < min){
                min = sum;
                sum = 0;
            }    
        }
        printf("%d\n", min);    
        
    }
    return 0;
}