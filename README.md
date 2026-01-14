# DSA
## Notes

Roadmap: → https://whimsical.com/harsha-verse-dsa-roadmap-PeL2uTdPZq6u4ECMiHEARR

![image.png](attachment:bbc3c32c-841e-4392-87aa-99965728ad53:image.png)

## Data Structures:

### Linear Data Structures:

- Arrays
- Strings
- Linked Lists (Singly, Doubly, Circular)
- Stacks
- Queues (Normal, Circular, Deque, Priority Queue)
- Hash Tables / Hash Maps

### Non-Linear Data Structures:

- Trees (Binary Tree, Binary Search Tree)
- Heaps (Min Heap, Max Heap)
- Tries (Prefix Trees)
- Graphs (Directed, Undirected, Weighted, Unweighted)

### Advanced:

- Union-Find (Disjoint Set Union)
- Segment Tree / Fenwick Tree (BIT)
- B-Trees / AVL / Red-Black Trees

**Bloom Filters:**

- LRU Cache (based on LinkedList + HashMap)

## Algorithms:

**Sorting Algorithms**

- Bubble Sort
- Merge Sort
- Insertion Sort
- Selection Sort
- Quick Sort

**Searching Algorithms**

- Binary Search
- Linear Search

**Graph Algorithms**

- BFS
- DFS
- Dijkstra’s Algorithm
- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm

**Dynamic Programming Algorithms**

- Fibonacci (Memoization, Tabulation)
- 0/1 Knapsack
- Longest Common Subsequence (LCS)

**Greedy Algorithms**

**Divide and Conquer**

- Merge Sort
- Quick Sort
- Binary Search
- Closest Pair of Points

**Backtracking**

- N-Queens

**Miscellaneous**

- Bitmasking
- Kadane’s Algorithm

# DSA Foundation / P**rerequisites**

## **Ultimate DSA Cheat Sheet**

---

## **1️⃣ Sums & Intervals**

| Concept | Formula | Example | Use Case | Python Formula  | Alternative Approach |
| --- | --- | --- | --- | --- | --- |
| Sum of first N natural numbers  (or)  `Subarray count` | `S = N(N+1)/2`  | N=5 → 1+2+3+4+5=15 | Fast sum of consecutive numbers | `S = n * (n + 1) // 2`  | `n + findSumRecursion(n - 1)` |
| Sum of first N `odd` numbers | `S = N^2` | N=4 → 1+3+5+7=16 | Pattern sums, series problems | `S = n * n`  or `S = n**2` |  |
| Sum of first N `even` numbers | `S = N(N+1)` | N=4 → 2+4+6+8=20 | Pattern sums, series problems | `S = n * (n + 1)`  | **`# find/calculate Nth Term`**

**`tn = a + (n - 1) * d;**
# here, a= first term, d= common difference, n= number of term`

**`S = (int)(n / 2) * (a + tn);**
# here a= first term, Tn= last term, n= number of term`
 |
| Sum of `squares` of first N numbers | `S = N(N+1)(2N+1)/6` | N=3 → 1²+2²+3²=14 | Algorithmic math, variance, patterns | `S = n * (n + 1) * (2 * n + 1) // 6` |  |
| Sum of `squares` of first N `odd` numbers | `S = N(2N-1)(2N+1)/3` | N=3 → 1²+3²+5²=35 | Math-heavy DSA problems,
Pattern recognition,
Competitive programming | `S = (n * (2 * n + 1) * (2 * n - 1)) // 3` | `S = n * (4 * n**2 - 1) // 3`  or  `int(n * ( 4 * n * n - 1) / 3)` |
| Sum of `squares` of first N `even` numbers | `S = 2N(N-1)(2N+1)/3` | N=3 → 2²+4²+6²=56 | Mathematical optimization,
Avoiding loops,
Large constraints | `S = (2 * n * (n + 1) * (2 * n + 1)) // 3` |  |
| Sum of `cubes` of first N numbers | `S = (N(N+1)/2)^2`  | N=3 → 1³+2³+3³=36 | Math problems, cubic sums | `S = (n * (n + 1) // 2) ** 2`  |  |
| Sum of `cubes` of first N `odd` numbers | `S = N^2(2N^2-1)` | N=2 → 1³+3³=28 | Advanced math sequences,
Olympiad-style problems,
Formula-based optimizations | `S = n * n * (2 * n * n - 1))`  or  `S = n**2 * (2 * n**2 - 1))` |  |
| Sum of `cubes` of first N `even` numbers | `S = 2N^2(N+1)^2` | N=2 → 2³+4³=72 | High-performance numerical problems,
Avoiding nested loops,
Mathematical reasoning in interviews | `S = 2 * (n * (n + 1))**2`  or  `S = 2 * n**2 * (n + 1)**2`  or  `S = 2 * n * n * (n + 1) * (n + 1)` |  |
| Sum of numbers in `interval` [a, b] | `S = ((b-a+1)(a+b))/2` | a=5, b=10 → 5+6+…+10=45 | Subarray sums, interval queries | `n = num2 - num1 + 1 # Number of terms`

`S = (n * (num1 + num2)) // 2` |  |
| Sum of multiples of k ≤ N | `k(m(m+1)/2),  m=N/k`  | k=3, N=10 → 3+6+9=18 | Multiples, Project Euler problems | `m = n // k # Integer division`

`k * m * (m + 1) // 2` |  |

---

## **2️⃣ Sequences: Arithmetic Progression (AP) & Geometric Progression (GP)**

| Concept | Formula | Example | Python Formula  | Use Case | Examples |
| --- | --- | --- | --- | --- | --- |
| AP `nth` term | `a_n = a + (n-1)d` | a=2, d=3, n=4 → 11 | **`# find/calculate Nth Term`

`tn = a + (n - 1) * d;**
# here, a= first term, d= common difference, n= number of term` | Generate linear sequences |  |
| Sum of `first n` AP terms | `S_n = (n/2)(2a + (n-1)d)` | a=2,d=3,n=4 → 2+5+8+11=26 |  | Linear sequence sums | **Example 1 – Simple interval
-** Sequence: 2, 4, 6, 8, 10
- First term `a = 2`, difference `d = 2`, n = 5
- Last term `a_n = 10`

Sum:
S5=5/2*(2+10)=5/2*12=30

**Example 2 – Custom difference
-** Sequence: 3, 7, 11, 15`a = 3`, `d = 4`, n = 4

Sum:
S4=4/2*(2∗3+(4−1)∗4)=2*(6+12)=36

**When to use AP:
-** Numbers grow linearly
**-** When numbers **increase (or decrease) by a fixed amount**

Examples:
- Sum of first N even numbers (d = 2)
- Monthly savings increasing by a fixed amount
- Positions in a linear sequence |
| GP `nth` term | `a_n = ar^(n-1)` | a=2, r=3, n=4 → 2*3³=54 | `a_n = a * r**(n - 1)` | Exponential sequences |  |
| Sum of `first n` GP terms | `S_n = a(r^(n-1)/(r-1)), r[≠](https://wumbo.net/symbols/not-equal/)1` | a=2,r=3,n=4 → 2+6+18+54=80 |  | Exponential growth, compounding | **Example 1 – Doubling sequence
-** Sequence: 1, 2, 4, 8, 16
- `a = 1`, `r = 2`, n = 5

Sum:
S5 = 1*((2^5−1)/2−1)=(32−1)/1=31

**Example 2 – Halving sequence
-** Sequence: 100, 50, 25, 12.5
- `a = 100`, `r = 0.5`, n = 4

Sum:
S4 = 100*((0.5^4−1)/(0.5−1)) = 100*((0.0625−1)/−0.5) = 100*(−0.9375/−0.5) = 187.5

**When to use GP
-** Numbers grow exponentially or geometrically
**-** When numbers **increase or decrease by a fixed multiple**

Examples:
- Compound interest (money grows by a percentage each year)
- Population growth with a fixed growth rate
- Exponential sequences (powers of 2, 3, etc.) |

---

## **3️⃣ Recursion**

| Concept | Recursive Formula (Math) | Example | Python Recursive Formula | Use Cases |
| --- | --- | --- | --- | --- |
| **Sum of first N numbers** | `S(n) = n + S(n-1)` | N=4 → 4+3+2+1=10 | `recursum(N) = N + recursum(N-1)` | Understanding recursion, sum of numbers |
| **Sum of first N `odd` numbers** | `S(n) = (2n-1) + S(n-1)` | N=4 → 1+3+5+7=16 | `odd_sum(n) = (2*n-1) + odd_sum(n-1)` | Pattern recursion, series |
| **Sum of first N `even` numbers** | `S(n) = 2n + S(n-1)` | N=4 → 2+4+6+8=20 | `even_sum(n) = 2*n + even_sum(n-1)` | AP-based recursion |
| **Sum of squares of first N natural numbers** | `S(n) = n^2 + S(n-1)` | N=3 → 1²+2²+3²=14 | `square_sum(n) = n*n + square_sum(n-1)` | Math-heavy DSA |
| **Sum of `squares` of first N `odd` numbers** | `S(n) = (2n-1)^2 + S(n-1)` | N=3 → 1²+3²+5²=35 | `odd_square_sum(n) = (2*n-1)**2 + odd_square_sum(n-1)` | Advanced recursion |
| **Sum of `squares` of first N `even` numbers** | `S(n) = (2n)^2 + S(n-1)` | N=3 → 2²+4²+6²=56 | `even_square_sum(n) = (2*n)**2 + even_square_sum(n-1)` | Pattern + math |
| **Sum of `cubes` of first N natural numbers** | `S(n) = n^3 + S(n-1)` | N=3 → 1³+2³+3³=36 | `cube_sum(n) = n**3 + cube_sum(n-1)` | Transition to formula |
| **Sum of `cubes` of first N `odd` numbers** | `S(n) = (2n-1)^3 + S(n-1)` | N=2 → 1³+3³=28 | `odd_cube_sum(n) = (2*n-1)**3 + odd_cube_sum(n-1)` | Olympiad problems |
| **Sum of `cubes` of first N `even` numbers** | `S(n) = (2n)^3 + S(n-1)` | N=2 → 2³+4³=72 | `even_cube_sum(n) = (2*n)**3 + even_cube_sum(n-1)` | Power series |
| **Sum of `interval` [num1,num2]** | `S(n) = num1 + S(num1+1, num2)` | num1=3,num2=6 → 3+4+5+6=18 | `recursum(num1,num2) = num1 + recursum(num1+1,num2)` | Interval sum using recursion |
| **Sum of consecutive integers from `num1` to `num2` in reverse order** (starting from the higher number `num2` down to the lower number `num1`) | `S(n) = num2 + S(num2-1, num1)` | Sum from 5 → 10 (num1=5, num2=10)

`S(10,5) = 10 + S(9,5)
S(9,5)  = 9  + S(8,5)
S(8,5)  = 8  + S(7,5)
S(7,5)  = 7  + S(6,5)
S(6,5)  = 6  + S(5,5)
S(5,5)  = 5  + S(4,5)
S(4,5)  = 0  (base case)` | `recursum(num2, num1) = num2 + recursum(num2` `- 1, num1)` | Similar to forward recursion, handles descending intervals |
| **Sum of multiples of k ≤ N** | `S(n)=n+S(n-k), if (n%k=0)` | k=3,N=10 → 3+6+9=18 | `multiple_sum(n,k)= n + multiple_sum(n-k,k)` | Filtering + recursion |
| **Fibonacci sequence** |  | n=5 → 0,1,1,2,3,5 | `fib(n)=fib(n-1)+fib(n-2)` | DP, sequence problems |

---

## **4️⃣ Bitwise Operations**

| Concept | Formula | Example | Use Case |
| --- | --- | --- | --- |
| Check even/odd | `num & 1` | 6 → even, 7 → odd

`num & 1 == 0 → even`, `num & 1 == 1 → odd` | Fast alternative to `% 2`

LSB determines even/odd |
| Least Significant Bit (LSB) | `num & -num` | 12 → 4 (binary 1100) | Bit manipulation, `Fenwick Tree` |
| XOR sum trick | `a ^ a = 0`, `a ^ 0 = a` | [2,3,2] → unique 3 using XOR | Find unique element in array |
| Remove LSB | `n & (n-1)` |  | Count set bits |
| Is power of 2 | `n & (n-1) == 0` |  | Bit tricks |
| Sum using Bit Manipulation | `sum ^= num` (XOR) for special cases |  |  |

---

## **5️⃣ Combinatorics & Factorials**

| Concept | Formula | Example | Use Case |
| --- | --- | --- | --- |
| Factorial | `N! = 1 . 2 . … . N` | 5! = 120 | Permutations, combinatorics |
| Combinations (nCr) | `C(n,r) = n!/r!(n-r)!` | 5C2 = 10 | Subsets, probability |
| Permutations (nPr) | `P(n,r) = n!/(n-r)!` | 5P2 = 20 | Ordered arrangements |
| Triangular numbers | `T_n = n(n+1)/2` | n=4 → 10 | Pair counting, sum patterns |

---

## **6️⃣ Arrays & Prefix Techniques**

| Concept | Formula | Example | Use Case |
| --- | --- | --- | --- |
| Prefix sum | `prefix[i] = prefix[i-1] + arr[i]` | arr=[1,2,3] → prefix=[1,3,6] | Range sum queries O(1) |
| Range sum [i,j] | `sum = prefix[j] - prefix[i-1]` | arr=[1,2,3,4], i=1,j=3 → 2+3+4=9 | Subarray sums |
| Prefix XOR | `prefixXOR[i] = prefixXOR[i-1] ^ arr[i]` | arr=[1,2,3] → prefix,
XOR=[1,3,0] | Range XOR queries |

---

## **7️⃣ Number Properties**

| Concept | Formula | Example | Use Case | Formula (**Python**) |
| --- | --- | --- | --- | --- |
| Prime number | Check divisibility up to √n | 7 → prime, 9 → not | Math problems, factorization |  |
| Armstrong number | Sum of digits^len = n | 153 → 1³+5³+3³=153 | Digit property problems |  |
| Automorphic number (*Number whose square ends with itself*) | n² ends with n | 5²=25 → automorphic | Digit pattern problems |  |
| Abundant number | Sum of divisors > n | 12 → 1+2+3+4+6=16>12 | Number theory |  |
| Palindrome number | `str(n)==str(n)[::-1]` | 121 → palindrome | Symmetry checks |  |
| Highest Common Factor (HCF) / GCD | Euclidean: `gcd(a,b)=gcd(b,a%b)` | gcd(12,18)=6 | Number theory, fraction simplification |  |
| Lowest Common Multiple (LCM) | `lcm(a,b) = a*b / gcd(a,b)` | lcm(4,6)=12 | Number theory, scheduling |  |
| Keep `summing digits` until a `single digit` remains (Digital root) | `1 + (n - 1) % 9` |  |  |  |
| Sum of digits | `sum_of_digits(n)=(n` `mod 10)+sum_of_digits(⌊n/10⌋)` |  |  | `s = n % 10 + s(n//10)` |
| Median | `(n//2)`-th element in sorted array | [2,5,1] → median=2 | Statistics in array problems |  |
| Average | `sum(arr)/n` | [1,2,3] → 2 | Mean of array/dataset |  |
| Find the g*reatest / largest* of the `Two` Numbers  | `max(a, b) = (a+b+|a-b|)/2` | a=10, b=20 → 20 |  | `max = a + b + abs(a - b) // 2`

`# Using Bitwise
a **- ((a - b) & ((a - b) >> 31))**
- ***31** comes from **32-bit integers**: MSB is at position 31 (0-indexed)
- For **64-bit integers**, you’d use >> 63*` |

---

## **8️⃣ Miscellaneous / Useful Patterns**

| Concept | Formula | Example | Use Case |
| --- | --- | --- | --- |
| Sum using loop | `sum=0; for i in range(a,b+1): sum+=i` | a=3,b=6 → 3+4+5+6=18 | Alternative to formula |
| Exponentiation | `a^n` | 2^5=32 | DP, combinatorics, powers |
| **Triangular numbers** —> Triangular numbers represent the `sum of the first **N natural numbers**`. They form a triangle when dots are arranged in rows. | `T_n = n(n+1)/2` | n=5 → 15 | Sum of first N numbers, series problems, stacking problems |
| Factor check | `n%i==0` | n=12,i=3 → divisible | Divisor problems |
| Subarray / Interval sum | `(b-a+1)*(a+b)//2` | a=3,b=6 → 18 | Interval sums safely in Python |
| Check even/odd using modulo | `num % 2 == 0 → even`, `num % 2 == 1 → odd` |  | Classic method, alternative to bitwise |
| Linearity of expectation | `E(X+Y)=E(X)+E(Y)` | Sum of multiple dice | Works **even if X,Y dependent** |

---

## **9️⃣ Power & Logarithmic Growth**

| Concept | Formula | Why It Matters |
| --- | --- | --- |
| Log base change | `log_b n = log n/log b` | Time complexity comparisons |
| Log sum | `log(ab) = log a + log b` | Recurrence relations |
| Log division | `log(a/b) = log a - log b` | Algorithm analysis |
| Log power | `log(n^k) = klog n` | Big-O simplification |
| Sum of logs | `log 1 + log 2 + ... + log n`≈ `nlog n` | Sorting complexity |

📌 **Asked in:** Merge sort, quick sort, recurrence analysis

---

## 10 Two-Pointer & Sliding Window Math

| Concept | Formula | Examples | Use Case |
| --- | --- | --- | --- |
| Window size | `right - left + 1` | left=2,right=4 → 3 | Sliding window |
| Subarray count | `n(n+1)/2` | Array length=5 → 15 subarrays | Counting subarrays |
| Pair count | `n(n-1)/2` |  | Combinations:

Handshake problems,
Number of edges in a complete graph,
Subarray / pair counting,
Combinatorial selection problems,
combinations of 2 elements |

📌 **Asked in:** Arrays, substrings, two pointers

---

## 11 Recurrence & Master Theorem Patterns

| Concept | Formula | Example | Use Case |
| --- | --- | --- | --- |
| Linear recurrence | `T(n) = T(n-1) + f(n)` | Fibonacci, sum of N numbers | DP problems, recursion analysis |
| Divide & Conquer | `T(n) = aT(n/b) + f(n)` | Merge sort T(n)=2T(n/2)+O(n) | Use **Master Theorem** to find O(n log n) |
| Master Theorem Cases | `f(n) = O(n^c) ), compare with ( n^(log_b a)` | Merge sort → O(n log n) | Recursion complexity analysis |

📌 **Asked in:** Merge sort, binary search, divide & conquer

---

## Triangular, Pair, Subarray & Subsequence Counts

| Concept | Formula | Example | Python Formula | Use Cases |
| --- | --- | --- | --- | --- |
| **Triangular Number** | `T_n = n(n+1)/2` | n=4 → 1+2+3+4=10 | `T = n*(n+1)//2` | Sum of first N numbers, series problems, stacking problems |
| **Pair Count (ordered)** | `P = n(n-1)` | n=5 → pairs = 5*4 = 20 | `pairs = n*(n-1)` | Permutations of 2 elements, sequence-based problems |
| **Pair Count (unordered)** | `P = n(n-1)/2` | n=5 → pairs = 5*4/2 = 10 | `pairs = n*(n-1)//2` | Handshake problems, complete graph edges, combinations of 2 elements |
| **Subarray Count (adjacent / contiguous)

`contiguous elements`** refer to data items that are *stored immediately next to each other in memory, without any gaps* | `S = n(n+1)/2` | Array length=4 → 4*5/2=10 subarrays | `subarrays = n*(n+1)//2` | Sliding window, range sum, contiguous segment problems |
| **Subarray Count (non-contiguous)** | `S = n * 2^(n-1)`  | n=3 → 3*2²=12 | `noncont_subarrays = n * 2**(n-1)` | Subarray selection where elements are not adjacent |
| **Subsequence Count (non-empty, any order)** | `2^n - 1` | n=3 → 2³=8 subsequences | `subseq = 2**n` | Include empty subset for combinatorial problems |
| **Subsequence Count (empty, any order)** | `2^n` | n=3 → 2³-1=7 subsequences | `subseq = 2**n - 1` | DP, combinatorics, subset enumeration, binary decisions |
| **Subsequence Count of length k** | `C(n,k) = n!/k!(n-k)!` | n=5, k=2 → 10 | `from math import comb; comb(n,k)` | Exact-length subsequence problems, combinatorial selection |

| Concept | Formula / Definition | Example | Explanation / Use Case | Python Formula | Alternatives |
| --- | --- | --- | --- | --- | --- |
| **Factorial (n!)** | `n! = n × (n-1)!` | 5! = 5×4×3×2×1 = 120 | Counting permutations of n distinct objects | `n * factorial_recursive(n-1)`

 | **Using Gamma Function / Stirling’s Approximation):**

`n!≈(sqrt(2πn)) (n/e)^n`

Python:
`# Stirling's approximation, rounded to nearest integer
**return round(math.sqrt(2*math.pi*n) * (n/math.e)**n)**` |
| **Combinations (nCr)**

`Order **doesn't** matter` | `C(n,r) = n!/r!(n-r)!` | 5C2 = 10 | Number of ways to choose r elements from n without order |  | *Calculate the number of ways to choose r items from a set of n items where **order doesn't matter*** |
| **Permutations (nPr)**

`Order matters` | `P(n,r) = n!/(n-r)!` | 5P2 = 20 | Number of ways to arrange r elements from n (order matters) |  | ***Calculate the number of ways to select and arrange r items from a total of n distinct items**, where the order of selection is crucial* |
| **Triangular numbers** | `T_n = n(n+1)/2` | n=4 → 1+2+3+4=10 | Sum of first n natural numbers, stacking or handshakes |  |  |
| **Fibonacci sequence** | `F_n = F_(n-1) + F_(n-2), F_0=0, F_1=1` | F_5 = 5 → 0,1,1,2,3,5 | Recursive & DP problems, rabbit breeding, tiling problems | `fibonacci_recursive(n-1) + fibonacci_recursive(n-2)`

 | **a series of numbers where `each number is the sum of the two preceding ones`, starting with 0 and 1 (0, 1, 1, 2, 3, 5, 8, 13...)** |
| **Prime numbers** | Number >1 with no divisors except 1 & itself | 2,3,5,7 | Used in hashing, modular arithmetic, cryptography | `is_prime_recursive(n, i+1)`

*Check divisibility recursively from 2 → sqrt(n).* | A prime number sequence **lists `numbers divisible only by 1 and themselves`, starting with 2, 3, 5, 7, 11, 13, and continuing infinitely** |
| **Palindrome (number/string)** | Reads same forward & backward | 121, "radar" | Used in string/number validation, reverse checks | `*is_palindrome_rec(s[1:-1])`

Check first and last characters, then recurse on middle substring.* | Palindrome - **`reads the same forwards and backward`.** |
| **Anagram** | Two strings with same character count | "listen" & "silent" | Used in strings, hashing, frequency count problems |  | an anagram refers to **`two strings that contain the exact same characters with the same frequencies, just in a different order`** (e.g., "listen" and "silent"). |
| **Armstrong number** | `sum(digit)^n = number`

Python:
`k = len(str(n))
return n == sum(int(digit)**k for digit in str(n))` | 153 (3 digits) → 1³+5³+3³=153

1634 (4 digits) → 1^4+6^4+3^4`4^4=1634
 | Number property problems, digit-based checks |  | It is a number that equals the `sum of its own digits each raised to the power of the total number of digits in the number`, creating a unique sequence like 0, 1, 2, ..., 9, 153, 370, 371, 407, 1634, 8208, 9474, and so on, with larger ones becoming rarer but theoretically infinite. For example, `153 is an Armstrong number because it has 3 digits, and 1³+5³+3³=153` |
| **Automorphic number** | `n is automorphic` `⟺ n^2≡n  (mod10k)` | 5²=25, 76²=5776 | Pattern-based problems, number theory |  | Number whose square ends with the number itself

Python:
`k = len(str(n))
return n**2 **% (10**k**) == n` |
| **Abundant number** | Sum of proper divisors > number | 12 → 1+2+3+4+6=16 >12 | Number classification, divisors, factorization problems |  |  |


# DSA Fundamentals

## Big-O Time & Space Complexity Table

| **Big-O** | **Time Complexity** | **Pattern (Time)** | **Example Algorithm Pattern (Time)** | **Space Complexity** | **Pattern (Space)** | **Example Algorithm Pattern (Space)** |
| --- | --- | --- | --- | --- | --- | --- |
| **O(1)** | Constant | Fixed number of operations.

Code with no loops or recursion; a fixed number of operations regardless of input size. | Accessing an element in an array by its index (`array[0]`) or adding two numbers, hash lookup, formula based solutions | Constant | Fixed variables | Scalar variables, swaps |
| **O(n)** | Linear | Single pass over input.

A single loop that iterates through the input (or a single dimension of the input) once. | Linear search, counting.

A simple `for` loop that iterates over every item in an array or list to find a specific value in an unsorted list. | Linear | Extra array or list | Copying array |
| **O(log n)** | Logarithmic | Input size halves each step.

The algorithm repeatedly halves the size of the problem space with each step. | Binary search, balanced BST search.

Binary search in a sorted array, where the search range is cut in half in each iteration. | Logarithmic | Recursion depth | Binary search recursion |
| **O(n log n)** | Linearithmic | Divide & conquer + combine.

An algorithm that divides the problem (log n) and then processes the elements in a linear fashion (n) during the merge or combine phase. | Merge sort, quicksort (avg).

Efficient sorting algorithms such as Merge Sort and Quick Sort. | Linear | Temporary arrays | Merge sort auxiliary array |
| **O(n²)** | Quadratic | Nested loops (same input).

Nested loops where the inner loop runs a number of times proportional to the outer loop's count. | Bubble sort, selection sort.

Simple sorting algorithms like bubble sort or selection sort, which involve comparing every element with every other element. | Quadratic | 2D data structures | Adjacency matrix |
| **O(n³)** | Cubic | Three nested loops | Floyd–Warshall | Cubic | 3D data structures | 3D DP table |
| **O(2ⁿ)** | Exponential | Recursive branching.

Recursive algorithms that solve a problem of size nn𝑛 by making multiple recursive calls for each input element. | Naive Fibonacci.

Calculating the Fibonacci sequence using a naive recursive approach.  | Linear | Recursion stack | Recursive calls depth |
| **O(n!)** | Factorial | All permutations | Traveling Salesman (brute force) | Linear | Recursion stack | Permutation generation |

---

## One-Line Mental Model 🧠

> Loops → n
>
>
> **Nested loops → n²**
>
> **Divide by 2 → log n**
>
> **Sort → n log n**
>
> **Branching recursion → exponential**
>

## Common Traps & Mistakes 🚫

- ❌ Counting constants (`O(2n)` instead of `O(n)`)
- ❌ Ignoring **recursion stack space**
- ❌ Assuming all nested loops are `O(n²)` (may be `O(n·m)`)
- ❌ Forgetting Python built-in complexities
- ❌ Confusing **average case** with **worst case**
- ❌ Ignoring auxiliary space (temporary arrays)
- ❌ Treating dictionary/set operations as always O(1) (collisions exist)

---

## Quick Big-O Identification Checklist 🧠

Ask yourself:

1. **How many loops are there?**
2. **Are loops nested or sequential?**
3. **Does the input size shrink or grow each step?**
4. **Is recursion used? How many recursive calls?**
5. **Are extra data structures created?**
6. **What dominates for large `n`?**
7. **Is this worst-case, average-case, or best-case?**
8. **Is space used by recursion or auxiliary storage?**