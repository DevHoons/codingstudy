# 다음 dataset에 들어있는 데이터 중에서 y 빈도수 찾기
dataset = ["yang", "jihoon", "helloworld", "Hi", "python", "java", "javascript", "party"]

y_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == "y":
            y_count += 1

print(y_count)