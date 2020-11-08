class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst = list()
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[n+i])
        return lst