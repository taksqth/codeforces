from collections import Counter
import io, os, sys

input = lambda: io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    _ = int(input().decode())
    a = list(map(int, input().decode().split()))
    cnt = Counter()
    for el in a:
        cnt[el] += 1
    if all([value % 2 == 0 for value in cnt.values()]):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


t = int(input().decode())
for _ in range(t):
    solve()
