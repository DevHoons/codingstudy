# 노드구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 노드와 노드 연결하기
node1 = Node(1)
node2 = Node(2)
node1.next = node2

# node1이 시작점이라는 것을 알고 데이터를 담는 변수
head = node1
