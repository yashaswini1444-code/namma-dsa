# Day 02: Python data structures

Problems: 1929, 1108, 2011, 1512

## 1. Lists

A list is an ordered collection. Index starts at **0**.

```python
nums = [10, 20, 30, 40]
nums[0]      # 10  (first)
nums[-1]     # 40  (last)
len(nums)    # 4
nums.append(50)   # add to the end -> [10, 20, 30, 40, 50]
```

**Slicing** `nums[start:end]` includes `start`, **excludes** `end`.

```python
nums[1:3]    # [20, 30]   -> index 1 and 2 only
nums[:2]     # [10, 20]
nums[2:]     # [30, 40, 50]
```

**Joining lists:** `+` joins, `*` repeats.

```python
[1, 2] + [3]     # [1, 2, 3]
[1, 2] * 2       # [1, 2, 1, 2]
```

## 2. Strings

A string is like a list of characters, but **immutable**: you cannot change it in place.
Every string method returns a **new** string.

```python
s = "a.b.c"
s[0]                  # "a"
s.replace(".", "-")   # "a-b-c"   (s is still "a.b.c")
s.split(".")          # ["a", "b", "c"]   string -> list
"-".join(["a", "b"])  # "a-b"             list -> string
"".join(["a", "b"])   # "ab"
"b" in s              # True  (substring check)
```

- `split(sep)` breaks a string into a list.
- `join(list)` glues a list of strings together, putting the separator **between** items.
- `replace(old, new)` swaps every `old` for `new`.

## 3. Dicts

A dict maps **keys -> values**. Lookup by key is O(1) on average.

```python
count = {"a": 2, "b": 1}
count["a"]            # 2
count.get("z", 0)     # 0   -> safe: default if key is missing
count["c"] = 5        # add / update
"a" in count          # True   -> checks KEYS
2 in count            # False  -> values are NOT checked
for key, value in count.items():
    print(key, value)
```

`count["z"]` on a missing key crashes with `KeyError`. Use `get(key, default)` instead.

### Frequency map

```python
count = {}
for x in items:
    count[x] = count.get(x, 0) + 1
```

`["a", "b", "a"]` -> `{"a": 2, "b": 1}`

## 4. Mistakes from today's practice

| What I wrote / thought | Why it's wrong | Correct |
|---|---|---|
| `nums[1:3]` includes index 0 and 3 | slice starts AT `start` and stops BEFORE `end` | index 1 and 2 only |
| `print(num)[0]` | wrong variable name, and `[0]` is applied to what print returns (`None`) | `print(nums[0])` |
| `[1, 2, 1*2]` to double a list | `1*2` is just the number 2 | `nums + nums` |
| `"+".join(["1","2","3"])` is `"123"` | the separator goes between items | `"1+2+3"` (use `"".join` for `"123"`) |
| `print(Hello!)` | text must be inside quotes, `!` is not a name | `print("Hello!")` |
| `ops.count("+")` on a list | `list.count` counts items EXACTLY equal to `"+"` | loop and use `"+" in op` |
| `value in my_dict` | `in` on a dict checks keys, not values | `value in my_dict.values()` |

## 5. Patterns learned

1. **Counter**: one variable, update it inside the loop, return it after. (LC 2011)
   ```python
   x = 0
   for op in operations:
       x += 1 if ... else -1
   ```
2. **Frequency map**: dict of "how many times have I seen this?" (LC 1512, LC 136)
3. **Pairs with earlier copies**: when you see a value, it pairs with every earlier copy,
   so add `count.get(num, 0)` **before** recording the current one. Turns an O(n^2)
   nested loop into O(n). (LC 1512)

## Key takeaway

Lists keep order, strings never change in place, and dicts answer "have I seen this / how
many times?" instantly.
