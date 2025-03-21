# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Complete the code here
        sortedList = self.mergeSort(nums)
        return sortedList[len(sortedList)-k]
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        # Complete the code here
        else:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            left = self.mergeSort(left)
            right = self.mergeSort(right)
            return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # Complete the code here
        newList = []
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                newList.append(left[i])
                i += 1
            else:
                newList.append(right[j])
                j += 1
            k += 1

        while i < len(left):
            newList.append(left[i])
            i += 1

        while j < len(right):
            newList.append(right[j])
            j += 1
        return newList

def test_findKthLargest(nums, k, expected_result):
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    
    if result == expected_result:
        print(f"✅ 테스트 통과: 결과가 일치합니다.")
    else:
        print(f"❌ 테스트 실패: 기대값={expected_result}, 출력값={result}")
    print(f"입력 배열: {nums}")
    print(f"k값: {k}")
    print(f"결과: {result}")
    print("-" * 40)

if __name__ == "__main__":
    print("예제 1:")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    test_findKthLargest(nums1, k1, 5)
    
    print("예제 2:")
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    test_findKthLargest(nums2, k2, 4)
    
    print("예제 3 - 배열 크기가 큰 경우:")
    nums3 = [-500] * 90000 + [1000] * 10000
    k3 = 10000
    test_findKthLargest(nums3, k3, 1000)
    
    print("예제 4 - 요소 값의 경계 테스트:")
    nums4 = [-10000, 10000, -5000, 5000, 0, 9999, -9999]
    k4 = 1
    test_findKthLargest(nums4, k4, 10000)
