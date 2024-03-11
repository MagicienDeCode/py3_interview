class Solution20_1:
    """
    main idea, add left parentheses to stack
    when right, verify empty, then verify if pop element and current right can form a correct parenthese
    """
    def isValid(self, s: str) -> bool:
        left_set = {'(','[','{'}
        stack = []
        for c in s:
            if c in left_set:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ']' and top != '[':
                    return False
                if c == ')' and top != '(':
                    return False 
                if c == '}' and top != '{':
                    return False
        return not stack

class Solution20_2:
    """
    main idea, add corresponded right prarentheses when meet left one,
    when right, verify empty, then verify if pop element equals to current one
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            else:
                if (len(stack) == 0) or (stack.pop() != c):
                    return False
        return not stack

class Solution1249:
    """
    main idea, ignore lower case english letters
    iterate given str using its index
    when left parentheses, add it in stack
    when right, if stack is empty, it means that current right one can't form a correct parenthese, so result_char_array[current_right_index] = ''
        if stack is not empty, pop element from stack
    after iteration, if stack is not empty, it means that we have more left parentheses, so result_char_array[all left parenthese's index] = ''
    convert char array to a string
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result_array = [c for c in s]
        for i in range(len(s)):
            ascii_code = ord(s[i])
            if 97 <= ascii_code <= 123:
                continue
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    result_array[i] = ''
                else:
                    stack.pop()
        while len(stack) != 0:
            result_array[stack.pop()] = ''

        return "".join(result_array)