
#include <iostream>
#include <string>
#include <stdio.h>
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
    std::cout << "number1";
    std::cin >> a;
    std::cout << "number2";
    std::cin >> b;
    std::cout << "input";
    std::cin >> input;
    std::cout << calc(5,2,'/');
    //std::string input;
    //std::cout << "Your name pls: ";
    //std::cin >> input;
    //std::cout << "name = " << input << "\n";
    return 0;  // Return success
}
/*
*/