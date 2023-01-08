# CamelCase

There is a sequence of words in CamelCase as a string of letters, **_s_**, having the following properties:

* It is a concatenation of one or more words consisting of English letters.
* All letters in the first word are lowercase.
* For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given **_s_**, determine the number of words in **_s_**.

### Example
**_s_ = _oneTwoThree_**

There are **3** words in the string: 'one', 'Two', 'Three'.

### Function Description

Complete the camelcase function in the editor below.

camelcase has the following parameter(s):

* string s: the string to analyze
### Returns

* int: the number of words in **_s_**
### Input Format

A single line containing string **_s_**.

### Constraints
* **1 <= length of _s_ <= 10<sup>5</sup>**

### Sample Input
<pre>
saveChangesInTheEditor
</pre>
### Sample Output
<pre>
5
</pre>
### Explanation

String **_s_** contains five words:

1. save
1. Changes
1. In
1. The
1. Editor

# My Solution

```javascript
    function camelcase(s) {

        let count = 1;
        let y = s.toUpperCase()
        for (let i in s) {
            if (s[i] == y[i]) {
                count++
            }
        }
        return count
    }
```