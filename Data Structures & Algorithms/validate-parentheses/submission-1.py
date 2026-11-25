class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {
            '}' : '{',
            ')' : "(",
            ']' : "["
        }

        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '{' or s[i] == '[':

                stack.append(s[i])
            
            else:
                
                if not(len(stack) > 0 and stack[-1] == mapping[s[i]]):
                    return False

                stack.pop()
        if len(stack)>0:
            return False
        return True