# Queue()로 큐 만들기 (가장 일반적인 큐, FIFO)
# queue 라이브러리에서는 Enqueue, Dequeue 대신 put, get 사용
import queue

# data_queue에 "queuetest"라는 값을 넣은 후 1을 Enqueue를 했다.
# 그리고 queue의 size를 출력해보면 2가 나오는 것을 확인할 수 있다.
# Dequeue를 하면 먼저 넣었던 queuetest가 출력이 된다.
# size가 2인 상태에서 Dequeue를 하고 size를 다시 출력해보면 1이 나온다.
# 다시 한 번 Dequeue를 하고 size를 출력하면 0이 나온다.
data_queue = queue.Queue()
data_queue.put("queuetest")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
