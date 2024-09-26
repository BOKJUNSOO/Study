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
        new_node = Node(key)    # 객체 생성
        new_node.next = self.head   # 생성된 객체의 next는 none 인데(defalut), SLL의 head로 지정
        self.head = new_node        # SSL의 head
        self.size += 1              

    def __len__(self):
        return len(self)
    
    def push_back(self,key):    # tail을 찾고 tail의 next를 tail로 지정
        v = Node(key)
        if self.size == 0:      # len(self) --> 객체 사이즈를 측정(__len__?)
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next    # while 문 탈출시 tail.next 는 None이므로, tail = tailnode 반환
            tail.next = v
        self.size += 1
    
    def __str__(self):
        return f"{self.head}\t{self.size}\t{self.head.next}"
    
    def pop_front(self):    # head 노드를 삭제하고 값을 리턴
        if self.size == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
        return key

    def pop_back(self):     # tail 노드를 삭제하고 값을 리턴
        if self.size == 0:
            return None
        else:
        # running tech
            prev = None
            tail = self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if self.size == 1:
                self.head = None
            else:
                prev.next = tail.next
                key = tail.key
                del tail
                self.size -= 1
                return key
    

L = SinglyLinkedList()
L.push_front(3)
L.push_back(2)
L.push_back(7)
L.pop_back()
print(L)
