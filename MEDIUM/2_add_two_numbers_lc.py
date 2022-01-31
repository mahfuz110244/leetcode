# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_value = ""
        while l1.next != None:
            first_value = str(l1.val) + first_value
            l1 = l1.next
        first_value = int(str(l1.val) + first_value)
        second_value = ""
        while l2.next != None:
            second_value = str(l2.val) + second_value
            l2 = l2.next
        second_value = int(str(l2.val) + second_value)
        sum_value = list(map(int, str(first_value + second_value)))
        l = ListNode(val=sum_value[len(sum_value) - 1])
        last_node = l
        # print(l.val)
        for i in range(len(sum_value) - 2, -1, -1):
            new_l = ListNode(val=sum_value[i])
            last_node.next = new_l
            last_node = last_node.next
        return l
