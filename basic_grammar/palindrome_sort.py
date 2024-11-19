def sort_palindrome(s:str) -> str:
    half = sorted(s[:len(s)//2])
    if len(s)%2 == 0: return ''.join(half) + ''.join(half[::-1])
    return ''.join(half) + s[len(s)//2] +''.join(half[::-1])

    """
    n = len(s)
    count = [0] * 26
    for c in s:
        count[ord(c)-97] += 1
    res = ['0'] * n
    next_index = 0
    for i in range(26):
        while count[i] > 0:
            current_char = chr(97+i)
            res[next_index] = current_char
            res[n-1-next_index] = current_char
            next_index += 1
            count[i] -= 2
    return "".join(res)
    """

print(sort_palindrome("baab"))
print(sort_palindrome("babab"))
print(sort_palindrome("cbaabc"))

print(sort_palindrome("baaab"))


    