/*
File_name : bigSum.c
Author : Pravesh Bawangade
*/

#include<stdio.h>

int main(){
    // inputs
    int N; 
    long sum = 0; 
    scanf("%d",&N); 
    long in_arr[N]; 
    for(int i=0; i < N; i++){
        scanf("%li",&in_arr[i]); 
    } 
    // main calculations
    for(int i=0; i < N; i++){
        sum = sum + (in_arr[i]) ; 
    } 
    printf("%ld\n", sum);
    return 0; 
}