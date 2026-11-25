class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        #what if nums2 is empty []
        merged = []
        p1, p2 = 0, 0


        while p1 < m and p2 < n:

            if nums2[p2] < nums1[p1]:

                merged.append(nums2[p2])

                p2 += 1
            else:

                merged.append(nums1[p1])

                p1 += 1
            
        
        if p1 == m:

            merged.extend(nums2[p2:])
            
        elif p2 == n:

            merged.extend(nums1[p1:m])
            
        else:
            raise Error
        
        for i in range(n+m):
            nums1[i] = merged[i]