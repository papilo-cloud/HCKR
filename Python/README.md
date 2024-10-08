# Hackerrank Archive

1. ## [Strings](#strings)
1. ## [Stacks](#stack)
3. ## [Linked List](#linkedList)
4. ## [Search](#search)
5. ## [Tree](#tree)
6. ## [Sorting](#sorting)
7. ## [Array](#array)
8. ## [Implementation](#implementation)
9. ## [Heap](#heap)


### Strings

- [Anagram](https://github.com/papilo-cloud/HCKR/blob/main/Python/strings/anagram.py) Two words are anagrams of one another if their letters can be rearranged to form the other word.

    Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

    #### Returns
    - int: the minimum number of characters to change or -1.
- [Pangrams](https://github.com/papilo-cloud/HCKR/blob/main/Python/strings/pangram.py) A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

    #### Example
    *s* = __The quick brown box jumps over the lazy dog__

    The string contains all letters in the English alphabet, so return pangram.

    #### Returns
    - It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.


### Stack

1. [Simple Text Editor](https://github.com/papilo-cloud/HCKR/blob/main/Python/stacks/simple_text_editor.py) Implement a simple text editor. The editor initially contains an empty string, __*S*__. Perform  __*Q*__ operations of the following __4__ types:

    1. append __(*W*)__ - Append string __*W*__ to the end of __*S*__.
    2. delete __(*K*)__ - Delete the last __*K*__ characters of __*S*__.
    3. print __(*K*)__ - Print the __*K<sup>th</sup>*__ character of __*S*__.
    4. undo __()__ - Undo the last (not previously undone) operation of type __1__ or __2__, reverting __*S*__ to the state it was in prior to that operation.

    #### Example
    __*S*__ = __'abcde'__
    __*ops*__ = __['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']__

2. [Balanced Brackets](https://github.com/papilo-cloud/HCKR/blob/main/Python/stacks/balanced_brackets.py) A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

    Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

    A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

    By this logic, we say a sequence of brackets is balanced if the following conditions are met:
    - It contains no unmatched brackets.
    - The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
    
    Given *n* strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return __YES__. Otherwise, return __NO__.

3. [Maximum Element](https://github.com/papilo-cloud/HCKR/blob/main/Python/stacks/max_element.py) You have an empty sequence, and you will be given __*N*__ queries. Each query is one of these three types:
    <pre>
    1 x  -Push the element x into the stack.
    2    -Delete the element present at the top of the stack.
    3    -Print the maximum element in the stack.
    </pre>
    #### Function Description

    Complete the getMax function in the editor below.

    getMax has the following parameters:
    - string operations[n]: operations as strings

    #### Returns
    - int[]: the answers to each type 3 query

4. [Equal Stacks](https://github.com/papilo-cloud/HCKR/blob/main/Python/stacks/equal_stacks.py) You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

    Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

    #### Example

    __*h*1 = [1,2,1,1]__
    __*h*2 = [1,1,2]__
    __*h*3 = [1,1]__



    There are __4, 3__ and __2__ cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from  __*h*1__ (heights = [1, 2]) and from  __*h*2__ (heights = [1, 1]) so that the three stacks all are 2 units tall. Return __2__ as the answer.

    __Note__: An empty stack is still a stack.

    #### Explanation
    Initially, the stacks look like this:

    ![image1](https://s3.amazonaws.com/hr-challenge-images/21404/1465645257-57311b88de-piles1.png)

    To equalize thier heights, remove the first cylinder from stacks  and , and then remove the top two cylinders from stack  (shown below).

    ![Image2](https://s3.amazonaws.com/hr-challenge-images/21404/1465645312-e48f85c176-piles2.png)

    The stack heights are reduced as follows:
    1. __8 - 3 = 5__
    2. __9 - 4 = 5__
    3. __7 - 1 - 1 = 5__

    All three stacks now have , the value to return.

5. [Largest Rectangle](https://github.com/papilo-cloud/HCKR/blob/main/Python/stacks/largest_rectangle.py) Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

    There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by __*h*[*i*] where *i* E [1,n]__. If you join __*k*__ adjacent buildings, they will form a solid rectangle of area __*k* x *min*(*h*[*i*],*h*[*i* + 1],....,*h*[*i* + *k* - 1])__.

    #### Example

    __*h* = [3,2,3]__

    A rectangle of height __*h* = 2__ and length __*k* = 3__ can be constructed within the boundaries. The area formed is __*h*.*k* = 2.3 = 6__.

    #### Function Description

    Complete the function <pre>largestRectangle</pre> int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

    largestRectangle has the following parameter(s):

    int h[n]: the building heights
    #### Returns
    - long: the area of the largest rectangle that can be formed within the bounds of consecutive buildings

    #### Explanation

    An explanation of the test case follows.

    ![Image](https://s3.amazonaws.com/hr-challenge-images/8136/1436794554-75e178e325-drawing47.svg)

6. [Game of Two Stacks](https://github.com/papilo-cloud/HCKR/blob/main/Python/stacks/two_stacks.py) Alexa has two stacks of non-negative integers, stack __*a[n]*__ and stack __*b[m]*__ where index __0__ denotes the top of the stack. Alexa challenges Nick to play the following game:

    - In each move, Nick can remove one integer from the top of either stack __*a*__ or stack __*b*__.

    - Nick keeps a running sum of the integers he removes from the two stacks.

    - Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer __*maxSum*__ given at the beginning of the game.
    - Nick's final score is the total number of integers he has removed from the two stacks.


### LinkedList

1. [Print the Element of a Linked List](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/print_linked_list.py) Given a pointer to the head node of a linked list, print each node's __*data*__ element, one per line. If the head pointer is null (indicating the list is empty), there is nothing to print.

    #### Function Description

    Complete the printLinkedList function in the editor below.

    printLinkedList has the following parameter(s):

    - SinglyLinkedListNode head: a reference to the head of the list
    #### Print

    For each node, print its __*data*__  value on a new line (console.log in Javascript).

2. [Print in Reverse](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/reverse_print.py) Given a pointer to the head of a singly-linked list, print each  value from the reversed list. If the given list is empty, do not print anything.

    #### Example

    __*head*__ refers to the linked list with __*data*__ values __1 -- 2 -- 3 -- *NULL*__ 

    Print the following:
    3
    2
    1

3. [Print Elements](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/print_linked_list.py) This is an to practice traversing a linked list. Given a pointer to the head node of a linked list, print each node's __*data*__ element, one per line. If the head pointer is null (indicating the list is empty), there is nothing to print.

4. [Insert a Node at the Tail](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/insert_node_at_tail.py) You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.

    #### Function Description

    Complete the insertNodeAtTail function in the editor below.

    insertNodeAtTail has the following parameters:

    - SinglyLinkedListNode pointer head: a reference to the head of a list
    - int data: the data value for the node to insert
    #### Returns

    - SinglyLinkedListNode pointer: reference to the head of the modified linked list

5. [Insert a Node at the Head](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/insert_node_at_head.py) Given a pointer to the head of a linked list, insert a new node before the head. The __*next*__ value in the new node should point to __*head*__ and the __*data*__ value should be replaced with a given value. Return a reference to the new head of the list. The head pointer given may be null meaning that the initial list is empty.

    #### Function Description

    Complete the function insertNodeAtHead in the editor below.

    insertNodeAtHead has the following parameter(s):

    - SinglyLinkedListNode llist: a reference to the head of a list
    - data: the value to insert in the __*data*__ field of the new node
    #### Input Format

    The first line contains an integer __*n*__, the number of elements to be inserted at the head of the list.
    The next __*n*__ lines contain an integer each, the elements to be inserted, one per function call.

6. [](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/.py)
6. [](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/.py)
6. [](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/.py)
6. [](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/.py)

### Search

1. [Missing Numbers](https://github.com/papilo-cloud/HCKR/blob/main/Python/search/missing-numbers.py) Given two arrays of integers, find which elements in the second array are missing from the first array.

    #### Example
    __*arr*__ = __[7,2,5,3,5,3]__
    __*brr*__ = __[7,2,5,4,6,3,5,3]__

    The __*brr*__ array is the orginal list. The numbers missing are __[4,6]__.

    #### Notes
    - If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
    - Return the missing numbers sorted ascending.
    - Only include a missing number once, even if it is missing multiple times.
    - The difference between the maximum and minimum numbers in the original list is less than or equal to __100__.

1. [Ice Cream Parlor](https://github.com/papilo-cloud/HCKR/blob/main/Python/search/icecream-parlor.py) Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

    Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

    #### Example.  
    __*m* = 6, *cost* = [1,3,4,5,6]__

    The two flavors that cost __1__ and __5__ meet the criteria. Using __1__-based indexing, they are at indices __1__ and __4__.

1. [Pairs](https://github.com/papilo-cloud/HCKR/blob/main/Python/search/pairs.py) Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

    #### Example
    __*k* = 1__
    __*arr* = [1,2,3,4]__


There are three values that differ by __*k* = 1__: __2 - 1 = 1__, __3 - 2 = 1__, and __4 - 3 = 1__. Return __3__.

1. [](https://github.com/papilo-cloud/HCKR/blob/main/Python/search/.py)
1. [](https://github.com/papilo-cloud/HCKR/blob/main/Python/search/.py)

### Tree

1. [Height of a Binary Tree](https://github.com/papilo-cloud/HCKR/blob/main/Python/Tree/max_height.py) The height of a binary tree is the number of edges between the tree's root and its furthest leaf. For example, the following binary tree is of height __2__:

    ![Images](https://s3.amazonaws.com/hr-assets/0/1527626183-88c8070977-isitBSTSample0.png)

2. [Binary Search Tree: insertion](https://github.com/papilo-cloud/HCKR/blob/main/Python/Tree/insert.py) You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. You just have to complete the function.

3. [Preorder Traversal](https://github.com/papilo-cloud/HCKR/blob/main/Python/Tree/preorder_traversal.py) Complete the __*preOrder*__ function in the editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

    #### Input Format

    Our test code passes the root node of a binary tree to the preOrder function.

    #### Constraints

    __1__ <= Nodes in the tree  <= __500__

    #### Output Format

    Print the tree's preorder traversal as a single line of space-separated values.

    #### Sample Input
    <pre>
    1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
    </pre>

    #### Sample Output

    <pre>
        1 2 5 3 4 6
    </pre>

4. [Inorder Traversal](https://github.com/papilo-cloud/HCKR/blob/main/Python/Tree/inorder.py) In this challenge, you are required to implement inorder traversal of a tree.

    Complete the __*inOrder*__ function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's inorder traversal as a single line of space-separated values.

     #### Input Format

    Our hidden tester code passes the root node of a binary tree to your $inOrder* function.

    #### Constraints

    __1__ <= __*Nodes in the tree*__  <= __500__

    #### Output Format

    Print the tree's inorder traversal as a single line of space-separated values.

    #### Sample Input
    <pre>
    1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
    </pre>

    #### Sample Output

    <pre>
        1 2 3 4 5 6
    </pre>

5. [Level Order Traversal](https://github.com/papilo-cloud/HCKR/blob/main/Python/Tree/level_order.py) Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. In level-order traversal, nodes are visited level by level from left to right. Complete the function  __*levelOrder*__ and print the values in a single line separated by a space.
    #### For example:
    <pre>
     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
    </pre>
    For the above tree, the level order traversal is
    __1-> 2-> 5-> 3-> 6-> 4__.

6. [Top View](https://github.com/papilo-cloud/HCKR/blob/main/Python/Tree/top_view.py) Given a pointer to the root of a binary tree, print the top view of the binary tree.

    The tree as seen from the top the nodes, is called the top view of the tree.
    #### For example:
    <pre>
     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
    </pre>
    For the above tree, the level order traversal is
    __1-> 2-> 5-> 6__.

7. [Is This a Binary Search Tree?](https://github.com/papilo-cloud/HCKR/blob/main/Python/Tree/is_binary_tree.py) Given the root node of a binary tree, can you determine if it's also a binary search tree?

    Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

    #### Input Format

    You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

    #### Constraints

    - __0 <= *data* <= 10<sup>4</sup>__

    #### Output Format

    You are not responsible for printing any output to stdout. Your function must return true if the tree is a binary search tree; otherwise, it must return false. Hidden code stubs will print this result as a Yes or No answer on a new line.

    #### Sample Input

    ![Image](https://s3.amazonaws.com/hr-challenge-images/8131/1461698192-c9e0fcb28d-BTinput.png)

    #### Sample Output

    No


### Sorting
1. [Closest Numbers](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/closest_num.py) Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

    #### Example
    __*arr*__ = __[5, 2, 3, 4, 1]__
    Sorted, __*arr'*__ = __[5, 2, 3, 4, 1]__. Several pairs have the minimum difference of __1__: __[(1,2), (2,3), (3,4), (4,5)]__. Return the array __[1, 2, 2, 3, 3, 4, 4, 5]__.

    #### Note
    As shown in the example, pairs may overlap.

    Given a list of unsorted integers, __*arr*__, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.

2. [Running Time of Insertion Sort](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/running_time.py) 

    ![Image](https://s3.amazonaws.com/hr-challenge-images/insertion-sort/InsertionSortRunningTime-small.png)

3. [Insertion Sort 1](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/insertion_a.py)
    #### Insertion Sort
    These challenges will cover Insertion Sort, a simple and intuitive sorting algorithm. We will first start with a nearly sorted list.

4. [Insertion Sort 2](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/insertion_b.py) In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.

    #### Example.

    __*n* = 7__
    __*arr* = [3, 4, 7, 5, 6, 2, 1]__

    Working from left to right, we get the following output:
    <pre>
        3 4 7 5 6 2 1
        3 4 7 5 6 2 1
        3 4 5 7 6 2 1
        3 4 5 6 7 2 1
        2 3 4 5 6 7 1
        1 2 3 4 5 6 7
    </pre>

5. [Quicksoer 1 - Partition](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/partition.py)

6. [Counting Srot 1](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/counting_sort_a.py)
    #### Alternative Sorting
    Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

    #### Example

    __*arr* = [1, 1, 3, 2, 1]__
    All of the values are in the range __[0...3]__, so create an array of zeros, __*result* = [0,0,0,0]__. The results of each iteration follow:

    <pre>
        i	arr[i]	result
        0	1	[0, 1, 0, 0]
        1	1	[0, 2, 0, 0]
        2	3	[0, 2, 0, 1]
        3	2	[0, 2, 1, 1]
        4	1	[0, 3, 1, 1]
    </pre>
    The frequency array is __[0, 3, 1, 1]__. These values can be used to create the sorted array as well: __*sorted* = [1, 1, 1, 2, 3]__.

    #### Note
    For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.

    #### Challenge
    Given a list of integers, count and return the number of times each value appears as an array of integers.

7. [Counting Srot 2](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/counting_sort_b.py) The counting sort is used if you just need to sort a list of integers. Rather than using a comparison, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

    For example, consider an array __*arr* = [1, 1, 3, 2, 1]__. All of the values are in the range __[0...3]__, so create an array of zeroes, __*result* = [0,0,0,0]__. The results of each iteration follow:
    <pre>
        i	arr[i]	result
        0	1	[0, 1, 0, 0]
        1	1	[0, 2, 0, 0]
        2	3	[0, 2, 0, 1]
        3	2	[0, 2, 1, 1]
        4	1	[0, 3, 1, 1]
    </pre>
    Now we can print the sorted array: __*sorted* = [1, 1, 1, 2, 3]__.

    #### Challenge
    Given an unsorted list of integers, use the counting sort method to sort the list and then print the sorted list.

8. [The Full Counting Sort](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/counting_sort.py) Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

    Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

    Design your counting sort to be stable.

    #### Example
    __*arr* = [[0, 'a'], [1, 'b'], [0, 'c'], [1, 'd']]__
    The first two strings are replaced with '-'. Since the maximum associated integer is __1__, set up a helper array with at least two empty arrays as elements. The following shows the insertions into an array of three empty arrays.
    <pre>
        i	string	converted	list
        0				[[],[],[]]
        1 	a 	-		[[-],[],[]]
        2	b	-		[[-],[-],[]]
        3	c			[[-,c],[-],[]]
        4	d			[[-,c],[-,d],[]]
    </pre>
    The result is then printed:  __- c - d__.

### Implementation

1. [Subarray Division](https://github.com/papilo-cloud/HCKR/blob/main/Python/Implementation/birthday.py) Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

    Lily decides to share a contiguous segment of the bar selected such that:

    - The length of the segment matches Ron's birth month, and,
    - The sum of the integers on the squares is equal to his birth day.

    Determine how many ways she can divide the chocolate.

    #### Example
    __*s* = [2, 2, 1, 3, 2]__
    __*d* = 4__
    __*m* = 2__

    Lily wants to find segments summing to Ron's birth day, __*d* = 4__ with a length equalling his birth month, __*m* = 2__. In this case, there are two segments meeting her criteria: __[2, 2]__ and __[1, 3]__.

2. [DEsigner PDF Viewer](https://github.com/papilo-cloud/HCKR/blob/main/Python/Implementation/designer_pdf.py) When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:
    
    ![Image](https://s3.amazonaws.com/hr-challenge-images/22869/1471640108-6c01750b16-PDF-highighting.png)

    #### Example
    __*h* = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5]__
    __*word* = *'torn'*__

    The heights are __*t* = 2, *o* = 1, *r* = 1__ and __*n* = 1__. The tallest letter is __2__  high and there are __4__  letters. The hightlighted area will be __2 * 4 = 8*mm*__  so the answer is  __8__ .


### Heap

- [QHEAP1](https://github.com/papilo-cloud/HCKR/blob/main/Python/Heap/q_heap.py) This question is designed to help you get a better understanding of basic heap operations.

    There are __3__ types of query:

    - "__1 *v*__" - Add an element __*v*__ to the heap.
    - "__2 *v*__" - Delete the element __*v*__ from the heap.
    - "__3__" - Print the minimum of all the elements in the heap.

    __NOTE:__ It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

    #### Input Format

    The first line contains the number of queries, __*Q*__.
    Each of the next __*Q*__ lines contains one of the __3__ types of query.

    #### Constraints
    __1 <= *Q* <= 10<sup>5</sup>__
    __-10<sup>5</sup> <= *v* <= 10<sup>9</sup>__

    #### Output Format

    For each query of type __3__, print the minimum value on a single line.

    #### Sample Input
    <pre>
    STDIN       Function
    -----       --------
    5           Q = 5
    1 4         insert 4
    1 9         insert 9
    3           print minimum
    2 4         delete 4
    3           print minimum
    </pre>

    #### Sample Output
    <pre>
    4  
    9 
    </pre>

- [Jesse and Cookies](https://github.com/papilo-cloud/HCKR/blob/main/Python/Heap/cookies.py) Jesse loves cookies and wants the sweetness of some cookies to be greater than value __*k*__. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

    sweetness = (__1__ x Least sweet cookie + __2__ x 2nd least sweet cookie).

    This occurs until all the cookies have a sweetness __>= *k*__.

    Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return __-1__.

    #### Example
    __*k* = 9__
    __*A* = [2, 7, 3, 6, 4, 6]__

    The smallest values are __2, 3__.
    Remove them then return __2 + 2 x 3 = 8__ to the array. Now __*A* = [8, 7, 6, 4, 6]__.
    Remove __4, 6__ and return __4 + 6 x 2 = 16__ to the array. Now __*A* = [16, 8, 7, 6]__.
    Remove __6, 7__, return __6 + 2 x 7 = 20__ and __*A* = [20, 16, 8, 7]__.
    Finally, remove __8, 7__ and return __7 + 2 x 8 = 23__ to __*A*__. Now __*A* = [23, 20, 16]__.
    All values are __>= *k* = 9__ so the process stops after __4__ iterations. Return __4__.

    #### Function Description
    Complete the cookies function in the editor below.

    cookies has the following parameters:

    - int k: the threshold value
    - int A[n]: an array of sweetness values
    #### Returns

    - int: the number of iterations required or __-1__