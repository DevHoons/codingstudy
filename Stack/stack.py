# 기본적인 append, pop 예시
data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)

print(data_stack.pop())

# 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수 사용X)
stack_list = list()

def push(data):
    stack_list.append(data)


def pop():
    data = stack_list[-1] # -1은 맨 끝의 인덱스를 가지고 옴
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(pop())
print(pop())
print(pop())