import sys

# 입력
input = sys.stdin.read  # 전체 입력을 한 번에 읽기
data = input().splitlines()  # 줄 단위로 나누기

# 첫 번째 줄: 테스트 케이스의 수
T = int(data[0])

# 결과를 저장할 리스트
results = []

# 각 테스트 케이스 처리
for i in range(1, T + 1):
    A, B = map(int, data[i].split())  # A와 B 읽기
    results.append(A + B)  # A + B 결과 저장

# 결과 출력
sys.stdout.write("\n".join(map(str, results)) + "\n")
