"""
Problem   : LC 1672 - Richest Customer Wealth
Link      : https://leetcode.com/problems/richest-customer-wealth/
Difficulty: Easy
Pattern   : 2D list + running maximum
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. Each inner list is one customer. Each number in it is money in one bank.
2. Create a variable richest = 0 to remember the biggest wealth seen so far.
3. Loop over each customer in accounts.
4. Wealth of the customer = sum of their list.
5. If wealth is bigger than richest -> update richest.
6. After the loop, return richest.

DRY RUN (accounts = [[1,5],[7,3],[3,5]]):
start           -> richest = 0
customer [1,5]  -> wealth = 6,  6 > 0  -> richest = 6
customer [7,3]  -> wealth = 10, 10 > 6 -> richest = 10
customer [3,5]  -> wealth = 8,  8 > 10? no -> richest stays 10
Output: 10
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > richest:
                richest = wealth
        return richest


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))              # expected: 6
    print(s.maximumWealth([[1, 5], [7, 3], [3, 5]]))            # expected: 10
    print(s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))   # expected: 17
    print(s.maximumWealth([[5, 5]]))                            # expected: 10


"""
TIME COMPLEXITY : O(m * n)  m customers, n banks each; sum() touches every number once
SPACE COMPLEXITY: O(1)      only two variables (richest, wealth), no extra lists

MISTAKES I MADE:
- First returned wealth instead of richest -> wealth only holds the LAST customer
- Thought [[5,5]] returns 5 -> it is ONE customer with TWO banks, so 5 + 5 = 10
- Counted indexes from 1 instead of 0 -> Python lists start at index 0

KEY INSIGHT:
- One inner list = one row = one customer. Sum each row, keep the running max
  in a variable outside the loop, and return that variable after the loop.
"""
