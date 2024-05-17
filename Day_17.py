# Problem link: https://leetcode.com/problems/delete-leaves-with-a-given-value/description
# Time: O(n)
# Space: O(n)
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.left is None and node.right is None and node.val == target:
                return None
                
            return node
    
        return dfs(root)
