/*
File_name : compareTriplet.c
Author : Pravesh Bawangade
*/

#include<stdio.h>

int main(){
    // inputs
    int Alice[3];
    int Bob[3];
    for(int i=0; i<3; i++){
        scanf("%d", &Alice[i]);
    }
    for(int i=0; i<3; i++){
        scanf("%d", &Bob[i]);
    }
    // main calculation
    int alice_pt = 0;
    int bob_pt = 0;
    for(int i=0; i<3; i++){
        if(Alice[i] > Bob[i]){
            alice_pt += 1;
        }
        else if(Alice[i] < Bob[i]){
            bob_pt += 1;
        }
        
    }
    printf("%d %d\n", alice_pt, bob_pt);
}