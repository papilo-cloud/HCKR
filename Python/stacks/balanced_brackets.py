def isBalanced(s):
    # Write your code here
    stack = []
    
    def main(string):
        for i in string:
            if opening_braces(i):
                stack.append(i)
            elif closing_braces(i):
                if not stack:
                    return 'NO'
                popped_brace = stack.pop()
                if not_a_match(popped_brace, i):
                    return 'NO'
                    
        if stack:
            return 'NO'
        return 'YES'
    
    def opening_braces(char):
        return char in ['{', '[', '(']
    
    def closing_braces(char):
        return char in ['}', ']', ')']
    
    def not_a_match(start, end):
        char = {'{': '}', '[': ']', '(': ')'}
        return char[start] != end

    return main(s)
