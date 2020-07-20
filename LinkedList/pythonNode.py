# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 연결된 리스트들을 관리하는 클래스
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data) # Node의 맨 앞에 있는 값을 가지고 와서 head 값에 넣어줌

    def add(self, data):
        if self.head == "":
            self.head = Node(data) # 일종의 방어코드로 head값이 없으면 추가할 데이터 값으로 head값을 만들어줌
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 링크드 리스트를 순회하여 데이터 출력
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# 데이터 추가
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()