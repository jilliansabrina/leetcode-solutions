class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                return hashmap[diff], i
            hashmap[j] = i

# BRUTE FORCE
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for x in range(len(nums)):
#             for y in range(len(nums)):
#                 if x == y:
#                     continue
#                 elif nums[x] + nums[y] == target:
#                     return [x,y]
