T = int(input())

# 각 테스트 케이스 처리
for i in range(1, T + 1):
    # 두 정수 A와 B 입력
    A, B = map(int, input().split())
    # 결과 출력
    print(f"Case #{i}: {A} + {B} = {A + B}")