# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # if not root:
        #     return True
        # result = self.combine(root)
        # # return result == sorted(result, key=lambda x: x.val)
        # return [node.val for node in result] == list(sorted(set([node.val for node in result])))
        self.prev = None
        return self.helper(root)

    def helper(self, node: TreeNode) -> bool:
        # if not node:
        #     return []
        # return self.combine(node.left) + [node] + self.combine(node.right)
        if not node:
            return True
        if not self.helper(node.left):
            return False
        if self.prev and self.prev.val >= node.val:
            return False
        self.prev = node
        return self.helper(node.right)


if __name__ == '__main__':
    right = TreeNode(-1)
    root = TreeNode(0)
    root.right = right
    s = Solution()
    print(s.isValidBST(root))

