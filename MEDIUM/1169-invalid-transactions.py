"""
1169
https://leetcode.com/problems/invalid-transactions
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
"""
from typing import List
from collections import defaultdict
"""
Time Complexity: O(n^2))
Space Complexity: O(n) 
"""
def invalidTransactions1(transactions: List[str]) -> List[str]:
    invalid_transactions = []
    for i, v1 in enumerate(transactions):
        t1 = v1.split(",")
        if int(t1[2]) > 1000:
            invalid_transactions.append(v1)
        else:
            for j, v2 in enumerate(transactions):
                if i != j:
                    t2 = v2.split(",") 
                    # print(i, j, t1, t2, int(t2[1])-int(t1[1]))
                    if t1[0] == t2[0] and abs(int(t2[1])-int(t1[1]))<=60 and t1[3] != t2[3]:
                        invalid_transactions.append(v1)
                        break
    return invalid_transactions

"""
Time Complexity: O(n) + O(nlogn)) = O(nlogn)
Space Complexity: O(n) 
"""
def invalidTransactions(transactions: List[str]) -> List[str]:
    invalid_transactions = []
    names_dict = defaultdict(lambda: defaultdict(set))
    for t in transactions:
        name, time, amount, city = t.split(",")
        names_dict[name][time].add(city)
    for t in transactions:
        name, time, amount, city = t.split(",")
        if int(amount) > 1000:
            invalid_transactions.append(t)
        else:
            for value in names_dict[name].keys():
                if -60 <= int(time) - int(value) <=60 and (len(names_dict[name][value])>1 or city not in names_dict[name][value]):
                    invalid_transactions.append(t)
                    break
    return invalid_transactions


if __name__ == '__main__':
    transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    print(invalidTransactions(transactions))

    transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    print(invalidTransactions(transactions))
