class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        currentSet, subsets = [], []




        def help(i,currentSet,subsets,nums):

            if i == len(nums):

                subsets.append(currentSet.copy())
                return

                
            
            currentSet.append(nums[i])
            help(i+1,currentSet,subsets,nums)
            currentSet.pop()


            help(i+1,currentSet,subsets,nums)
        

        help(0,currentSet,subsets,nums)

        return subsets
            


