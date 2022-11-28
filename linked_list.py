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