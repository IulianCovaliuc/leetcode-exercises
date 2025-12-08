#
# * Given an integer array nums, return true if any value appears at least twice in the array,
# * and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        # * Using Set for better time complexity
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False


# * Test Cases
# [1,2,3,1]
# [1,2,3,4]
# [1,1,1,3,3,4,3,2,4,2]

print(Solution.containsDuplicate(list, [1, 2, 3, 1]))
