#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll i, j, q, qt, x, k;

int main()
{
    scanf("%lld", &q);
    multiset<ll> s;
    for (i = 0; i < q; ++i)
    {
        scanf("%lld %lld", &qt, &x);
        if (qt == 1)
        {
            s.insert(x);
        }
        else if (qt == 2)
        {
            scanf("%lld", &k);
            auto it = s.upper_bound(x);
            for (j = 0; it != s.begin() && j < k; --it, ++j)
            {
            }
            printf("%lld\n", (j < k) ? -1 : *it);
        }
        else
        {
            scanf("%lld", &k);
            auto it = s.lower_bound(x);
            for (j = 1; it != s.end() && j < k; ++it, ++j)
            {
            }
            printf("%lld\n", (it == s.end()) ? -1 : *it);
        }
    }

    return 0;
}