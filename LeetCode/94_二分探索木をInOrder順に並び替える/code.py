# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        
        if root is None:
            return list

        def inorder(node, list):
            if node.left is not None:
                inorder(node.left, list)
            list.append(node.val)
            if node.right is not None:
                inorder(node.right, list)
            return list

        return inorder(root, list)

        