# Valid parenthesis
#given a string of parentheses, determine if it is valid
#valid means each opening parenthesis has a matching closing parenthesis and they are properly nested
            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (char == ')' and top != '(') or \
                   (char == '}' and top != '{') or \
                   (char == ']' and top != '['):
                    return False
        
        return not stack
s="([{}])"
obj=Solution()
result=obj.isValid(s)
print(result)
