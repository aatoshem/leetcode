# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    def dfs(tree, currHeight):
        # keep track of isBalanced flag
        # keep track of height of each node

        # leaf nodes have height -1
        # makes calculation of height workout
        # currHeight = max(-1, -1) + 1, which will be 0
        if tree is None:
            return (True, -1)

        isLeftBal, rh = dfs(tree.left, currHeight)
        isRightBal, lh = dfs(tree.right, currHeight)

        # +1 to account for the root of each subtree
        currHeight = max(rh, lh) + 1

        isSubTreebal = isLeftBal and isRightBal and abs(rh - lh) <= 1

        return (isSubTreebal, currHeight)

    return dfs(tree, 0)[0]