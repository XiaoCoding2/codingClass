#include <iostream>
using namespace std;

//continue operation until num ends as 1
bool ends_as_one(int num){
    cout << '|';
    cout << num << '\n';
    while(num!=1){
        if(num%2==0){
            num=num/2;
            cout << num << '\n';
        }
        else if(num%2==1){
            num=(num*3)+1;
            cout << num << '\n';
        }
    }
    cout << '|';
    return true;
}

int main(){
    /*
    for(int i=1;i<100;i++){
        ends_as_one(i);
        cout << '\n';
    }
    */
    ends_as_one(837799); //837,799
    return 0;
}