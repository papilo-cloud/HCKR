# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    hash_table = {}
    chrs = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(h)):
        hash_table[chrs[i]] = h[i]
    
    n = len(word)
    maxx = 0
    for i in range(n):
        maxx = max(maxx, hash_table[word[i]])
    return maxx * n