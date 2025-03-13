def binsearch(n, S, x):
    low, high = 0, n-1
    location = -1
    # Complete the code here
    
    while low <= high:
        mid = (low + high) // 2

        if S[mid] == x:
            location = mid
            break

        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid -1
            
    return location





def test_case(S, x, expected_location):
    n = len(S)
    result = binsearch(n, S, x)
    
    if result == expected_location:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_location}, 출력값={result}")
    print(f"입력 배열: {S}")
    print(f"찾는 값: {x}")
    print(f"출력값: {result}")
    print("-" * 40)



print("######Example 1######")
S = [5, 7, 8, 10, 11, 13]
x = 15 
expected_location = -1
test_case(S, x, expected_location)

print("######Example 2######") 
S = [5, 7, 8, 10, 11, 13]
x = 10 
expected_location = 3
test_case(S, x, expected_location)

print("######Example 3######") 
S = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 7
expected_location = 3
test_case(S, x, expected_location)

print("######Example 4######") 
S = [5]
x = 5
expected_location = 0
test_case(S, x, expected_location)

print("######Example 5######") 
S = []
x = 10
expected_location = -1
test_case(S, x, expected_location)
