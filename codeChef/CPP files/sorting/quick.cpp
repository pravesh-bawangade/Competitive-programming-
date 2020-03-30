#include<iostream>
using namespace std;

int partition(int *A, int start, int end){

    int pivot = A[end];
    int pIndex = start;
    for(int i = start; i<end;i++){
        if(A[i]<=pivot){
            swap(A[i], A[pIndex]);
            pIndex++;
        }
    }
    swap(A[pIndex],A[end]);
    return pIndex;
}

int QuickSort(int *A, int start, int end){
    if(start<end){
        int pIndex = partition(A, start, end);
        QuickSort(A,start, pIndex-1);
        QuickSort(A,pIndex+1, end);
    }
}

int main(){
    int A[]  = {7,6,5,4,3,2,1,0};
    QuickSort(A,0,7);
    for(int i =0; i<8;i++) cout<<A[i]<<" ";
}
