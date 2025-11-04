# LeetCode .20 Exercise Regarding Parenthesis (easy level)

class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}':'{',']':'[' }
        
        for symbol in s:
            # If it's an opening bracket, push onto stack
            if symbol in mapping.values():
                stack.append(symbol)
            # If it's a closing bracket, check for a match
            elif symbol in mapping.keys():
                if not stack or mapping[symbol] != stack.pop():
                    return False
            else:
                return False
                
        return not stack 

    
print(Solution().isValid("()"))      # True
print(Solution().isValid("()[]{}"))  # True
print(Solution().isValid("(]"))      # False
print(Solution().isValid("([)]"))    # False
print(Solution().isValid("{[]}"))    # True
