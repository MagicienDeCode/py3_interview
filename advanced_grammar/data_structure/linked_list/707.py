class Node:
    def __init__(self,val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index >= self.size: return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        if index == 0: self.addAtHead(val)
        elif index == self.size: self.addAtTail(val)
        else:
            self.size += 1
            node = Node(val)
            current = self.head
            for _ in range(index-1):
                current = current.next
            after_insert = current.next
            current.next = node
            node.next = after_insert

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: return
        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0: self.head = self.head.next
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
            if index == self.size - 1: self.tail = current

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)