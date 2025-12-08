# Leetcode 242 -- Python3
# * Valid Anagram
# * Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# * An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # * If the Strings are different sizes they can't be an anagram
        if len(s) != len(t):
            return False

        character_counts = {}

        # * Counting the Characters in S String
        for char in s:
            character_counts[char] = character_counts.get(char, 0) + 1

        # * Now Decreasing them while scanning String T

        for char in t:
            if char not in character_counts:
                return False

            character_counts[char] -= 1
            if character_counts[char] < 0:
                return False

        # * Everything should now be Zero

        return all(count == 0 for count in character_counts.values())


def test():
    sol = Solution()
    assert sol.isAnagram("racecar", "carrace") == True
    assert sol.isAnagram("listen", "silent") == True
    assert sol.isAnagram("hello", "bello") == False
    assert sol.isAnagram("", "") == True
    assert sol.isAnagram("a", "aa") == False
    print("All tests passed!")


test()
