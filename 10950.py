# Number of test cases
T = int(input())

# List to store results
results = []

# Loop through each test case
for _ in range(T):
    # Read integers A and B
    A, B = map(int, input().split())
    # Compute the sum and store it in the results list
    results.append(A + B)

# Print all results at once
for result in results:
    print(result)