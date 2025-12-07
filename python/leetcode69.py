class Solution:
    def mySqrt(self, x: int) -> int:

        # * Using Binary Search
        left, right = 0, x

        result = 0

        while left <= right:
            mid_value = left + ((right - left) // 2)
            if mid_value**2 > x:
                right = mid_value - 1
            elif mid_value**2 < x:
                left = mid_value + 1
                result = mid_value
            else:
                return mid_value

        return result


print(Solution.mySqrt(int, 10))
