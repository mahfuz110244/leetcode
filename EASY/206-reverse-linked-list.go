/*
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
*/
package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList1(head *ListNode) *ListNode {
	var reverseNode *ListNode = nil
	// var cur *ListNode = head
	for head != nil {
		// var currentNode *ListNode = nil
		// backup original next hop
		currentNode := head
		nextHead := head.Next
		// reverse linkage direction
		currentNode.Next = reverseNode
		reverseNode = currentNode
		// fmt.Println(head, reverseNode)

		// move to next position
		head = nextHead
		// fmt.Println(head, reverseNode)
	}
	return reverseNode
}

func reverseList(head *ListNode) *ListNode {
	/*
		Runtime: 0 ms, faster than 100.00% of Go online submissions for Reverse Linked List.
		Memory Usage: 2.6 MB, less than 91.09% of Go online submissions for Reverse Linked List.
	*/
	var reverseNode *ListNode
	// var cur *ListNode = head
	for head != nil {
		// var currentNode *ListNode = nil
		// backup original next hop
		nextHead := head.Next
		// reverse linkage direction
		head.Next = reverseNode
		reverseNode = head
		// fmt.Println(head, reverseNode)

		// move to next position
		head = nextHead
		// fmt.Println(head, reverseNode)
	}
	return reverseNode
}
func main() {
	node5 := ListNode{
		Val:  5,
		Next: nil,
	}
	node4 := ListNode{
		Val:  4,
		Next: &node5,
	}
	node3 := ListNode{
		Val:  3,
		Next: &node4,
	}
	node2 := ListNode{
		Val:  2,
		Next: &node3,
	}
	node1 := ListNode{
		Val:  1,
		Next: &node2,
	}
	for node1.Next != nil {
		fmt.Println(node1.Val)
		node1 = *node1.Next
	}

	fmt.Println(reverseList(&node1))
	// fmt.Println(reverseList1(&node1))
}
