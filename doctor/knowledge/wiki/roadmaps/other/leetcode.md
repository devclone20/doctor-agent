# Leetcode Roadmap

## 1 D Dynamic Programming

# 1-D Dynamic Programming

Dynamic programming is the technique of breaking a problem into overlapping subproblems, solving each once, and storing the result to avoid recomputation. In one-dimensional DP, each state depends only on a fixed number of previous states, so the solution builds a single array from left to right. The first step is always identifying the recurrence: what does the answer at position i depend on? The problems here cover the core DP patterns you will see repeatedly: linear sequences, knapsack decisions, and string segmentation. DP problems are notoriously hard to recognize, and the only reliable way to get better at them is to solve many and study the structure of their recurrences.

Visit the following resources to learn more:

- [@article@1-D Dynamic Programming Problem](https://www.scaler.com/topics/data-structures/1-d-dynamic-programming-problem/)
- [@video@5 Simple Steps for Solving Dynamic Programming Problems](https://www.youtube.com/watch?v=aPQY__2H3tE)

## 2 D Dynamic Programming

# 2-D Dynamic Programming

Two-dimensional DP extends the same ideas to problems where the state depends on two variables simultaneously, typically two indices into two sequences or two dimensions of a grid. The table is now a matrix, and each cell is filled based on cells above it, to its left, or diagonally adjacent. The problems here include string comparison (edit distance, longest common subsequence), grid path counting, and interval DP where you think about ranges rather than prefixes. These problems tend to be harder to set up than 1-D DP, but once you identify the state and the transition, the code follows directly from the recurrence.

Visit the following resources to learn more:

- [@video@Learn Dynamic Programming with Animations – Full Course for Beginners](https://www.youtube.com/watch?v=66hDgWottdA)
- [@video@Dynamic Programming 2D - Full Course - Python](https://www.youtube.com/watch?v=qMky6D6YtXU)

## 3Sum

# 3Sum

Given an array of integers, find all unique triplets that sum to zero. You sort the array first, then for each element use two pointers to find pairs that complete the triplet. The sort plus two pointers bring it from O(n³) to O(n²). This problem teaches you to extend the two pointer technique beyond pairs and introduces how sorting enables smarter traversal.

Visit the following resources to learn more:

- [@article@3Sum - LeetCode](https://leetcode.com/problems/3sum/description/)
- [@video@3Sum (Updated Solution)](https://www.youtube.com/watch?v=TBePcj8DgxM)
- [@video@3 Sum (LeetCode 15)](https://www.youtube.com/watch?v=cRBSOz49fQk&t=39s)

## Advanced Graphs

# Advanced Graphs

Advanced graph problems involve weighted edges, which require more sophisticated algorithms than simple BFS or DFS. Dijkstra's algorithm finds the shortest path in a weighted graph using a min-heap. Prim's and Kruskal's algorithms find the minimum spanning tree, connecting all nodes at minimum total cost. These algorithms are more complex than anything seen so far, and the problems here often combine the algorithm with an additional constraint, such as a limit on the number of steps or a non-standard cost function. Understanding the conditions under which each algorithm applies is as important as knowing how to implement it.

## Arrays  Hashing

# Arrays & Hashing

Arrays and hash maps are the building blocks of almost every algorithm problem. Before learning any pattern, you need to be comfortable navigating an array and reaching for a hash map when you need fast lookups. Most problems in this stage are solved in one or two passes, and the main skill you are developing is recognizing when a hash map can replace a nested loop. If you find yourself thinking about checking membership or counting frequencies, a hash map is almost always the right tool.

Visit the following resources to learn more:

- [@article@DSA Arrays](https://www.w3schools.com/dsa/dsa_data_arrays.php)
- [@article@DSA Hash Tables](https://www.w3schools.com/dsa/dsa_theory_hashtables.php)
- [@article@Learning Data Structures](https://medium.com/@ashissh.dev/learning-data-structures-arrays-and-hash-tables-6ced329a9189)
- [@video@Ep.1 - Arrays & Hashing](https://www.youtube.com/watch?v=nET1jqI_Ntk)

## Backtracking

# Backtracking

Backtracking is a systematic way to explore all possible solutions by making a choice, recursing, and undoing the choice when you backtrack. It is the right tool for problems that ask for all combinations, all permutations, all subsets, or any valid configuration. The key skill is recognizing when to prune: stopping a branch early when you can tell it cannot lead to a valid solution. Without pruning, backtracking is just brute force. Most problems here share the same recursive skeleton and differ only in the constraints that determine valid choices and stopping conditions.

Visit the following resources to learn more:

- [@article@Backtracking Overview](https://www.hellointerview.com/learn/code/backtracking/overview)
- [@video@Backtracking Algorithm in 120 Seconds](https://www.youtube.com/watch?v=RtpJOGvfo7E)
- [@video@Introduction to Backtracking - Brute Force Approach](https://www.youtube.com/watch?v=DKCbsiDBN6c)

## Best Time To Buy And Sell

# Best Time to Buy and Sell Stock

Given an array of daily stock prices, find the maximum profit from one buy and one sell. You track the minimum price seen so far and the best profit achievable at each step using a single pass. This is the simplest sliding window problem since the window always expands from the current day, and it teaches you how to track a running minimum and maximum simultaneously.

Visit the following resources to learn more:

- [@article@Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [@video@LeetCode Best Time to Buy and Sell Stock Solution](https://www.youtube.com/watch?v=3RHCb8LY-X4)
- [@video@Best Time to Buy and Sell Stock](https://www.youtube.com/watch?v=kJZrMGpyWpk)

## Binary Search

# Binary Search

Binary search is not just for finding an element in a sorted array. It is a general technique for eliminating half the search space at each step, and it applies whenever you can define a condition that splits possible answers into a valid half and an invalid half. The problems in this stage move from the textbook version to more creative applications: searching in rotated arrays, and binary searching on the answer itself rather than on the input. Getting binary search right under pressure, with correct boundary conditions, is a skill that requires deliberate practice.

Visit the following resources to learn more:

- [@article@Binary Search](https://www.w3schools.com/dsa/dsa_algo_binarysearch.php)
- [@video@Binary Search Algorithm in 100 Seconds](https://www.youtube.com/watch?v=MFhxShGxHWc)

## Binary Search

# Binary Search

Given a sorted array and a target, return the index of the target or -1 if not found. You repeatedly halve the search space by comparing the middle element to the target. This is the simplest form of binary search and the one you must be able to write without mistakes before moving to harder variants.

Visit the following resources to learn more:

- [@article@Binary Search](https://leetcode.com/problems/binary-search/)
- [@video@Binary Search | Leet code 704 | Theory explained + Python code](https://www.youtube.com/watch?v=B7lMQIcIyN4)

## Binary Tree Level Order

# Binary Tree Level Order Traversal

Given a binary tree, return its node values level by level. You use a queue to process all nodes at one level before moving to the next, collecting each level into its own list. This is the entry point for tree BFS and teaches you the queue-based level tracking pattern that applies to many tree and graph problems.

Visit the following resources to learn more:

- [@article@Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [@video@Binary Tree Level Order Traversal | Live Coding with Explanation](https://www.youtube.com/watch?v=vQrggrFMyp8)
- [@video@Binary Tree Level Order Traversal (BFS)](http://youtube.com/watch?v=2_tm34ZtYT4)

## Binary Tree Maximum Path Sum

# Binary Tree Maximum Path Sum

Given a binary tree where nodes can have negative values, find the maximum sum of any path between any two nodes. At each node you decide whether to extend either child's path or start fresh, tracking the global maximum as you go. This is one of the hardest tree DFS problems and teaches you to separate what you return up the recursion from what you record as your answer.

Visit the following resources to learn more:

- [@article@Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [@video@Binary Tree Maximum Path Sum - LeetCode 124 - Python](https://www.youtube.com/watch?v=cfn-G-7vVlo)
- [@video@LeetCode 124. Binary Tree Maximum Path Sum](https://www.youtube.com/watch?v=mOdetMWwtoI)

## Bit Manipulation

# Bit Manipulation

Bit manipulation uses the binary representation of integers directly through bitwise operators: AND, OR, XOR, and shifts. It is useful for problems involving pairs, uniqueness, flags, or any situation where you need to extract or toggle individual bits. XOR is particularly powerful because it is its own inverse: XOR-ing a value twice cancels out. The problems here are mostly short, but they require a different way of thinking about numbers. Once you internalize the basic bit operations, you will start seeing where they can replace more expensive data structures in problems across other categories.

Visit the following resources to learn more:

- [@article@Bit manipulation](https://cp-algorithms.com/algebra/bit-manipulation.html)
- [@video@Algorithms: Bit Manipulation](https://www.youtube.com/watch?v=NLKQEOgBAnw)
- [@video@Bitwise Operators and WHY we use them](https://www.youtube.com/watch?v=igIjGxF2J-w)

## Burst Balloons

# Burst Balloons

Given an array of balloons with values, burst all of them to maximize coins, where bursting a balloon gives coins equal to the product of itself and its neighbors. You use interval DP: instead of choosing which balloon to burst first, you choose which to burst last within each interval. This problem teaches you that sometimes reversing the order of decisions makes the DP structure cleaner.

Visit the following resources to learn more:

- [@article@Burst Balloons](https://leetcode.com/problems/burst-balloons/)
- [@video@Minimum Number of Arrows to Burst Balloons](https://www.youtube.com/watch?v=lPmkKnvNPrw)
- [@video@Understand LeetCode 312. Burst Balloons in 6 minutes](https://www.youtube.com/watch?v=o3-PUPXiVfI)

## C

# C++

C++ is the language of choice for competitive programmers and is common in companies where raw performance matters, such as systems, gaming, or high-frequency trading. It has the fastest execution time of any commonly used interview language and gives you direct access to the standard template library, which includes a heap, set, map, and many other useful structures. The tradeoff is verbosity and the overhead of managing memory manually in some cases. If you are already proficient in C++, it is an excellent interview language. If you are starting from scratch, the learning curve is steep.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated C++ Roadmap](https://roadmap.sh/cpp)

## Character Replacement

# Longest Repeating Character Replacement

Given a string and a number k, find the length of the longest substring where you can replace at most k characters to make all characters the same. You track the count of the most frequent character in the window, and if the window size minus that count exceeds k, you shrink from the left. This problem teaches you a clever invariant: you never need to shrink the window below its maximum size seen so far.

Visit the following resources to learn more:

- [@article@Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [@video@LeetCode Longest Repeating Character Replacement Solution](https://www.youtube.com/watch?v=00FmUN1pkGE)
- [@video@Longest Repeating Character Replacement - Leetcode 424](https://www.youtube.com/watch?v=tkNWKvxI3mU)

## Cheapest Flights Within K Stops

# Cheapest Flights Within K Stops

Given a graph of flights with prices, find the cheapest route from source to destination using at most k stops. This is a modified Dijkstra or Bellman-Ford problem where the constraint is on the number of edges, not just total cost. This problem teaches you how to add an extra dimension (number of steps) to a shortest path algorithm.

Visit the following resources to learn more:

- [@article@Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- [@video@LeetCode 787. Cheapest Flights Within K Stops](https://www.youtube.com/watch?v=vWgoPTvQ3Rw)
- [@video@Leetcode - Cheapest Flights Within K Stops (Python)](https://www.youtube.com/watch?v=Jbb9qNIAyg0)

## Climbing Stairs

# Climbing Stairs

You can climb one or two steps at a time. Find the number of distinct ways to reach the top of n stairs. The number of ways to reach step n is the sum of ways to reach n-1 and n-2, which is exactly the Fibonacci pattern. This is the entry point to DP and teaches you to see a problem as a recurrence: the answer at each state depends on previous states.

Visit the following resources to learn more:

- [@article@Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [@video@Climbing Stairs - Leetcode 70 - Dynamic Programming (Python)](https://www.youtube.com/watch?v=I-R1XsECJu8)
- [@video@Climbing Stairs - LeetCode 70 - JavaScript](https://www.youtube.com/watch?v=Ifek5h5VqJw)

## Clone Graph

# Clone Graph

Given a connected undirected graph, return a deep copy of it. You use DFS or BFS and a hash map to track which nodes have already been cloned, so you do not create duplicate copies when revisiting nodes. This problem teaches you to handle graphs with cycles during traversal, which requires tracking visited nodes from the start.

Visit the following resources to learn more:

- [@article@Clone Graph](https://leetcode.com/problems/clone-graph/)
- [@video@Clone Graph - LeetCode 133 - Python](https://www.youtube.com/watch?v=2Qzj0t8nrCk)
- [@video@Clone Graph - Leetcode 133 - Graphs (Python)](https://www.youtube.com/watch?v=wWE7YzuBBkE)

## Coin Change

# Coin Change

Given coin denominations and a target amount, find the minimum number of coins needed. You build a DP table where each amount stores the fewest coins to make it, using each coin to update future amounts. This is the canonical unbounded knapsack problem and teaches you bottom-up DP where you iterate over amounts rather than items.

Visit the following resources to learn more:

- [@article@Coin Change](https://leetcode.com/problems/coin-change/)
- [@video@Coin Change Problem | Minimum Number Of Coins Needed](https://www.youtube.com/watch?v=KnWorqyDSLA)
- [@video@Coin Change - LeetCode 322 - Python - Visually Explained](https://www.youtube.com/watch?v=Z6fauIHQiUk)

## Combination Sum

# Combination Sum

Given an array of distinct integers and a target, return all unique combinations that sum to the target, where each number can be used unlimited times. You use backtracking, and at each step either reuse the current number or move to the next. This problem teaches you how to allow repetition in backtracking by staying at the same index instead of advancing.

Visit the following resources to learn more:

- [@article@Combination Sum](https://leetcode.com/problems/combination-sum/)
- [@video@LEETCODE 39 COMBINATION SUM](https://www.youtube.com/watch?v=uaqDhPGR4ow)
- [@video@Combination Sum - Leetcode 39 - Recursive Backtracking](https://www.youtube.com/watch?v=utBw5FbYswk)

## Container With Most Water

# Container With Most Water

Given an array of bar heights, find two bars that together with the x-axis form a container holding the most water. You start with the widest possible container and move the pointer on the shorter side inward, since that is the only move that could increase the area. This problem teaches the key insight that moving the longer side never helps, which is a non-obvious greedy choice that the two pointer pattern makes visible.

Visit the following resources to learn more:

- [@article@Container With Most Water - LeetCode](https://leetcode.com/problems/container-with-most-water/description/)
- [@video@Container With Most Water - Leetcode 11](https://www.youtube.com/watch?v=Y_4_or0Sc7I)
- [@video@Container With Most Water | Detailed Explanation](https://www.youtube.com/watch?v=mVkyZzmuQmg)

## Contains Duplicate

# Contains Duplicate

Given an array, return true if any value appears more than once. The brute force compares every pair, but a hash set lets you check for duplicates in a single pass. Simple as it sounds, this problem is your first introduction to using a set for O(1) membership checks, a pattern you will see in almost every stage.

Visit the following resources to learn more:

- [@article@Contains Duplicate - LeetCode](https://leetcode.com/problems/contains-duplicate/description/)
- [@video@Contains Duplicate](https://www.youtube.com/watch?v=a1_r3cLQ6wg)

## Counting Bits

# Counting Bits

Given an integer n, return an array where each element is the number of 1 bits in its binary representation from 0 to n. You can use DP: the number of bits in i equals one plus the bits in i with its lowest set bit removed. This problem teaches you to combine bit manipulation with DP to avoid recomputing from scratch for each number.

Visit the following resources to learn more:

- [@article@Counting Bits](https://leetcode.com/problems/counting-bits/)
- [@video@Counting Bits - LeetCode 338 - Python](https://www.youtube.com/watch?v=AACAzLKE9MI)
- [@video@Counting Bits | Leetcode #338](https://www.youtube.com/watch?v=awxaRgUB4Kw)

## Course Schedule

# Course Schedule

Given a list of courses and prerequisites, determine if it is possible to finish all courses. This is a cycle detection problem in a directed graph: if any cycle exists, the schedule is impossible. You can solve it with DFS by tracking nodes in the current recursion path. This problem teaches you topological sort thinking and is a gateway to all dependency-based graph problems.

Visit the following resources to learn more:

- [@article@Course Schedule](https://leetcode.com/problems/course-schedule/)
- [@video@LeetCode 207: Course Schedule | Topological Sort](https://www.youtube.com/watch?v=EUDwWbvtB_Q)
- [@video@Course Schedule (Detecting Cycles in a Graph)](https://www.youtube.com/watch?v=nz5V5pOiT8w)

## Daily Temperatures

# Daily Temperatures

Given an array of daily temperatures, return an array where each element is the number of days until a warmer temperature. A monotonic stack stores indices of temperatures in decreasing order, and whenever a warmer day is found, all colder days in the stack get their answer. This problem is the entry point for the monotonic stack pattern, which appears in many harder problems.

Visit the following resources to learn more:

- [@article@Daily Temperatures - LeetCode](https://leetcode.com/problems/daily-temperatures/description/)
- [@video@Daily Temperatures (LeetCode 739)](https://www.youtube.com/watch?v=ekFs9Nb2RNQ)
- [@video@Daily Temperatures - Leetcode 739](https://www.youtube.com/watch?v=_ZEvmycwXHs)

## Design Add And Search Words

# Design Add and Search Words Data Structure

Build a data structure that supports adding words and searching for words where a dot can match any letter. Exact characters navigate the trie normally, while a dot triggers DFS across all child nodes. This problem teaches you how to combine trie traversal with backtracking for wildcard matching.

Visit the following resources to learn more:

- [@article@Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- [@video@Design Add And Search Word Data Structure](https://www.youtube.com/watch?v=zDyoxl29yns)
- [@video@Design Add and Search Words Data Structure | Made Easy](https://www.youtube.com/watch?v=wyUO7Oq9uS4)

## Edit Distance

# Edit Distance

Given two strings, find the minimum number of insertions, deletions, or replacements to transform one into the other. A 2D DP table tracks the cost to convert each prefix of one string to each prefix of the other. This problem teaches you the three-way choice at each cell (insert, delete, replace) and is a foundational example of DP on two sequences.

Visit the following resources to learn more:

- [@article@Edit Distance](https://leetcode.com/problems/edit-distance/)
- [@video@Edit Distance (LeetCode 72) | Full step by step solution](https://www.youtube.com/watch?v=HwDXH35lr0o)
- [@video@Edit Distance - LeetCode 72 - Python - Visually Explained](https://www.youtube.com/watch?v=c3KYnQ-VEhs)

## Find Median From Data Stream

# Find Median from Data Stream

Design a data structure that supports adding numbers one by one and returning the median at any point. You maintain two heaps: a max-heap for the lower half and a min-heap for the upper half, keeping them balanced so the median is always accessible at the top. This is the defining two-heap problem and teaches you how splitting a dataset into two heaps gives O(log n) insertion and O(1) median retrieval.

Visit the following resources to learn more:

- [@article@Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [@video@Find Median from Data Stream: Real-Time Median with Heaps](https://www.youtube.com/watch?v=SdURPlHqc1g)

## Gas Station

# Gas Station

Given gas amounts and costs at each station on a circular route, find the starting station from which you can complete the circuit. If total gas is at least total cost, a solution exists, and the starting point is always after the last segment where the running tank went negative. This problem teaches you that a global observation (total gas vs total cost) can determine existence, while a local scan finds the answer.

Visit the following resources to learn more:

- [@article@Gas Station](https://leetcode.com/problems/gas-station/)
- [@video@L82. Gas Station | Greedy Approach | Leetcode 134](https://www.youtube.com/watch?v=SmTow5Ht4iU)
- [@video@LeetCode 134 | Gas Station Problem Visually Explained](https://www.youtube.com/watch?v=9h-2YiTNam4)

## Generate Parentheses

# Generate Parentheses

Given n, generate all combinations of well-formed parentheses. You build strings recursively, adding an opening bracket if you still have some left and a closing bracket only if it would not break validity. This problem sits at the boundary between stack and backtracking thinking and teaches you to use constraints to prune the search space before exploring it.

Visit the following resources to learn more:

- [@article@Generate Parentheses - LeetCode](https://leetcode.com/problems/generate-parentheses/description/)
- [@video@LeetCode 22. Generate Parentheses](https://www.youtube.com/watch?v=qBbZ3tS0McI)
- [@video@Generate Parentheses - Leetcode 22](https://www.youtube.com/watch?v=oC4saZRNwfI)

## Go

# Go

Go is a statically typed, compiled language designed for simplicity and performance. It is increasingly popular in backend and infrastructure roles and is commonly used at companies like Uber, Cloudflare, and Docker. Its syntax is minimal, and its concurrency model is distinctive, but for LeetCode purposes, what matters is its straightforward standard library and fast execution. Go does not have a built-in generic data structure library as rich as Java or C++, so you will sometimes need to implement things like heaps from scratch using the container/heap interface. It is a good choice if Go is your day-to-day language.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Go Roadmap](https://roadmap.sh/golang)

## Graphs

# Graphs

Graphs generalize trees by allowing arbitrary connections and cycles. The two core traversal techniques, DFS and BFS, work on graphs the same way they do on trees, but you must now track visited nodes explicitly to avoid infinite loops. This stage covers the main graph problem types: counting connected components, detecting cycles, finding shortest paths in unweighted graphs, and topological ordering of dependencies. Grids are also implicit graphs, where each cell is a node and adjacency is defined by its four neighbors. Most graph problems reduce to one of these patterns once you recognize the structure.

Visit the following resources to learn more:

- [@article@Graphs DSA](https://www.w3schools.com/dsa/dsa_theory_graphs.php)
- [@video@Learn Graphs in 5 minutes 🌐](https://www.youtube.com/watch?v=-VgHk7UMPP4)

## Greedy

# Greedy

Greedy algorithms make the locally optimal choice at each step and never revisit decisions. They are faster and simpler than DP when they work, but proving that a greedy choice leads to a globally optimal solution is not always obvious. The problems in this stage cover the most common greedy patterns: interval scheduling, jump games, and character frequency problems. A useful habit is to first ask whether a greedy approach is correct before coding it: can a short-sighted choice ever lead you away from the best solution? If the answer is yes, you probably need DP instead.

Visit the following resources to learn more:

- [@article@DSA Greedy Algorithms](https://www.w3schools.com/dsa/dsa_ref_greedy.php)
- [@video@Greedy Algorithms Tutorial – Solve Coding Challenges](https://www.youtube.com/watch?v=bC7o8P_Ste4)

## Group Anagrams

# Group Anagrams

Given a list of strings, group together all strings that are anagrams of each other. Since anagrams share the same characters, sorting each string gives a common key you can use in a hash map. A more optimal approach uses character frequency arrays as keys instead of sorting. This problem teaches you to think about what makes two things equivalent and use that equivalence as a grouping key, a useful mental model for many hash map problems.

Visit the following resources to learn more:

- [@article@Group Anagrams - LeetCode](https://leetcode.com/problems/group-anagrams/description/)
- [@video@Group Anagrams](https://www.youtube.com/watch?v=eDmxPfVa81k)

## Happy Number

# Happy Number

A happy number is one that eventually reaches 1 when you repeatedly replace it with the sum of the squares of its digits. Detect whether a number is happy. This is a cycle detection problem: if the process loops without reaching 1, the number is not happy. You can use Floyd's algorithm or a set to detect the cycle. This problem teaches you to recognize cycle detection in non-graph contexts.

Visit the following resources to learn more:

- [@article@Happy Number](https://leetcode.com/problems/happy-number/)
- [@video@Happy Number - LeetCode 202 - Python](https://www.youtube.com/watch?v=8wDuRgQ2dvw)
- [@video@Happy Number (LeetCode 202) | Full solution](https://www.youtube.com/watch?v=LkD0D0Xy-ro)

## Heap  Priority Queue

# Heaps and Priority Queue

A heap is the right data structure when you repeatedly need the largest or smallest element from a changing collection. The problems in this stage cover three heap patterns: top-k elements (maintain a heap of size k), two heaps (split a dataset into two halves to track the median), and k-way merge (combine multiple sorted sequences using a single heap). If you find yourself wanting to sort something repeatedly as new elements arrive, a heap is almost always the better choice. Getting comfortable with heap operations and knowing which variant to reach for is the main skill this stage develops.

Visit the following resources to learn more:

- [@article@Priority Queue](https://www.programiz.com/dsa/priority-queue)
- [@video@Learn Priority Queue data structures in 5 minutes 🥇](https://www.youtube.com/watch?v=7z_HXFZqXqc)
- [@video@Heaps in 3 minutes — Intro](https://www.youtube.com/watch?v=0wPlzMU-k00)

## House Robber

# House Robber

You are a robber planning to steal from houses in a row. You cannot rob two adjacent houses. Find the maximum amount you can steal. At each house you choose to rob it and skip the previous, or skip it and keep the best from before. This problem teaches the classic DP choice between taking the current element and combining it with a past state, or skipping it.

Visit the following resources to learn more:

- [@article@House Robber](https://leetcode.com/problems/house-robber/)
- [@video@House Robber - LeetCode 198 - Python](https://www.youtube.com/watch?v=r-ib63mhrNM)
- [@video@House Robber - Leetcode 198 - Dynamic Programming (Python)](https://www.youtube.com/watch?v=kIII1uT6F8Y)

## Implement Trie

# Implement Trie

Build a trie data structure that supports inserting a word, searching for an exact word, and checking if any word starts with a given prefix. Each node stores a map of child characters and a flag marking word endings. This problem teaches you the trie structure itself, which is prerequisite knowledge for all harder trie problems.

Visit the following resources to learn more:

- [@article@Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [@video@Implement Trie (Prefix Tree) - LeetCode 202 - Python](https://www.youtube.com/watch?v=1YmGVaGb-Gc)
- [@video@Implement Trie (Prefix Tree) - Trees (Python)](https://www.youtube.com/watch?v=8mhw5WT2x0U)

## Insert Interval

# Insert Interval

Given a sorted list of non-overlapping intervals and a new interval, insert it and merge any overlaps. You add all intervals that end before the new one starts, merge all that overlap with it, then add the rest. This problem teaches you to handle three distinct regions when inserting into a sorted interval list, a pattern that requires careful boundary thinking.

Visit the following resources to learn more:

- [@article@Insert Interval](https://leetcode.com/problems/insert-interval/)
- [@video@Insert Interval - LeetCode 57 - Python](https://www.youtube.com/watch?v=bx261hofOyk)
- [@video@Insert Interval (LeetCode 57) Full solution with different scenarios](https://www.youtube.com/watch?v=wCBtjZxw1xY)

## Intervals

# Intervals

Interval problems appear frequently in scheduling, calendar, and range-based questions. The dominant technique is sorting by start or end time, which turns an otherwise quadratic overlap-checking problem into a linear scan. Once sorted, you can merge overlaps, count simultaneous events, or find gaps with a single pass. The harder problems in this stage combine interval sorting with a heap to answer queries efficiently. The key mindset shift is thinking of intervals as objects with a start and end, and reasoning about what it means for two intervals to overlap, contain, or be adjacent.

Visit the following resources to learn more:

- [@article@DSA Fundamentals: Intervals - From Theory to LeetCode Practice](https://www.jaykye.dev/blog/dsa-intervals-fundamentals)

## Java

# Java

Java is one of the most commonly used interview languages, especially at large companies with backend and enterprise codebases. Its type system is verbose but explicit, and the standard library is comprehensive with well-documented data structures including priority queues, linked lists, and tree maps. Java forces you to think about types and interfaces clearly, which can actually help structure your thinking on harder problems. The main downside for interview prep is boilerplate: simple operations require more lines than in Python or Ruby. If Java is your primary language, it is a strong and widely accepted choice.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Java Roadmap](https://roadmap.sh/java)

## Javascript

# JavaScript

JavaScript is a solid choice if you already use it professionally or are preparing for frontend-focused roles. Its array methods and object literals are expressive, and most algorithmic patterns translate naturally to it. The main limitation is that JavaScript lacks a built-in heap or priority queue, so you will need to implement one or use a library when heap problems arise. If you are comfortable with JavaScript and do not want to switch languages just for interviews, it is a perfectly valid choice.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)

## Jump Game Ii

# Jump Game II

Given the same setup, find the minimum number of jumps to reach the last index. You greedily track the end of the current jump range and the furthest you can reach within it, incrementing the jump count when you exhaust the current range. This problem teaches you the two-range greedy technique, where you separate the current jump's boundary from the next one. Visit the question on the LeetCode [website](https://leetcode.com/problems/jump-game-ii/).

Visit the following resources to learn more:

- [@article@Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [@video@PASS the coding interview | #45 Jump Game II (Leetcode)](https://www.youtube.com/watch?v=G8isnm2OylM)
- [@video@Jump Game II - Leetcode 45 - Recursive Backtracking (Python)](https://www.youtube.com/watch?v=CsDI-yQuGeM)

## Jump Game

# Jump Game

Given an array where each element is the maximum jump length from that position, determine if you can reach the last index. You track the furthest position reachable so far and update it at each step. This problem teaches you the core greedy insight: you never need to track which specific jumps you take, only how far you can reach.

Visit the following resources to learn more:

- [@article@Jump Game](https://leetcode.com/problems/jump-game/)
- [@video@LeetCode 55. Jump Game (Algorithm Explained)](https://www.youtube.com/watch?v=Zb4eRjuPHbM)
- [@video@Jump Game (LeetCode 55) | Full solution](https://www.youtube.com/watch?v=Gtugy3mRV-A)

## K Closest Points To Origin

# K Closest Points to Origin

Given a list of points, return the k closest to the origin. A max-heap of size k keeps the k smallest distances seen so far, ejecting any point farther than the current kth closest as you iterate. This problem shows how to adapt the top-k pattern to a custom comparison and is good practice for heap problems with custom keys.

Visit the following resources to learn more:

- [@article@K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- [@video@K Closest Points to Origin | Leetcode #973](https://www.youtube.com/watch?v=VORIA407dB4)
- [@video@K Closest Points to Origin - Leetcode 973 - Heaps (Python)](https://www.youtube.com/watch?v=IGRUukbD6p8)

## Koko Eating Bananas

# Koko Eating Bananas

Koko can eat at most k bananas per hour and must finish all piles within h hours. Find the minimum k. The answer lies in a range, and you can binary search on that range, checking for each candidate k whether it is feasible. This problem teaches you to binary search on the answer rather than on the input array, a shift in thinking that unlocks many harder problems.

Visit the following resources to learn more:

- [@article@Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [@video@Koko Eating Bananas](https://www.youtube.com/watch?v=JGYXNpZaW2U)
- [@video@BS-12. Koko Eating Bananas](https://www.youtube.com/watch?v=qyfekrNni90)

## Kth Largest Element In An Array

# Kth Largest Element in an Array

Given an unsorted array and an integer k, return the kth largest element. You can use a min-heap of size k: iterate through the array, push each element, and pop when the heap exceeds k. The top of the heap is then the kth largest. This problem teaches the core heap pattern: maintain a fixed-size heap to track top-k elements without sorting the entire array.

Visit the following resources to learn more:

- [@article@Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [@video@Kth Largest Element in an Array](https://www.youtube.com/watch?v=dXV83KXt7KA)
- [@video@Kth Largest Element in an Array - Heaps (Python)](https://www.youtube.com/watch?v=ZmGk7h8KZLs)

## Largest Rectangle In Hist

# Largest Rectangle in Histogram

Given an array of bar heights, find the area of the largest rectangle that fits in the histogram. A monotonic stack tracks bars in increasing order of height, and each time a shorter bar is encountered, rectangles extending from the previous bars are resolved. This is one of the hardest stack problems and teaches you to use a stack to resolve pending computations when a condition breaks.

Visit the following resources to learn more:

- [@article@Largest Rectangle in Histogram - LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)
- [@video@Largest Rectangle in Histogram](https://www.youtube.com/watch?v=ZGMw8Bvpwd4)
- [@video@L12. Largest Rectangle in Histogram | Stack and Queue Playlist](https://www.youtube.com/watch?v=Bzat9vgD0fs)

## Linked List Cycle

# Linked List Cycle

Given the head of a linked list, determine if it contains a cycle. The fast and slow pointer technique has one pointer move one step at a time and the other move two steps at a time; if there is a cycle, they will eventually meet. This problem introduces the fast-and-slow-pointer pattern, which is used in several more advanced linked list problems.

Visit the following resources to learn more:

- [@article@Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [@video@LeetCode Linked List Cycle Solution Explained - Java](https://www.youtube.com/watch?v=6OrZ4wAy4uE)
- [@video@Linked List Cycle - Leetcode 141 - Linked Lists (Python)](https://www.youtube.com/watch?v=y-ckZ2hpC8Y)

## Linked List

# Linked List

Linked list problems test your ability to manipulate pointers directly, without the convenience of index-based access. The core techniques are the dummy node (to simplify edge cases at the head), the fast and slow pointer (to find midpoints and detect cycles), and in-place reversal (to rearrange nodes without extra memory). These three techniques cover the majority of linked list problems. The problems here also build the pointer intuition you will need when working with trees in the next stage.

Visit the following resources to learn more:

- [@article@DSA Linked Lists](https://www.w3schools.com/dsa/dsa_theory_linkedlists.php)
- [@article@Understanding Linked Lists: A Beginner’s Guide](https://medium.com/@ogundipe.eniola/understanding-linked-lists-a-beginners-guide-a7ca6aa6ee04)
- [@video@Learn Linked Lists in 13 minutes 🔗](https://www.youtube.com/watch?v=N6dOwBde7-M)

## Longest Common Prefix

# Longest Common Prefix

Given an array of strings, find the longest common prefix among all of them. One approach inserts all strings into a trie and traverses down as long as each node has exactly one child and is not a word end. This problem is simpler than the others but it teaches you that tries are not only for search, they also encode shared structure between strings.

Visit the following resources to learn more:

- [@article@Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [@video@Longest Common Prefix - Leetcode 14 - Arrays & Strings (Python)](https://www.youtube.com/watch?v=8C6F8_nM0qs)
- [@video@LeetCode 14. Longest Common Prefix Solution Explained - Java](https://www.youtube.com/watch?v=bl8ue-dTxgs)

## Longest Common Subsequence

# Longest Common Subsequence

Given two strings, find the length of their longest common subsequence. If characters match, you extend the LCS from the diagonal; otherwise you take the best from dropping one character in either string. This is the canonical 2D DP problem and teaches you how a 2D table captures the relationship between two sequences simultaneously.

Visit the following resources to learn more:

- [@article@Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [@video@Longest Common Subsequence (LeetCode 1143)](https://www.youtube.com/watch?v=e9tUPwZZSBI)
- [@video@Longest Common Subsequence Problem Visually Explained](https://www.youtube.com/watch?v=4ClOkX0SWW4)

## Longest Increasing Subsequ

# Longest Increasing Subsequence

Given an array, find the length of the longest strictly increasing subsequence. For each element, you check all previous elements that are smaller and extend the best subsequence ending there. This problem teaches you patience sorting and the classic O(n²) DP formulation, with an O(n log n) binary search optimization as a natural follow-up.

Visit the following resources to learn more:

- [@article@Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [@video@Longest Increasing Subsequence - Leetcode 300](https://www.youtube.com/watch?v=MrPa5EFcDCU)
- [@video@Longest Increasing Subsequence Problem Explained](https://www.youtube.com/watch?v=iQP5XFeXiMQ)

## Lowest Common Ancestor

# Lowest Common Ancestor of a BST

Given a BST and two nodes, find their lowest common ancestor. Because it is a BST, you can use the values to decide whether to go left, right, or stop: the ancestor is where the two nodes diverge. This problem teaches you to exploit BST ordering as a navigation tool, rather than doing a general tree search.

Visit the following resources to learn more:

- [@article@Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [@video@LOWEST COMMON ANCESTOR OF A BINARY TREE I](https://www.youtube.com/watch?v=WO1tfq2sbsI)
- [@video@Lowest Common Ancestor of a Binary Search Tree](https://www.youtube.com/watch?v=r6AXIfdi9oQ)

## Math  Geometry

# Math and Geometry

Math and geometry problems test your ability to translate a visual or numerical pattern into clean algorithmic logic. Many of these problems have elegant solutions that depend on a single mathematical observation, such as the structure of matrix rotation or the periodicity of digit sums. Unlike the earlier stages, there is no dominant pattern here. Instead, you are developing the habit of looking for structure in a problem before reaching for a general algorithm. These problems are a good test of problem-solving maturity: can you find the insight, or do you default to brute force?

Visit the following resources to learn more:

- [@article@Basic Geometry](https://cp-algorithms.com/geometry/basic-geometry.html)

## Maximum Depth Of Binary Tree

# Maximum Depth of Binary Tree

Given a binary tree, return its maximum depth, meaning the number of nodes along the longest root-to-leaf path. You recursively compute the depth of left and right subtrees and return one plus the greater. This is the simplest tree DFS problem and teaches you to think about trees recursively: a tree's depth is defined in terms of its subtrees' depths.

Visit the following resources to learn more:

- [@article@Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [@video@LeetCode 104: Maximum Depth of Binary Tree | Recursive DFS](https://www.youtube.com/watch?v=p-eMCRpvbIY)
- [@video@Maximum Depth of Binary Tree - Leetcode 104 - Trees (Python)](https://www.youtube.com/watch?v=ScvTcU2Aifs)

## Median Of Two Arrays

# Median of Two Sorted Arrays

Given two sorted arrays, find the median of their combined elements in O(log(min(m, n))). You binary search on the smaller array to find a partition where all elements on the left side are smaller than all on the right. This is one of the hardest binary search problems and teaches you to think about partitioning rather than searching for a single value.

Visit the following resources to learn more:

- [@article@Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [@video@Median of Two Sorted Arrays Python Solution - LeetCode #4](https://www.youtube.com/watch?v=BhxyUWR_Efc)
- [@video@Median of Two Sorted Arrays](http://youtube.com/watch?v=eUvfNcHhi5o)

## Meeting Rooms

# Meeting Rooms

Given a list of meeting time intervals, determine if a person can attend all of them. You sort by start time and check if any meeting starts before the previous one ends. This is the simplest interval problem and teaches you that sorted order plus a single-pass scan resolves most interval overlap questions instantly.

Visit the following resources to learn more:

- [@article@Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- [@video@Meeting Rooms - LeetCode 252 Python](https://www.youtube.com/watch?v=XI9L0HDl-No)
- [@video@Leetcode Premium - Intervals Interview Question](https://www.youtube.com/watch?v=5nqLIwo0oC0)

## Merge Intervals

# Merge Intervals

Given a list of intervals, merge all overlapping ones. You sort by start time and iterate, extending the current interval when the next one overlaps, or starting a new one when it does not. This is the foundational interval problem and teaches you that sorting by start time reduces the overlap check to a single comparison with the previous interval's end.

Visit the following resources to learn more:

- [@article@Merge Intervals](https://leetcode.com/problems/merge-intervals/https://leetcode.com/problems/merge-intervals/)
- [@video@Merge Intervals - Leetcode 56 - Arrays & Strings (Python)](https://www.youtube.com/watch?v=HCbKvBOlMVI)
- [@video@Leetcode - Merge Intervals (Python)](https://www.youtube.com/watch?v=iT9_MU2L3H0)

## Merge K Sorted Lists

# Merge K Sorted Lists

Given k sorted linked lists, merge them into one sorted list using a min-heap. You insert the head of each list into the heap, then repeatedly extract the minimum and push the next node from that list. This problem sits at the intersection of heaps and linked lists and is the canonical k-way merge example.

Visit the following resources to learn more:

- [@article@Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [@video@Merge K Sorted Arrays - Min Heap Algorithm](https://www.youtube.com/watch?v=ptYUCjfNhJY)
- [@video@Merge K Sorted Linked Lists - Leetcode 23 - Heaps (Python)](https://www.youtube.com/watch?v=RyrVWP76lVo)

## Merge K Sorted Lists

# Merge K Sorted Lists

Given k sorted linked lists, merge them into one sorted list. The optimal approach uses a min-heap to always extract the smallest current node across all lists. This problem connects linked list manipulation with heap usage and is the defining example of the k-way merge pattern.

Visit the following resources to learn more:

- [@article@Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [@video@Merge K Sorted Linked Lists - Leetcode 23 - Heaps (Python)](https://www.youtube.com/watch?v=RyrVWP76lVo)
- [@video@Merge K Sorted Arrays - Min Heap Algorithm](https://www.youtube.com/watch?v=ptYUCjfNhJY)

## Merge Two Sorted Lists

# Merge Two Sorted Lists

Given the heads of two sorted linked lists, merge them into one sorted list by splicing nodes together without creating new ones. You compare the heads of both lists at each step and attach the smaller node to your result. This problem teaches you the dummy node technique, which simplifies edge cases when building a new list from scratch.

Visit the following resources to learn more:

- [@article@Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [@video@LeetCode 21: Merge Two Sorted Lists (Visualization)](https://www.youtube.com/watch?v=E5XXiY6QnAs)
- [@video@Merge Two Sorted Lists - Leetcode 21 - Linked Lists (Python)](https://www.youtube.com/watch?v=5Rec4JS9H5o)

## Min Cost To Connect All Points

# Min Cost to Connect All Points

Given a list of points, find the minimum cost to connect all of them, where cost is the Manhattan distance between two points. This is a minimum spanning tree problem solvable with Prim's algorithm using a min-heap, always picking the cheapest edge to an unvisited node.

Visit the following resources to learn more:

- [@article@Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
- [@video@Min Cost to Connect All Points | Prim's Algorithm |](https://www.youtube.com/watch?v=hsr7KolYDH0)
- [@video@Min Cost to Connect All Points (Prim's Algorithm to Create MST)](https://www.youtube.com/watch?v=8VPIrqwQ8sQ)

## Min Interval To Include Query

# Minimum Interval to Include Each Query

Given a list of intervals and queries, for each query find the length of the smallest interval that contains it. You sort both intervals and queries, use a min-heap keyed by interval length, and process queries in order. This is the hardest interval problem in this stage and teaches you the offline query technique, processing queries in sorted order alongside a heap.

Visit the following resources to learn more:

- [@article@Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)
- [@video@Minimum Interval to Include Each Query: 1851](https://www.youtube.com/watch?v=FZtDTYzVUhU)

## Min Stack

# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element, all in O(1) time. The trick is to maintain a second stack that tracks the current minimum at each level. This problem teaches you that stacks can be augmented to carry extra state without breaking their core behavior.

Visit the following resources to learn more:

- [@article@Min Stack - LeetCode](https://leetcode.com/problems/min-stack/description/)
- [@video@Min Stack (LeetCode 155)](https://www.youtube.com/watch?v=lkYzexIVlOY)
- [@video@Min Stack - Leetcode 155 - Stacks (Python)](https://www.youtube.com/watch?v=RfMroCV17-4)

## Minimum In Rotated Array

# Find Minimum in Rotated Sorted Array

Given a rotated sorted array, find the minimum element in O(log n). The minimum is always at the rotation point, and you can locate it by checking which half is sorted and narrowing toward the unsorted side. This problem teaches you to think about what binary search is really doing: eliminating halves, not just finding a value.

Visit the following resources to learn more:

- [@article@Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [@video@LeetCode 153. Find Minimum in Rotated Sorted Array](https://www.youtube.com/watch?v=IzHR_U8Ly6c)
- [@video@Find Minimum in Rotated Sorted Array](https://www.youtube.com/watch?v=H2U24n4bcQQ)

## Minimum Window Substring

# Minimum Window Substring

Given strings s and t, find the smallest substring of s that contains all characters of t. You expand the right pointer until you have a valid window, then shrink from the left as much as possible while keeping it valid. This is one of the hardest sliding window problems and teaches you to manage a character frequency map as the window changes.

Visit the following resources to learn more:

- [@article@Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [@video@Leetcode - Minimum Window Substring (Python)](https://www.youtube.com/watch?v=CX6_L9GLldU)
- [@video@L12. Minimum Window Substring](https://www.youtube.com/watch?v=WJaij9ffOIY)

## More Excersises

# More Exercises

Below you can find other popular questions covering Math and Geometry. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Multiply Strings](https://leetcode.com/problems/multiply-strings/)
- [@article@Detect Squares](https://leetcode.com/problems/detect-squares/)
- [@article@Plus One](https://leetcode.com/problems/plus-one/)
- [@article@Count Primes](https://leetcode.com/problems/count-primes/)
- [@article@Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Binary Search. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [@article@Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
- [@article@Capacity to Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- [@article@Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [@article@Find Peak Element](https://leetcode.com/problems/find-peak-element/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Heap and Priority Queue. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [@article@Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
- [@article@Design Twitter](https://leetcode.com/problems/design-twitter/)
- [@article@Reorganize String](https://leetcode.com/problems/reorganize-string/)
- [@article@Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Sliding Window. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- [@article@Fruits into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
- [@article@Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [@article@Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
- [@article@Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

## More Excersises

# More Exercises

Below you can find other popular questions covering 1-D Dynamic Programming. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@House Robber II](https://leetcode.com/problems/house-robber-ii/)
- [@article@Decode Ways](https://leetcode.com/problems/decode-ways/)
- [@article@Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [@article@Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [@article@Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Backtracking. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Subsets II](https://leetcode.com/problems/subsets-ii/)
- [@article@Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- [@article@Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- [@article@Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [@article@Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Arrays & Hashing. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [@article@Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
- [@article@Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- [@article@Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
- [@article@Majority Element](https://leetcode.com/problems/majority-element/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Greedy. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Hand of Straights](https://leetcode.com/problems/hand-of-straights/)
- [@article@Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-a-target-triplet/)
- [@article@Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)
- [@article@Candy](https://leetcode.com/problems/candy/)
- [@article@IPO](https://leetcode.com/problems/ipo/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Two Pointers. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Sort Colors](https://leetcode.com/problems/sort-colors/)
- [@article@Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [@article@Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [@article@Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)
- [@article@4Sum](https://leetcode.com/problems/4sum/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Intervals. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [@article@Employee Free Time](https://leetcode.com/problems/employee-free-time/)
- [@article@Car Pooling](https://leetcode.com/problems/car-pooling/)
- [@article@Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
- [@article@My Calendar I](https://leetcode.com/problems/my-calendar-i/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Graphs. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [@article@Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- [@article@Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [@article@Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [@article@Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Linked List. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [@article@Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
- [@article@Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [@article@LRU Cache](https://leetcode.com/problems/lru-cache/)
- [@article@Reverse Nodes in K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Stack. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- [@article@Car Fleet](https://leetcode.com/problems/car-fleet/)
- [@article@Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
- [@article@Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
- [@article@Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Trees. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [@article@Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- [@article@Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [@article@Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [@article@Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Bit Manipulation. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Missing Number](https://leetcode.com/problems/missing-number/)
- [@article@Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- [@article@Power of Two](https://leetcode.com/problems/power-of-two/)
- [@article@Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
- [@article@Single Number II](https://leetcode.com/problems/single-number-ii/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Advanced Graphs. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- [@article@Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)
- [@article@Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [@article@Minimum Spanning Tree](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)
- [@article@Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

## More Excersises

# More Exercises

Below you can find other popular questions covering 2-D Dynamic Programming. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [@article@Coin Change II](https://leetcode.com/problems/coin-change-ii/)
- [@article@Target Sum](https://leetcode.com/problems/target-sum/)
- [@article@Interleaving String](https://leetcode.com/problems/interleaving-string/)
- [@article@Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

## More Excersises

# More Exercises

Below you can find other popular questions covering Tries. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/)
- [@article@Sum of Prefix Scores of Strings](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/)
- [@article@Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)
- [@article@Index Pairs of a String](https://leetcode.com/problems/index-pairs-of-a-string/)
- [@article@Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Math and Geometry. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Multiply Strings](https://leetcode.com/problems/multiply-strings/)
- [@article@Detect Squares](https://leetcode.com/problems/detect-squares/)
- [@article@Plus One](https://leetcode.com/problems/plus-one/)
- [@article@Count Primes](https://leetcode.com/problems/count-primes/)
- [@article@Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Binary Search. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [@article@Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
- [@article@Capacity to Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- [@article@Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [@article@Find Peak Element](https://leetcode.com/problems/find-peak-element/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Heap and Priority Queue. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [@article@Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
- [@article@Design Twitter](https://leetcode.com/problems/design-twitter/)
- [@article@Reorganize String](https://leetcode.com/problems/reorganize-string/)
- [@article@Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Sliding Window. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- [@article@Fruits into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
- [@article@Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [@article@Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
- [@article@Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

## More Exercises

# More Exercises

Below you can find other popular questions covering 1-D Dynamic Programming. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@House Robber II](https://leetcode.com/problems/house-robber-ii/)
- [@article@Decode Ways](https://leetcode.com/problems/decode-ways/)
- [@article@Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [@article@Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [@article@Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Backtracking. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Subsets II](https://leetcode.com/problems/subsets-ii/)
- [@article@Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- [@article@Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- [@article@Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [@article@Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Arrays & Hashing. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [@article@Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
- [@article@Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- [@article@Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
- [@article@Majority Element](https://leetcode.com/problems/majority-element/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Greedy. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Hand of Straights](https://leetcode.com/problems/hand-of-straights/)
- [@article@Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-a-target-triplet/)
- [@article@Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)
- [@article@Candy](https://leetcode.com/problems/candy/)
- [@article@IPO](https://leetcode.com/problems/ipo/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Two Pointers. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Sort Colors](https://leetcode.com/problems/sort-colors/)
- [@article@Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [@article@Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [@article@Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)
- [@article@4Sum](https://leetcode.com/problems/4sum/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Intervals. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [@article@Employee Free Time](https://leetcode.com/problems/employee-free-time/)
- [@article@Car Pooling](https://leetcode.com/problems/car-pooling/)
- [@article@Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
- [@article@My Calendar I](https://leetcode.com/problems/my-calendar-i/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Graphs. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [@article@Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- [@article@Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [@article@Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [@article@Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Linked List. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [@article@Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
- [@article@Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [@article@LRU Cache](https://leetcode.com/problems/lru-cache/)
- [@article@Reverse Nodes in K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Stack. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- [@article@Car Fleet](https://leetcode.com/problems/car-fleet/)
- [@article@Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
- [@article@Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
- [@article@Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Trees. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [@article@Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- [@article@Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [@article@Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [@article@Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Bit Manipulation. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Missing Number](https://leetcode.com/problems/missing-number/)
- [@article@Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- [@article@Power of Two](https://leetcode.com/problems/power-of-two/)
- [@article@Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
- [@article@Single Number II](https://leetcode.com/problems/single-number-ii/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Advanced Graphs. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- [@article@Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)
- [@article@Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [@article@Minimum Spanning Tree](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)
- [@article@Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

## More Exercises

# More Exercises

Below you can find other popular questions covering 2-D Dynamic Programming. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [@article@Coin Change II](https://leetcode.com/problems/coin-change-ii/)
- [@article@Target Sum](https://leetcode.com/problems/target-sum/)
- [@article@Interleaving String](https://leetcode.com/problems/interleaving-string/)
- [@article@Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

## More Exercises

# More Exercises

Below you can find other popular questions covering Tries. Work through these once you are comfortable with the five above.

Visit the following resources to learn more:

- [@article@Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/)
- [@article@Sum of Prefix Scores of Strings](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/)
- [@article@Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)
- [@article@Index Pairs of a String](https://leetcode.com/problems/index-pairs-of-a-string/)
- [@article@Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

## N Queens

# N-Queens

Place n queens on an n by n chessboard so that no two queens attack each other, and return all valid configurations. You place queens row by row and use sets to track which columns and diagonals are occupied, backtracking when a row has no valid placement. This is the classic constraint satisfaction problem and teaches you to use auxiliary state to prune the search space aggressively.

Visit the following resources to learn more:

- [@article@N-Queens](https://leetcode.com/problems/n-queens/)
- [@video@The N Queens Problem using Backtracking/Recursion](https://www.youtube.com/watch?v=wGbuCyNpxIg)

## Network Delay Time

# Network Delay Time

Given a network of nodes and weighted directed edges, find the time it takes for a signal to reach all nodes from a source. This is Dijkstra's algorithm: you use a min-heap to always process the closest unvisited node next. This problem teaches you Dijkstra's algorithm in its clearest form, without extra complications, making it the best starting point for weighted shortest path problems.

Visit the following resources to learn more:

- [@article@Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- [@video@Network Delay Time (Djikstra's Algorithm)](https://www.youtube.com/watch?v=Bp7STMWMMQw)
- [@video@Network Delay Time | Leetcode #743](https://www.youtube.com/watch?v=YHx6r9pM5e0)

## Non Overlapping Intervals

# Non-overlapping Intervals

Given a list of intervals, find the minimum number of intervals to remove so that the rest do not overlap. You sort by end time and greedily keep every interval that does not conflict with the last kept one. This problem teaches the classic interval scheduling insight: always prefer the interval that ends earliest, since it leaves the most room for future intervals.

Visit the following resources to learn more:

- [@article@Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [@video@Non-overlapping Intervals - LeetCode 435 - Python](https://www.youtube.com/watch?v=2LUQ6tBdGxo)
- [@video@Non-overlapping Intervals (LeetCode 435)](https://www.youtube.com/watch?v=XsrJgwGlRoc)

## Non Overlapping Intervals

# Non-overlapping Intervals

Given a list of intervals, find the minimum number to remove so that no two intervals overlap. Sorting by end time and greedily keeping non-conflicting intervals gives the maximum number you can keep, and the answer is total minus that. This problem reinforces the greedy interval scheduling principle and connects directly to the activity selection problem in algorithm theory.

Visit the following resources to learn more:

- [@article@Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [@video@Non-overlapping Intervals (LeetCode 435)](https://www.youtube.com/watch?v=XsrJgwGlRoc)
- [@video@Non-overlapping Intervals - LeetCode 435](https://www.youtube.com/watch?v=2LUQ6tBdGxo)

## Number Of 1 Bits

# Number of 1 Bits

Given a 32-bit integer, count how many bits are set to 1. You can check the last bit with a bitwise AND and shift right repeatedly, or use the trick n & (n-1) which clears the lowest set bit, counting until n becomes zero. This problem teaches you to inspect and clear individual bits, a fundamental bit manipulation skill.

Visit the following resources to learn more:

- [@article@Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [@video@Number of 1 Bits | Live Coding with Explanation | Leetcode - 191](https://www.youtube.com/watch?v=wLHhAHkID9M)
- [@video@Number of 1 Bits - Leetcode 191 - Bit Manipulation (Python)](https://www.youtube.com/watch?v=1JfdvPk-iHg)

## Number Of Islands

# Number of Islands

Given a 2D grid of land and water cells, count the number of islands. You do DFS from each unvisited land cell, marking the entire connected landmass as visited before moving on. This is the entry point for graph DFS on a matrix and teaches you to treat a grid as an implicit graph where adjacency is defined by up, down, left, right neighbors.

Visit the following resources to learn more:

- [@article@Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [@video@Number of Islands (LeetCode 200) | Full solution](https://www.youtube.com/watch?v=ZgCZfXPo3hI)
- [@video@Number of Islands - Leetcode 200 - Graphs (Python)](https://www.youtube.com/watch?v=gCswsDauXPc)

## Pacific Atlantic Water Flow

# Pacific Atlantic Water Flow

Given a matrix of heights, find all cells from which water can flow to both the Pacific and Atlantic oceans. You reverse the problem: do BFS inward from each ocean's border, marking all reachable cells, then return cells reachable from both. This problem teaches you that reversing the direction of traversal can turn an exponential problem into a linear one.

Visit the following resources to learn more:

- [@article@Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [@video@Pacific Atlantic Water Flow - Leetcode 417 - Graphs (Python)](https://www.youtube.com/watch?v=pDvvDvgHUKE)
- [@video@[Java] Leetcode 417. Pacific Atlantic Water Flow [Search #4]](https://www.youtube.com/watch?v=ZQp1oGp1y6s)

## Partition Labels

# Partition Labels

Given a string, partition it into as many parts as possible so that each letter appears in at most one part. You find the last occurrence of each character first, then greedily extend the current partition's boundary as you scan. This problem teaches you how to greedily build non-overlapping intervals using the last-occurrence anchor, a pattern that appears in several interval problems.

Visit the following resources to learn more:

- [@article@Partition Labels](https://leetcode.com/problems/partition-labels/)
- [@video@Partition Labels (LeetCode 763) | Solution with animations](https://www.youtube.com/watch?v=aUVEMnlcw4E)
- [@video@LeetCode 763. Partition Labels (Solution Explained)](https://www.youtube.com/watch?v=5NCjHqx2v-k)

## Permutations

# Permutations

Given an array of distinct integers, return all possible orderings. Unlike subsets, order matters here, so at each step you pick any unused element and continue recursively. This problem teaches you the difference between combination-style and permutation-style backtracking, and how to track which elements have been used.

Visit the following resources to learn more:

- [@article@Permutations](https://leetcode.com/problems/permutations/)
- [@video@Permutations (LeetCode 46) | Full solution with backtracking examples](https://www.youtube.com/watch?v=H232aocj7bQ)
- [@video@Permutations - Leetcode 46 - Recursive Backtracking (Python)](https://www.youtube.com/watch?v=gFm1lEfnzUQ)

## Pick A Language

# Pick a language

For LeetCode and technical interviews, the language you use matters less than how well you know it. Pick one language and stick with it throughout your preparation. Switching between languages wastes time and splits your focus. What interviewers care about is whether you can write clean, correct code and explain your reasoning clearly. That said, some languages have practical advantages: Python is concise and fast to write, which is helpful under time pressure. Java and C++ are common in companies that care about performance. JavaScript is a natural choice if you are coming from frontend development.

## Powx N

# Pow(x, n)

Implement the power function that raises x to the nth power, including negative exponents, in O(log n). You use fast exponentiation: square the base and halve the exponent at each step, handling odd exponents by multiplying in an extra factor. This problem teaches you recursive divide-and-conquer on a numerical computation, and is the standard way to implement exponentiation efficiently. Visit the question on the LeetCode [website](https://leetcode.com/problems/powx-n/).

Visit the following resources to learn more:

- [@article@Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [@video@POW(x,n) | Binary Exponentiation | Leetcode](https://www.youtube.com/watch?v=l0YC3876qxg)
- [@video@Pow(x, n) Python Solution - LeetCode #50](https://www.youtube.com/watch?v=bP4lhQP7_ao)

## Python

# Python

Python is the most popular language for LeetCode preparation and for good reason. Its syntax is concise, its built-in data structures like lists, dictionaries, and sets map directly to the structures you use in almost every problem, and the standard library includes a heap module and collections utilities that save significant time. Writing a sliding window or a DFS in Python requires far fewer lines than in most other languages. If you do not have a strong preference, Python is the recommended default for this roadmap.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Python Roadmap](https://roadmap.sh/python)

## Reconstruct Itinerary

# Reconstruct Itinerary

Given a list of airline tickets, reconstruct the itinerary in lexical order starting from JFK, using all tickets exactly once. You use DFS with a sorted adjacency list and add nodes to the result only after all their outgoing edges are exhausted, which is Hierholzer's algorithm for Eulerian paths. This problem teaches you a non-obvious graph traversal where the order of adding nodes to the result is reversed.

Visit the following resources to learn more:

- [@article@Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)
- [@video@Reconstruct Itinerary | Leetcode #332](https://www.youtube.com/watch?v=WYqsg5dziaQ)
- [@video@Leetcode - Reconstruct Itinerary (Python)](https://www.youtube.com/watch?v=iHhNWam4BSM)

## Regular Expression Matching

# Regular Expression Matching

Given a string and a pattern with dot and star wildcards, determine if the pattern matches the entire string. A 2D DP table tracks whether each prefix of the string matches each prefix of the pattern, with special handling for the star operator. This is one of the hardest 2D DP problems and teaches you to handle optional repetition in DP, where a character can appear zero or more times.

Visit the following resources to learn more:

- [@article@Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
- [@video@Regular Expression Matching Python Solution - LeetCode #10](https://www.youtube.com/watch?v=ZNI_yXaGlxY)
- [@video@Regular Expression Matching | Brute Force | Optimal](https://www.youtube.com/watch?v=3vbBrl-LeDc)

## Reorder List

# Reorder List

Given a linked list, reorder it so that nodes alternate from the front and back of the original list. You find the middle, reverse the second half, then merge the two halves. This problem combines three sub-techniques (finding middle, reversing, merging) and teaches you to decompose complex pointer problems into simpler steps.

Visit the following resources to learn more:

- [@article@Reorder List](https://leetcode.com/problems/reorder-list/)
- [@video@LeetCode Reorder List Solution Explained - Java](https://www.youtube.com/watch?v=xRYPjDMSUFw)
- [@video@Reorder List (LeetCode 143) | Full Solution](https://www.youtube.com/watch?v=Pno7rUOZM-o)

## Replace Words

# Replace Words

Given a dictionary of root words and a sentence, replace each word in the sentence with its shortest matching root from the dictionary. You insert all roots into a trie, then for each word in the sentence traverse the trie character by character until you hit a root or fail. This problem teaches you practical trie lookup with early termination, which is the core of trie efficiency.

Visit the following resources to learn more:

- [@article@Replace Words](https://leetcode.com/problems/replace-words/)
- [@video@Leetcode 648 Replace Words](https://www.youtube.com/watch?v=5liJnc8iNeY)
- [@video@✅ Replace Words - LeetCode 648 - Strings - Tries - Explained in Detail - Interview Solution](https://www.youtube.com/watch?v=HdQeNCwE2tU)

## Reverse Bits

# Reverse Bits

Given a 32-bit unsigned integer, reverse its bits. You build the result bit by bit by extracting the last bit from the input and shifting it into the result. This problem teaches you how to construct a new number bit by bit using shifts and masks, which is useful in many low-level and embedded contexts.

Visit the following resources to learn more:

- [@article@Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- [@video@Reverse Bits - LeetCode 190 - Python](https://www.youtube.com/watch?v=PywybHkTtPo)
- [@video@Reverse Bits | Leetcode 190 | Easy](https://www.youtube.com/watch?v=-5z9dimxxmI)

## Reverse Linked List

# Reverse Linked List

Given the head of a linked list, reverse it in place and return the new head. You iterate through the list, keeping track of the previous node, current node, and next node, rewiring each pointer as you go. This is the first linked list problem most people learn and it teaches you the three-pointer technique that underlies almost every in-place list manipulation.

Visit the following resources to learn more:

- [@article@Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [@video@Reverse Linked List - Leetcode 206 - Linked Lists (Python)](https://www.youtube.com/watch?v=KRxeMng7fBU)
- [@video@LeetCode - Reverse Linked List Solution](https://www.youtube.com/watch?v=NhapasNIKuQ)

## Rotate Image

# Rotate Image

Given an n by n matrix, rotate it 90 degrees clockwise in place. You first transpose the matrix (swap across the diagonal), then reverse each row. This problem teaches you that complex in-place transformations often decompose into two simpler operations applied in sequence.

Visit the following resources to learn more:

- [@article@Rotate Image](https://leetcode.com/problems/rotate-image/)
- [@video@Rotate Image (Leetcode 48) | Full solution](https://www.youtube.com/watch?v=Ux058jpRB9Y)
- [@video@Rotate Image - Leetcode 48 - Arrays & Strings (Python)](https://www.youtube.com/watch?v=-jhbxNJijyE)

## Ruby

# Ruby

Ruby is an expressive, readable language with clean syntax and strong built-in enumerable methods that make array and hash manipulation concise. It is less common in technical interviews than Python, JavaScript, or Java, but it is a valid choice if you use it professionally and are comfortable with it. One practical consideration is that Ruby solutions on LeetCode are sometimes slower than equivalent solutions in compiled languages, which can occasionally cause timeout issues on harder problems. Use Ruby if it is your strongest language, but be aware of this limitation.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Ruby Roadmap](https://roadmap.sh/ruby)

## Rust

# Rust

Rust is a systems programming language focused on memory safety and performance without a garbage collector. It is gaining popularity for roles in systems programming, WebAssembly, and performance-critical applications. For LeetCode, Rust is the most challenging language to use due to its strict ownership model, which can make pointer-heavy problems like linked lists and trees significantly more complex to implement than in other languages. If you are already comfortable with Rust and want to use it for interviews, it is possible and impressive, but it is not recommended as a starting point for interview preparation.

Visit the following resources to learn more:

- [@official@Visit the Dedicated Rust Roadmap](https://roadmap.sh/rust)

## Scala

# Scala

Scala is a functional and object-oriented language that runs on the JVM and is popular in data engineering and distributed systems roles. Its expressive type system and functional abstractions like pattern matching and higher-order functions can make some algorithmic problems elegant to solve. However, Scala is rarely the expected language in general software engineering interviews, and LeetCode support for it is more limited. Choose Scala only if you are specifically targeting roles where it is the primary language and you are already fluent in it.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Scala Roadmap](https://roadmap.sh/scala)

## Search In Rotated Array

# Search in Rotated Sorted Array

A sorted array has been rotated at an unknown index. Find a target value in O(log n). At every step, one of the two halves must be sorted, and you can use that to decide which half to search. This problem teaches you to apply binary search even when the input is not perfectly sorted, by adding a condition to identify the sorted half.

Visit the following resources to learn more:

- [@article@Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [@video@LeetCode 33. Search in Rotated Sorted Array](https://www.youtube.com/watch?v=QdVrY3stDD4)
- [@video@Search in Rotated Sorted Array](https://www.youtube.com/watch?v=4Ik1nCLjwcI)

## Serialize And Deserialize

# Serialize and Deserialize Binary Tree

Design an algorithm to convert a binary tree to a string and reconstruct it exactly from that string. One approach uses BFS level-order, encoding null pointers explicitly so the structure can be recovered. This problem teaches you that tree traversal is not just for reading trees but also for encoding and rebuilding them, a fundamental idea in tree design problems.

Visit the following resources to learn more:

- [@article@Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [@video@Serialize and Deserialize a Binary Tree](https://www.youtube.com/watch?v=Q9DrSCqg1rw)

## Set Matrix Zeroes

# Set Matrix Zeroes

Given a matrix, if any cell is zero, set its entire row and column to zero, in place. The trick is to record which rows and columns need zeroing before making any changes, using the first row and column as markers to avoid extra space. This problem teaches you to use existing space within the matrix to avoid allocating extra memory, a useful in-place technique.

Visit the following resources to learn more:

- [@article@Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- [@video@Set Matrix Zeroes - LeetCode 73 - Python](https://www.youtube.com/watch?v=IJ24FVsgPFU)
- [@video@Set Matrix Zeroes (LeetCode 73) | Full solution](https://www.youtube.com/watch?v=dSxt3ZCbIqA)

## Single Number

# Single Number

Given an array where every element appears twice except one, find the element that appears only once. XOR of a number with itself is zero, and XOR of a number with zero is the number itself, so XOR-ing all elements cancels duplicates and leaves the unique one. This problem is the entry point to bit manipulation and teaches you that XOR is a surprisingly powerful tool for finding missing or unique values.

Visit the following resources to learn more:

- [@article@Single Number](https://leetcode.com/problems/single-number/)
- [@video@Single Number - LeetCode 136 - Python #leetcode](https://www.youtube.com/watch?v=JnM0SQGlLY4)
- [@video@Single Number - Leetcode 136 - Bit Manipulation (Python)](https://www.youtube.com/watch?v=mriHA5vEh0A)

## Sliding Window Maximum

# Sliding Window Maximum

Given an array and a window size k, return the maximum value in each window. A monotonic deque stores indices in decreasing order of value, so the front is always the current maximum. This problem teaches you the monotonic deque, which gives O(n) window max where a heap would give O(n log n).

Visit the following resources to learn more:

- [@article@Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [@video@Sliding Window Maximum (LeetCode 239)](https://www.youtube.com/watch?v=WcTMo1SHV_s)
- [@video@Sliding Window Maximum: Efficient  Solution](https://www.youtube.com/watch?v=5VjQD62gOYA)

## Sliding Window

# Sliding Window

The sliding window pattern is used when you need to find an optimal subarray or substring that satisfies some constraint. Instead of checking every possible subarray from scratch, you maintain a window with two pointers and update the result incrementally as the window expands or shrinks. Fixed-size windows are straightforward; variable-size windows require a clear rule for when to shrink from the left. This stage also introduces the monotonic deque, which extends sliding window to problems that need the maximum or minimum within the window at each step.

Visit the following resources to learn more:

- [@article@Sliding Window Technique: A Comprehensive Guide](https://leetcode.com/discuss/post/3722472/sliding-window-technique-a-comprehensive-ix2k/)
- [@article@Sliding Window in 7 minutes | LeetCode Pattern](https://www.youtube.com/watch?v=y2d0VHdvfdc)

## Spiral Matrix

# Spiral Matrix

Given an m by n matrix, return all elements in spiral order. You maintain four boundaries (top, bottom, left, right) and peel one layer at a time, moving right, down, left, then up, shrinking the boundaries after each direction. This problem teaches careful boundary management and is a good test of whether you can translate a visual pattern into clean code.

Visit the following resources to learn more:

- [@article@Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [@video@Spiral Matrix (LeetCode 54) | Full Solution](https://www.youtube.com/watch?v=aqVW8IuXUF0)
- [@video@Spiral Matrix - Leetcode 54 - Arrays & Strings (Python)](https://www.youtube.com/watch?v=fcn8qkRcFVM)

## Stacks

# Stacks

A stack is the right tool whenever you need to process elements in a last-in-first-out order, or when you need to track something that will be resolved later. Many stack problems involve matching pairs, maintaining a running minimum or maximum, or deferring a computation until a future element triggers it. The monotonic stack variant, where you maintain elements in increasing or decreasing order, is particularly important and appears frequently in harder problems involving histograms, temperatures, and next greater elements.

Visit the following resources to learn more:

- [@article@DSA Stacks](https://www.w3schools.com/dsa/dsa_data_stacks.php)
- [@video@wtf is “the stack” ?](https://www.youtube.com/watch?v=CRTR5ljBjPM)

## Subsets

# Subsets

Given an array of unique integers, return all possible subsets, including the empty set. You use backtracking to make a binary decision at each element: include it or skip it, building subsets recursively. This problem teaches the foundation of backtracking, the include/exclude decision tree that underpins all subset and combination problems.

Visit the following resources to learn more:

- [@article@Subsets](https://leetcode.com/problems/subsets/)
- [@video@Subsets (LeetCode 78) | Full solution with backtracking examples](https://www.youtube.com/watch?v=3tpjp5h3M6Y)
- [@video@Subsets - Leetcode 78 - Recursive Backtracking (Python)](https://www.youtube.com/watch?v=UP3dOYJa05s)

## Substring Without Repetition

# Longest Substring Without Repeating Characters

Find the length of the longest substring that contains no duplicate characters. You expand the right pointer and shrink the left pointer whenever a duplicate enters the window, using a set to track current characters. This is the canonical variable-size sliding window problem and teaches you the expand-then-shrink rhythm that most substring problems follow.

Visit the following resources to learn more:

- [@article@Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [@video@Longest Substring Without Repeating Characters](https://www.youtube.com/watch?v=FCbOzdHKW18)
- [@video@Longest Substring Without Repeating Characters](https://www.youtube.com/watch?v=V3lL9RaZKaA)

## Sum Of Two Integers

# Sum of Two Integers

Calculate the sum of two integers without using the plus or minus operators. XOR gives the sum without carries, and AND shifted left gives the carries. You repeat until there are no more carries. This problem teaches you how addition works at the bit level and deepens your understanding of carry propagation.

Visit the following resources to learn more:

- [@article@Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- [@video@Sum of Two Integers - LeetCode 371 - Python](https://www.youtube.com/watch?v=MmIx_NrCkGI)
- [@video@Google Interview Question - Sum of Two Integers - LeetCode 371](https://www.youtube.com/watch?v=6vETcY7qfEo)

## Swim In Rising Water

# Swim in Rising Water

Given a grid where each cell has a height, find the earliest time t such that you can travel from top-left to bottom-right, moving only through cells with height at most t. You binary search on t or use Dijkstra treating each cell's height as the cost. This problem teaches you to reframe a graph problem as a min-max path problem, where you minimize the maximum cost along any path.

Visit the following resources to learn more:

- [@article@Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)
- [@video@Leetcode - Swim in Rising Water (Python)](https://www.youtube.com/watch?v=QJuzj-Gm-IM)
- [@video@Swim in Rising Water | Different Ways To Think](https://www.youtube.com/watch?v=9WYhuzn8hd8)

## Task Scheduler

# Task Scheduler

Given a list of tasks and a cooldown n, find the minimum time needed to finish all tasks, with the constraint that the same task must wait n intervals between executions. A greedy approach with a max-heap always schedules the most frequent remaining task, filling cooldown gaps with other tasks or idle time. This problem teaches you to combine a heap with a greedy scheduling strategy.

Visit the following resources to learn more:

- [@article@Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [@video@LeetCode 621. Task Scheduler (Algorithm Explained)](https://www.youtube.com/watch?v=eGf-26OTI-A)
- [@video@Task Scheduler - LeetCode 621 - Python](https://www.youtube.com/watch?v=CHlCkJadQ7o)

## Top K Frequent Elements

# Top K Frequent Elements

Given an array and a number k, return the k most frequent elements. You could sort by frequency, but the optimal approach uses bucket sort. Since no element can appear more times than the length of the array, you can create buckets indexed by frequency and scan from the top. This problem bridges hash maps and sorting, and introduces the idea that the constraints of a problem often suggest a faster algorithm.

Visit the following resources to learn more:

- [@article@Top K Frequent Elements - LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)
- [@video@Top K Elements in 6 minutes](https://www.youtube.com/watch?v=6_v6OoxvMOE)

## Trapping Rain Water

# Trapping Rain Water

Given an array of bar heights representing an elevation map, compute how much water can be trapped between the bars after rain. For each position, the water level is determined by the shorter of the tallest bars to its left and right. Two pointers eliminate the need to precompute these maximums separately. This is one of the hardest two-pointer problems and teaches you to reason about what constrains a value from both directions.

Visit the following resources to learn more:

- [@article@Trapping Rain Water - LeetCode](https://leetcode.com/problems/trapping-rain-water/description/)
- [@video@How to Solve Trapping Rainwater in 2 MINUTES](https://www.youtube.com/watch?v=Gu6Iu4q2sd8)
- [@video@Trapping Rain Water](https://www.youtube.com/watch?v=KFdHpOlz8hs)

## Trees

# Trees

Trees are the data structure where recursion becomes natural. Most tree problems follow one of two patterns: DFS, where you go deep before backtracking, and BFS, where you process nodes level by level. DFS is usually implemented recursively and is good for path-based and structural problems. BFS uses a queue and is good for level-based problems and shortest-path questions on unweighted trees. The key habit to build here is thinking clearly about what a function returns versus what it records as a side effect, since many tree problems require tracking a global answer while the recursion handles local decisions.

Visit the following resources to learn more:

- [@article@Trees DSA](https://www.w3schools.com/dsa/dsa_theory_trees.php)
- [@article@Trees](https://www.programiz.com/dsa/trees)
- [@video@Tree data structures in 2 minutes 🌳](https://www.youtube.com/watch?v=Etpc_-br5rI&t=1s)

## Tries

# Tries

A trie is a tree structure built from the characters of strings, where each path from the root to a marked node spells out a word. It is the right data structure when you need fast prefix lookups across a large set of strings. A hash map can check if a whole word exists, but a trie can check if any word in your dictionary starts with a given prefix in O(length) time. The three problems in this stage cover building a trie, searching with wildcards, and using a trie to prune a grid search, which together cover the full range of trie applications in interviews.

Visit the following resources to learn more:

- [@article@Trying to Understand Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)
- [@video@Data Structures: Tries](https://www.youtube.com/watch?v=zIjfhVPRZCg)

## Two Pointers

# Two Pointers

Two pointers is the first real pattern you will learn, and it is one of the most reusable. The idea is simple: instead of checking every pair of elements with nested loops, you place one pointer at each end of a sorted structure and move them toward each other based on a condition. This brings many O(n²) problems down to O(n). Most problems here require a sorted input, so sorting is often the first step. Mastering this pattern also prepares you for fast and slow pointers, which appear in linked list problems later.

Visit the following resources to learn more:

- [@article@Mastering Problem Solving: Two Pointers](https://medium.com/@elfrmkr98/mastering-problem-solving-two-pointers-technique-23dafb17e90b)
- [@video@Two Pointers in 7 minutes](https://www.youtube.com/watch?v=QzZ7nmouLTI)

## Two Sum Ii

# Two Sum II

Given a sorted array, find two numbers that add up to a target and return their positions. Because the array is sorted, you can use two pointers starting from each end and move them based on whether the current sum is too large or too small. This is where the two pointer pattern clicks for most learners, since the sorted order gives a clear rule for which pointer to move.

Visit the following resources to learn more:

- [@article@Two Sum II - Input Array Is Sorted - LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
- [@video@Two Sum II - Leetcode 167](https://www.youtube.com/watch?v=ciPrKYoOQkI)
- [@video@[Java] Leetcode 167. Two Sum II](https://www.youtube.com/watch?v=CWUnvUJ29zw)

## Two Sum

# Two Sum

You are given an array of integers and a target number. The goal is to find two numbers in the array that add up to the target and return their positions. The naive approach checks every pair, but the key insight is using a hash map to store numbers you have already seen, bringing the solution from O(n²) down to O(n). This problem teaches the core habit of trading space for time, a trade-off you will use constantly in harder problems.

Visit the following resources to learn more:

- [@article@Two Sum - LeetCode](https://leetcode.com/problems/two-sum/description/)
- [@video@Two Sum - Leetcode 1 - Hashmaps & Sets (Python)](https://www.youtube.com/watch?v=aRE7Nxb3Qfs)

## Unique Paths

# Unique Paths

A robot starts at the top-left of an m by n grid and can only move right or down. Find the number of unique paths to the bottom-right. Each cell's count is the sum of the cell above and the cell to the left. This is the simplest 2D DP problem and teaches you to think in terms of a grid where each cell builds on its neighbors.

Visit the following resources to learn more:

- [@article@Unique Paths](https://leetcode.com/problems/unique-paths/)
- [@video@Unique Paths - Leetcode 62 - Dynamic Programming (Python)](https://www.youtube.com/watch?v=3ZFvBlynmls)
- [@video@Unique Paths (LeetCode 62)](https://www.youtube.com/watch?v=Ee-rJmkwaTM)

## Valid Anagram

# Valid Anagram

Given two strings, decide if one is an anagram of the other, meaning both contain the exact same characters with the same frequency. The trick is not to sort (which works but is slower), but to count character frequencies using a hash map and compare them. This problem teaches you to think about strings as frequency distributions rather than sequences of characters.

Visit the following resources to learn more:

- [@article@Valid Anagram - LeetCode](https://leetcode.com/problems/valid-anagram/description/)
- [@video@Valid Anagram | LeetCode problem 242 | Top 150 interview question series](https://backoffice.roadmap.sh/tree/leetcode)

## Valid Palindrome

# Valid Palindrome

Given a string, determine if it reads the same forward and backwards after removing non-alphanumeric characters and ignoring case. Two pointers start at each end and move inward, comparing characters as they go. This problem teaches you to use two pointers on a string and is a clean entry point for understanding how pointers can replace nested loops.

Visit the following resources to learn more:

- [@article@Valid Palindrome - LeetCode](https://leetcode.com/problems/valid-palindrome/description/)
- [@video@Valid Palindrome - LeetCode 125 | Two Pointers](https://www.youtube.com/watch?v=pf5RT8Oi7rk)
- [@video@LeetCode Valid Palindrome](https://www.youtube.com/watch?v=rYyn9Vc-dBQ)

## Valid Parentheses

# Valid Parentheses

Given a string of brackets, determine if it is valid, meaning every opening bracket is closed by the same type in the correct order. You push opening brackets onto a stack and pop when you see a closing bracket, checking for a match. This is the canonical stack problem and teaches you the key idea: a stack naturally tracks things that need a future match.

Visit the following resources to learn more:

- [@article@Valid Parentheses - LeetCode](https://leetcode.com/problems/valid-parentheses/description/)
- [@video@Valid Parentheses (LeetCode 20)](https://www.youtube.com/watch?v=TaWs8tIrnoA)
- [@video@Valid Parentheses - Leetcode 20 - Stacks (Python)](https://www.youtube.com/watch?v=7-_V-ufnF4c)

## What Are Coding Patterns

# What are coding patterns?

Coding patterns are recurring problem-solving strategies that apply across many different problems. Instead of memorizing solutions, you learn to recognize the structure of a problem and match it to a pattern you already know. Once you internalize around fifteen to twenty patterns, you can approach most interview problems with a starting point rather than a blank page. This roadmap is organized around those patterns.

Visit the following resources to learn more:

- [@article@Don’t Just LeetCode; Follow the Coding Patterns Instead](https://levelup.gitconnected.com/dont-just-leetcode-follow-the-coding-patterns-instead-4beb6a197fdb)
- [@video@Data Structure and Algorithm Patterns for LeetCode Interviews](https://www.youtube.com/watch?v=Z_c4byLrNBU)

## What Is Leetcode

# What is LeetCode

LeetCode is an online platform with hundreds of coding problems used by software engineers to prepare for technical interviews. Companies like Google, Meta, Amazon, and Microsoft use similar problems in their hiring process to evaluate how candidates think through algorithmic challenges. You do not need to solve thousands of problems to be ready. What matters is understanding the patterns behind problems well enough to apply them to ones you have never seen before. LeetCode is the practice ground, not the goal.

Visit the following resources to learn more:

- [@official@LeetCode](https://leetcode.com/)
- [@article@What I Learned From LeetCode](https://tenmilesquare.com/resources/software-development/what-i-learned-from-leetcode/)

## Word Break

# Word Break

Given a string and a dictionary of words, determine if the string can be segmented into a sequence of dictionary words. You use DP where each position stores whether the substring up to that point can be formed, checking every possible last word. This problem teaches you how to use a boolean DP array to track reachability, a pattern that appears in many string segmentation problems.

Visit the following resources to learn more:

- [@article@Word Break](https://leetcode.com/problems/word-break/)
- [@video@Word Break (LeetCode 139)](https://www.youtube.com/watch?v=hK6Git1o42c)
- [@video@Word Break - LeetCode 139 - Python](https://www.youtube.com/watch?v=TK9pptFzH-A)

## Word Ladder

# Word Ladder

Given a start word and an end word, find the shortest transformation sequence where each step changes exactly one letter and every intermediate word must exist in a given word list. BFS gives the shortest path, and each word's neighbors are found by replacing each character with every letter. This is the hardest graph problem in this stage and teaches you to model an abstract problem as a shortest-path graph problem.

Visit the following resources to learn more:

- [@article@Word Ladder](https://leetcode.com/problems/word-ladder/)
- [@video@Word Ladder (LeetCode 127) | Interview Essential](https://www.youtube.com/watch?v=kFKcWYCUpBg)
- [@video@Word Ladder | Leetcode #127](https://www.youtube.com/watch?v=ZVJ3asMoZ18)

## Word Search Ii

# Word Search II

Given a board of characters and a list of words, return all words that exist in the board. You build a trie from the word list and do DFS from each cell, pruning paths that do not match any trie prefix. This problem is the hardest trie problem in this stage and teaches you how a trie dramatically reduces the search space compared to checking each word separately.

Visit the following resources to learn more:

- [@article@Word Search II](https://leetcode.com/problems/word-search-ii/)
- [@video@[Java] Leetcode 212. Word Search II [Backtracking #12]](https://www.youtube.com/watch?v=IryjR5DteW4)
- [@video@Word Search II | DFS + Map | DFS + TRIE | Leetcode #212](https://www.youtube.com/watch?v=EmvsBM7o-5k)

## Word Search

# Word Search

Given a 2D grid of characters and a word, determine if the word exists in the grid by following adjacent cells. You do DFS from each cell that matches the first character, marking visited cells to avoid reuse in the current path. This problem teaches you backtracking on a 2D grid, where you must undo your visited marks when a path fails.

Visit the following resources to learn more:

- [@article@Word Search](https://leetcode.com/problems/word-search/)
- [@video@LeetCode Word Search Solution Explained - Java](https://www.youtube.com/watch?v=m9TrOL1ETxI)
- [@video@Word Search - Leetcode 79 - Recursive Backtracking (Python)](https://www.youtube.com/watch?v=Sn2DqF-S2h8)
