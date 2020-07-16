# tuple로 우선순위와 데이터를 추가해야한다.
import queue

# 숫자가 낮은게 가장 우선순위가 높은것이다.
data_queue = queue.PriorityQueue()
data_queue.put((3, "queuetest"))
data_queue.put((10, 3))
data_queue.put((5, "priorityqueue"))

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())