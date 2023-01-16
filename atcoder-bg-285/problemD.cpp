#include <bits/stdc++.h>
#define L(i, j, k) for (int i = (j); i <= (k); ++i)
#define R(i, j, k) for (int i = (j); i >= (k); --i)
#define ll long long
#define sz(a) ((int)(a).size())
#define vi vector<int>
#define me(a, x) memset(a, x, sizeof(a))
#define ull unsigned long long
#define ld __float128
#define pb push_back

using namespace std;

#define MAXN 200005

int n, cnt;
string s, t;
map<string, int> m;
int color[MAXN];
vi graph[MAXN];

void dfs(int i)
{
    if (color[i] == 2)
        return;
    color[i] = 1;
    for (auto n : graph[i])
    {
        if (color[n] == 1)
        {
            cout << "No\n";
            exit(0);
        }
        dfs(n);
    }
    color[i] = 2;
}

int main()
{
    ios ::sync_with_stdio(false);
    cin >> n;
    L(i, 0, n - 1)
    {
        cin >> s >> t;
        if (!m[s])
            m[s] = ++cnt;
        if (!m[t])
            m[t] = ++cnt;
        graph[m[s]].pb(m[t]);
    }
    L(i, 1, cnt)
    {
        dfs(i);
    }
    cout << "Yes\n";
    return 0;
}