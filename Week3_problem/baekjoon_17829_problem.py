# https://www.acmicpc.net/problem/17829

class Solution:
    def pooling(self, matrix, x, y, N):
        while N > 1:
            newMatrix = [[0] * (N//2) for _ in range(N//2)]
            for i in range(N//2):
                for j in range(N//2):
                    max_elem = -10000  
                    secondNum = [
                        matrix[2*i][2*j], matrix[2*i][2*j+1],
                        matrix[2*i+1][2*j], matrix[2*i+1][2*j+1]
                    ]
                    secondNum.sort()
                    newMatrix[i][j] = secondNum[2]
            matrix = newMatrix  
            N = N // 2  
        return matrix[0][0]

def test_pooling(matrix, expected_result):
    n = len(matrix)
    solution = Solution()
    result = solution.pooling(matrix, 0, 0, n)
    
    if result == expected_result:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_result}, 출력값={result}")
    
    print(f"입력 행렬 크기: {n}x{n} (N=2^{n.bit_length()-1})")
    
    if n > 8:
        print("입력 행렬 (너무 크므로 일부만 표시):")
        for i in range(min(4, n)):
            print(" ".join(map(str, matrix[i][:4])) + " ... " + " ".join(map(str, matrix[i][-4:])))
        print("...")
        for i in range(max(0, n-4), n):
            print(" ".join(map(str, matrix[i][:4])) + " ... " + " ".join(map(str, matrix[i][-4:])))
    else:
        print("입력 행렬:")
        for row in matrix:
            print(" ".join(map(str, row)))
    
    print(f"결과: {result}")
    print("-" * 40)



if __name__ == "__main__":
    print("테스트 케이스 1:")
    matrix1 = [
        [-6, -8, 7, -4],
        [-5, -5, 14, 11],
        [11, 11, -1, -1],
        [4, 9, -2, -4]
    ]
    test_pooling(matrix1, 11)
    
    print("테스트 케이스 2:")
    matrix2 = [
        [-1, 2, 14, 7, 4, -5, 8, 9],
        [10, 6, 23, 2, -1, -1, 7, 11],
        [9, 3, 5, -2, 4, 4, 6, 6],
        [7, 15, 0, 8, 21, 20, 6, 6],
        [19, 8, 12, -8, 4, 5, 2, 9],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    test_pooling(matrix2, 17)
    
    print("테스트 케이스 3:")
    matrix3 = [
        [-7, -9, 8, -5],
        [-6, -6, 15, 12],
        [12, 12, -2, -2],
        [5, 10, -3, -5]
    ]
    test_pooling(matrix3, 12)
    
    print("테스트 케이스 4 (최소 크기 N=2):")
    matrix4 = [
        [-10000, 10000],
        [10000, -10000]
    ]
    test_pooling(matrix4, 10000)

    print("테스트 케이스 5 (최대 크기 N=1024):")
    matrix5 = []
    for i in range(1024):
        row = []
        for j in range(1024):
            if (i + j) % 3 == 0:
                value = 10000
            elif (i + j) % 3 == 1:
                value = -10000 
            else:
                value = (i * j) % 10000 - 5000
            row.append(value)
        matrix5.append(row)
    solution = Solution()
    expected_result5 = solution.pooling(matrix5, 0, 0, 1024)
    test_pooling(matrix5, 10000)
