# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        count = 0
        while (temp.next != None):
            temp = temp.next
            count +=1
        mid = count//2 if count%2==0 else (count//2)+1
        temp = head
        while(mid != 0):
            temp = temp.next
            mid -=1
        return temp