#include <bits/stdc++.h>
using namespace std;

#define VI vector<int>
#define pb push_back

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

const int N = 210000;
int i, u, v, n, m, r, vis[N];
VI e[N];

void dfs(int v)
{
    vis[v] = 1;
    ++r;
    if (r >= 1000000)
    {
        cout << r << '\n';
        exit(0);
    }
    for (auto u : e[v])
    {
        if (!vis[u])
            dfs(u);
    }
    vis[v] = 0;
}

int main()
{
    cin >> n >> m;
    for (i = 0; i < m; ++i)
    {
        cin >> u >> v;
        e[u].pb(v);
        e[v].pb(u);
    }
    r = 0;
    dfs(1);
    cout << r << '\n';
}