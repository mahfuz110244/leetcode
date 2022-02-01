"""
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
	reverse_node = None
	while head:
		next_head = head.next
		head.next = reverse_node
		reverse_node = head
		head = next_head
	return reverse_node

if __name__ == "__main__":
	n5 = ListNode(5)
	n4 = ListNode(4, n5)
	n3 = ListNode(4, n4)
	n2 = ListNode(4, n3)
	n1 = ListNode(4, n2)
	print(reverseList(n1))