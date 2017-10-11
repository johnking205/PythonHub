#Add Two Numbers (Linked Lists)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currentNode1 = l1
        currentNode2 = l2
        carry = 0
        
        while(currentNode1.next != None):
            #logic for adding linked lists together

x = Solution()

l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l11.next = l12
l12.next = l13

l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)
l21.next = l22
l22.next = l23

x.addTwoNumbers(l11,l21)