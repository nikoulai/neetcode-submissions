class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        m = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for i in s:

            if i == "{" or i == "(" or i == "[":

                stack.append(i)
            
            else:

                if len(stack) == 0:
                    return False 
                
                if stack.pop() != m[i]:
                    return False
        
        return len(stack) == 0
                
