
#include <vector>
#include <iostream>
#include <string>

using namespace std;

class Stack{
private:
    vector<int> items;

public:
    void push(int item) {
        items.push_back(item);
    }

    int pop(){
        if(!isEmpty()){
            int topItem=items.back();
            items.pop_back();
            return topItem;
        } else{
            throw out_of_range("Out of range");
        }
    }

    int peek() {
        if(!isEmpty()){
            return items.back();
        } else{
            throw out_of_range("Out of range");
        }
    }

    bool isEmpty() {
        return items.empty();
    }

    int size() {
        return items.size();
    }
};

string reverse(const string& s){
    Stack k;
    string r_str="";
    for(char lttr : s){
        k.push(lttr);
    }
    while(!k.isEmpty()){
        r_str+=k.peek();
        k.pop();
    }
    return r_str;
}

bool palindrome(const string& s){
    string reversed=reverse(s);
    if (reversed==s){
        return true;
    }
    return false;
}

int main() {
    Stack s;
    s.push(1);
    s.push(2);
    s.push(3);

    cout << "peek " << s.peek() << endl;

    string input="Hello";
    string output=reverse(input);
    cout << output << endl;

    cout << palindrome("racecar") << endl;
//    cout << "Stack size: " << s.size() << endl;
//
//    cout << "Popped element: " << s.pop() << endl;
//    cout << "Stack size after pop: " << s.size() << endl;
//
}

