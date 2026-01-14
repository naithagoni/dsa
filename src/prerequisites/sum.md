# Find the Sum of N Natural Numbers or Find the Sum of the Any N Natural Numbers  or  Find the Sum of the First N Natural Numbers

- no fixed formula exists unless we know which numbers are chosen. Use sum(list) if the numbers are arbitrary.
```py
# Sum of any N natural numbers
numbers = [3, 7, 12, 8, 5]  # any 5 natural numbers
sum_any_N = sum(numbers)
print("Sum of any N natural numbers:", sum_any_N)
```

```py
## FORMULA BASED "SUM"
# Sum of first N natural numbers
n = 5
# n * (n + 1) / 2   # 15.0 (float division)
# n * (n + 1) // 2 or int(n * (n + 1) / 2)  # 15   (integer/floor division)
sum_first_N = n * (n + 1) // 2
print("Sum of first", n, "natural numbers:", sum_first_N)
```

```py
## RECURSION BASED "SUM"
def recursum(n) -> int:
  if n == 0:
    return n
  return n + recursum(n - 1)
n, sum = 5,0
print("Sum:", recursum(n))
```


### Comparison:
- Recursive sum: `O(n)` time, `O(n)` space (stack frames)
- Formula sum: `O(1)` time, `O(1)` space  —> Better performant

## Recursive Sum Complexity:

### Step-by-step:

- **Time Complexity: O(n)**
    - For `n = 5`, the function calls itself **5 times**.
    - Each call performs **one addition**, so total operations ~ n.
- **Space Complexity: O(n)**
    - Each recursive call is stored on the **call stack** until base case is reached.
    - For large `n`, this can lead to **stack overflow** or increased memory usage.

**Example:**

For `n = 5`, the stack looks like:

```
recursum(5)
recursum(4)
recursum(3)
recursum(2)
recursum(1)
recursum(0) -> base case
```

- 6 function calls on the stack at the same time → O(n) space

---

## Formula Sum Complexity:

```python
sum = n * (n +1) // 2
```

### Step-by-step:

- **Time Complexity: O(1)**
    - Only **one multiplication, one addition, one division**.
    - Number of operations does **not depend on n**.
- **Space Complexity: O(1)**
    - No recursion → no stack frames.
    - Only **one variable** is needed to store the result.

**Example:**

For `n = 5`:

```
5 * (5 + 1) // 2 = 30 // 2 = 15
```

- Done in **constant time and memory**.