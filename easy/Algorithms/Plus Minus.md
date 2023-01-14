# Plus Minus

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with **6** places after the decimal.

**Note:** This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to **10<sup>-4</sup>** are acceptable.

### Example
**_arr_ = [1, 1, 0, -1, -1]**

There are **_n_ = 5** elements, two positive, two negative and one zero. Their ratios are **2/5 = 0.400000**, **2/5 = 0.400000** and **2/5 = 0.200000**. Results are printed as:

<pre>
0.400000
0.400000
0.200000
<?pre>
### Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

* int arr[n]: an array of integers
### Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with **6** digits after the decimal. The function should not return a value.

### Input Format

The first line contains an integer, **_n_**, the size of the array.
The second line contains **_n_** space-separated integers that describe **_arr_[n]**.

### Constraints

**0 < _n_ <= 100**
**-100 <= _arr_[i] <= 100**

### Output Format

**Print** the following **3** lines, each to **6** decimals:

1. proportion of positive values
1. proportion of negative values
1. proportion of zeros
### Sample Input

<pre>
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
</pre>

### Sample Output

<pre>
0.500000
0.333333
0.166667
</pre>

### Explanation

There are **3** positive numbers, **2** negative numbers, and **1** zero in the array.
The proportions of occurrence are positive: **3/6 = 0.500000**, negative: **2/6 = 0.333333** and zeros: **2/6 = 0.166667**.

## My Solution
```javascript
    function plusMinus(arr) {
        const x = arr.length;
        let post = 0
        let negt = 0
        let zero = 0
        for(let i of arr){
            if(i < 1 && i !=0){
                negt += 1
            }
            if(i >= 1){
                post += 1           
            }
            if(i ==0){
                zero += 1
            }        
        }
        console.log((post/x).toFixed(6))
        console.log((negt/x).toFixed(6))
        console.log((zero/x).toFixed(6))
    }
```