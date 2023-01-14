# Simple Array Sum

Given an array of integers, find the sum of its elements.

For example, if the array **_arr_ = [1,2,3], 1 + 2 + 3 = 6**, so return **6**.

### Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

* ar: an array of integers
### Input Format

The first line contains an integer, **_n_**, denoting the size of the array.
The second line contains **_n_** space-separated integers representing the array's elements.

### Constraints
**0 < _n, ar_[_i_] <= 1000**

### Output Format

Print the sum of the array's elements as a single integer.

### Sample Input
<pre>
6
1 2 3 4 10 11
</pre>
### Sample Output
<pre>
31
</pre>
### Explanation

We print the sum of the array's elements: **1 + 2 + 3 + 4 + 10 + 11 = 31**

## My Solution

```javascript
    function simpleArraySum(ar) {
        const ans = ar.reduce((a,b) => a+b)
        return ans 
    }
```