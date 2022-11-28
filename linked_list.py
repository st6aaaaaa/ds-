class Node:
    def __init__(self, i):
        self.val = i
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.root = None
        self.size = -1

    def get(self, index: int) -> int:

        if index < 0 or index > self.size:
            return -1

        if self.size == -1:
            return -1
        if self.root is None:
            return -1
        if index == 0:
            return self.root.val

        cnt = 0
        cur = self.root
        while cnt != index:
            cur = cur.next
            cnt += 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        # self.addAtIndex(0,val)

        self.size += 1
        newNode = Node(val)
        newNode.next = self.root
        self.root = newNode

    def addAtTail(self, val: int) -> None:
        # self.addAtIndex(self.size+1,val)

        if self.root is None:
            self.size += 1
            self.root = Node(val)
        else:
            cnt = 0
            cur = self.root
            while cnt != self.size:
                cur = cur.next
                cnt += 1
            cur.next = Node(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size + 1:
            return
        if self.size == -1 and index == 0:
            newNode = Node(val)
            newNode.next = self.root
            self.root = newNode
            self.size += 1
            return
        if index == 0:

            newNode = Node(val)
            newNode.next = self.root
            self.root = newNode
            self.size += 1

            return
        else:

            cur = self.root
            nex = None

            cnt = 0
            while cnt != index - 1:
                print(cur.val)
                cur = cur.next
                cnt += 1
            nex = cur.next
            cur.next = Node(val)
            cur.next.next = nex
            self.size += 1
            return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.root = self.root.next
            return
        else:
            cnt = 0
            cur = self.root
            prev = None
            while cnt != index:
                prev = cur
                cur = cur.next
                cnt += 1
            prev.next = cur.next
            self.size -= 1
            return

        # Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

def size_of_linked_list(root):
    arr=[root]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return len(arr)


'''Given the head of a linked list, remove the nth node 
from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:


Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''


def removeNthFromEnd(head, n: int):
    c = function(head, n)
    if c == 0:
        head = head.next
        return head
    else:
        cnt = 1
        cur = head
        while cnt != c:
            head = head.next
            cnt += 1
        head.next = head.next.next
        return cur
def function(node, n):
    arr = [node]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return len(arr) - n

'''You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made 
by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]'''


def mergeTwoLists(list1, list2):
    arr = []
    while list1 and list2:
        if list1.val <= list2.val:
            arr.append(list1)
            list1 = list1.next
        else:
            arr.append(list2)
            list2 = list2.next
    if list1 is None:
        arr.append(list2)
    else:
        arr.append(list1)

    for i in range(len(arr) - 1):
        arr[i].next = arr[i + 1]
    return arr[0]
