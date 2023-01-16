#include <bits/stdc++.h>
#define L(i, j, k) for (int i = (j); i <= (k); ++i)
#define R(i, j, k) for (int i = (j); i >= (k); --i)
#define ll long long
#define sz(a) ((int)(a).size())
#define vi vector<int>
#define me(a, x) memset(a, x, sizeof(a))
#define ull unsigned long long
#define ld __float128

using namespace std;

ll ret;
ll ex;

int main()
{
    ios ::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string s;
    cin >> s;
    ret = 0;
    ex = 1;
    R(i, s.size() - 1, 0)
    {
        ret += ((int)s[i] - 'A' + 1) * ex;
        ex *= 26;
    }
    cout << ret << '\n';

    return 0;
}