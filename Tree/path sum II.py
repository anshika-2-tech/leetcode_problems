# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def solve(node, r_ts, path):
            if not node:
                return

            path.append(node.val)
            
            if not node.left and not node.right and r_ts == node.val:
                ans.append(path[:])

            solve(node.left, r_ts - node.val, path)
            solve(node.right, r_ts - node.val, path)

            path.pop()   

        solve(root, targetSum, [])
        return ans