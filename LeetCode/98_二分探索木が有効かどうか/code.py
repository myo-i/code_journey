# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(currentNode, low=-math.inf, high=math.inf):
            if currentNode is None:
                return True

            if currentNode.val <= low or currentNode.val >= high:
                return False


            return (checkBST(currentNode.right, currentNode.val, high) and
                     checkBST(currentNode.left, low, currentNode.val))

        return checkBST(root)