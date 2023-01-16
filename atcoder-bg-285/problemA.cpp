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

int a, b;

int main()
{
    ios ::sync_with_stdio(false);
    cin >> a >> b;
    if (a > b)
    {
        swap(a, b);
    }
    cout << (b / 2 == a ? "Yes" : "No") << '\n';
    return 0;
}