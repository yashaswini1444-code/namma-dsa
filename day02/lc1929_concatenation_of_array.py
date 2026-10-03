"""
Problem   : LC 1929 - Concatenation of Array
Link      : https://leetcode.com/problems/concatenation-of-array/
Difficulty: Easy
Pattern   : List concatenation
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. The answer is the list nums written twice, one copy after the other.
2. In Python, + on two lists joins them into a NEW list.
3. So nums + nums gives exactly the answer. Return it.

DRY RUN (nums = [1,2,1]):
step 1 -> first copy  = [1,2,1]
step 2 -> second copy = [1,2,1]
step 3 -> join them   = [1,2,1,1,2,1]
Output: [1,2,1,1,2,1]
"""


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.getConcatenation([1, 2, 1]))      # expected: [1, 2, 1, 1, 2, 1]
    print(s.getConcatenation([1, 3, 2, 1]))   # expected: [1, 3, 2, 1, 1, 3, 2, 1]


"""
TIME COMPLEXITY : O(n)  because + copies all n items of both lists into a new list
SPACE COMPLEXITY: O(n)  because the answer list has 2n items (2n -> drop the 2 -> n)

MISTAKES I MADE:
- In practice I wrote [1, 2, 1*2] instead of nums + nums -> 1*2 is just the number 2,
  it does not repeat the list. Use nums + nums (or nums * 2) on the whole list.

KEY INSIGHT:
- + on lists means "join", not "add numbers". nums + nums is a new list of length 2n.
"""
