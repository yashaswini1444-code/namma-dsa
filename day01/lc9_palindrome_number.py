"""
Problem   : LC 9 - Palindrome Number
Link      : https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Pattern   : Math - digit reversal with while loop
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. A negative number can never be a palindrome (the "-" is only on the left)
   -> return False.
2. Save the original value of x, because the loop will change x.
3. Create reverse = 0 to build the reversed number.
4. While x > 0:
   - digit = x % 10           -> take the last digit
   - reverse = reverse * 10 + digit -> add that digit to the end of reverse
   - x = x // 10              -> remove the last digit from x
5. After the loop, return True if reverse == original, else False.

DRY RUN (x = 121):
start    -> original = 121, reverse = 0

round | x before | digit = x % 10 | reverse = reverse * 10 + digit | x = x // 10
------+----------+----------------+-------------------------------+------------
  1   |   121    |       1        |      0 * 10 + 1 = 1           |     12
  2   |    12    |       2        |      1 * 10 + 2 = 12          |      1
  3   |     1    |       1        |     12 * 10 + 1 = 121         |      0

x = 0 -> loop stops
reverse (121) == original (121) -> True
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        return reverse == original


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))     # expected: True
    print(s.isPalindrome(-121))    # expected: False
    print(s.isPalindrome(10))      # expected: False
    print(s.isPalindrome(0))       # expected: True
    print(s.isPalindrome(12321))   # expected: True


"""
TIME COMPLEXITY : O(d)  d = number of digits; the loop runs once per digit
SPACE COMPLEXITY: O(1)  only a few variables (original, reverse, digit)

MISTAKES I MADE:
- Wrote digit = digit % 10 instead of digit = x % 10 (used digit before creating it)
- Put x = x // 10 outside the while loop -> infinite loop (indentation bug)
- Named the variable reverse but returned rev -> NameError
- Didn't understand at first how rev * 10 + digit builds the reversed number

KEY INSIGHT:
- % 10 takes the last digit, // 10 removes it, rev * 10 + digit appends it to
  the end of rev. Save the original before the loop because the loop destroys x.
"""
