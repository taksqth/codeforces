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

int n;

int main()
{
    ios ::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string s;

    cin >> n;
    cin >> s;

    L(i, 1, n - 1)
    {
        L(j, 0, n - 1 - i)
        {
            if (s[j] == s[j + i])
            {
                cout << j << '\n';
                break;
            }
            if (j + i == n - 1)
            {
                cout << n - i << '\n';
            }
        }
    }

    return 0;
}