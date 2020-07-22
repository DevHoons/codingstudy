# 간단한 해쉬 예
# hash table 만들기 (python list 활용)
hash_table = list([i for i in range(10)])
print(hash_table)

# hash function 만들기
# 다양한 해쉬 함수 고안 기법이 있으며, 가장 간단한 방식이 Division 법
# => 나누기를 통한 나머지 값을 사용하는 기법
# 5로 나누어서 나머지값을 사용하기 때문에 key값이 얼마던지 간에 고정된 해시길이를 반환 함
def hash_func(key):
    return key % 5

# hash table에 저장하기
# 데이터에 따라 필요시 key 생성 방법 정의가 필요함
data1 = "Andy"
data2 = "Dave"
data3 = "Trump"

# ord() => 문자의 ASCII(아스키)코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
# data key값 추출하기
print(ord(data1[0]), hash_func(ord(data1[0])))

# 해쉬테이블에 값 저장 예
# data:value 와 같이 data와 value를 넣으면, 해당 data에 대한 key를 찾아서,
# 해당 key에 대응하는 해쉬주소에 value를 저장하는 예
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

# 해쉬 테이블에서 특정 주소의 데이터를 가져오는 함수
storage_data("Andy", "01012345678")
storage_data("Dave", "01098765432")
storage_data("Trump", "12312312312")

# 실제 데이터를 저장하고 읽어오기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data("Andy"))