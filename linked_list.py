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


'''Given the head of a linked list, 
rotate the list to the right by k places.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109'''


def rotateRight( head, k):
    if not head:
        return None
    if k == 0:
        return head
    else:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        for i in range(k % len(arr)):
            a = arr.pop()
            arr.insert(0, a)
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        arr[len(arr) - 1].next = None
        return arr[0]

    ##############       second solution
    #############################################
import collections
    def rotateRight(head, k):
        if not head or k == 0:
            return head
        else:
            d = collections.deque()
            cnt = 0
            while head:
                d.append(head)
                head = head.next
                cnt += 1
            d.rotate(k % cnt)
            for i in range(cnt - 1):
                d[i].next = d[i + 1]
            d[cnt - 1].next = None
            return d[0]

'''Given a non-negative integer represented as a linked 
list of digits, plus one to the integer.

The digits are stored such that the most significant 
digit is at the head of the list.
Example 1:

Input: head = [1,2,3]
Output: [1,2,4]
Example 2:

Input: head = [0]
Output: [1]
 
Constraints:

The number of nodes in the linked list is in the range [1, 100].
0 <= Node.val <= 9
The number represented by the linked list does not 
contain leading zeros except for the zero itself. '''

class ListNode:
    def __init__(self,val):
        self.val =val
        self.next = None

def plusOne(head) :
    if not head.next and head.val <= 8:
        return ListNode(head.val + 1)
    else:
        arr = []
        while head:
            arr.append(head)
            head = head.next

        cur = ListNode(0)
        arr.insert(0, cur)

        if arr[len(arr) - 1].val <= 8:
            arr[len(arr) - 1].val += 1
            return arr[1]
        else:
            arr[len(arr) - 1].val = 0
            carr = 1
            i = len(arr) - 2
            while i >= 0:
                tmp = arr[i].val + carr
                arr[i].val = (arr[i].val + carr) % 10

                if tmp % 10 != 0:
                    break
                carr = 1
                i -= 1

            if i != 0:
                return arr[1]
            else:
                arr[0].next = arr[1]
                return arr[0]