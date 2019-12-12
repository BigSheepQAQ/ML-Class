#include <bits/stdc++.h>
using namespace std;
int n, m;
string str;
int main()
{
    freopen("VLC.csv", "r", stdin);
    freopen("VLCout.dat", "w", stdout);
    getline(cin, str);
    for (int i = 2; i <= 138; i++)
    {
        getline(cin, str);
        cout << "[" << str << "],\n";
    }
    return 0;
}