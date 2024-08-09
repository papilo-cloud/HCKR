1. [Alternating Characters]() You are given a string containing characters **_A_** and **_B_** only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

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
