def matrixmult(n, A, B):
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        # Complete the code here
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C





def test_case(A, B, expected_result):
    n = len(A)
    result = matrixmult(n, A, B)
    
    if result == expected_result:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_result}, 출력값={result}")
    print(f"입력 행렬 A: {A}")
    print(f"입력 행렬 B: {B}")
    print(f"결과 행렬 C: {result}")
    print("-" * 40)



print("######Example 1######") 
A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
expected_result = [[28, 38], [26, 36]]
test_case(A, B, expected_result)

print("######Example 2######") 
A = [[1, 2], [3, 4]]
B = [[4, 1], [1, 0]]
expected_result = [[6, 1], [16, 3]]
test_case(A, B, expected_result)
