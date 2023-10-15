# Taum and B'day
Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy ***b*** black gifts and ***w*** white gifts.

* The cost of each black gift is ***bc*** units.
* The cost of every white gift is ***wc*** units.
* The cost to convert a black gift into white gift or vice versa is ***z*** units.

Determine the minimum cost of Diksha's gifts.

### Example
**_b_ = 3**
**_w_ = 5**
**_bc_ = 3**
**_wc_ = 4**
**_z_ = 1**




He can buy a black gift for **3** and convert it to a white gift for **1**, making the total cost of each white gift **4**. That matches the cost of a white gift, so he can do that or just buy black gifts and white gifts. Either way, the overall cost is **3 x 5 + 5 x 4 = 29**.

## Function Description

Complete the function taumBday in the editor below. It should return the minimal cost of obtaining the desired gifts.

taumBday has the following parameter(s):

* int b: the number of black gifts
* int w: the number of white gifts
* int bc: the cost of a black gift
* int wc: the cost of a white gift
* int z: the cost to convert one color gift to the other color

### Returns

* int: the minimum cost to purchase the gifts

### Input Format

The first line will contain an integer ***t***, the number of test cases.

The next ***t*** pairs of lines are as follows:
- The first line contains the values of integers ***b*** and ***w***.
- The next line contains the values of integers ***bc***, ***wc***, and ***z***.

### Constraints

**1 <= _t_ <= 10**
**0 <= _b_,_w_,_bc_,_wc_,_z_ <= 10<sup>9</sup>**


### Output Format

***t*** lines, each containing an integer: the minimum amount of units Taum needs to spend on gifts.

### Sample Input
<pre>
STDIN   Function
-----   --------
5       t = 5
10 10   b = 10, w = 10
1 1 1   bc = 1, wc = 1, z = 1
5 9     b = 5, w = 5
2 3 4   bc = 2, wc = 3, z = 4
3 6     b = 3, w = 6
9 1 1   bc = 9, wc = 1, z = 1
7 7     b = 7, w = 7
4 2 1   bc = 4, wc = 2, z = 1
3 3     b = 3, w = 3
1 9 2   bc = 1, wc = 9, z = 2
</pre>

### Sample Output
<pre>
20
37
12
35
12
</pre>

### Explanation

* Test Case #01:
Since black gifts cost the same as white, there is no benefit to converting the gifts. Taum will have to buy each gift for 1 unit. The cost of buying all gifts will be: 
 **_b_ x _bc_ + _w_ x _wc_ = 10 x 1 + 10 x 1 = 20**.

* Test Case #02:
Again, he cannot decrease the cost of black or white gifts by converting colors._z_ is too high. He will buy gifts at their original prices, so the cost of buying all gifts will be: **_b_ x _bc_ + _w_ x _wc_ = 5 x 2 + 9 x 3 = 10 + 27 = 37**.

* Test Case #03:
Since **_bc_ > _wc_ + _z_**, he will buy **_b_ + _w_ = 3 + 6 = 9** white gifts at their original price of **1**.**_b_ = 3**  of the gifts must be black, and the cost per conversion, **_z_ = 1**. Total cost is **9 x 1 + 3 x 1 = 12**.

* Test Case #04:
Similarly, he will buy  white gifts at their original price, . For black gifts, he will first buy white ones and color them to black, so that their cost will be reduced to . So cost of buying all gifts will be: .

* Test Case #05: He will buy black gifts at their original price, . For white gifts, he will first black gifts worth  unit and color them to white for  units. The cost for white gifts is reduced to  units. The cost of buying all gifts will be: .