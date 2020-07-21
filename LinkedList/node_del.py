# head 삭제
# 마지막 노드 삭제
# 중간 노드 삭제
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

    def delete(self, data):
        if self.head == "":
            print("해당 값을 가진 노드가 없습니다.")
            return
        # head 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
print(linkedlist1.head)
# head 삭제
linkedlist1.delete(0)
print(linkedlist1.head)

linkedlist1 = NodeMgmt(0)

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()

linkedlist1.delete(4)
linkedlist1.desc()

linkedlist1.delete(9)
linkedlist1.desc()