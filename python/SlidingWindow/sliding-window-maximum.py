# 239. Sliding Window Maximum
# Hard
# Topics
# Companies
# Hint
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from typing import List

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) == 0 or k == 0:
#             return []

#         ans = []
#         l, r = 0, min(len(nums) - 1, k - 1)

#         while r < len(nums):
#             res = nums[l]
#             for i in range(l, r + 1):
#                 res = max(res, nums[i])
#             ans.append(res)
#             l += 1
#             r += 1

#         return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass

if __name__ == '__main__':
    res = Solution()
    print(res.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(res.maxSlidingWindow(nums = [1], k = 1))

