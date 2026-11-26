# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        [mini,maxi] = sorted([p.val,q.val])
        curr = root

        while True:
            if mini<curr.val and maxi<curr.val:
                curr = curr.left

            elif mini>curr.val and maxi>curr.val:
                curr = curr.right
            
            else:
                return curr
        



        