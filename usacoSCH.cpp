
//https://usaco.org/index.php?page=viewproblem2&cpid=915
#include <algorithm>
#include <iostream>
#include <array>
#include <cmath>
using namespace std;

class solution{
public:
    void print1(int arr[3]){
        cout << arr[0] << ' ' << arr[1] << ' ' << arr[2] << '\n';
    }
    int min_moves(int locations[3]){
        for(int i=0;;i++){
            sort(locations,locations+3);
            int min_num=locations[0];
            int mid_num=locations[1];
            int max_num=locations[2];
            print1(locations);
            //find distances
            int d_1=mid_num-min_num;
            int d_2=max_num-mid_num;
            int min_d;
            if(d_1<=d_2){min_d=d_1;}
            else{min_d=d_2;}
            //check if herded
            if(d_1==1 and d_2==1){
                return i;
                break;
            }
            if(d_1==1){
                return i+2;
            }
            if(d_2==1){
                return i+2;
            }
            //put farthest in min distance
            if(min_d==d_1){
                locations[2]=min_num+1;
            }
            else if(min_d==d_2){
                locations[0]=mid_num+1;
            }
            else{
                cout << "what?" << '\n';
                break;
            }
        }
        return 0;
    }
    int max_moves(int locations[3]){
        print1(locations);
        int min_num=locations[0];
        int mid_num=locations[1];
        int max_num=locations[2];
        //
        int d_1=mid_num-min_num;
        int d_2=max_num-mid_num;
        //
        int max_d;
        if(d_1>=d_2){
            max_d=d_1;
        }
        else{
            max_d=d_2;
        }
        return max_d-1;
    }
};
int main(){
    //min func doesn't work for below test case (5)
    int arr[3]={4, 100, 200};
    int arr2[3];
    copy(arr,arr+3,arr2);
    solution sol;
    cout << sol.min_moves(arr) << '\n';
    cout << sol.max_moves(arr2) << '\n';
    return 0;
}