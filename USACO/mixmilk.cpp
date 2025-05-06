
#include <iostream>
#include <string>
#include <array>
using namespace std;

array<int,2> pour_milk(int amount1,int amount2,int limit2){
    int amount1_new;
    int amount2_new;
    array<int,2> arr;
    if (amount1 + amount2 <= limit2){
        amount1_new = 0;
        amount2_new = (amount1 + amount2);
    }
    else{
        amount2_new = limit2;
        amount1_new = (amount1+amount2)-limit2;
    }
    arr = {amount1_new, amount2_new};
    return arr;
}

int main(){
    /*
    20 20
    15 0
    14 7
    */
    int c1=20;
    int m1=20;
    int c2=15;
    int m2=0;
    int c3=14;
    int m3=7;
    int count=0;
    array<int,2> arr2;
    for(int i=0;i<100;i++){
        count+=1;
        if(count==1){
            arr2 = pour_milk(m1, m2, c2);
            m1=arr2[0];
            m2=arr2[1];
        }
        if(count==2){
            arr2 = pour_milk(m2, m3, c3);
            m2=arr2[0];
            m3=arr2[1];
        }
        if(count>=3){
            arr2 = pour_milk(m3, m1, c1);
            m3=arr2[0];
            m1=arr2[1];
            count=0;
        }
    }
    cout << m1 << endl;
    cout << m2 << endl;
    cout << m3 << endl;
    return 0;
}