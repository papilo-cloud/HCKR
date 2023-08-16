# Left Rotation

A left rotation operation on an array of size ***n*** shifts each of the array's elements **1** unit to the left. Given an integer, ***d***, rotate the array that many steps left and return the result.

### Example
**_d_ = 2**
**_arr_ = [1,2,3,4,5]**
After **2** rotations, **_arr'_ = [1,2,3,4,5]** .

### Function Description

Complete the rotateLeft function in the editor below.

rotateLeft has the following parameters:

* int d: the amount to rotate by
* int arr[n]: the array to rotate

### Returns

* int[n]: the rotated array

### Input Format

The first line contains two space-separated integers that denote ***n***, the number of integers, and ***d***, the number of left rotations to perform.
The second line contains ***n*** space-separated integers that describe **_n_[]**.

### Constraints
* **1 <= _n_ <= 10<sup>5</sup>**
* **1 <= _d_ <= n**
* **1 <=a[i]<= 10<sup>6</sup>**

### Sample Input
<pre>
54
12345
</pre>

### Sample Output
<pre>
51234
</pre>

### Explanation

To perform **_d_ = 4** left rotations, the array undergoes the following sequence of changes:

```mermaid
    [1,2,3,4,5] --> [2,3,4,5,1] --> [3,4,5,1,2] --> [4,5,1,2,3] --> [5,1,2,3,4]
```

## My Solution.

```javascript
    function rotateLeft(d, arr) {
        for (let i = 0; i < d; i++) {
            let start = arr[0];
            for (let j = 0; j < arr.length; j++) {
                arr[j] = arr[j + 1];
            }
            arr[arr.length- 1] = start;
        }
    return arr;
}
```