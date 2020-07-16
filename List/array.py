# 1차원 배열 리스트로 구현
data = [1,2,3,4,5]
print(data) # [1, 2, 3, 4, 5]

# 2차원 배열 리스트로 구현
data = [[1,2,3], [4,5,6], [7,8,9]]
print(data) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## 1차원 배열에 접근하기
print(data[0]) # [1, 2, 3]
## 2차원 배열에 접근하기
print(data[0][0]) # 1
print(data[0][1]) # 2
print(data[0][2]) # 3
print(data[1][0]) # 4
print(data[2][2], data[2][1], data[2][0]) # 9 8 7

# 다음 dataset에 들어있는 데이터 중에서 y 빈도수 찾기
dataset = ["yang", "jihoon", "helloworld", "Hi", "python", "java", "javascript", "party"]

y_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == "y":
            y_count += 1

print(y_count)