class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isvalidalphanumerical(c):

            if 'a'<= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':

                return True
        

        l = 0
        r = len(s) -1 

        while r>=l:

            if not isvalidalphanumerical(s[l]):
                l+=1
                continue
            if not isvalidalphanumerical(s[r]):
                r-=1
                continue
                
            if s[l].lower() != s[r].lower():
                return False
        
            l+=1
            r-=1
            
        return True
                
            
