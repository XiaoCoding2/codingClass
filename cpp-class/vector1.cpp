
#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    cout << v[0] << ' ' << v[1] << ' ' << v[2] << endl;
    for(int x=0;x<v.size();x++){
        cout << v[x] << endl;
    }
    for(auto x:v){
        cout << x << endl;
    }
    for(int x=0;x<=3;++x){
        cout << x << endl;
    }
    return 0;
}