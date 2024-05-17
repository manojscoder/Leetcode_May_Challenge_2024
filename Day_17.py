# Problem link: https://leetcode.com/problems/delete-leaves-with-a-given-value/description
# Time: O(n)
# Space: O(n)
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def check(node):
            return not node.left and not node.right and node.val == target
            
        def dfs(node):
            if not node or check(node):
                return None
            
            node.left = dfs(node.left)
            if check(node):
                return None
            node.right = dfs(node.right)
            if check(node):
                return None
                
            return node
        
        return dfs(root)
