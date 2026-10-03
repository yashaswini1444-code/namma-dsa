"""
Problem   : LC 1108 - Defanging an IP Address
Link      : https://leetcode.com/problems/defanging-an-ip-address/
Difficulty: Easy
Pattern   : String replace
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. Every "." in the address must become "[.]".
2. Strings are immutable, so I cannot change them in place.
3. str.replace(old, new) builds a NEW string with every old swapped for new.
4. Return address.replace(".", "[.]").

DRY RUN (address = "1.1.1.1"):
step 1 -> "1"  stays "1"
step 2 -> "."  becomes "[.]"   (happens 3 times)
step 3 -> join -> "1[.]1[.]1[.]1"
Output: "1[.]1[.]1[.]1"
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.defangIPaddr("1.1.1.1"))       # expected: 1[.]1[.]1[.]1
    print(s.defangIPaddr("255.100.50.0"))  # expected: 255[.]100[.]50[.]0


"""
TIME COMPLEXITY : O(n)  because replace() walks the whole string once
SPACE COMPLEXITY: O(n)  because replace() builds a new string (strings are immutable)

MISTAKES I MADE:
- None in the final code. Needed a hint to remember that replace() exists.

KEY INSIGHT:
- Strings cannot be changed in place. replace(), split(), join() all return a NEW
  string, so always use (or return) the result.
"""
