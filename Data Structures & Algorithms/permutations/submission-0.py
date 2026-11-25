class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        return self.helper(0,nums)

    def helper(self,i,nums):

        if i == len(nums):

            return [[]]
        
        perms = self.helper(i+1,nums)
        resPerms = []
        for p in perms:
            for pos in range(len(p)+1):

                permCopy = p.copy()
                permCopy.insert(pos,nums[i])

                resPerms.append(permCopy)
        
        return resPerms