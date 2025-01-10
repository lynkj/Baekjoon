import heapq
import sys

input = sys.stdin.read
data = input().split()

# 입력 데이터 처리
N = int(data[0])  # 숫자의 개수
numbers = list(map(int, data[1:]))

# 최소 힙과 최대 힙 선언
min_heap = []  # 큰 절반의 값들을 저장 (최소 힙)
max_heap = []  # 작은 절반의 값들을 저장 (최대 힙, 음수로 저장하여 최대 힙처럼 사용)

# 결과 저장 리스트
results = []

# 각 숫자에 대해 처리
for num in numbers:
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)  # 최대 힙에 음수로 추가
    else:
        heapq.heappush(min_heap, num)  # 최소 힙에 추가

    # 힙의 균형을 유지하기 위해 교환
    if min_heap and -max_heap[0] > min_heap[0]:
        min_val = heapq.heappop(min_heap)
        max_val = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, max_val)
        heapq.heappush(max_heap, -min_val)

    # 중앙값은 최대 힙의 루트 값
    results.append(-max_heap[0])

# 결과 출력
print("\n".join(map(str, results)))
