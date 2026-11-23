class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = []

        for i in range(len(nums)):
            for j in range(i + 1):
                if nums[i] + nums[j] == target and i != j:
                    two_sum.append(j)
                    two_sum.append(i)
                    break
        return two_sum

        