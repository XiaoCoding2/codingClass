
#include <iostream>
#include <vector>
#include <array>
using namespace std;

int main(){
    int num=3;
    array<array<int,3>,num> lines={
        {1, 2, 1},
        {3, 2, 1},
        {1, 3, 1}
    };

    array<int,3> cups={1,2,3};
    vector<int,num> choices={};
    for(auto line:lines){
        int cup1=line[0];
        int cup2=line[1];
        int guess=line[2];
        int temp=cups[cup1-1];
        cups[cup1-1]=cups[cup2-1];
        cups[cup2-1]=temp;
        choices.push_back(cups[guess-1]);
    }
    //
    int good_choice=0;
    for(auto choice:choices){
        if (choice>good_choice){
            good_choice=choice;
        }
    }
    //
    int points=0;
    for(auto choice:choices){
        if(choice==good_choice){
            points++;
        }
    }
    cout << points << endl;
}