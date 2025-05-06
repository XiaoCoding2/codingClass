
#include <iostream>
using namespace std;

int notmain(){
    /*
    int arr[] = {1,2,3,4};
    int* ptr = arr;
    cout << " -val & ptr- " << *ptr;
    ptr++;
    cout << " -val & ptr- " << *ptr;
    return 0;
    */
    
}

int main2() {
    int a = 5;
    int* ptr = &a;
    int** pptr = &ptr;
    //
    cout << "Value of a: " << a << endl;  // 5
    cout << "Value at ptr: " << *ptr << endl;  // 5
    cout << "Value at pptr: " << **pptr << endl;  // 5
    //
    return 0;
}



int main() {
    main2();
    /*
    int size;
    cout << "Enter size of array: ";
    cin >> size;
    int* arr = new int[size]; // Allocate array
    for (int i = 0; i < size; i++) {
        arr[i] = i * 10;  // Assign values
    }
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    delete[] arr;  // Free memory
    return 0;
    */
    return 0;
}