#include<iostream>

struct Node{
    int data;
    Node* link;
};

Node* top = NULL;
void Push(int x){
    struct Node* temp = (struct Node*) malloc(sizeof(Node*));
    temp->data = x;
    temp->link = top;
    top = temp;
}
void Pop(){
    struct Node *temp;
    if(top == NULL) return;
    temp = top;
    top = top->link;
    free(temp);
}