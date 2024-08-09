def pangrams(s):
    # Write your code here
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    hash_table = {}
    is_pangram = True
    
    for char in s.lower():
        if (hash_table.get(char) == None):
            hash_table[char] = 1
    for char in alphabets:
        if hash_table.get(char) == None:
            is_pangram = False
    
    if is_pangram:
        return 'pangram'
    else:
        return 'not pangram'