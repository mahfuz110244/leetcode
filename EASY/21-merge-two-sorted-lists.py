"""
https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        temp, res = None, None
        while list1 and list2:
            if list1.val <= list2.val:
                if temp:
                    temp.next = list1
                    temp = temp.next
                else:
                    temp = list1
                    res = temp
                list1 = list1.next
            else:
                if temp:
                    temp.next = list2
                    temp = temp.next
                else:
                    temp = list2
                    res = temp
                list2 = list2.next
        while list1:
            temp.next = list1
            temp = temp.next
            list1 = list1.next
        while list2:
            temp.next = list2
            temp = temp.next
            list2 = list2.next
        return res

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == "__main__":
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(4, n4)
    n2 = ListNode(4, n3)
    n1 = ListNode(4, n2)
    merge_list = Solution().mergeTwoLists(n1, n2)
    print(merge_list)