1. [Alternating Characters](https://github.com/papilo-cloud/HCKR/blob/main/Javascript/Algorithms/alternatingCharacters.js) You are given a string containing characters **_A_** and **_B_** only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

    Your task is to find the minimum number of required deletions.

    ### Example
    **_s_ = _AABAAB_**

    Remove an **_A_** at positions **0** and **3** to make **_s_ = _ABAB_** in **2** deletions.

    ### Function Description

    Complete the alternatingCharacters function in the editor below.

    alternatingCharacters has the following parameter(s):

    * string s: a string

    ### Returns

    * int: the minimum number of deletions required

    ### Input Format

    The first line contains an integer **_q_**, the number of queries.

    The next **_q_** lines each contain a string **_s_** to analyze.

    ### Constraints
    * **1 <= _q_ <= 10**
    * **1 <= length of _s_ <= 10<sup>5</sup>**

    * Each string **_s_** will consist only of characters **_A_** and **_B_**.

    ### Sample Input
    <pre>
    5
    AAAA
    BBBBB
    ABABABAB
    BABABA
    AAABBB
    </pre>

    ### Sample Output
    <pre>
    3
    4
    0
    0
    4
    </pre>

    ### Explanation

    The characters bolder are the ones that can be deleted so that the string does not have matching adjacent characters.

    A**AAA** -> A (3 deletions)<br>
    B**BBBB** -> B (4 deletions)<br>
    ABABABAB -> ABABABAB (0 deletions)<br>
    BABABA -> BABABA (0 deletions)<br>
    A**AA**B**BB** -> AB (4 deletions)

2.[Angry Professor](https://github.com/papilo-cloud/HCKR/blob/main/Javascript/Algorithms/angryProfessor.js) A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (**_arrivalTime_ <= 0**) to arrived late (**_arrivalTime_ > 0**).

    Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

    ### Example

    **_n_ = 5**

    **_k_ = 3**

    **_a_ = [-2,-1,0,1,2]**

    The first **3** students arrived on. The last **2** were late. The threshold is **3** students, so class will go on. Return YES.

    **Note**: Non-positive arrival times (**_a_[_i_] <= 0**) indicate the student arrived early or on time; positive arrival times (**_a_[_i_] > 0**) indicate the student arrived **_a_[_i_]** minutes late.

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
    * **1 <= _k_ <= _n_**
    * **-100 <= _a_[_i_] <= 100, _where i_ E [1,..._n_]**

    ### Sample Input

    2

    4 3

    -1 -3 4 2

    4 2

    0 -1 2 1

    ### Sample Output

    YES

    NO

    ### Explanation

    For the first test case, **_k_ = 3**. The professor wants at least **3** students in attendance, but only **2** have arrived on time ( **-3** and **-1**) so the class is cancelled.

    For the second test case, **_k_ = 2**. The professor wants at least **2** students in attendance, and there are **2** who arrived on time (**0** and -**1**). The class is not cancelled.

3. [Beautiful Days at the Movies](https://github.com/papilo-cloud/HCKR/blob/main/Javascript/Algorithms/beautifulDays.js) Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number **12**, its reverse is 21. Their difference is **9**. The number **120** reversed is **21**, and their difference is **99**.

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
4. [Bill Division](https://github.com/papilo-cloud/HCKR/blob/main/Javascript/Algorithms/billDivision.js) Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

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

5. [Camel Case](https://github.com/papilo-cloud/HCKR/blob/main/Javascript/Algorithms/camelCase.js) There is a sequence of words in CamelCase as a string of letters, **_s_**, having the following properties:

    * It is a concatenation of one or more words consisting of English letters.
    * All letters in the first word are lowercase.
    * For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

    Given **_s_**, determine the number of words in **_s_**.

    ### Example
    **_s_ = _oneTwoThree_**

    There are **3** words in the string: 'one', 'Two', 'Three'.

    ### Function Description

    Complete the camelcase function in the editor below.

    camelcase has the following parameter(s):

    * string s: the string to analyze
    ### Returns

    * int: the number of words in **_s_**
    ### Input Format

    A single line containing string **_s_**.

    ### Constraints
    * **1 <= length of _s_ <= 10<sup>5</sup>**

    ### Sample Input
    <pre>
    saveChangesInTheEditor
    </pre>
    ### Sample Output
    <pre>
    5
    </pre>
    ### Explanation

    String **_s_** contains five words:

    1. save
    1. Changes
    1. In
    1. The
    1. Editor

6. [Compare The Triple](https://github.com/papilo-cloud/HCKR/blob/main/Javascript/Algorithms/compareTriplet.js) Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

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
