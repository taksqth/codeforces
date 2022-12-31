#include <bits/stdc++.h>
using namespace std;

#define ll long long
ll mod = 998244353;
ll ret;

int i, j, n, l, l2, l3;

int main()
{
    cin >> n;

    char s[n];
    cin >> s;

    ll dp[27 * 27];
    ll dpn[27 * 27];

    for (i = 0; i < 27 * 27; ++i)
    {
        dp[i] = 0;
    }
    dp[0] = 1;

    for (i = 0; i < n; ++i)
    {
        if (s[i] != '?')
        {
            l = (int)s[i] - 'a' + 1;
            for (j = 0; j < 27 * 27; ++j)
            {
                dpn[j] = 0;
            }
            for (l2 = 0; l2 < 27; ++l2)
            {
                if (l != l2)
                {
                    for (l3 = 0; l3 < 27; ++l3)
                    {
                        if (l != l3)
                        {
                            dpn[l * 27 + l2] += dp[l2 * 27 + l3];
                            dpn[l * 27 + l2] %= mod;
                        }
                    }
                }
            }
        }
        else
        {
            for (l = 1; l < 27; ++l)
            {
                for (l2 = 0; l2 < 27; ++l2)
                {
                    dpn[l * 27 + l2] = 0;
                    if (l != l2)
                    {
                        for (l3 = 0; l3 < 27; ++l3)
                        {
                            if (l != l3)
                            {
                                dpn[l * 27 + l2] += dp[l2 * 27 + l3];
                                dpn[l * 27 + l2] %= mod;
                            }
                        }
                    }
                }
            }
        }
        for (j = 0; j < 27 * 27; ++j)
        {
            dp[j] = dpn[j];
        }
    }

    ret = 0;
    for (i = 0; i < 27 * 27; ++i)
    {
        ret += dp[i];
        ret %= mod;
    }
    cout << ret << '\n';
    return 0;
}