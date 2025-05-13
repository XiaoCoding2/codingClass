
#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
using namespace std;


int main(){
    ifstream infile("data.in");
    ofstream outfile("data.out");
    int n;
    infile >> n;
    vector<vector<int>> moves(n);
    for (int i=0;i<n;++i){
        int a, b, g;
        infile >> a >> b >> g;
        moves[i] = {a, b, g};
        cout << a << " " << b << " " << g << endl;
    }
    array<int,3> cups;
    cups={1,2,3};
    vector<int> choices;
    choices={};
    for(auto line:moves){
        int cup1=line[0];
        int cup2=line[1];
        int guess=line[2];
        int temp=cups[cup1-1];
        cups[cup1-1]=cups[cup2-1];
        cups[cup2-1]=temp;
        choices.push_back(cups[guess-1]);
    }
    //for(auto choice:choices){
    //cout << choice << endl;}
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
    outfile << points << endl;
    infile.close();
    outfile.close();
}