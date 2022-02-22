/*
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
*/

package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists2(list1 *ListNode, list2 *ListNode) *ListNode {
    if list1 == nil {
        return list2
    }
    if list2 == nil {
        return list1
    }
    var prev *ListNode
    var res *ListNode
    for list1 != nil && list2 !=nil {
        if list1.Val <= list2.Val {
            if prev != nil {
                prev.Next = list1
                prev = prev.Next
                
            } else {
                prev = list1
                res = prev
            }
            list1 = list1.Next    
        } else {
            if prev != nil {
                prev.Next = list2
                prev = prev.Next
            } else {
                prev = list2
                res = prev
            }
            list2 = list2.Next    
        }
    }
    for list1 != nil {
        prev.Next = list1
        prev = prev.Next
        list1 = list1.Next    
    }
    for list2 != nil {
        prev.Next = list2
        prev = prev.Next
        list2 = list2.Next    
    }
   return res
}

func mergeTwoLists1(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	var prev *ListNode
	var res *ListNode
	fmt.Println(prev, res)
	// temp1 := list1
	// for temp1 != nil {
	//     fmt.Println(temp1, temp1.Val, temp1.Next)
	//     if prev == nil {
	//         prev = temp1
	//         res = prev
	//     } else {
	//         prev.Next = temp1
	//         prev = prev.Next
	//     }
	//     fmt.Println(prev, res)
	//     temp1 = temp1.Next
	//     fmt.Println()
	// }
	// fmt.Println(prev, res)
	// result := prev
	// fmt.Println(list1)
	temp1 := list1
	temp2 := list2
	for temp1 != nil && temp2 != nil {
		if temp1.Val <= temp2.Val {
			fmt.Println(temp1.Val)
			if prev == nil {
				prev = temp1
				res = prev
			} else {
				prev.Next = temp1
				prev = prev.Next
				fmt.Println(prev, prev.Next)
			}
			temp1 = temp1.Next
		} else {
			fmt.Println(temp2.Val)
			if prev == nil {
				prev = temp2
				res = prev
			} else {
				prev.Next = temp2
				prev = prev.Next
				fmt.Println(prev, prev.Next)
			}
			temp2 = temp2.Next
		}
		// prev = prev.Next
		// fmt.Println(prev)
	}
	for temp1 != nil {
		fmt.Println(temp1.Val)
		prev.Next = temp1
		prev = prev.Next
		fmt.Println(prev, prev.Next)
		temp1 = temp1.Next
	}
	for temp2 != nil {
		fmt.Println(temp2.Val)
		prev.Next = temp2
		prev = prev.Next
		fmt.Println(prev, prev.Next)
		temp2 = temp2.Next
	}
	return res
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	if list1.Val <= list2.Val {
		list1.Next = mergeTwoLists(list1.Next, list2)
		return list1
	} else {
		list2.Next = mergeTwoLists(list1, list2.Next)
		return list2
	}
}

func main() {
	node4 := ListNode{
		Val:  4,
		Next: nil,
	}
	node34 := ListNode{
		Val:  3,
		Next: &node4,
	}
	node24 := ListNode{
		Val:  2,
		Next: &node4,
	}
	node12 := ListNode{
		Val:  1,
		Next: &node24,
	}
	node13 := ListNode{
		Val:  1,
		Next: &node34,
	}
	// for node13.Next != nil {
	// 	fmt.Println(node13.Val)
	// 	node13 = *node13.Next
	// }
	list1 := node13
	// for list1.Next != nil {
	// 	fmt.Println(list1.Val)
	// 	list1 = *list1.Next
	// }
	list2 := node12
	mergeTwoLists(&list1, &list2)

}
