# Compare the Triplets

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

* If a[i] > b[i], then Alice is awarded 1 point.
* If a[i] < b[i], then Bob is awarded 1 point.
* If a[i] = b[i], then neither person receives a point.

Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

### Example

a = [1, 2, 3]

b = [3, 2, 1]

* For elements *0*, Bob is awarded a point because a[0] .
* For the equal elements a[1] and b[1], no points are earned.
* Finally, for elements 2, a[2] > b[2] so Alice receives a point.
The return array is [1, 1] with Alice's score first and Bob's second.

### Function Description

Complete the function compareTriplets in the editor below.

compareTriplets has the following parameter(s):

* int a[3]: Alice's challenge rating
* int b[3]: Bob's challenge rating
### Return

* int[2]: Alice's score is in the first position, and Bob's score is in the second.

### Input Format

The first line contains 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.

The second line contains 3 space-separated integers, b[0], b[1], and b[2], the respective values in triplet b.

### Constraints

* 1 ≤ a[i] ≤ 100
* 1 ≤ b[i] ≤ 100
### Sample Input 0
<pre>
5 6 7
3 6 10
</pre>

### Sample Output 0
<pre>
1 1
</pre>

### Explanation 0

In this example:

* **_a_ = (_a_[0],_a_[1],_a_[2]) = (5,6,7)**
* **_b_ = (_b_[0],_b_[1],_b_[2]) = (3,6,10)**

Now, let's compare each individual score:

* **_a_[0] > b[0]**, so Alice receives **1** point.
* **_a_[1] = b[1]**, so nobody receives a point.
* **_a_[2] < b[2]**, so Bob receives **1** point.

Alice's comparison score is **1**, and Bob's comparison score is **1**. Thus, we return the array **[1,1]**.

### Sample Input 1
<pre>
17 28 30
99 16 8
</pre>

### Sample Output 1
<pre>
2 1
</pre>
### Explanation 1

Comparing the 0-<sup>th</sup>- elements, **17 < 99** so Bob receives a point.

Comparing the 1_<sup>st</sup> and 2_<sup>nd</sup> elements, **28 > 16** and **30 > 8** so Alice receives two points.

The return array is **[2,1]**.

## My Solution

```javascript
    function compareTriplets(a, b) {
        var an = 0
        var bn = 0
        for (var i = 0; i < a.length; i++) {
            if (a[i] > b[i]) {
                an += 1
            }
            if (a[i] < b[i]) {
                bn += 1
            }
        }
        const ans = [an,bn]
        return ans
    }
```