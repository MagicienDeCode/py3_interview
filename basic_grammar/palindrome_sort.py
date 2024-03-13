def sort_palindrome(s:str) -> str:
    n = len(s)
    count = [0] * 26
    for c in s:
        count[ord(c)-97] += 1
    res = ['a'] * n
    next_index = 0
    for i in range(26):
        while count[i] > 0:
            current_char = chr(97+i)
            res[next_index] = current_char
            res[n-1-next_index] = current_char
            next_index += 1
            count[i] -= 2
    return "".join(res)

print(sort_palindrome("baab"))
print(sort_palindrome("babab"))
print(sort_palindrome("cbaabc"))


    