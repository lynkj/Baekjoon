# 체스 말의 기준 개수
required_pieces = [1, 1, 2, 2, 2, 8]

# 입력받기 (예: "0 1 2 2 7 3")
input_pieces = list(map(int, input().split()))

# 부족하거나 초과된 개수 계산
result = [required - input_pieces[i] for i, required in enumerate(required_pieces)]

# 결과 출력
print(" ".join(map(str, result)))