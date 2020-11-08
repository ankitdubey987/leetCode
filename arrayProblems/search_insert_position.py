# search_insert_position.py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums.count(target)==0:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else:
            return nums.index(target)