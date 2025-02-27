# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise,
# return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.
from typing import List
import math

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = math.floor(l + ((r - l) / 2))
#             if nums[mid] == target:
#                 return mid
#             if nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid -1
#         return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         s, e = 0, len(nums) - 1

#         while s <= e: # Both converge on the same element [example 2]
#             mid = s + ((e - s) // 2)
#             if target < nums[mid]: # Move left
#                 e = mid - 1
#             elif target > nums[mid]: # Move right
#                 s = mid + 1
#             else:
#                 return mid

#         return -1

# Using template
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)

            if target < nums[m]:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1

if __name__ == '__main__':
    res = Solution()
    print(res.search([-1, 0, 3, 5, 9, 12], 9))
    # l, r  m
    # 0, 6  3
    # 4, 6  5
    # 4, 5  4
    print(res.search([-1, 0, 3, 5, 9, 12], 12))
    # l, r  m
    # 0, 6  3
    # 4, 6  5
    print(res.search([-1, 0, 3, 5, 9, 12], 2))
    # l, r  m
    # 0, 6  3
    # 0, 3  1
    # 2, 3  2
    print(res.search([5], 5))
    print(res.search([5, 6], 6))
    # l, r  m
    # 0, 3  1

# Rough
# [ 0, 1, 2, 3, 4,  5]
# [-1, 0, 3, 5, 9, 12]

