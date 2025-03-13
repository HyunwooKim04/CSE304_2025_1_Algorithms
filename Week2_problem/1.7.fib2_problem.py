import time

def fib2(n):
    f = [0] * (n + 1)
    if n > 0:
        # Complete the code here
        f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        
    return f[n]






def test_case(n, expected_result):
    stime = time.time()
    result = fib2(n)
    etime = time.time() - stime
    
    print(f"입력값: {n}")
    print(f"출력값: {result}")
    print(f"실행 시간: {round(etime, 5)}초")
    
    if result == expected_result:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_result}, 출력값={result}")
    print("-" * 40)



print("######Example 1######")
n = 30
expected_result = 832040
test_case(n, expected_result)

print("######Example 2######") 
n = 36
expected_result = 14930352
test_case(n, expected_result)

print("######Example 3######") 
n = 40
expected_result = 102334155
test_case(n, expected_result)

print("######Example 4######") 
n = 0
expected_result = 0
test_case(n, expected_result)

print("######Example 5######") 
n = 1
expected_result = 1
test_case(n, expected_result)
