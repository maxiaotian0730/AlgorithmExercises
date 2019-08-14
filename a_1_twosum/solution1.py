class Solution(object):
    @classmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            first_num = nums[i]
            for j in range(i + 1, len(nums)):
                second_num = nums[j]
                if (first_num + second_num) == target:
                    return [i, j]

        return False


if __name__ == "__main__":
    nums = [1, 2, 33, 4, 5, 6, 7, 8, 9, 10]
    target =35
    print(Solution.twoSum(nums, target))
