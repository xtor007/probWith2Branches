//
//  main.cpp
//  veryGoodProject
//
//  Created by Anatoliy Khramchenko on 2/20/21.
//  Copyright © 2021 Anatoliy Khramchenko. All rights reserved.
//

#include <iostream>
using namespace std;

int AnatoliyTop (int a) {
    if (a == 6) {
        return 4;
    } else {
        return a;
    }
}



int main(int argc, const char * argv[]) {
    cout << "Yarik loh";
    cout << "Vvedite chyslo";
    int k;
    cin >> k;
    cout << AnatoliyTop(k);
    return 0;
}
