from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        def _bst_from_preorder(root_idx, tree_min, tree_max):
            root_val = preorder[root_idx]
            if not tree_min < root_val < tree_max:
                return root_idx, None

            root = TreeNode(root_val)

            if root_idx + 1 == len(preorder):
                return root_idx, root

            root_idx += 1
            root_idx, root.left = _bst_from_preorder(root_idx, tree_min, root_val)
            root_idx, root.right = _bst_from_preorder(root_idx, root_val, tree_max)

            return root_idx, root

        return _bst_from_preorder(0, float('-inf'), float('inf'))[1]