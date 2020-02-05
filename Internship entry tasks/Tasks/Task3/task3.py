"""
File Name : task3.py
Author : Pravesh Bawangade
Functions: 1. findOrder(n) - returns order of given sequence.
"""      
def findOrder(n):
    """
    Find order of given dependencies.
    Inputs: n - list of lists consisting of dependencies.
    Returns: r - output sequence
    """
    out = dict()
    r =""
    for x in n:
        l = ""
        for i in n:
            if x[0] == i[0]:
                l = l + i[1]
        out[x[0]] = l
    print(out)
    for i in out:
        for j in out[i]:
            if j in out:
                r = r + i + j + out[j]
    return r

if __name__ == "__main__":
    print("Input dependencies [['A','B'],['A','C'],['E','A']] ....")
    order = findOrder([['A','B'],['A','C'],['E','A']])
    
    print("Order is : "+ order)