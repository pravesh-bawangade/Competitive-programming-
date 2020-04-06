#include <iostream>
#include <fstream>

using namespace std;

long int countSplitInv(int a[], int low, int mid, int high);

long int countInv(int a[], int low, int high) {
  if (low < high) {
    long int mid = low + (high - low)/2;
    long int left_inv = countInv(a, low, mid);
    long int right_inv = countInv(a, mid+1, high);
    long int split_inv = countSplitInv(a, low, mid, high);
    return left_inv + right_inv + split_inv;
  }
  return 0;
}

long int countSplitInv(int a[], int low, int mid, int high) {
  int n1 = mid - low + 1;
  int n2 = high - mid;
  
  int *left_a = new int[n1];
  int *right_a = new int[n2];
  
  for (int i = 0; i < n1; i++) 
    left_a[i] = a[low + i];
  for (int i = 0; i < n2; i++)
    right_a[i] = a[mid + 1 + i];
  
  int i = 0, j = 0;
  int k = low;
  long int count = 0;
  
  while (i < n1 && j < n2) {
    if (left_a[i] <= right_a[j]) {
      a[k] = left_a[i];
      i++;
    }
    
    else {
      a[k] = right_a[j];
      j++;
      count += n1 - i;
    }
    k++;
  }
  
  while (i < n1) {
    a[k] = left_a[i];
    k++;
    i++;
  }
  
  while (j < n2) {
    a[k] = right_a[j];
    k++;
    j++;
    count += n1 - i;
  }
  
  delete [] left_a;
  delete [] right_a;
  
  return count;
}

int main(int argc, char *argv[]) {
  int a[100000];
  int num;
  int i = 0;
  ifstream myfile (argv[1]);
  if (myfile.is_open())
  {
    while (myfile >> num)
    {
      a[i] = num;
      i++;
    }
    myfile.close();
  }
  long int count = countInv(a,0,100000);
  cout << count << '\n';
  return 0;
}