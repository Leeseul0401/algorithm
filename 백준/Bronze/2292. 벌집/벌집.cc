#include <iostream>
using namespace std;

int main() {
    int x = 1;
    int N = 0;
    int input = 0;
    
    cin >> input;
    
    while(true) {
        x += (N * 6);
        N++;
        if(x >= input) {
            break;
        }
        
    }
    cout << N << endl;
}