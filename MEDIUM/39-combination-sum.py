"""
https://leetcode.com/problems/combination-sum/
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

"""
from re import T
from typing import List
def combinationSumShajal(candidates: List[int], target: int) -> List[List[int]]:
        hash_set = set()
        result = []
        
        def subset(candidates, temp_result, temp_sum):
            if temp_sum == target and tuple(temp_result) not in hash_set:
                result.append(temp_result[:])
                hash_set.add(tuple())
            
            if temp_sum > target:
                return
            
            for pivot in range(len(candidates)):
                temp_sum += candidates[pivot]
                temp_result.append(candidates[pivot])
                subset(candidates, temp_result, temp_sum)
                p = temp_result.pop()
                temp_sum -= p
        subset(candidates, [], 0)
        print(result)
        return result

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur: List[int], total):
        if total == target :
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target :
            return
        
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i+1, cur, total)
    dfs(0, [], 0)
    return res


if __name__ == "__main__":
	print(combinationSum([2, 3, 6, 7], 7))
        