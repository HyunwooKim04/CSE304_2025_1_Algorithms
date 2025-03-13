import threading

# https://leetcode.com/problems/first-bad-version/description/

def isBadVersion(version):
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        
        return low



def test_case(n, expected_bad_version, timeout=1):
    global bad_version
    bad_version = expected_bad_version
    sol = Solution()
    
    result_container = []

    def run_test():
        try:
            result = sol.firstBadVersion(n)
            result_container.append(result)
        except Exception as e:
            result_container.append(e)

    test_thread = threading.Thread(target=run_test)
    test_thread.start()
    test_thread.join(timeout)

    if test_thread.is_alive():
        raise RuntimeError("실행 시간이 너무 깁니다.")

    result = result_container[0]
    elapsed_time = timeout

    if isinstance(result, Exception):
        print(f"❌ 테스트 실패: {result}")
    elif result == expected_bad_version:
        print(f"✅ 테스트 통과: Target={expected_bad_version}, Output={result}")
    else:
        print(f"❌ 테스트 실패: Target={expected_bad_version}, Output={result}")


test_case(5, 4)
test_case(1, 1)
test_case(100, 10)
test_case(100, 50)
test_case(10**6, 987654)
test_case(10**6, 500000)
test_case(2147483648, 2147483000)
