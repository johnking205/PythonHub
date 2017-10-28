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
        :rtype: array of ListNode.val
        """
        currentNode1 = l1
        currentNode2 = l2
        carry = 0
        sumNodes = []

        while (currentNode1 != None) and (currentNode2 != None):
            #logic for adding linked lists together
            currentSumNode = ListNode(0)
            currentSumNode.val = (currentNode1.val + currentNode2.val + carry) % 10
            sumNodes.append(currentSumNode)
            if(currentNode1.val + currentNode2.val + carry) >= 10:
                carry = 1
            else:
                carry = 0
            
            currentNode1 = currentNode1.next
            currentNode2 = currentNode2.next

#        if carry == 1:
#           sumNodes.append(ListNode(1))
        if currentNode1 != None:
            sumNodes.append(currentNode1)
            sumNodes[-1].val = (sumNodes[-1].val + carry) % 10
            if(sumNodes[-1].val + carry) == 1:
                sumNodes.append(ListNode(1))
        elif currentNode2 != None:
            sumNodes.append(currentNode2)
            sumNodes[-1].val = (sumNodes[-1].val + carry) % 10
            if(sumNodes[-1].val + carry) == 1:
                sumNodes.append(ListNode(1))
        elif carry == 1:
            sumNodes.append(ListNode(1))

        nodeVals = []
        for i in sumNodes:
            nodeVals.append(i.val)
        
        return nodeVals


x = Solution()

l11 = ListNode(0)
#l12 = ListNode(8)
#l13 = ListNode(3)
#l11.next = l12
#l12.next = l13

l21 = ListNode(0)
#l22 = ListNode(9)
#l23 = ListNode(4)
#l21.next = l22
#l22.next = l23

print(x.addTwoNumbers(l11,l21))