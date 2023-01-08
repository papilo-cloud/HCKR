# Mars Exploration.

A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.

![alt text](https://s3.amazonaws.com/hr-challenge-images/16032/1453204202-9e3fd295bb-NASA_Mars_Rover.jpg "NASA_Mars_Rover")

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, **_s_**, determine how many letters of the SOS message have been changed by radiation.

### Example
**_s_ = 'SOSTOT**

The original message was SOSSOS. Two of the message's characters were changed in transit.

### Function Description

Complete the marsExploration function in the editor below.

marsExploration has the following parameter(s):

* string s: the string as received on Earth
### Returns

* int: the number of letters changed during transmission
### Input Format

There is one line of input: a single string, **_s_**.

### Constraints

* **1 <= length of _s_ <= 99**
* **length of _s_ modulo 3= 0**
* **_s_** will contain only uppercase English letters, ascii[A-Z].
### Sample Input 0
<pre>
SOSSPSSQSSOR
</pre>

### Sample Output 0
<pre>
3
</pre>

### Explanation 0

**_s_ = SOSSPSSQSSOR**, and signal length **|_s_| = 12**. They sent **_4_** SOS messages (i.e.: **12/3 = 4** ).
<pre>
Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR
Difference:          X  X   X
</pre>

### Sample Input 1
<pre>
SOSSOT
</pre>

### Sample Output 1
<pre>
1
</pre>

### Explanation 1

**_s_ = SOSSOT**, and signal length **|_s_| = 6**. They sent 2  SOS messages (i.e.: **6/3 = 2** ).
<pre>
Expected Signal: SOSSOS     
Received Signal: SOSSOT
Difference:           X
</pre>

### Sample Input 2
<pre>
SOSSOSSOS
</pre>
### Sample Output 2
<pre>
0
</pre>
### Explanation 2

Since no character is altered, return 0.

## My Solution

```javascript
    function marsExploration(s) {
        let res = [...s].map((d, i) => (i) % 3 == 0 ? ' ' + d : d).join('')
        let r = res.split(' ')
  
        let p;
        let count = 0
        for (let i = 1; i < r.length; i++) {
            p = r[i]
            if (p[0] !== 'S') {
                count++
            }
            if (p[1] !== 'O') {
                count++
            }
            if (p[2] !== 'S') {
                count++
            }
        }
        return count
    }
```