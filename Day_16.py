# Problem link: https://leetcode.com/problems/evaluate-boolean-binary-tree/description
# Time: O(n)
# Space: O(n) for recursion call stack
class Solution:
    def evaluateTree(self, node: Optional[TreeNode]) -> bool:
        if not node.left:
            return True if node.val == 1 else False
            
        if node.val == 2:
            return self.evaluateTree(node.left) or self.evaluateTree(node.right)
        return self.evaluateTree(node.left) and self.evaluateTree(node.right)
