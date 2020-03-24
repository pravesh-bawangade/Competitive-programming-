#include<iostream>

int euclid_gcd(int a, int b){
    int dividend = a >= b ? a:b;
    int divisor = a <= b ? a:b;
    while(divisor != 0){
        int remainder = dividend % divisor;
        dividend = divisor;
        divisor = remainder;
    }
    return dividend;

}

int euclid_gcd_recur(int a, int b){
    return b==0 ? a:euclid_gcd_recur(b, a%b);
}

int main(){
    return 0;
}