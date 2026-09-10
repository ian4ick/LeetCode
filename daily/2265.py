# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.cnt = 0

        def post_order(node: TreeNode) -> tuple[int, int]:
            if node is None:
                return (0, 0)

            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)

            node_sum = left_sum + right_sum + node.val
            node_count = left_count + right_count + 1

            if node.val == node_sum // node_count:
                self.cnt += 1

            return (node_sum, node_count)

        post_order(root)

        return self.cnt