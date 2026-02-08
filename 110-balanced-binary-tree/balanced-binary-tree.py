class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0   # height of empty tree
            
            left = dfs(node.left)
            if left == -1:
                return -1  # left subtree already unbalanced
            
            right = dfs(node.right)
            if right == -1:
                return -1  # right subtree already unbalanced
            
            if abs(left - right) > 1:
                return -1  # current node unbalanced
            
            return 1 + max(left, right)  # return height
        
        return dfs(root) != -1
