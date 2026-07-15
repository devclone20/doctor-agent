# Datastructures And Algorithms Roadmap

## 2 3 Trees

# Complex Data Structures

Complex data structures are advanced structures that are used for storing and organizing data in a more specialized way to manage larger amounts of data more effectively. These include Trees, Graphs, Hash Tables, and Heaps. Trees allow for hierarchical data structures and can be utilized in many ways like Binary Trees, AVL Trees etc. Graphs are networks consisting of nodes or vertices, connected by edges. Hash Tables use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. Heaps are a special case of a binary tree where the parent nodes are compared to their children with specific rules.

## A Algorithm

# A* Algorithm

## Advanced Data Structures

# Advanced Data Structures

Advanced data structures are an integral part of advanced programming. They include structures such as Binary Search Trees (BST), Balanced trees like AVL Trees, Red-Black Trees, Heap, Disjoint Data Set, Trie, Suffix Array, Suffix tree and others. BST is a node-based data structure where each node contains a key, a pointer to left child and a pointer to right child. AVL and Red-Black trees are self-balancing binary search trees. Disjoint set data structure supports union and find operations making them useful in computer vision for segmentation. Trie is an ordered tree structure used for faster retrievals, while Suffix Array and Suffix tree are data structures used in pattern matching algorithms. These structures offer an efficient way of manipulating and storing data.

## Algorithmic Complexity

# Algorithmic Complexity

"Algorithmic Complexity" refers to the computing resources needed by an algorithm to solve a problem. These computing resources can be the time taken for program execution (time complexity), or the space used in memory during its execution (space complexity). The aim is to minimize these resources, so an algorithm that takes less time and space is considered more efficient. Complexity is usually expressed using Big O notation, which describes the upper bound of time or space needs, and explains how they grow in relation to the input size. It's important to analyze and understand the algorithmic complexity to choose or design the most efficient algorithm for a specific use-case.

## Array

# Array

Visit the following resources to learn more:

- [@video@Arrays in Python](https://www.youtube.com/watch?v=gDqQf4Ekr2A&ab_channel=codebasics)
- [@video@Arrays in Java](https://www.youtube.com/watch?v=ei_4Nt7XWOw&ab_channel=BroCode)
- [@video@Arrays in Javascript](https://www.youtube.com/watch?v=yQ1fz8LY354)
- [@video@Arrays in GoLang](https://www.youtube.com/watch?v=e-oBn806Pzc&pp=ygUIYXJyYXkgZ28%3D)
- [@video@Arrays in C#](https://www.youtube.com/watch?v=YiE0oetGMAg&pp=ygUIYXJyYXkgYyM%3D)
- [@video@Arrays in C++](https://www.youtube.com/watch?v=G38hQKXa_RU&pp=ygUJYXJyYXkgYysr)
- [@video@Arrays in Rust](https://www.youtube.com/watch?v=cH6Qv47MPwk&pp=ygUKYXJyYXkgcnVzdA%3D%3D)
- [@video@Arrays in Ruby](https://www.youtube.com/watch?v=SP3Vf2KcYeU&pp=ygUKYXJyYXkgcnVieQ%3D%3D)

## Asymptotic Notation

# Asymptotic Notation

Asymptotic notation is a way to describe the limiting behavior of a function, typically representing the time or space complexity of an algorithm, as the input size grows. It focuses on the dominant terms and ignores constant factors and lower-order terms, providing a simplified and generalized way to compare the efficiency of different algorithms. Common notations include Big O, Big Omega, and Big Theta, which represent upper bound, lower bound, and tight bound, respectively.

Visit the following resources to learn more:

- [@article@Asymptotic Analysis: Big-O Notation and More](https://www.programiz.com/dsa/asymptotic-notations)
- [@article@The Big O Notation](https://towardsdatascience.com/big-o-notation-32fb458e5260/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)

## Avl Trees

# AVL Trees

An **AVL tree** is a type of binary search tree that is self-balancing, which means the heights of the two child subtrees of any node in the tree differ by at most one. If at any point the difference becomes greater than one, rebalancing is done to restore the property. The tree is named after its inventors, G.M. Adelson-Velsky and E.M. Landis, who introduced it in 1962. Each node in an AVL tree carries extra information (its Balance Factor) which could be either -1, 0, or +1. AVL trees balance themselves by rotating sub-trees in different manners(named as Left-Left rotation, Right-Right rotation, Left-Right rotation, and Right-Left rotation) whenever an insert operation causes the balance factor to go beyond this range.

Visit the following resources to learn more:

- [@video@AVL trees in 5 minutes — Intro & Search](https://www.youtube.com/watch?v=DB1HFCEdLxA)

## B Trees

# B-Trees

B-Tree is a self-balanced search tree data structure that maintains sorted data and allows for efficient insertion, deletion, and search operations. It is most commonly used in systems where read and write operations are performed on disk, such as databases and file systems. The main characteristic of a B-Tree is that all leaves are at the same level, and the internal nodes can store more than one key. Each node in a B-Tree contains a certain number of keys and pointers which navigate the tree. The keys act as separation values which divide its subtrees. For example, if a node contains the values \[10,20,30\] it has four children: the first contains values less than 10, the second contains values between 10 and 20, the third contains values between 20 and 30, and the fourth contains values greater than 30.

Visit the following resources to learn more:

- [@video@B-trees in 4 minutes — Intro](https://www.youtube.com/watch?v=FgWbADOG44s)

## Backtracking

# Backtracking

Backtracking is a powerful algorithmic technique that aims to solve a problem incrementally, by trying out an various sequences of decisions. If at any point it realizes that its current path will not lead to a solution, it reverses or "backtracks" the most recent decision and tries the next available route. Backtracking is often applied in problems where the solution requires the sequence of decisions to meet certain constraints, like the 8-queens puzzle or the traveling salesperson problem. In essence, it involves exhaustive search and thus, can be computationally expensive. However, with the right sorts of constraints, it can sometimes find solutions to problems with large and complex spaces very efficiently.

Visit the following resources to learn more:

- [@video@What is backtracking?](https://www.youtube.com/watch?v=Peo7k2osVVs)

## Basic Data Structures

# Basic Data Structures

The five main types of basic data structures are: **Arrays**, **Linked Lists**, **Stacks**, **Queues**, and **Hash Tables**.

*   **Arrays** are static data structures that store elements of the same type in contiguous memory locations.
*   **Linked Lists** are dynamic data structures that store elements in individual nodes, with each node pointing to the next.
*   **Stacks** follow the Last-In-First-Out principle (LIFO) and primarily assist in function calls in most programming languages.
*   **Queues** operate on the First-In-First-Out principle (FIFO) and are commonly used in task scheduling.
*   Lastly, **Hash Tables** store key-value pairs allowing for fast insertion, deletion, and search operations.

## Bb Trees

# B/B+ Trees

`B trees` and `B+ trees` are both types of self-balancing, sorted, tree-based data structures that maintain sorted data in a way that allows for efficient insertion, deletion, and search operations. A `B tree` is a tree data structure in which each node has multiple keys and can be in more than two children nodes. Each internal node in a `B tree` can contain a variable number of keys and pointers. The keys act as separation values which divide its subtrees. One important aspect of a `B tree` is that every key in the node also appears in the parent node. On the other hand, a `B+ tree` is an extension of a `B tree` which allows for efficient traversal of data. In a `B+ tree`, data pointers are stored only at the leaf nodes of the tree, making every leaf node of a `B+ tree` a linked list. The intermediary nodes only use the keys to aid with the search.

Visit the following resources to learn more:

- [@video@B Trees and B+ Trees. How they are useful in Databases](https://www.youtube.com/watch?v=aZjYr87r1b8)

## Bellman Ford Algoritm

# Bellman-Ford

The **Bellman Ford algorithm** is a method used in graph theory for finding the shortest path between a single source vertex and all other vertices in a weighted graph. This algorithm is significant because it is capable of handling graphs with negative weight edges, unlike Dijkstra's algorithm. It follows a bottom-up approach, filling up the distance table gradually while relaxing edges. The algorithm gets its name from its developers, Richard Bellman and Lester Ford. However, it can lead to an infinite loop if there are negative weight cycles in the graph, which should be addressed separately using another check.

## Big  Notation

# Big-Ω Notation

The Big Omega (Ω) notation is used in computer science to describe an algorithm's lower bound. Essentially, it provides a best-case analysis of an algorithm's efficiency, giving us a lower limit of the performance. If we say a function f(n) is Ω(g(n)), it means that from a certain point onwards (n0 for some constant n0), the value of g(n) is a lower bound on f(n). It implies that f(n) is at least as fast as g(n) past a certain threshold. This means that the algorithm won't perform more efficiently than the Ω time complexity suggests.

## Big  Notation

# Big-θ Notation

Big Theta (θ) notation is used in computer science to describe an asymptotic tight bound on a function. This essentially means it provides both an upper and lower bound for a function. When we say a function f(n) is θ(g(n)), we mean that the growth rate of f(n) is both bounded above and below by the function g(n) after a certain point. This is more precise than Big O and Big Omega notation, which provide only an upper and a lower bound, respectively. Big Theta notation tells us exactly how a function behaves for large input values. For example, if an algorithm has a time complexity of θ(n^2), it means the running time will increase quadratically with the input size.

## Big O Notation

# Big O Notation

"Big O" notation, officially known as O-notation, is used in computer science to describe the performance or complexity of an algorithm. Specifically, it provides an upper bound on the time complexity, describing the worst-case scenario. Thus, it gives an upper limit on the time taken for an algorithm to complete based on the size of the input. The notation is expressed as O(f(n)), where f(n) is a function that measures the largest count of steps that an algorithm could possibly take to solve a problem of size n. For instance, O(n) denotes a linear relationship between the time taken and the input size, while O(1) signifies constant time complexity, i.e., the time taken is independent of input size. Remember, Big O notation is only an approximation meant to describe the scaling of the algorithm and not the exact time taken.

Visit the following resources to learn more:

- [@article@Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [@video@Introduction to Big O Notation and Time Complexity](https://www.youtube.com/watch?v=D6xkbGLQesk)
- [@video@Big-O Notation](https://www.youtube.com/watch?v=BgLTDT03QtU)

## Binary Search Trees

# Binary Search Trees

A **Binary Search Tree** (BST) is a type of binary tree data structure where each node carries a unique key (a value), and each key/node has up to two referenced sub-trees, the left and right child. The key feature of a BST is that every node on the right subtree must have a value greater than its parent node, while every node on the left subtree must have a value less than its parent node. This property must be true for all the nodes, not just the root. Due to this property, searching, insertion, and removal of a node in a BST perform quite fast, and the operations can be done in O(log n) time complexity, making it suitable for data-intensive operations.

Visit the following resources to learn more:

- [@video@Binary Search Tree Part-1](https://youtu.be/lFq5mYUWEBk?si=GKRm1O278NCetnry)
- [@video@Binary Search Tree Part-2](https://youtu.be/JnrbMQyGLiU?si=1pfKn2akKXWLshY6)

## Binary Search

# Binary Search

`Binary Search` is a type of search algorithm that follows the divide and conquer strategy. It works on a sorted array by repeatedly dividing the search interval in half. Initially, the search space is the entire array and the target is compared with the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target, and repeating this until the target is found. If the search ends with the remaining half being empty, the target is not in the array. Binary Search is log(n) as it cuts down the search space by half each step.

Visit the following resources to learn more:

- [@video@Learn Binary Search in 10 minutes](https://www.youtube.com/watch?v=xrMppTpoqdw)

## Binary Trees

# Binary Trees

A **Binary Tree** is a type of tree data structure in which each node has at most two children, referred to as the left child and the right child. This distinguishes it from trees in which nodes can have any number of children. A binary tree is further classified as a strictly binary tree if every non-leaf node in the tree has non-empty left and right child nodes. A binary tree is complete if all levels of the tree, except possibly the last, are fully filled, and all nodes are as left-justified as possible. Multiple algorithms and functions employ binary trees due to their suitable properties for mathematical operations and data organization.

Visit the following resources to learn more:

- [@video@Binary Tree](https://youtu.be/4r_XR9fUPhQ?si=PBsRjix_Z9kVHgMM)

## Breadth First Search

# Breadth First Search

Breadth-First Search (BFS) is a searching algorithm used to traverse or search in data structures like a tree or a graph. The algorithm starts with a root node and visits the nodes in a level by level manner (i.e., visiting the ones nearest to the root first). It makes use of a queue data structure to store nodes not yet visited. A check is performed before nodes are put in the queue. This is to ensure same node is not visited twice. BFS can be used in multiple areas like finding shortest paths, serialized tree or in test case scenarios where all vertices are equally important.

## Breadth First Search

# Breadth First Search

Breadth-First Search (BFS) is a searching algorithm that's used in tree or graph data structures. It starts from the root (the topmost node in the tree) and expands all neighboring nodes at the present depth prior to moving on to nodes at the next depth level. This technique uses a queue data structure to remember to explore the next vertex or node and every edge that leads to a vertex will be explored, which ensures the discovery of every vertex reachable from the source. BFS is complete in nature, which means if the searched node is in the tree, BFS is guaranteed to find it.

## Brute Force

# Brute Force

"Brute Force" is a straightforward method to solve problems. It involves trying every possible solution until the right one is found. This technique does not require any specific skills or knowledge and the approach is directly applied to the problem at hand. However, while it can be effective, it is not always efficient since it often requires a significant amount of time and resources to go through all potential solutions. In terms of computational problems, a brute force algorithm examines all possibilities one by one until a satisfactory solution is found. With growing complexity, the processing time of brute force solutions dramatically increases leading to combinatorial explosion. Brute force is a base for complex problem-solving algorithms which improve the time and space complexity by adding heuristics or rules of thumb.

Visit the following resources to learn more:

- [@article@Brute Force Technique in Algorithms](https://medium.com/@shraddharao_/brute-force-technique-in-algorithms-34bac04bde8a)
- [@video@Brute Force Algorithm Explained With C++ Examples](https://www.youtube.com/watch?v=BYWf6-tpQ4k)

## Bubble Sort

# Bubble Sort

Bubble Sort is a simple sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. It gets its name because with each iteration the largest element "bubbles" up to its proper location. It continues this process of swapping until the entire list is sorted in ascending order. The main steps of the algorithm are: starting from the beginning of the list, compare every pair of adjacent items and swap them if they are in the wrong order, and then pass through the list until no more swaps are needed. However, despite being simple, Bubble Sort is not suited for large datasets as it has a worst-case and average time complexity of O(n²), where n is the number of items being sorted.

Visit the following resources to learn more:

- [@article@Bubble Sort Visualize](https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/)
- [@video@Bubble Sort](https://www.youtube.com/watch?v=Jdtq5uKz-w4)
- [@video@Bubble Sort](https://www.youtube.com/watch?v=p__ETf2CKY4)

## C

# C#

C# (pronounced "C sharp") is a general purpose programming language made by Microsoft. It is used to perform different tasks and can be used to create web apps, games, mobile apps, etc.

Visit the following resources to learn more:

- [@article@C# Learning Path](https://docs.microsoft.com/en-us/learn/paths/csharp-first-steps/?WT.mc_id=dotnet-35129-website)
- [@article@Introduction to C#](https://docs.microsoft.com/en-us/shows/CSharp-101/?WT.mc_id=Educationalcsharp-c9-scottha)
- [@video@C# tutorials](https://www.youtube.com/watch?v=gfkTfcpWqAY&list=PLTjRvDozrdlz3_FPXwb6lX_HoGXa09Yef)
- [@feed@Explore top posts about C#](https://app.daily.dev/tags/csharp?ref=roadmapsh)

## C

# C++

C++ is a powerful general-purpose programming language. It can be used to develop operating systems, browsers, games, and so on. C++ supports different ways of programming like procedural, object-oriented, functional, and so on. This makes C++ powerful as well as flexible.

Visit the following resources to learn more:

- [@official@Visit Dedicated C++ Roadmap](https://roadmap.sh/cpp)
- [@article@Learn Cpp](https://learncpp.com/)
- [@article@C++ Reference](https://en.cppreference.com/)
- [@feed@Explore top posts about C++](https://app.daily.dev/tags/c++?ref=roadmapsh)

## Common Runtimes

# Algorithmic Complexity

"Algorithmic Complexity" refers to the computing resources needed by an algorithm to solve a problem. These computing resources can be the time taken for program execution (time complexity), or the space used in memory during its execution (space complexity). The aim is to minimize these resources, so an algorithm that takes less time and space is considered more efficient. Complexity is usually expressed using Big O notation, which describes the upper bound of time or space needs, and explains how they grow in relation to the input size. It's important to analyze and understand the algorithmic complexity to choose or design the most efficient algorithm for a specific use-case.

## Complex Data Structures

# Complex Data Structures

Complex data structures are advanced structures that are used for storing and organizing data in a more specialized way to manage larger amounts of data more effectively. These include Trees, Graphs, Hash Tables, and Heaps. Trees allow for hierarchical data structures and can be utilized in many ways like Binary Trees, AVL Trees etc. Graphs are networks consisting of nodes or vertices, connected by edges. Hash Tables use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. Heaps are a special case of a binary tree where the parent nodes are compared to their children with specific rules.

## Constant

# Constant

Constant time complexity is denoted as O(1). This means the running time of the algorithm remains constant, regardless of the size of the input data set. Whether you're working with an array of 10 elements or 1 million, if an operation takes the same amount of time regardless of the size of the array, it is said to have a constant time complexity. For example, accessing any element in an array by index is an O(1) operation, as the access operation takes the same amount of time regardless of the position of the element in the array.

## Control Structures

# Control Structures

Control structures are fundamental elements in most programming languages that facilitate the flow of control through a program. There are three main types of control structures: Sequential, Selection and Iteration.

*   **Sequential** control structures are the default mode where instructions happen one after another.
*   **Selection** control structures (often called "conditional" or "decision" structures) allow one set of instructions to be executed if a condition is true and another if it's false. These typically include `if...else` statements.
*   **Iteration** control structures (also known as _loops_) allow a block of code to be repeated multiple times. Common loop structures include `for`, `while`, and `do...while` loops. All these control structures play a vital role in shaping the program logic.

## Cyclic Sort

# Cyclic Sort

## Depth First Search

# Depth First Search

**Depth-First Search (DFS)** is an algorithm used for traversing or searching tree or graph data structures. The process starts at the root node (selecting some arbitrary node as the root in the case of a graph), and explores as far as possible along each branch before backtracking. It uses a last in, first out (LIFO) stack to remember to get the next vertex to start a search when a dead end occurs in any iteration. DFS has been used in a variety of applications including finding connected components, topological sorting, and finding articulation points (or cut vertices) in a graph.

Visit the following resources to learn more:

- [@video@Learn Depth First Search in 7 minutes](https://youtu.be/by93qH4ACxo?si=FXcUfuwB5atV5SIY)

## Depth First Search

# Depth First Search

Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The process starts at the root (in the case of a tree) or an arbitrary node (in case of a graph), and explores as far as possible along each branch before retracing steps. Essentially, DFS is about diving deep into the tree/graph from a starting point, and when no more nodes are left to explore, it backtracks, moving up the tree/graph. This repeat until all nodes have been visited. This algorithm is often used in simulation of game states, solving puzzles and finding connected components in a graph.

## Dijkstras Algorithm

# Dijkstra's Algorithm

Dijkstra's algorithm is a popular method used in computing and graph theory for finding the shortest paths between nodes in a graph. Named after Dutch computer scientist Edsger W. Dijkstra, this algorithm works by visiting vertices in the graph starting from the object's starting point and gradually spreading out until the shortest path to the desired endpoint is known. This algorithm is applicable in such situation where all the edges are non-negative. Linear data structures such as stacks and queues are commonly used in the implementation of this algorithm. Although its worst-case time complexity appears to be high (O(|V|^2)), it runs significantly faster in practice.

## Directed Graph

# Directed Graph

A **Directed Graph**, also known as a DiGraph, is a set of vertices and a collection of directed edges. Each directed edge has an initial vertex, also called the tail, and a terminal vertex, also known as the head. The directed edge is said to point from the tail to the head. To visualize this, think of a graph where the nodes are cities and the edges are one-way roads. Directed graphs are often used to represent relationships between objects where direction does matter, such as a sequence of events in a workflow.

## Disjoint Set Union Find

# Disjoint Set (Union-Find)

A **disjoint-set** data structure, also called a union-find data structure or merge-find set, is a data structure that tracks a partition of a set into numerous non-overlapping subsets. It provides near-constant-time operations to add new sets, to merge existing sets, and to determine whether elements are in the same set. The underlying algorithm uses two main techniques, `Union by Rank` and `Path Compression`, to achieve the efficient time complexity. Each element is represented as a node, and each group of disjoint sets forms a tree structure. Disjoint sets are useful in multitude of graph algorithms like Kruskal’s algorithm and many more.

## Divide And Conquer

# Divide and Conquer

Divide and conquer is a powerful algorithm design technique that solves a problem by breaking it down into smaller and easier-to-manage sub-problems, until these become simple enough to be solved directly. This approach is usually carried out recursively for most problems. Once all the sub-problems are solved, the solutions are combined to give a solution to the original problem. It is a common strategy that significantly reduces the complexity of the problem.

Visit the following resources to learn more:

- [@video@Divide & Conquer Algorithm In 3 Minutes](https://www.youtube.com/watch?v=YOh6hBtX5l0)

## Dynamic Programming

# Dynamic Programming

**Dynamic Programming** is a powerful problem-solving method that solves complex problems by breaking them down into simpler subproblems and solving each subproblem only once, storing their results using a memory-based data structure (like an array or a dictionary). The principle of dynamic programming is based on _Bellman's Principle of Optimality_ which provides a method to solve optimization problems. In practical terms, this approach avoids repetitive computations by storing the results of expensive function calls. This technique is widely used in optimization problems where the same subproblem may occur multiple times. Dynamic Programming is used in numerous fields including mathematics, economics, and computer science.

Visit the following resources to learn more:

- [@article@Getting Started with Dynamic Programming in Data Structures and Algorithms](https://medium.com/@PythonicPioneer/getting-started-with-dynamic-programming-in-data-structures-and-algorithms-126c7a16775c)
- [@video@What Is Dynamic Programming and How To Use It](https://www.youtube.com/watch?v=vYquumk4nWw&t=4s)
- [@video@5 Simple Steps for Solving Dynamic Programming Problems](https://www.youtube.com/watch?v=aPQY__2H3tE)

## Edabit

# Edabit

[Edabit](https://edabit.com/) is an online platform designed to improve coding skills for various programming languages like JavaScript, Python, C#, PHP, Java, Swift, Ruby, and C++. This platform is centered around practice and engagement, through interactive challenges that assist in learning the syntax, structure, and basic concepts of the aforementioned languages. Edabit does not just provide the solution but the process, showcasing different approaches to solving the challenges. For each challenge, it represents the difficulty level and assigned category, allowing users to choose and practice according to proficiency level and need.

## Exponential

# Exponential

Exponential time complexity is denoted as `O(2^n)`, where a growth in `n` leads to an exponential growth in the number of steps required to complete a task. It means that the time complexity will double with every additional element in the input set. This is seen in many recursive algorithms, where a problem is divided into two sub-problems of the same type. Examples of such algorithms include the naive recursive approach for the Fibonacci sequence or the Towers of Hanoi problem. Although exponential time complexity solutions are often simpler to implement, they are inefficient for larger input sizes.

## Factorial

# Factorial

Factorial, often denoted as `n!`, is a mathematical operation. In the context of computer science and algorithm complexity, it represents an extremely high growth rate. This occurs because of the way a factorial is calculated: The product of all positive integers less than or equal to a non-negative integer `n`. Thus, if an algorithm has a complexity of O(n!), it means the running time increases factorially based on the size of the input data set. That is, for an input of size `n`, the algorithm does `n` \* `(n-1)` \* `(n-2)` \* ... \* `1` operations. O(n!) is essentially the worst case scenario of complexity for an algorithm and is seen in brute-force search algorithms, such as the traveling salesman problem via brute-force.

## Fast And Slow Pointers

# Fast and Slow Pointers

## Fenwick Trees

# Fenwick Trees

Fenwick Trees, also known as Binary Indexed Trees, are data structures that can efficiently support the operation of updating elements and calculating prefix sums in a table of numbers. This makes it particularly useful in situations where the table gets updated often and different kinds of queries (such as sum of elements) need to be answered fast. A Fenwick Tree typically takes O(log n) time for both updation and query operations, which is more efficient than an array or a segment tree. It achieves this efficiency by storing partial sum information in the array. This allows for efficient calculation of sum ranges, with the operation of adding an element and getting the sum of a range both achieve in O(log n) time.

## Functions

# Functions

Functions in programming are named sections of a program that perform a specific task. They allow us to write a piece of code once and reuse it in different places throughout the program, making our code more modular and easier to maintain. Functions often take in input, do something with it, and return output. Functions can be categorized into four main types:

*   **Built-in** functions: provided by the programming language, like `print()` in Python.
*   **User-defined** functions: written by the user for a specific use case.
*   **Anonymous** functions: also known as lambda functions, which are not declared using the standard keyword (`def` in Python, for example).
*   **Higher-order** functions: functions that take other functions as arguments or return a function.

## Go

# Go

Go is an open source programming language supported by Google. Go can be used to write cloud services, CLI tools, used for API development, and much more.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Go Roadmap](https://roadmap.sh/golang)
- [@official@A Tour of Go – Go Basics](https://go.dev/tour/welcome/1)
- [@official@Go Reference Documentation](https://go.dev/doc/)
- [@article@Go by Example - annotated example programs](https://gobyexample.com/)
- [@article@Making a RESTful JSON API in Go](https://thenewstack.io/make-a-restful-json-api-go/)
- [@article@Go, the Programming Language of the Cloud](https://thenewstack.io/go-the-programming-language-of-the-cloud/)
- [@feed@Explore top posts about Golang](https://app.daily.dev/tags/golang?ref=roadmapsh)

## Graph Data Structures

# Graph Data Structure

A **Graph Data Structure** consists of a set of vertices (or nodes) and edges where each edge connects a pair of vertices. It can be visualized as networks consisting of elements in interconnected various relationships. There are two major types of graphs: Directed and Undirected. In a directed graph, all the edges are unidirectional - they only go one way. On the other hand, in an undirected graph, the edges are not directed - they are bidirectional. Another concept important to graphs is the idea of 'Weighted' and 'Unweighted' graphs. In a weighted graph, each edge is assigned a weight or cost. Unweighted graphs don't have these extra edge information. Graphs have a diverse set of applications in computer science, from creating connections between web pages to modeling networks and much more.

## Greedy Algorithms

# Greedy Algorithms

Greedy algorithms follow the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. They are used for optimization problems. An optimal solution is one where the value of the solution is either maximum or minimum. These algorithms work in a " greedy" manner by choosing the best option at the current, disregarding any implications on the future steps. This can lead to solutions that are less optimal. Examples of problems solved by greedy algorithms are Kruskal's minimal spanning tree algorithm, Dijkstra's shortest path algorithm, and the Knapsack problem.

Visit the following resources to learn more:

- [@video@Greedy Algorithms Tutorial ](https://www.youtube.com/watch?v=bC7o8P_Ste4)

## Hash Tables

# Hash Tables

`Hash Tables` are specialized data structures that allow fast access to data based on a key. Essentially, a hash table works by taking a key input, and then computes an index into an array in which the desired value can be found. It uses a hash function to calculate this index. Suppose the elements are integers and the hash function returns the value at the unit's place. If the given key is 22, it will check the value at index 2. Collisions occur when the hash function returns the same output for two different inputs. There are different methods to handle these collisions such as chaining and open addressing.

Visit the following resources to learn more:

- [@video@Hash Table](https://www.youtube.com/watch?v=KEs5UyBJ39g&ab_channel=takeUforward)
- [@video@Python Hash Table Part 1](https://www.youtube.com/watch?v=ea8BRGxGmlA)
- [@video@Python Hash Table Part 2](https://www.youtube.com/watch?v=54iv1si4YCM)

## Heap Sort

# Heap Sort

Heap Sort is an efficient, comparison-based sorting algorithm. It utilizes a data structure known as a 'binary heap', and works by dividing its input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region. It's an in-place algorithm but not a stable sort. It involves building a Max-Heap, which is a specialized tree-based data structure, and then swapping the root node (maximum element) with the last node, reducing the size of heap by one and heapifying the root node. The maximum element is now at the end of the list and this step is repeated until all nodes are sorted. Heap Sort offers a good worst-case runtime of O(n log n), irrespective of the input data.

Visit the following resources to learn more:

- [@article@Heap Sort Visualize](https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/tutorial/)
- [@video@Heap sort in 4 minutes](https://www.youtube.com/watch?v=2DmK_H7IdTo)

## Heap

# Heap

A heap is a type of data structure in computer science that is like a tree, where each parent node is always bigger (in a max heap) or smaller (in a min heap) than its child nodes.

Visit the following resources to learn more:

- [@article@Heap Data Structure](https://www.programiz.com/dsa/heap-data-structure)
- [@video@Heap Data Structure](https://www.youtube.com/watch?v=t0Cq6tVNRBA)
- [@video@Heaps and Priority Queues](https://www.youtube.com/watch?v=B7hVxCmfPtM)

## How To Calculate Complexity

# How to Calculate Complexity?

The process of calculating algorithmic complexity, often referred to as Big O notation, involves counting the operations or steps an algorithm takes in function of the size of its input. The aim is to identify the worst-case, average-case, and best-case complexity. Generally, the main focus is on the worst-case scenario which represents the maximum number of steps taken by an algorithm. To calculate it, you consider the highest order of size (n) in your algorithm's steps. For instance, if an algorithm performs a loop 5 times for 'n' items, and then does 3 unrelated steps, it has a complexity of O(n), because the linear steps grow faster than constant ones as n increases. Other complexities include O(1) for constant complexity, O(n) for linear complexity, O(n^2) for quadratic complexity, and so on, based on how the steps increase with size.

Visit the following resources to learn more:

- [@video@Time & Space Complexity](https://www.youtube.com/watch?v=Z0bH0cMY0E8)
- [@video@How Write and Analyze Algorithm](https://www.youtube.com/watch?v=xGYsEqe9Vl0)

## In Order Traversal

# In-Order Traversal

In order traversal is a method for traversing binary trees. This method follows a specific order: Left Node, Root Node, then Right Node (L-N-R). Starting from the leftmost node of the tree, you first visit the left subtree, then the root node, and finally the right subtree. If the tree is a binary search tree, in order traversal will output the values of the nodes in the tree in ascending order. This traversal method is recursive in nature, as it requires each subtree to be visited in the exact same way.

## Indexing

# Indexing

Indexing is a data structure technique to efficiently retrieve data from a database. It essentially creates a lookup that can be used to quickly find the location of data records on a disk. Indexes are created using a few database columns and are capable of rapidly locating data without scanning every row in a database table each time the database table is accessed. Indexes can be created using any combination of columns in a database table, reducing the amount of time it takes to find data.

Indexes can be structured in several ways: Binary Tree, B-Tree, Hash Map, etc., each having its own particular strengths and weaknesses. When creating an index, it's crucial to understand which type of index to apply in order to achieve maximum efficiency. Indexes, like any other database feature, must be used wisely because they require disk space and need to be maintained, which can slow down insert and update operations.

## Insertion Sort

# Insertion Sort

Visit the following resources to learn more:

- [@course@Insertion Sort](https://youtu.be/JU767SDMDvA)
- [@article@Insertion Sort Visualization](https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/)

## Isam

# ISAM

ISAM, which stands for Indexed Sequential Access Method, is a type of disk storage access method developed by IBM. It combines features of both sequential and direct access methods to store and retrieve data. ISAM primarily organizes data sequentially but creates an index to provide direct access to the data blocks. This index allows for quick retrieval of data records, improving efficiency and performance. A key feature of ISAM is that it maintains the data sequence even after insertions and deletions, ensuring that the data remains ordered for efficient processing.

Visit the following resources to learn more:

- [@video@DBMS - Index Sequential Access Method (ISAM)](https://www.youtube.com/watch?v=EiW1VVPor10)

## Island Traversal

# Island traversal

## Java

# Java

Java is general-purpose language, primarily used for Internet-based applications. It was created in 1995 by James Gosling at Sun Microsystems and is one of the most popular options for backend developers.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Java Roadmap](https://roadmap.sh/java)
- [@official@Java Website](https://www.java.com/)
- [@video@Java Crash Course](https://www.youtube.com/watch?v=eIrMbAQSU34)
- [@video@Complete Java course](https://www.youtube.com/watch?v=xk4_1vDrzzo)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Javascript

# JavaScript

JavaScript allows you to add interactivity to your pages. Common examples that you may have seen on the websites are sliders, click interactions, popups and so on. Apart from being used on the frontend in browsers, there is Node.js which is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@article@The Modern JavaScript Tutorial](https://javascript.info/)
- [@article@Official Documentation](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [@video@JavaScript Crash Course for Beginners](https://youtu.be/hdI2bqOjy3c)
- [@video@Node.js Crash Course](https://www.youtube.com/watch?v=fBNz5xF-Kx4)
- [@video@Node.js Tutorial for Beginners](https://www.youtube.com/watch?v=TlB_eWDSMt4)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Kruskals Algorithm

# Kruskal's Algorithm

Kruskal's algorithm is a popular procedure in computer science for finding minimum spanning trees in a graph, developed by Joseph Kruskal in 1956. The algorithm operates by sorting the edges of the graph by their weight in ascending order. Then, it loops through each, adding the edge to the spanning tree if it doesn't form a circuit with the edges already there. This process repeats until all the vertices in the graph are included in the tree. Kruskal's algorithm belongs to the group of Greedy Algorithms as it tries to find the local optimum at each stage with the hope of finding the global optimum. It has an overall time complexity of O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.

## Kth Element

# Kth Element

## Language Syntax

# Language Syntax

Language syntax refers to the set of rules that dictate how programs written in a particular programming language must be structured. This can include rules for how to declare variables, how to call functions, how to structure control flow statements, and so on. Syntax varies significantly between different programming languages, so it is critical to grasp the specific syntax of the language you are using. It’s similar to grammar in human languages - putting words in the wrong order or including extraneous punctuation can make a sentence hard to understand, and the same applies to programming. Incorrect syntax leads to syntax errors which prevent your code from executing.

Learn the language syntax of the programming language you are using.

## Leetcode

# Leetcode

[LeetCode](https://leetcode.com/) is a widely recognized online platform used for preparing coding interviews and improving problem-solving skills. It offers a vast collection of programming challenges that can be solved in multiple programming languages. The problems are categorized by difficulty level, and each problem has a solution provided by the community. LeetCode also provides a discussion board for each problem where users can discuss solutions, optimized ideas, and their thoughts. It also features mock interviews, articles, and a strong community of programmers to engage and learn from.

## Linear Search

# Linear Search

Linear search is one of the simplest search algorithms. In this method, every element in an array is checked sequentially starting from the first until a match is found or all elements have been checked. It is also known as sequential search. It works on both sorted and unsorted lists, and does not need any preconditioned list for the operation. However, its efficiency is lesser as compared to other search algorithms since it checks all elements one by one.

Visit the following resources to learn more:

- [@video@Learn Linear Search in 3 minutes](https://www.youtube.com/watch?v=246V51AWwZM)

## Linear

# Linear Indexing

Linear indexing is a type of data structure method where each element of an array is indexed successively in a linear format. This method treats multi-dimensional arrays as a long vector and provides a simple way to traverse through all the elements of the array in a sequence without the need for multiple loop statements. For instance, in a 2D array, the first index refers to rows and the second to columns. Using linear indexing, elements are indexed from top left to bottom right moving row by row. Despite its simplicity, this method is often less efficient than other forms of indexing for multidimensional arrays.

## Linear

# Linear

Linear time complexity, denoted as O(n), is one of the best possible algorithmic performance situations. An algorithm is said to have a linear time complexity when the running time increases at most linearly with the size of the input data. This means that if you double the size of the input, the running time will at most double as well. In an ideal situation, every single element in the data set should be viewed exactly once. Sorting algorithms such as counting sort and bucket sort have linear time complexity under certain conditions.

## Linked Lists

# Linked Lists

Linked Lists are a type of data structure used for storing collections of data. The data is stored in nodes, each of which contains a data field and a reference (link) to the next node in the sequence. Structurally, a linked list is organized into a sequence or chain of nodes, hence the name. Two types of linked lists are commonly used: singly linked lists, where each node points to the next node and the last node points to null, and doubly linked lists, where each node has two links, one to the previous node and another one to the next. Linked Lists are used in other types of data structures like stacks and queues.

Visit the following resources to learn more:

- [@video@Introduction To Linked List](https://youtu.be/Nq7ok-OyEpg?si=xttaGoYKcoJ09Ln2)
- [@video@Python Linked List](https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=4&ab_channel=codebasics)

## Logarithmic

# Logarithmic

Logarithmic time complexity (O(log n)) often indicates that the algorithm halves the size of the input at each step. It's more efficient compared to linear time complexity. Binary search is a classic example of logarithmic time complexity where at every step, the algorithm breaks the list into half until it finds the desired element. As the size of the input increases, the growth of the time taken by an algorithm with logarithmic complexity grows slowly because it divides the problem into smaller parts in each step.

## Merge Intervals

# Merge Intervals

## Merge Sort

# Merge Sort

**Merge sort** is a type of sorting algorithm that follows the divide-and-conquer paradigm. It was invented by John von Neumann in 1945. This algorithm works by dividing an unsorted list into `n` partitions, each containing one element (a list of one element is considered sorted), then repeatedly merging partitions to produce new sorted lists until there is only 1 sorted list remaining. This resulting list is the fully sorted list. The process of dividing the list is done recursively until it hits the base case of a list with one item. Merge sort has a time complexity of `O(n log n)` for all cases (best, average and worst), which makes it highly efficient for large data sets.

Visit the following resources to learn more:

- [@article@Merge Sort Visualize](https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/)
- [@video@Merge Sort](https://www.youtube.com/watch?v=4VqmGXwpLqc)

## Minimum Spanning Tree

# Graph Data Structure

A **Graph Data Structure** consists of a set of vertices (or nodes) and edges where each edge connects a pair of vertices. It can be visualized as networks consisting of elements in interconnected various relationships. There are two major types of graphs: Directed and Undirected. In a directed graph, all the edges are unidirectional - they only go one way. On the other hand, in an undirected graph, the edges are not directed - they are bidirectional. Another concept important to graphs is the idea of 'Weighted' and 'Unweighted' graphs. In a weighted graph, each edge is assigned a weight or cost. Unweighted graphs don't have these extra edge information. Graphs have a diverse set of applications in computer science, from creating connections between web pages to modeling networks and much more.

## Multi Threaded

# Multi-threaded

## Oop Basics

# OOP Basics

Object-oriented programming (OOP) is a programming paradigm that uses "objects" to design applications and software. In OOP, each object is an instance of a class. A class defines the properties (often known as attributes or fields) and methods (actions) that are common to all objects of a certain kind. A key principle of OOP is the ability to hide certain parts of the objects’ data from the outside, a concept known as encapsulation. Other key principles are inheritance, a way to form new classes using classes that have already been defined, and polymorphism, the concept of designing objects to share behaviors and being able to override shared behaviors with specifics.

Visit the following resources to learn more:

- [@video@Object-Oriented Programming (Simplified)](https://youtu.be/pTB0EiLXUC8?si=I8rV2K5fhpoqmixX)

## Pick A Language

# Pick a Language

Pick a programming language to practice data structures and algorithms with. You should pick a language that you are comfortable with or plan to adopt.

## Platforms To Practice

# Platforms for Practice

There are numerous platforms for practicing data structures and algorithms. Some of the notable ones include LeetCode, with a vast collection of challenges and a robust community, and HackerRank, which provides a diverse set of problems and hosts competitive coding contests. Other platforms such as CodeChef, AtCoder, and TopCoder also host contests and have a vast problemset archive. For those interested in learning through problem-solving and real-world coding, platforms like Project Euler and CodeSignal could be more appealing. Practice can also be undertaken through interactive platforms like Codewars and Exercism, which offer gamified experiences. Another option is InterviewBit, which provides problems contextualized within interview scenarios. These platforms cover a broad range of difficulty levels and languages, offering a comprehensive practice environment for beginners and experts alike.

## Polynomial

# Polynomial

Polynomial time complexity, denoted as O(n^k), is a class of time complexity that represents the amount of time an algorithm takes to run as being proportional to the size of the input data raised to a constant power 'k'. Polynomial time complexity includes runtimes like O(n), O(n^2), O(n^3), etc. The value 'n' is a representation of the size of the input, while 'k' represents a constant. Algorithms running in polynomial time are considered to be reasonably efficient for small and medium-sized inputs, but can become impractical for large input sizes due to the rapid growth rate of function.

## Post Order Traversal

# Post-Order Traversal

Post Order Traversal is a technique used in Binary Tree structure where each node is processed after its child nodes. As the name suggests, it first traverses the left subtree, then the right subtree, and finally the root node. The process is recursively repeated for each subtree until the entire tree has been traversed. This traversal method is often used for calculations that require that all child nodes be processed before the parent, such as evaluating a mathematical expression represented in a tree structure.

## Pre Order Traversal

# Pre-Order Traversal

Pre Order Traversal is a very specific kind of tree traversal in data structures. In this method of traversal, the process starts from the root node, then proceeds to the left subtree, and finally to the right subtree. To put it concisely, the order of traversal is Root, Left, and Right (often abbreviated as R-L-R). This makes it particularly useful in scenarios where it's important to duplicate or clone a tree, or to get a prefix expression (Polish notation) of a binary expression tree.

## Prims Algorithm

# Prim's Algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.

## Problem Solving Techniques

# Problem Solving Techniques

"Problem Solving Techniques" is a topic that explore various methods used to solve problems in computing and mathematics. They are approaches and procedures that help in the systematic identification and resolution of complex issues. Some of these techniques include "Divide and Conquer" where a problem is split into subproblems to make it easier to solve, "Dynamic Programming" which solves problems by dividing them into smaller similar sub-problems and storing the solutions of these subproblems to avoid unnecessary calculations, "Greedy Algorithms" which make the globally optimal choice at each step, "Backtracking" is used when problem can be solved incrementally, "Branch and Bound" method is used for optimization problems. These techniques are designed to efficiently solve problems by significantly reducing the time and computational effort required.

## Programming Fundamentals

# Programming Fundamentals

Programming Fundamentals are the basic concepts and principles that form the foundation of any computer programming language. These include understanding variables, which store data for processing, control structures such as loops and conditional statements that direct the flow of a program, data structures which organize and store data efficiently, and algorithms which step by step instructions to solve specific problems or perform specific tasks. Mastery of these fundamentals forms the basis for learning any specific programming language and for writing efficient, effective code.

## Pseudo Code

# Pseudo Code

Pseudo code is a plain language description of the steps in an algorithm or another system. It is intended for human reading rather than machine reading. Pseudo code often uses control structures and terms common to popular high-level programming languages without strictly adhering to the syntax of any particular one. The foremost aim of pseudocode is to explain the inner "algorithmic thinking" behind coding, rather than focusing on the syntax of a particular language. A nice feature of pseudocode is that it is largely able to be understood by a wider range of people than the corresponding code in a specific programming language, which enhances its roles in drafting, documentation, learning, and collaboration aspects.

## Python

# Python

Python is a well known programming language which is both a strongly typed and a dynamically typed language. Being an interpreted language, code is executed as soon as it is written and the Python syntax allows for writing code in functional, procedural or object-oriented programmatic ways.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Python Roadmap](https://roadmap.sh/python)
- [@official@Python Website](https://www.python.org/)
- [@official@Python Getting Started](https://www.python.org/about/gettingstarted/)
- [@article@Automate the Boring Stuff](https://automatetheboringstuff.com/)
- [@article@Python principles - Python basics](https://pythonprinciples.com/)
- [@article@Python Crash Course](https://ehmatthes.github.io/pcc/)
- [@article@An Introduction to Python for Non-Programmers](https://thenewstack.io/an-introduction-to-python-for-non-programmers/)
- [@article@Getting Started with Python and InfluxDB](https://thenewstack.io/getting-started-with-python-and-influxdb/)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## Queues

# Queues

Queues are a type of data structure in which elements are held in a sequence and access is restricted to one end. Elements are added ("enqueued") at the rear end and removed ("dequeued") from the front. This makes queues a First-In, First-Out (FIFO) data structure. This type of organization is particularly useful for specific situations such as printing jobs, handling requests in a web server, scheduling tasks in a system, etc. Due to its FIFO property, once a new element is inserted into the queue, all elements that were inserted before the new element must be removed before the new element can be invoked. The fundamental operations associated with queues include Enqueue (insert), Dequeue (remove) and Peek (get the top element).

Visit the following resources to learn more:

- [@video@Queue](https://www.youtube.com/watch?v=M6GnoUDpqEE)
- [@video@Python Queue](https://www.youtube.com/watch?v=rUUrmGKYwHw)

## Quick Sort

# Quick Sort

Quicksort, also known as partition-exchange sort, is an efficient, in-place sorting algorithm, which uses divide and conquer principles. It was developed by Tony Hoare in 1959. It operates by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. This process continues until the base case is achieved, which is when the array or sub-array has zero or one element, hence is already sorted. Quicksort can have worst-case performance of O(n^2) if the pivot is the smallest or the largest element in the array, although this scenario is rare if the pivot is chosen randomly. The average case time complexity is O(n log n).

Visit the following resources to learn more:

- [@article@Quick Sort Visualize](https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/visualize/)
- [@video@A Complete Overview of Quicksort](https://www.youtube.com/watch?v=0SkOjNaO1XY)
- [@video@QuickSort](https://www.youtube.com/watch?v=7h1s2SojIRw)
- [@video@QuickSort Analysis](https://www.youtube.com/watch?v=-qOVVRIZzao)

## Randomised Algorithms

# Randomised Algorithms

Randomised algorithms are a type of algorithm that employs a degree of randomness as part of the logic of the algorithm. These algorithms use random numbers to make decisions, and thus, even for the same input, can produce different outcomes on different executions. The correctness of these algorithms are probabilistic and they are particularly useful when dealing with a large input space. There are two major types of randomised algorithms: Las Vegas algorithms, which always give the correct answer, but their running time is a random variable; and Monté Carlo algorithms, where the algorithm has a small probability of viability or accuracy.

Visit the following resources to learn more:

- [@video@Algorithm Classification Randomized Algorithm](https://www.youtube.com/watch?v=J_EVG6yCOz0)

## Recursion

# Recursion

Recursion is a method where the solution to a problem depends on solutions to shorter instances of the same problem. It involves a function calling itself while having a condition for its termination. This technique is mostly used in programming languages like C++, Java, Python, etc. There are two main components in a recursive function: the base case (termination condition) and the recursive case, where the function repeatedly calls itself. All recursive algorithms must have a base case to prevent infinite loops. Recursion can be direct (if a function calls itself) or indirect (if the function A calls another function B, which calls the first function A).

Visit the following resources to learn more:

- [@video@Recursion in 100 Seconds](https://www.youtube.com/watch?v=rf60MejMz3E)

## Ruby

# Ruby

Ruby is a high-level, interpreted programming language that blends Perl, Smalltalk, Eiffel, Ada, and Lisp. Ruby focuses on simplicity and productivity along with a syntax that reads and writes naturally. Ruby supports procedural, object-oriented and functional programming and is dynamically typed.

Visit the following resources to learn more:

- [@official@Ruby Website](https://www.ruby-lang.org/en/)
- [@article@Learn Ruby in 20 minutes](https://www.ruby-lang.org/en/documentation/quickstart/)
- [@article@Ruby, An Introduction to a Programmer’s Best Friend](https://thenewstack.io/ruby-a-programmers-best-friend/)
- [@feed@Explore top posts about Ruby](https://app.daily.dev/tags/ruby?ref=roadmapsh)

## Rust

# Rust

Rust is a modern systems programming language focusing on safety, speed, and concurrency. It accomplishes these goals by being memory safe without using garbage collection.

Visit the following resources to learn more:

- [@article@The Rust Programming Language - online book](https://doc.rust-lang.org/book/)
- [@article@Rust by Example - collection of runnable examples](https://doc.rust-lang.org/stable/rust-by-example/index.html)
- [@article@Rust vs. Go: Why They’re Better Together](https://thenewstack.io/rust-vs-go-why-theyre-better-together/)
- [@article@Rust by the Numbers: The Rust Programming Language in 2021](https://thenewstack.io/rust-by-the-numbers-the-rust-programming-language-in-2021/)
- [@feed@Explore top posts about Rust](https://app.daily.dev/tags/rust?ref=roadmapsh)

## Search Algorithms

# Graph Data Structure

A **Graph Data Structure** consists of a set of vertices (or nodes) and edges where each edge connects a pair of vertices. It can be visualized as networks consisting of elements in interconnected various relationships. There are two major types of graphs: Directed and Undirected. In a directed graph, all the edges are unidirectional - they only go one way. On the other hand, in an undirected graph, the edges are not directed - they are bidirectional. Another concept important to graphs is the idea of 'Weighted' and 'Unweighted' graphs. In a weighted graph, each edge is assigned a weight or cost. Unweighted graphs don't have these extra edge information. Graphs have a diverse set of applications in computer science, from creating connections between web pages to modeling networks and much more.

## Search Algorithms

# Tree Data Structures

A **Tree data structure** is a type of non-linear, hierarchical data structure that consists of nodes connected by edges. It follows the parent-child relationship, with the top node being called the root. Each node in a tree can have child nodes and each of these child nodes has a single parent node. Nodes with same parents are known as siblings. Nodes without any children are referred to as leaves. Its structure allows the organization of data in a natural hierarchy. The simplification it provides in accessing, managing and manipulating data with complex relationships makes it a vital data structure in computer science. Implementations of the tree data structure are seen in databases, file systems, and HTML DOM.

## Search Algorithms

# Search Algorithms

Search algorithms are techniques used for finding a specific item or group of items among a collection of data. The primary types of search algorithms are linear search, binary search, depth-first search, and breadth-first search. Linear and binary search are explained in this section. The other two types in a next section of this roadmap.

## Segment Trees

# Segment Trees

A **Segment Tree** is a data structure designed for efficient processing of range queries and updates on array elements. In a situation where you have an array and you need to execute several types of queries including updating array elements and computing sum or minimum or maximum of elements in a given range, segment trees could be a great choice. The tree itself is a height-balanced binary tree and is filled with data from the input array. The leaves of the Segment Tree contain the array elements, while the internal nodes store information needed for processing the query, often the sum, minimum, or maximum of the elements represented by their child nodes. Efficient implementation of segment trees can achieve query and update operations in logarithmic time.

## Selection Sort

# Selection Sort

Selection Sort is a simple and intuitive sorting algorithm. It works by dividing the array into two parts - sorted and unsorted. Initially, the sorted part is empty and the unsorted part contains all the elements. The algorithm repeatedly selects the smallest (or largest, if sorting in descending order) element from the unsorted part and moves that to the end of the sorted part. The process continues until the unsorted part becomes empty and the sorted part contains all the elements. Selection sort is not efficient on large lists, as its time complexity is O(n²) where n is the number of items.

Visit the following resources to learn more:

- [@article@Selection Sort Visualize](https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/practice-problems/)
- [@video@Selection sort in 3 minutes](https://www.youtube.com/watch?v=g-PGLbMth_g&t=5s)

## Shortest Path Algorithms

# Graph Data Structure

A **Graph Data Structure** consists of a set of vertices (or nodes) and edges where each edge connects a pair of vertices. It can be visualized as networks consisting of elements in interconnected various relationships. There are two major types of graphs: Directed and Undirected. In a directed graph, all the edges are unidirectional - they only go one way. On the other hand, in an undirected graph, the edges are not directed - they are bidirectional. Another concept important to graphs is the idea of 'Weighted' and 'Unweighted' graphs. In a weighted graph, each edge is assigned a weight or cost. Unweighted graphs don't have these extra edge information. Graphs have a diverse set of applications in computer science, from creating connections between web pages to modeling networks and much more.

## Skip List

# Skip List

A **Skip List** is a probabilistic data structure that allows efficient search, insertion, and removal operations. It is a layered list that consists of a base list holding all the elements and several lists layered on top, each layer containing a random subset of the elements from the layer below. The highest level contains only one element, the maximum. Every element in the lists is connected by a link to the element of the same value in the list below. This structure provides a balance between the speed of binary search trees and the ease of implementation of linked lists, providing an efficient means for storing data while allowing fast retrieval, even within large sets of data.

Visit the following resources to learn more:

- [@video@Skip Lists](https://www.youtube.com/watch?v=NDGpsfwAaqo)

## Sliding Window Technique

# Sliding Window Technique

The **Sliding Window Technique** is an algorithmic paradigm that manages a subset of items in a collection of objects, like an array or list, by maintaining a range of elements observed, which is referred to as the 'window'. The window 'slides' over the data to examine different subsets of its contents. This technique is often used in array-related coding problems and is particularly useful for problems that ask for maximums or minimums over a specific range within the dataset. This technique can help to greatly reduce the time complexity when dealing with problems revolving around sequential or contiguous data. Common examples of its application are in solving problems like maximum sum subarray or minimum size subsequence with a given sum.

Visit the following resources to learn more:

- [@article@Mastering Sliding Window Techniques](https://medium.com/@rishu__2701/mastering-sliding-window-techniques-48f819194fd7)
- [@video@Sliding window technique](https://www.youtube.com/watch?v=p-ss2JNynmw)

## Sorting Algorithms

# Sorting Algorithms

Sorting algorithms are used to rearrange a given array or list elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of element in the respective data structure. For example, the numerical order is a commonly used sequence but a lexicographical order is also a commonly used sequence type. There are several types of sorting algorithms: quick sort, bubble sort, merge sort, insertion sort, selection sort, heap sort, radix sort, bucket sort among others. Each has its own properties and are suited to specific types of tasks and data.

## Stacks

# Stacks

A **stack** is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO (Last In First Out) or FILO (First In Last Out). Mainly three basic operations are performed in the stack:

1.  **Push**: adds an element to the collection.
    
2.  **Pop**: removes an element from the collection. A pop can result in stack underflow if the stack is empty.
    
3.  **Peek** or **Top**: returns the top item without removing it from the stack.
    

The basic principle of stack operation is that in a stack, the element that is added last is the first one to come off, thus the name "Last in First Out".

Visit the following resources to learn more:

- [@article@Leetcode](https://leetcode.com/problems/valid-parentheses/)
- [@video@Stacks](https://www.youtube.com/watch?v=GYptUgnIM_I&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=69&ab_channel=takeUforward)
- [@video@Stack Data Structure Tutorial](https://www.youtube.com/watch?v=O1KeXo8lE8A)
- [@video@Python Stacks](https://www.youtube.com/watch?v=zwb3GmNAtFk)

## Suffix Trees And Arrays

# Suffix Trees and Arrays

**Suffix Trees and Arrays** are advanced data structures used primarily for string manipulation and searches. A **Suffix Tree** is a compressed trie containing all the suffixes of a given text as their keys and positions as their values. On the other hand, a **Suffix Array** is a sorted array of all possible suffixes of a given text. Both these data structures provide an efficient way to store and search substrings in a text, but differ in terms of space complexity and time complexity.

## Time Vs Space Complexity

# Time vs Space Complexity

In the context of algorithmic complexity, "time" refers to the amount of computational time that the algorithm takes to execute, while "space" refers to the amount of memory that the algorithm needs to complete its operation. The time complexity of an algorithm quantifies the amount of time taken by an algorithm to run, as a function of the size of the input to the program. The space complexity of an algorithm quantifies the amount of space or memory taken by an algorithm to run, as a function of the size of the input to the program. It's important to note that time and space are often at odds with each other; optimizing an algorithm to be quicker often requires taking up more memory, and decreasing memory usage can often make the algorithm slower. This is known as the space-time tradeoff.

Visit the following resources to learn more:

- [@article@Cheat Sheet](https://www.bigocheatsheet.com/)
- [@video@Big O Notation — Calculating Time Complexity](https://www.youtube.com/watch?v=Z0bH0cMY0E8)
- [@video@Free Code Camp Big-O Tutorial](https://youtu.be/Mo4vesaut8g?si=1jyb-EkfCLf9PNND)

## Tree Based

# Tree-Based Indexing

Tree-based indexing involves using data structures that follow a tree-like model, with parent nodes, child nodes, and leaf nodes in a hierarchical order. Two popular tree-based indexing methods are B-tree and B+ tree. In a B-tree index, every data record is associated with a leaf node, while internal nodes can be linked to a number of lower nodes within a certain range. On the other hand, B+ tree index structure makes all records reside at the leaf level, with the internal nodes only containing key values. The path from the root to every leaf node in both B-tree and B+ tree is the same length, which allows for efficient and consistent retrieval times.

## Tree Data Structures

# Tree Data Structures

A **Tree data structure** is a type of non-linear, hierarchical data structure that consists of nodes connected by edges. It follows the parent-child relationship, with the top node being called the root. Each node in a tree can have child nodes and each of these child nodes has a single parent node. Nodes with same parents are known as siblings. Nodes without any children are referred to as leaves. Its structure allows the organization of data in a natural hierarchy. The simplification it provides in accessing, managing and manipulating data with complex relationships makes it a vital data structure in computer science. Implementations of the tree data structure are seen in databases, file systems, and HTML DOM.

## Tree Traversal

# Tree Data Structures

A **Tree data structure** is a type of non-linear, hierarchical data structure that consists of nodes connected by edges. It follows the parent-child relationship, with the top node being called the root. Each node in a tree can have child nodes and each of these child nodes has a single parent node. Nodes with same parents are known as siblings. Nodes without any children are referred to as leaves. Its structure allows the organization of data in a natural hierarchy. The simplification it provides in accessing, managing and manipulating data with complex relationships makes it a vital data structure in computer science. Implementations of the tree data structure are seen in databases, file systems, and HTML DOM.

## Trie

# Trie

A **Trie**, also called digital tree and sometimes radix tree or prefix tree, is a type of search tree that is used to store a dynamic set or associative array where the keys are usually strings. Unlike binary search trees, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated. All the descendants of any one node have a common prefix of the string associated with that node, and the root is associated with the empty string. A 'trie' is thus a way to represent the 're**trie**val' of information and is a type of tree structure used for this purpose. Typical usage scenarios could be in storing a predictive text or autocomplete dictionary, such as found on your smartphone or search engine.

## Two Heaps

# Two Heaps

The two heaps method uses a max-heap to store the lower half of the numbers and a min-heap to store the upper half. This setup allows you to quickly access the largest value of the lower half and the smallest value of the upper half in constant time. Insertions and deletions take logarithmic time, and the heaps are balanced so that the median can be found in O(1) time. This approach is especially useful for dynamically maintaining the median of a long or streaming data sequence, where repeatedly sorting the data would be inefficient (O(n log n) per sort).

Visit the following resources to learn more:

- [@article@Two Heaps — A Coding Pattern for Median-finding (Emre Bolat)](https://emre.me/coding-patterns/two-heaps/)
- [@video@Coding Pattern - Two Heaps](https://www.youtube.com/watch?v=9P7W5aEaatQ)

## Two Pointer Technique

# Two Pointer Technique

The **two-pointer technique** is a strategy that can be used to solve certain types of problems, particularly those that involve arrays or linked lists. This technique primarily involves using two pointers, which navigate through the data structure in various ways, depending on the nature of the problem. The pointers could traverse the array from opposite ends, or one could be moving faster than the other - often referred to as the `slow` and `fast` pointer method. This technique can greatly optimize performance by reducing time complexity, often enabling solutions to achieve O(n) time complexity.

Visit the following resources to learn more:

- [@article@Two Pointers Technique](https://medium.com/@johnnyJK/data-structures-and-algorithms-907a63d691c1)
- [@article@Mastering the Two Pointers Technique: An In-Depth Guide](https://lordkonadu.medium.com/mastering-the-two-pointers-technique-an-in-depth-guide-3c2167584ccc)
- [@video@Visual introduction Two Pointer Algorithm](https://www.youtube.com/watch?v=On03HWe2tZM)

## Undirected Graph

# Undirected Graph

An **Undirected Graph** is a type of graph in which the edges are not directed. That is, they do not point in any specific direction and are not ordered pairs. They cannot be referred to as originating or ending node, instead, they are endpoints of the edges. In this type of graph, the edges essentially represent a two-way relationship, in the sense that, a travel can be made back and forth between the two vertices without any restriction. Every edge of the undirected graph always connects two different vertices or nodes.

## What Are Data Structures

# What are Data Structures?

Data structures are specialized formats for organizing and storing data in a computer so that it can be used efficiently. They provide a means to manage large amounts of data efficiently for uses such as large databases and internet indexing services. They are critical to programming and are used in almost all software systems including web development, operating systems, image editing, and much more. Some common types of data structures are arrays, linked lists, queues, stacks, trees, and graphs. The choice of the data structure often begins from the choice of an abstract data type, a broad type encapsulating various possible data structures."

Visit the following resources to learn more:

- [@video@What an Algorithms and More(MIT)](https://youtu.be/Zc54gFhdpLA?si=F_1QRigN_h2t2nSp&t=133)
- [@video@What Are Data Structures?](https://www.youtube.com/watch?v=bum_19loj9A)
- [@video@Introduction to Algorithms](https://www.youtube.com/watch?v=0IAPZzGSbME)

## Why Are Data Structures Important

# Importance of Data Structures

Data structures are crucial in the field of computer science and coding because they offer a method of organizing and storing data in an efficient and manageable format. They're critical because they form the foundation for modern algorithm design. Your ability to choose or design the most suited data structure for a particular task can be the difference between a solution that's functional and efficient and one that isn't. They allow data to be processed in a variety of ways - stored, sorted, ordered, or accessed - which is integral to software or database development. By implementing effective data structures, programmers can enhance performance, ease coding procedures, allow flexibility of data and most importantly, reduce complexity of code in a significant manner.

Visit the following resources to learn more:

- [@video@What are Data Structures? Why is it Important?](https://www.youtube.com/watch?v=18V8Avz2OH8)
