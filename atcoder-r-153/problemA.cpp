#include <bits/stdc++.h>
using namespace std;

int n;
string s;

int main()
{
    scanf("%d", &n);
    n += 99999;
    s = to_string(n);
    s = s.substr(0, 1) + s.substr(0, 1) + s.substr(1, 3) + s.substr(3, 1) + s.substr(4, 2) + s.substr(4, 1);
    printf("%s\n", s.c_str());

    return 0;
}