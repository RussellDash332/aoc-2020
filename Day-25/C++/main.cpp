#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    long long m = 20201227, cpk, dpk, p = 0, s = 1, a = 1, b = -1, f = 1;
    cin >> cpk >> dpk;

    while (p <= m) {
        if (s % m == cpk) {
            a = p;
        }
        if (s % m == dpk) {
            b = p;
        }
        if (a > 0 && b > 0) {
            break;
        }
        p++;
        s = (s * 7) % m;
    }
    for (int i = 0; i < a; i++) {
        f = (f * s) % m;
    }
    cout << "Part 1: " << f << endl;
    cout << "Part 2: THE END!" << endl;

    return 0;
}