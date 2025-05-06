
#include <iostream>
using namespace std;
int main(){
    int x;
    int a;
    int b;
    //
    x=5;
    a=x++;
    b=++x;
    cout << a << ' ' << b << ' ' << x << endl;
}