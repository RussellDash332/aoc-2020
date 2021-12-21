#include <bits/stdc++.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    vector<int> v;
    string m;
    int sum = 0, mini = 0, maxi = 0;

    while (cin >> m) {
        int r = 0, c = 0;
        for (int i = 0; i < 7; i++) {
            r *= 2;
            r += (m[i] == 'B');
        }
        for (int i = 7; i < 10; i++) {
            c *= 2;
            c += (m[i] == 'R');
        }
        int id = 8 * r + c;
        maxi = max(maxi, id);
        if (mini == 0) {
            mini = id;
        } else {
            mini = min(mini, id);
        }
        v.push_back(id);
    }

    cout << "Part 1: " << maxi << endl;

    for (int i = mini; i <= maxi; i++) {
        sum += i;
    }
    for (int i = 0; i < v.size(); i++) {
        sum -= v[i];
    }
    cout << "Part 2: " << sum << endl;

    return 0;
}