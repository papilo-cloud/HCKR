# Bill Division

Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: **_bill_ = [2,4,6]**. Anna declines to eat item **_k_ = _bill_[2]** which costs **6**. If Brian calculates the bill correctly, Anna will pay **(2 + 4)/2 = 3**. If he includes the cost of **_bill_[k]**, he will calculate **(2 + 4 + 6)/2 = 6**. In the second case, he should refund **3** to Anna.

### Function Description

Complete the bonAppetit function in the editor below. It should print <pre>Bon Appetit</pre> if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

* bill: an array of integers representing the cost of each item ordered
* k: an integer representing the zero-based index of the item Anna doesn't eat
* b: the amount of money that Anna contributed to the bill
### Input Format

The first line contains two space-separated integers **_n_** and **_k_**, the number of items ordered and the **0**-based index of the item that Anna did not eat.

The second line contains **_n_** space-separated integers **_bill_[_i_]** where **0 <= _i_ < _n_**.

The third line contains an integer, **_b_**, the amount of money that Brian charged Anna for her share of the bill.

### Constraints
* **2 <= _n_ <= 10<sup>5</sup>**
* **2 <= _k_ < _n_**
* **2 <= _bill_[_i_] <= 10<sup>4</sup>**

* The amount of money due Anna will always be an integer
### Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e. **_b<sub>charged</sub>_ - _b<sub>actual</sub>_**, ) that Brian must refund to Anna. This will always be an integer.

### Sample Input 0
<pre>
4 1
3 10 2 9
12
</pre>
### Sample Output 0
<pre>
5
</pre>

### Explanation 0

Anna didn't eat item **_bill_[1] = 10**, but she shared the rest of the items with Brian. The total cost of the shared items is **3 + 2 + 9 = 14** and, split in half, the cost per person is **_b<sub>actual</sub>_ = 7**. Brian charged her ** _b<sub>charged</sub> = 12_** for her portion of the bill. We print the amount Anna was overcharged, **_b<sub>charged</sub>_ - _b<sub>actual</sub>_ = 12 - 7 = 12**, on a new line.

### Sample Input 1
<pre>
4 1
3 10 2 9
7
</pre>

### Sample Output 1
<pre>
4 1
3 10 2 9
7
</pre>
### Sample Output 1
<pre>
Bon Appetit
</pre>

### Explanation 1
Anna didn't eat item **_bill_[1]**, but she shared the rest of the items with Brian. The total cost of the shared items is **3 + 2 + 9 = 14** and, split in half, the cost per person is **_b<sub>actual</sub>_ = 7**. Because **_b<sub>actual</sub>_ = _b<sub>charged</sub>_ = 7**, we print <pre>Bon Appetit</pre> on a new line.

# My Solution.

```javascript
    function bonAppetit(bill, k, b) {
        const annaSum = bill.filter((x,i) =>  (i != k) )
        const sum = annaSum.reduce((a,b) => a + b)
        const totalBill = bill.reduce((a,b) => a + b)
        
        const total = sum / 2
        if (b == total) {
            console.log('Bon Appetit')
        } else {
            const refund = (totalBill/2) - total
            console.log(`${refund}`)
        }
    }

```