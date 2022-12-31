#include <bits/stdc++.h>
using namespace std;

#define vi vector<int>

int t, n, i, j, k, l, l2;

int main()
{
    cin >> t;

    for (i = 0; i < t; ++i)
    {
        cin >> n;
        vi arr(n, 0);

        j = 1;
        k = 0;
        l = 1;
        while (j <= n)
        {
            while (arr[k] != 0)
            {
                k = (k + 1) % n;
            }
            l2 = l++;
            while (l2 > 0)
            {
                k = (k + 1) % n;
                while (arr[k] != 0)
                {
                    k = (k + 1) % n;
                }
                --l2;
            }
            arr[k] = j++;
        }

        for (j = 0; j < n; ++j)
        {
            cout << arr[j];
            if (j != n - 1)
            {
                cout << ' ';
            }
        }
        cout << '\n';
    }

    return 0;
}