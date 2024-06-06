class Node:
    def __init__(self,val: int):
        self.val = val
        self.next = None
        self.pre = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.front = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        new_node = Node(value)
        if not self.front and not self.last:
            self.front = new_node
            self.last = new_node
        else:
            new_node.next = self.front
            self.front.pre = new_node
            self.front = new_node

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        new_node = Node(value)
        if not self.front and not self.last:
            self.front = new_node
            self.last = new_node
        else:
            new_node.pre = self.last
            self.last.next = new_node
            self.last = new_node

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.last = None
            self.front = None
        else:
            self.front = self.front.next
            self.front.pre = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.last = None
            self.front = None
        else:
            self.last = self.last.pre
            self.last.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.last.val

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.max_size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()