"""
Problem   : LC 2011 - Final Value of Variable After Performing Operations
Link      : https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
Difficulty: Easy
Pattern   : Counter variable
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. Start with x = 0.
2. Each operation is one of "++X", "X++", "--X", "X--".
3. If the operation has a "+" in it -> it is an increment, so x += 1.
4. Otherwise it is a decrement, so x -= 1.
5. After the loop, return x.

DRY RUN (operations = ["--X","X++","X++"]):
start  -> x = 0
"--X"  -> no "+" -> x = -1
"X++"  -> has "+" -> x = 0
"X++"  -> has "+" -> x = 1
Output: 1
"""


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for op in operations:
            if "+" in op:
                x += 1
            else:
                x -= 1
        return x


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.finalValueAfterOperations(["--X", "X++", "X++"]))         # expected: 1
    print(s.finalValueAfterOperations(["++X", "++X", "X++"]))         # expected: 3
    print(s.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))  # expected: 0


"""
TIME COMPLEXITY : O(n)  because I look at each of the n operations once
                        ("+" in op is O(1) here: every op is only 3 characters)
SPACE COMPLEXITY: O(1)  because only one variable x, no extra lists

MISTAKES I MADE:
- In practice I tried operations.count("+") -> count() on a LIST only counts items
  that are EXACTLY "+", and no item is just "+", so it gave 0.
  Use "+" in op on each STRING instead.

KEY INSIGHT:
- "in" on a string checks for a substring. I don't need to match all 4 forms,
  just check whether a "+" appears anywhere in the operation.
"""
