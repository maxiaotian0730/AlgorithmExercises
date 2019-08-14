class Solution(object):
    @classmethod
    def twoSum(self, nums, target):
        """
        hash,题目默认所有数据值均有一个
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            else_num = target - num
            if else_num in hashmap:
                return [hashmap[else_num], index]
            hashmap[num] = index
        return None


if __name__ == "__main__":
    nums = [1, 2, 33, 4, 5, 6, 7, 8, 9, 10]
    target = 37
    print(Solution.twoSum(nums, target))
