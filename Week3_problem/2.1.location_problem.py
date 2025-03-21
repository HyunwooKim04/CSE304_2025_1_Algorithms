def location(low, high, S, x):
    if low > high:
        return -1  # 찾을 값이 없으면 -1을 반환
    
    mid = (low + high) // 2  # 중간 인덱스를 계산

    if S[mid] == x:
        return mid  # 찾은 값이 중간 값이면 인덱스 반환
    elif S[mid] < x:
        return location(mid + 1, high, S, x)  # 중간 값보다 크다면 오른쪽 반을 검색
    else:
        return location(low, mid - 1, S, x)  # 중간 값보다 작다면 왼쪽 반을 검색

def test_case(S, x, expected_result):
    result = location(0, len(S)-1, S, x)
    
    if result == expected_result:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_result}, 출력값={result}")
    print(f"입력 배열 S: {S}")
    print(f"찾는 값 x: {x}")
    print(f"위치 인덱스: {result}")
    print("-" * 40)


if __name__ == "__main__":
    print("######Example 1######")
    S = [5, 7, 8, 10, 11, 13]
    x = 15 
    expected_result = -1
    test_case(S, x, expected_result)
    
    print("######Example 2######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 10 
    expected_result = 3
    test_case(S, x, expected_result)
    
    print("######Example 3######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 5
    expected_result = 0
    test_case(S, x, expected_result)
    
    print("######Example 4######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 13
    expected_result = 5
    test_case(S, x, expected_result)
