import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    m = []
    for i in range(8):
        m.append(list(input()))
    word = []
    for i in range(8):
        for j in range(8):
            if m[i][j] != '.':
                while j < 8 and m[i][j] != '.':
                    word.append(m[i][j])
                    j += 1
    sys.stdout.write("".join(word) + "\n")


t = int(input())
for _ in range(t):
    solve()
