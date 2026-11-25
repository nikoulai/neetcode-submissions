class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combs = []
        currentComb = []

        def helper(i,n,k,combs,currentComb):

            if len(currentComb) == k:
                combs.append(currentComb.copy())
            
            if i > n:
                return
            
            for j in range(i,n+1):
                currentComb.append(j)
                helper(j+1,n,k,combs,currentComb)
                
                currentComb.pop()
            
        helper(1,n,k,combs,[])
        return combs

        