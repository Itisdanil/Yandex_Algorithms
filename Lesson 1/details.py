n, k, m = map(int,input().split())
def details(n, m, k):
    count = 0
    if m <= k:
        while n >= k:
            count_zag = n // k
            n_ost = n % k
            count_det_s_zag = k // m
            izl = k % m
            count += count_zag * count_det_s_zag
            n = n_ost + (izl * count_zag)
    return count
print(details(n, m, k))