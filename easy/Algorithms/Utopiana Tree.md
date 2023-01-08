# Utopian Tree.

The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after **_n_** growth cycles?

For example, if the number of growth cycles is **_n_ = 5**, the calculations are as follows:

```
Period  Height
0          1
1          2
2          3
3          6
4          7
5          14
```

### Function Description

Complete the utopianTree function in the editor below.

utopianTree has the following parameter(s):

* int n: the number of growth cycles to simulate
## Returns

* int: the height of the tree after the given number of cycles
### Input Format

The first line contains an integer, **_t_**, the number of test cases.

**_t_** subsequent lines each contain an integer, **_n_**, the number of cycles for that test case.

### Constraints

**1 <= _t_ <= 10**

**0 <= _n_ <= 60**

### Sample Input
<pre>
3
0
1
4
</pre>

### Sample Output
<pre>
1
2
7
</pre>

### Explanation

There are 3 test cases.

In the first case (**_n_ = 0**), the initial height (**_H_ = 1**) of the tree remains unchanged.

In the second case (**_n_ = 1**), the tree doubles in height and is **2** meters tall after the spring cycle.

In the third case (**_n_ = 4**), the tree doubles its height in spring (**_n_ = 1, _H_ = 2**), then grows a meter in summer (**_n_ = 2, _H_ = 3**), then doubles after the next spring (**_n_ = 3, _H_ = 6**), and grows another meter after summer (**_n_ = 4, _H_ = 7**). Thus, at the end of 4 cycles, its height is **_7_** meters.

## My Solution.

```javascript
    function utopianTree(n) {
        let H=0
        for (let i = 0; i <= n; i++) {
            if (i == 0 ) {
                H = 1
            }
            if (i == 1) {
                H = 2
            }
            if (i> 1 && i % 2 == 0) {
                H += 1
            } if (i > 1 && i %2 != 0) {
                H *= 2
            }
        }
        return H
    }
```