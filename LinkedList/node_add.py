# 링크드 리스트로 데이터 추가하기
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

# 링크드 리스트 데이터 출력하기(검색하기)
node = head
while node.next:
    print(node.data) # 데이터 순회
    node = node.next
print(node.data)