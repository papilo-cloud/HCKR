def anagram(s):
    # Write your code here
    count = 0
    half_len = len(s) // 2
    right = list(s[half_len:])
    start_index = 0
    
    if len(s) % 2 != 0:
        return -1

    while start_index < half_len:
        if s[start_index] not in right:
            count += 1
        else:
            a = right.index(s[start_index])
            right.pop(a)
        start_index += 1
    return count

print(anagram('fdhlvosfpafhalll'))