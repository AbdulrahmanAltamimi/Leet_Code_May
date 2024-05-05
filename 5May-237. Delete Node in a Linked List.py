# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # assign the node's value to the next node's value 
        # [4>5>1>9] > [4>1>1>9]
        node.val = node.next.val
        # assign the next node to the next next node
        #  # [4>5>1>9] > [4>1>9]
        node.next = node.next.next

                
