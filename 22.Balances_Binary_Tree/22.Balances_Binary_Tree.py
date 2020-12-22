'''
	Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104	


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root): # return (depth, isBalance)
            if root == None:
                return 0, True
            leftH, leftB = dfs(root.left) # left height, left balance
            rightH, rightB = dfs(root.right) # right height, right balance
            return max(leftH, rightH) + 1, abs(leftH - rightH) <= 1 and leftB and rightB
        
        return dfs(root)[1]