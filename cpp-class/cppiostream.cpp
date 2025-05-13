
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Redirect standard input and output
    if (!freopen("test.in", "r", stdin) || !freopen("test.out", "w", stdout)) {
        perror("freopen");
        return 1;
    }

    int n;
    cin >> n;                      // now reads from input.in

    vector<int> nums;
    for(int i=0;i<n;++i){
        int x;
        cin >> x;
        nums.push_back(x);
    }

    cout << nums[1] << "\n";           // now writes to output.out

    return 0;
}