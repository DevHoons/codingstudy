# 링크드 리스트로 중간에 데이터 추가하기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 데이터를 추가하는 함수
def add(data):
    node = head
    # 맨 끝에 있는 노드를 찾아가기 위한 로직
    while node.next:
        node = node.next
    
    node.next = Node(data)

node1 = Node(1)
head = node1

for index in range(2, 10):
    add(index)

# 중간에 데이터 넣기
node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data) # 데이터 순회
    node = node.next
print(node.data)