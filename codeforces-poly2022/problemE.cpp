#include <bits/stdc++.h>
using namespace std;

int n, m, mel, d, u, v, i;
bool visited[200005];
unordered_set<int> m1, m2;

tuple<int, int, int, int> dfs(int cur, int depth, vector<int> graph[])
{
    visited[cur] = true;

    int tm1moves = 0;
    int tm2moves = 0;
    int rm1depth = 0;
    int rm2depth = 0;
    int m1moves = 0;
    int m2moves = 0;
    int m1depth = 0;
    int m2depth = 0;

    for (auto ne : graph[cur])
    {
        if (visited[ne])
            continue;
        auto [m1moves, m2moves, m1depth, m2depth] = dfs(ne, depth + 1, graph);
        rm1depth = max(max(rm1depth, m1depth), m2depth - d);
        rm2depth = max(max(rm2depth, m2depth), m1depth - d);
        tm1moves += max(max(0, m1moves - 2 * depth), (m2depth - depth - d) * 2);
        tm2moves += max(max(0, m2moves - 2 * depth), (m1depth - depth - d) * 2);
    }
    if (m1.find(cur) != m2.end())
    {
        rm1depth = max(depth, rm1depth);
    }
    else
    {
        rm1depth = max(0, rm1depth);
    }
    if (m2.find(cur) != m2.end())
    {
        rm2depth = max(depth, rm2depth);
    }
    else
    {
        rm2depth = max(0, rm2depth);
    }

    tm1moves += min(rm1depth, depth) * 2;
    tm2moves += min(rm2depth, depth) * 2;

    return make_tuple(tm1moves, tm2moves, rm1depth, rm2depth);
}

int main()
{
    cin >> n >> d;
    vector<int> graph[n + 1];

    for (i = 0; i < n - 1; ++i)
    {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    cin >> m;
    for (i = 0; i < m; ++i)
    {
        cin >> mel;
        m1.insert(mel);
    }

    cin >> m;
    for (i = 0; i < m; ++i)
    {
        cin >> mel;
        m2.insert(mel);
    }

    auto r = dfs(1, 0, graph);
    cout << get<0>(r) + get<1>(r) << '\n';

    return 0;
}
