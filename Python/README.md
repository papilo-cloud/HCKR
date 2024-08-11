# Hackerrank Archive

1. ## [Strings](#strings)
1. ## [Stacks](#stacks)
3. ## [Linked List](#LinkedList)


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

### Linked List

1. [Print the Element of a Linked List](https://github.com/papilo-cloud/HCKR/blob/main/Python/LinkedList/print_linked_list.py) Given a pointer to the head node of a linked list, print each node's __*data*__ element, one per line. If the head pointer is null (indicating the list is empty), there is nothing to print.

    #### Function Description

    Complete the printLinkedList function in the editor below.

    printLinkedList has the following parameter(s):

    - SinglyLinkedListNode head: a reference to the head of the list
    #### Print

    For each node, print its __*data*__  value on a new line (console.log in Javascript).