# Hackerrank Archive

1. ## [Strings](#strings)
1. ## [Stacks](#stack)
3. ## [Linked List](#linkedList)
4. ## [Search](#search)
5. ## [Tree](#tree)
6. ## [Sorting](#sorting)
7. ## [Array](#array)


### Strings

- [Anagram](https://github.com/papilo-cloud/Python_Data_Structures-/blob/main/Hackerrank/strings/anagram.py) Two words are anagrams of one another if their letters can be rearranged to form the other word.

    Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

    #### Returns
    - int: the minimum number of characters to change or -1.
- [Pangrams](https://github.com/papilo-cloud/Python_Data_Structures-/blob/main/Hackerrank/strings/pangram.py) A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

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


### Sorting
1. [Closest Numbers](https://github.com/papilo-cloud/HCKR/blob/main/Python/sorting/closest_num.py) Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

    #### Example
    __*arr*__ = __[5, 2, 3, 4, 1]__
    Sorted, __*arr'*__ = __[5, 2, 3, 4, 1]__. Several pairs have the minimum difference of __1__: __[(1,2), (2,3), (3,4), (4,5)]__. Return the array __[1, 2, 2, 3, 3, 4, 4, 5]__.

    #### Note
    As shown in the example, pairs may overlap.

    Given a list of unsorted integers, __*arr*__, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.