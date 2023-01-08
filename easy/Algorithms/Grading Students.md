# Grading Students

HackerLand University has the following grading policy:

* Every student receives a **_grade_** in the inclusive range from **0** to **100**.
* Any grade less than **40** is a failing grade.

Sam is a professor at the university and likes to round each student's **_grade_** according to these rules:

* If the difference between the **_grade_** and the next multiple of 5 is less than 3, round **_grade_** up to the next multiple of 5.
* If the value of **_grade_** is less than 38, no rounding occurs as the result will still be a failing grade.
### Examples

* **_grade_** = **84** round to **85** (85 - 84 is less than 3)
* **_grade_** = **29** do not round (result is less than 40)
* **_grade_** = **57** do not round (60 - 57 is 3 or higher)

Given the initial value of **_grade_** for each of Sam's **_n_** students, write code to automate the rounding process.

### Function Description

Complete the function gradingStudents in the editor below.

gradingStudents has the following parameter(s):

* int grades[n]: the grades before rounding
### Returns
* int[n]: the grades after rounding as appropriate

### Input Format

The first line contains a single integer, **_n_**, the number of students.

Each line **_i_** of the **_n_** subsequent lines contains a single integer, **grades[_i_]**.

### Constraints
* **1 <= _n_ 60**
* **1 <= _grades_[_i_] 100**

### Sample Input 0
<pre>
4
73
67
38
33
</pre>

### Sample Output 0
<pre>
75
67
40
33
</pre>

### Explanation 0

![image](https://s3.amazonaws.com/hr-challenge-images/0/1484768684-54439977a1-curving2.png "curving2")

1. Student **1** received a **73**, and the next multiple of **5** from **73** is **75**. Since **75 - 73 < 3**, the student's grade is rounded to **75**.
1. Student **2** received a **67**, and the next multiple of **5** from **67** is **70**. Since **70 - 67 = 3**, the grade will not be modified and the student's final grade is **67**.
1. Student **3** received a **38**, and the next multiple of **5** from **38** is **40**. Since **40 - 38 < 3**, the student's grade will be rounded to **40**.
1. Student **4** received a grade below **33**, so the grade will not be modified and the student's final grade is **33**.

## My Solution

