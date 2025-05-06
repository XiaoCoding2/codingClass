
#include <iostream>
#include <string>
using namespace std;

int printplane(int plane[3][3]){
    for(int i=0;i<=2;i++){
        for(int n=0;n<=2;n++){
            cout << plane[i][n] << ' ';
        }
        cout << "\n";
    }
    return 0;
}

int inputplane(int plane[3][3]){
    for(int i=0;i<=2;i++){
        for(int n=0;n<=2;n++){
            int x;
            cout << "row " << i << " colomn " << n << ": ";
            cin >> x;
            plane[i][n]=x;
        }
    }
    return 0;
}

int sumplane(int plane[3][3]){
    int curSum=0;
    for(int i=0;i<=2;i++){
        for(int n=0;n<=2;n++){
            curSum+=plane[i][n];
        }
    }
    return curSum;
}

int maxandminplane(int plane[3][3]){
    int curMax=0;
    int curMin=9990;
    for(int i=0;i<=2;i++){
        for(int n=0;n<=2;n++){
            if(plane[i][n]>curMax){
                curMax=plane[i][n];
            }
            if(plane[i][n]<curMin){
                curMin=plane[i][n];
            }
        }
    }
    return curMax; //curMin for Min num
}

int swapplane(int plane[][]){
    int lplane=plane.length()-1;
    for(int i=0;i<=lplane;i++){
        for(int n=0;n<=lplane;n++){
            plane[i][n]=plane[n][i];
        }
    }
    return 0;
}

int main(){
    int plane[3][3]={
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    swapplane(plane);
    cout << printplane(plane);
    cout << maxandminplane(plane) << '\n';
    cout << sumplane(plane) << '\n';
    //printplane(plane);
    return 0;
}