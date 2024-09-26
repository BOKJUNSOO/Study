## 자료구조
# 스택
class Stack:
    def __init__(self):
        self.item = []          # class 객체 생성할때 호출
    
    def push(self,val):
        self.item.append(val) # list의 append 연산

    def pop(self):
        try:
            return self.item.pop() #defalut 값으로 pop연산
        except IndexError:
            print("Stack is Empty")
    
    def top(self):
        try:
            return self.item[-1]
        except IndexError:
            print("Stact is Empty")
    
    def __str__(self):
        return f"{self.item}"   # __str__ : return 은 문자열!

    def __len__(self):
        return len(self.item)

# 큐
class queue:
    def __init__(self):
        self.item = []
        self.first_index = 0

    def enque(self, val):
        self.item.append(val)

    def dequeue(self):
        if self.first_index == len(self.item):
            print("queue is empty")
        else:
            self.item.pop(self.first_index)
    
    def __str__(self):
        return f"{self.item}"

# 한방향 연결 리스트
class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = None
    def __str__(self):
        return f"{self.key}"

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def push_front(self,key):
        new_node = Node(key)
