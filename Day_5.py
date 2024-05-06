# Problem link: https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Time: O(1)
# Space: O(1)
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
