def counting_sort(arr, l, r):
    n = len(arr)
    cnt = [0] * (r - l + 1)
    ret = [0] * n
    for el in arr:
        cnt[el - l] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]
    for i in range(n - 1, -1, -1):
        ret[cnt[arr[i] - l] - 1] = arr[i]
        cnt[arr[i] - l] -= 1
    return ret  # or change arr inplace


print(counting_sort([234, 32512, 64343, 234, 6436, 2423, 6343456], 234, 6343456))
