
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
double calc(double a,double b,char c) {
    if(c=='+'){
        return (a+b);
    }
    else if(c=='-'){
        return (a-b);
    }
    else if(c=='*'){
        return (a*b);
    }
    else if(c=='/'){
        return (a/b);
    }
    else{
        std::cout << "ONLY +-*/";
        return 0;
    }
}

int main() {
    double a;
    double b;
    char input;
    cout << "number1 ";
    cin >> a;
    cout << "number2 ";
    cin >> b;
    cout << "input ";
    cin >> input;
    cout << calc(5,2,'/');
    //std::string input;
    //std::cout << "Your name pls: ";
    //std::cin >> input;
    //std::cout << "name = " << input << "\n";
    return 0;  // Return success
}
/*
*/