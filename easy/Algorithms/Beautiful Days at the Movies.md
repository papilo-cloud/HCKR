# Beautiful Days at the Movies.

Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number **12**, its reverse is 21. Their difference is **9**. The number **120** reversed is **21**, and their difference is **99**.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days, **[_i...j_]** and a number **_k_**, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where **|_i-reverse_(_i_)|** is evenly divisible by **_k_**. If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range.

### Function Description

Complete the beautifulDays function in the editor below.

beautifulDays has the following parameter(s):

* int i: the starting day number
* int j: the ending day number
* int k: the divisor

### Returns

* int: the number of beautiful days in the range

### Input Format

A single line of three space-separated integers describing the respective values of **_i_**, **_j_**, and **_k_**.

### Constraints

* **1 <= _i_ <= _j_ <= 2 x 10<sup>6</sup>**
* **1 <= _k_ <= 2 x 10<sup>9</sup>**

### Sample Input

20 23 6

### Sample Output

2

### Explanation

Lily may go to the movies on days **_20_**, **_21_**, **_22_**, and **_23_**. We perform the following calculations to determine which days are beautiful:

* Day **_20_** is beautiful because the following evaluates to a whole number: **(|20-02| / 6) = 18/6 = 3**
* Day **21** is not beautiful because the following doesn't evaluate to a whole number: **(|21-12| / 6) = 9/6 = 1.5**
* Day **22** is beautiful because the following evaluates to a whole number: **(|22-22| / 6) = 0/6 = 0**
* Day **23** is not beautiful because the following doesn't evaluate to a whole number: **(|23-32| / 6) = 9/6 = 1.5**

Only two days, **20** and **22**, in this interval are beautiful. Thus, we print **2** as our answer.

## My Solution.

```javascript
    function beautifulDays(i, j, k) {
        let beautiful = 0
        for (let x = i; x <= j; x++) {
            let str = x.toString()
            let num = [...str].reverse().join('')
            let ans = (((x - num)/k)%1 == 0)
            if (ans) {
                beautiful += 1
            }
        }
        return beautiful
    }
```