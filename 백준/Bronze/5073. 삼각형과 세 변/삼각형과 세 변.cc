#include <iostream>
#include <algorithm>
using namespace std;

int main() {

    int A;
    int B;
    int C;
    


    
    while(true) {
        cin >> A >> B >> C;
        if(A == 0 || B == 0 || C == 0) break;
        int longest = A;
        int sumOther = B + C;

        if(B > longest) { longest = B; sumOther = A + C;};
        if(C > longest) { longest = C; sumOther = A + B;};
        if(longest >= sumOther) {
            
            cout << "Invalid" << endl;
        } else {
            if(A == B && A == C && B == C) {
                cout << "Equilateral" << endl;
            } else if(A == B || A == C || B == C) {
                cout << "Isosceles" << endl;
            } else {
                cout << "Scalene" << endl;
            }
        };

        
        
        
        
    }
    return 0;
}