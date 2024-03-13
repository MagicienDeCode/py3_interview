def median_of_array(arr):
    print(arr)
    n = len(arr)
    return arr[n // 2] if n % 2 != 0 else arr[n // 2 - 1]

def median_of_medians(arr):
    subarray_medians = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            subarray_medians.append(median_of_array(subarray))
    subarray_medians.sort()
    return median_of_array(subarray_medians)


print(median_of_medians([1,2,3,4,5]))
print("======================================")

def xiang1(arr):
    res = []
    left = 0
    right = len(arr)
    flag = True
    while left + 1 <= right:
        res += arr[left:right]
        if flag:
            right -= 1
        else:
            left +=1
        flag = not flag
    res.sort()
    print(res)
    n = len(res)
    return res[n // 2] if n % 2 != 0 else res[n // 2 - 1]

print(xiang1([1,2,3,4,5]))