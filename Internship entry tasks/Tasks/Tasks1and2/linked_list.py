"""
File Name : linked_list.py
Author : Pravesh Bawangade
Classes: 1. Node() - Creation of Node for Linked list.
         2. LinkedList() - Manipulation of Linked List using different functions defined in this class. 
"""

class Node:
    """
    Creation of node for linked list.
    """
    def __init__(self, data=None, next=None, prev=None):
        """
        input: data - data for the node.
               next - object of next node of type Node
               prev - object of prev node of type Node
        """
        self.data = data 
        self.next = next
        self.prev = prev
    

class LinkedList:
    """
    This class serves with relevant functions for manipulation of Linked list.   

    """
    def __init__(self):
        """
        initialise head as object of class Node.
        """
        self.head = Node()

    def addNode(self, data=None, index=None):
        """
        This function is used to add node in any index position.
        if index is none then the node will be created at the end of the linked list.
        input: data - data for Node.
               index - index at which the node should be created.
        returns: None
        """
        current = self.head
        if index != None: 
            next = self.getNext(index)
            while True:
                if current.next != next:
                    current = current.next
                else:
                    current.prev.next = Node(data, current.next, current.prev)
                    return
        else:
            while current.next != None:
                current = current.next
            current.next = Node(data, None, self.getTail())

    def getTail(self):
        """
        Returns tail node object of class node.
        """
        current  = self.head
        while current.next != None:
            current = current.next
        return current

    def listElements(self):
        """
        returns: LList - consisting of the data from each node in the linked list.
        """
        current = self.head
        LList = []
        while current.next != None:
            current = current.next
            LList.append(current.data)
        return LList

    def printLL(self):
        """
        prints the list consisting of the data from each node in the linked list.
        """
        print(self.listElements())
        
    def getElement(self, index):
        """
        inputs : index - the index from which data is required
        returns : data from the node at the given index if index is within range else returns "Out of Range!"
        """
        l = self.listElements()
        if index < len(l):
            return self.listElements()[index]
        else:
            return "Out of Range!"

    def size(self):
        """
        returns : size of the linked list.
        """
        return len(self.listElements())

    def getPrev(self, index):
        """
        inputs : index - index from which previous element is expected.
        returns : object of type Node at position previous to the index given.
        """
        count = 0
        current = self.head
        while True:
            if count <= index:
                current  = current.next
                count +=1
            else:
                return current.prev

    def getNext(self, index):
        """
        inputs : index - index from which next element is expected.
        returns : object of type Node at position next to the index given.
        """
        count = 0
        current = self.head
        while True:
            if count <= index:
                current  = current.next
                count +=1
            else:
                return current.next

    def delElement(self, index):
        """
        Removes the node from the linked list at the given index.
        inputs : index - index at which the node should be removed.
        returns : None
        """
        count = 0
        current = self.head
        while True:
            if count < index:
                current  = current.next
                count +=1
            else:
                current.next = current.next.next
                break
    
    def addLinkedList(self, data, index):
        """
        inputs : index - index from which linked list shoulde be added.
                 data - linked list of type LinkedList which should be added in the given index position.
        returns : None.
        """
        current = self.head
        if index != None: 
            next = self.getNext(index)
            while True:
                if current.next != next:
                    current = current.next
                else:
                    current.prev.next = data.getPrev(1)
                    data.getTail().next = current
                    return


if __name__ == "__main__":

    print("*********************************")
    print("Submission Q1: Implemented Classes for Implementing Doublely LinkedList.")
    print("Initializing Linked List....")
    x = LinkedList()
    print("Creating nodes for data [1, 12, 34, 45, 67] using addNode() function of class LinkedList")
    x.addNode(1)
    x.addNode(12)
    x.addNode(34)
    x.addNode(45)
    x.addNode(67)
    print("print linked list using printLL() function from class LinkedList")
    x.printLL()
    print("Size of linked list using size() function from class LinkedList" )
    print("Size : " + str(x.size()))
    print("Get data of node at particular index using getElement(index) function from class LinkedList.")
    print("Element at index 3 - "+ str(x.getElement(3)))
    print("*********************************")
    print("Submission Q2: Adding linked list in existing LinkedList.")
    print("Initializing new linked list 'y': ")
    y = LinkedList()
    print("Creating nodes for data [4, 5, 6, 7, 8] using addNode() function of class LinkedList")
    y.addNode(4)
    y.addNode(5)
    y.addNode(6)
    y.addNode(7)
    y.addNode(8)
    print("print linked list using printLL() function from class LinkedList")
    print("Y -")
    y.printLL()
    print("X -")
    x.printLL()
    print("Adding linked list 'y' in existing LinkedList 'x' at index 1 using addLinkedList() function of class LinkedList:")
    x.addLinkedList(y, 1)
    x.printLL()
    print("*********************************")