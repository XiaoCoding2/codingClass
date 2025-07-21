#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct bigInt {
    vector<int> number;
    bigInt(){}
    bigInt(unsigned int num1){
        switch (num1){
            case 0:
                number.push_back(num1);
                break;
            default:
                while(num1>0){
                    number.push_back(num1%10);
                    num1/=10;
                }
        }
    }
    size_t len(){
        size_t length=number.size();
        return length;
    }
    void append(int num){
        number.push_back(num);
    }
    void print(){
        for(int i=number.size()-1;i>=0;i--){
            cout << number[i];
        }
        cout << '\n';
    }
    int operator[](int idx){
        return number[idx];
    }
    bigInt operator+(bigInt newNum){
        size_t max_len;
        size_t min_len;
        if(number.size()>newNum.len()){
            max_len=number.size();
            min_len=newNum.len();
        }
        else{
            max_len=newNum.len();
            min_len=number.size();
        }
        int carry=0;
        bigInt total;
        for(int i=0;i<min_len;i++){
            int digit_sum=number[i]+newNum[i]+carry;
            carry=0;
            if(digit_sum>9){
                carry=1;
                total.append(digit_sum-10);
            }
            else{
                total.append(digit_sum);
            }
        }
        bool extra=false;
        for(int i=min_len;i<max_len;i++){
            extra=true;
            //temp solution
            //for fib, newNum is always bigger,
            //so we add digits from newNum
            //NOTE: not a permanent solution
            int last_num=carry+newNum[i];
            total.append(last_num);
        }
        if(extra==false and carry==1){
            total.append(carry);
        }
        return total;
    }
};

int main(){
    bigInt num1=0;
    bigInt num2=1;
    bigInt sum;
    for(int i=2;i<=104911;i++){
        sum=num1+num2;
        num1=num2;
        num2=sum;
        cout << "sum=";
        sum.print();
    }
    return 0;
}
