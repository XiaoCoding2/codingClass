#include <iostream>
using namespace std;

int main(){
    for(int i=1;i<=9;i++){
        float B=9.51+(0.001*i);
        float eq=B*B+B;
        if(eq==100){
            cout << B;
            break;
        }
        cout << B << ',' << eq << '\n';
    }
    cout << "\nfinished";
    return 0;
}