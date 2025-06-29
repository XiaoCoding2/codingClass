
#include <iostream>
using namespace std;

// Prints Collatz sequence for a given num until it reaches 1
void ends_as_one(int num) {
    cout << '|';
    while (true){
        cout << num << '\n';
        if (num==1){
            break;
        }
        num = (num % 2 == 0) ? num / 2 : num * 3 + 1;
    }
    cout << '|';
}

int main() {
    // Uncomment to test multiple starting numbers
    /*
    for (int i = 1; i < 100; ++i) {
        ends_as_one(i);
        cout << "\n\n";
    }
    */
    ends_as_one(837799); // Test with known longest sequence start
    return 0;
}