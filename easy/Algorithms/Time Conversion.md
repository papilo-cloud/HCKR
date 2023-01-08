# Time Conversion.

Given a time in **12**-hour AM/PM format, convert it to military (24-hour) time.

**Note**: - 12:00:00AM on a **12**-hour clock is 00:00:00 on a **24**-hour clock.
 12:00:00PM on a **12**-hour clock is 12:00:00 on a **24**-hour clock.

### Example

* **s = '12:01:00PM'**

Return '12:01:00'.

* **s = '12:01:00AM'**

Return '00:01:00'.

### Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in **24** hour format.

timeConversion has the following parameter(s):

* string s: a time in **12** hour format
### Returns
* string: the time in **24** hour format

### Input Format

A single string **_s_** that represents a time in **12**-hour clock format (i.e.: **hh:mm:ssAM** or **hh:mm:ssPm**).

### Constraints

* All input times are valid

### Sample Input 0

07:05:45PM

### Sample Output 0

19:05:45

##  My Solution

```javascript
    function timeConversion(s) {
        const y = s.split(':')[0]
        const num = Number(y) + 12
        const am = s.substr(0, s.indexOf('AM'))
        const x = y == 12 ?'12' + s.substr(2,6): num + s.substr(2,6)

        if (s.includes('PM')) {
            return x
        }
        const ans = y == 12 ? '00' +s.substr(2,6) : am
        return ans
    }
```