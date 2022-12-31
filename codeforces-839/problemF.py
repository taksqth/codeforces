def solve():
    n, m, k = map(int, input().split())

    mxs = [[] for _ in range(k + 1)]
    for i in range(k + 1):
        input()
        for _ in range(n):
            mxs[i].append(list(map(int, input())))

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    possible_moves = []
    for mx in mxs:
        possible_moves.append(set())
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                tcolor = mx[i][j]
                if all([mx[i + oi][j + oj] != tcolor for oi, oj in dirs]):
                    possible_moves[-1].add((i, j))
    possible_moves = [(len(moves), i, moves) for i, moves in enumerate(possible_moves)]
    possible_moves = list(sorted(possible_moves, reverse=True))
    print(possible_moves[0][1] + 1)
    _, _, moves = possible_moves[0]
    smoves = []
    for j, (_, i, nmoves) in enumerate(possible_moves[1:]):
        for mi, mj in moves.difference(nmoves):
            if mxs[i][mi][mj] != mxs[possible_moves[j][1]][mi][mj]:
                smoves.append(f"1 {mi+1} {mj+1}")
        moves = nmoves
        smoves.append(f"2 {i+1}")
    print(len(smoves))
    for smove in smoves:
        print(smove)


solve()
