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


'''Given a linked list, swap every two adjacent nodes and 
return its head. You must solve the problem without modifying 
the values in the list's nodes (i.e., only nodes themselves may be changed.)
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:
Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]'''

### solutiion first
def swapPairs(head):
    if head and head.next is None:
        return head

    if not head:
        return None

    else:
        arr = []

        while head:
            arr.append(head)
            head = head.next

        if len(arr) % 2 == 0:

            for i in range(0, len(arr), 2):
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp

        else:
            for i in range(0, len(arr) - 1, 2):
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp

        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        arr[-1].next = None
        return arr[0]

######################### solution second

def swapPairs(head):
    if head and head.next is None:
        return head

    if not head:
        return None

    else:
        arr = []

        while head:
            arr.append(head)
            head = head.next

        i = 0
        n = len(arr)
        res = []

        while i < n - 1:
            res.append(arr[i + 1])
            res.append(arr[i])
            i += 2
        if n % 2:
            res.append(arr[-1])
        for i in range(n - 1):
            res[i].next = res[i + 1]
        res[n - 1].next = None
        return res[0]

'''Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. If the two linked 
lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the
entire linked structure.
Note that the linked lists must retain their original 
structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):
intersectVal - The value of the node where the intersection occurs. 
This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) 
to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) 
to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass
 the two heads, headA and headB to your program. If you correctly return 
 the intersected node, then your solution will be accepted.
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (
note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, 
it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; 
There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 
in A and B (2nd node in A and 3rd node in B) are different node references. 
In other words, they point to two different locations in memory, while 
the nodes with value 8 in A and B (3rd node in A and 4th node in B) point 
to the same location in memory.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if 
the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before 
the intersected node in B.
Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it 
reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, 
while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.'''
def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    arr1 = []
    cur1 = headA
    while cur1:
        arr1.append(cur1.val)
        cur1 = cur1.next

    arr2 = []
    cur2 = headB
    while cur2:
        arr2.append(cur2.val)
        cur2 = cur2.next

    i = len(arr1) - 1
    j = len(arr2) - 1
    intersect = deque()

    while i >= 0 and j >= 0:
        if arr1[i] == arr2[j]:
            intersect.appendleft(arr1[i])
        else:
            break
        i -= 1
        j -= 1

    if len(intersect) == 0:
        return None
    else:
        while headA.val != intersect[0]:
            headA = headA.next

        while headB.val != intersect[0]:
            headB = headB.next

        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

'''Given the head of a singly linked list and two integers 
left and right where left <= right, reverse the nodes of the 
list from position left to position right, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n'''


def reverseBetween(head, left: int, right: int):
    arr = []
    res = []
    cnt = 0
    while head:

        if left - 1 <= cnt <= right - 1:
            arr.append(head.val)

        res.append(head.val)
        cnt += 1
        head = head.next

    res = res[:left - 1] + arr[::-1] + res[right:]
    for i in range(len(res)):
        res[i] = ListNode(res[i])
    for i in range(len(res) - 1):
        res[i].next = res[i + 1]
    res[len(res) - 1].next = None
    return res[0]


'''Given the head of a sorted linked list, delete all 
nodes that have duplicate numbers, leaving only distinct numbers 
from the original list. Return the linked list sorted as well. 
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]'''

import collections as coll

def deleteDuplicates(head):
    arr = []
    if not head:
        return None

    while head:
        arr.append(head.val)
        head = head.next
    c = coll.Counter(arr)
    mass = [i for i in c if c[i] == 1]
    if len(mass) == 0:
        return None

    for i in range(len(mass)):
        mass[i] = ListNode(mass[i])
    for i in range(len(mass) - 1):
        mass[i].next = mass[i + 1]
    mass[len(mass) - 1].next = None
    return mass[0]


'''Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that 
can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is 
connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.'''


def hasCycle(head) -> bool:

    s = set()
    while head:
        if head in s:
            return True
        else:
            s.add(head)
        head = head.next
    return False

    #####################  Second solution
    cnt = 0
    while head:
        if cnt > 10 ** 4:
            return True
        cnt += 1
        head = head.next

    return False


'''Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []'''


def sortList(head):
    ###################

    ##        FIRST SOLUTION

    def length_of_linked_list(node):
        if not node:
            return None
        else:
            arr = []
            while node:
                arr.append(node)
                node = node.next
            return arr[len(arr) // 2]

    def merge(headA, headB):
        ans = ListNode()
        b = ans

        while headA and headB:
            if headA.val < headB.val:
                ans.next = headA
                ans = ans.next
                headA = headA.next
            else:
                ans.next = headB
                ans = ans.next
                headB = headB.next

        if headA is None:
            ans.next = headB
        else:
            ans.next = headA

        return b.next

    def merge_sort(node):

        if not node or not node.next:
            return node
        else:
            nB = length_of_linked_list(node)

            a = node
            nA = a

            while a.next is not nB:
                a = a.next
            a.next = None

            nA = merge_sort(nA)
            nB = merge_sort(nB)

            return merge(nA, nB)

    return merge_sort(head)

    ######################################################
    ###

    #      SECOND SOLUTION
def sortList(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    arr.sort()
    if len(arr) == 0:
        return None

    for i in range(len(arr)):
        arr[i] = ListNode(arr[i])
    for i in range(len(arr) - 1):
        arr[i].next = arr[i + 1]
    arr[len(arr) - 1].next = None
    return arr[0]


'''Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0'''


def getDecimalValue(head) -> int:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    power = len(arr) - 1
    res = 0
    while power >= 0:
        res = res + (arr[power]) * 2 ** (len(arr) - 1 - power)
        power -= 1
    return res



def reverse_linked_list(head):
    previous = None
    cur = head
    while cur :
        node_next = cur.next
        cur.next = previous
        previous = cur
        cur = node_next
    return previous


'''Given the head of a singly linked list, sort the list using insertion sort, 
and return the sorted list's head.
The steps of the insertion sort algorithm:
Insertion sort iterates, consuming one input element each repetition 
and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. 
The partially sorted list (black) initially contains only the first element in the list. 
One element (red) is removed from the input data and inserted in-place into the sorted 
list with each iteration.

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
'''

def func(head):
    ans = ListNode()
    cur = head
    while cur :
        prev = ans
        while prev.next and prev.next.val <= cur.val:
            prev = prev.next
        tmp = cur.next
        cur.next = prev.next
        prev.next = cur
        cur = tmp
    return ans.next

def insertionsort(head):
    arr =[]
    while head :
        arr.append(head.val)
        head = head.next
    if not arr:
        return None
    arr.sort()
    for i in range(len(arr)):
        arr[i] = ListNode(arr[i])
    for i in range(len(arr)-1):
        arr[i].next = arr[i+1]
    arr[len(arr)-1].next = None
    return arr[0]