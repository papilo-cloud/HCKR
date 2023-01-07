# Angry Professor.

A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (**_arrivalTime_ <= 0**) to arrived late (**_arrivalTime_ > 0**).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

### Example

**_n_ = 5**
**_k_ = 3**
**_a_ = [-2,-1,0,1,2]**

The first **3** students arrived on. The last **2** were late. The threshold is **3** students, so class will go on. Return YES.

**Note**: Non-positive arrival times (**_a_[_i_] <= 0) indicate the student arrived early or on time; positive arrival times (**_a_[_i_] > 0**) indicate the student arrived **_a_[_i_]** minutes late.

### Function Description

Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):

* int k: the threshold number of students
* int a[n]: the arrival times of the **_n_** students
### Returns

* string: either YES or NO

### Input Format

The first line of input contains _**t**_, the number of test cases.

Each test case consists of two lines.

The first line has two space-separated integers, _**n**_ and _**k**_, the number of students (size of _**a**_) and the cancellation threshold.
The second line contains _**n**_ space-separated integers (**_a_[1],_a_[2],...,_a_[_n_]**) that describe the arrival times for each student.

### Constraints

* **1 <= _t_ <= 10**
* **1 <= _n_ <= 1000**
* **1 <= _k_ <= 10**
* **-1000 <= _a_[_i_] <= 100, _where i_ E [1,..._n_]**

### Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Sample Output

YES
NO

### Explanation

For the first test case, **_k_ = 3. The professor wants at least **3** students in attendance, but only **2** have arrived on time ( **-3** and **-1**) so the class is cancelled.

For the second test case, **_k_ = 2. The professor wants at least **2** students in attendance, and there are **2** who arrived on time (**0** and -**1**). The class is not cancelled.

## My Solution.

```javascript
    function angryProfessor(k, a) {
        let H=0
        for (let i = 0; i < a.length; i++) {
            if (a[i] <=0) {
                H += 1 
            }
        }     
        if (H >= k ) {
            return 'NO'
        } else {
            return 'YES'
        }
}
```