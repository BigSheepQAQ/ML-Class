#include <bits/stdc++.h>
using namespace std;
int n, m;
string str;
int main()
{
    freopen("VLC.txt", "r", stdin);
    freopen("VLCout.dat", "w", stdout);
    getline(cin, str);
    cout << "dataSet=[\n";
    for (int i = 2; i <= 138; i++)
    {
        getline(cin, str);
        cout << "[" << str << "],\n";
    }
    cout << "]";
    return 0;
}