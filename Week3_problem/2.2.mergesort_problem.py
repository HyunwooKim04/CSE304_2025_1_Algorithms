def merge(h, m, U, V, S):
    assert sorted(U) == U  # U는 정렬되어 있어야 함
    assert sorted(V) == V  # V는 정렬되어 있어야 함
    
    i = j = k = 0
    # 두 배열을 병합하여 S에 저장
    while i < h and j < m:
        if U[i] <= V[j]:
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1

    # U에 남은 값이 있으면 모두 S에 추가
    while i < h:
        S[k] = U[i]
        i += 1
        k += 1

    # V에 남은 값이 있으면 모두 S에 추가
    while j < m:
        S[k] = V[j]
        j += 1
        k += 1

def mergesort(n, S):
    if n > 1:
        h = n // 2  # 중간 인덱스
        m = n - h   # 나머지 부분의 길이
        U = S[:h]   # 왼쪽 배열
        V = S[h:]   # 오른쪽 배열
        
        # 왼쪽 배열과 오른쪽 배열을 각각 정렬
        mergesort(len(U), U)
        mergesort(len(V), V)
        
        # 정렬된 U와 V를 병합하여 S에 저장
        merge(h, m, U, V, S)

def test_merge(U, V, expected_result):
    h = len(U)
    m = len(V)
    S = [-1] * (h + m)  # 병합된 배열을 담을 리스트
    
    merge(h, m, U, V, S)
    
    if S == expected_result:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_result}, 출력값={S}")
    print(f"입력 배열 U: {U}")
    print(f"입력 배열 V: {V}")
    print(f"병합 결과 S: {S}")
    print("-" * 40)

def test_mergesort(S, expected_result):
    original = S.copy()
    
    mergesort(len(S), S)
    
    if S == expected_result:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_result}, 출력값={S}")
    print(f"입력 배열: {original}")
    print(f"정렬 결과: {S}")
    print("-" * 40)


if __name__ == "__main__":
    print("######Example 1 for 'merge()'######")
    U = [17, 19, 39, 41, 73]
    V = [16, 22, 66, 94, 98]
    expected_result = [16, 17, 19, 22, 39, 41, 66, 73, 94, 98]
    test_merge(U, V, expected_result)
    
    print("######Example 2 for 'merge()'######")
    U = [1, 3, 5, 7, 9]
    V = [2, 4, 6, 8, 10]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_merge(U, V, expected_result)
    
    print("######Example 3 for 'mergesort()'######")
    S = [22, 98, 17, 16, 19, 73, 94, 41, 39, 66]
    expected_result = [16, 17, 19, 22, 39, 41, 66, 73, 94, 98]
    test_mergesort(S, expected_result)
    
    print("######Example 4 for 'mergesort()'######")
    S = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
    test_mergesort(S, expected_result)
