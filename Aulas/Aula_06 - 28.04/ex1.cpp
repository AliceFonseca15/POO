// Revisão da introdução em POO
#include <iostream>
#include <string>

// & mostra o valor que está na variavel

int main(){

    int x = 0;  //A variavel é uma instância de tipo 
    int c = 5;
    int z = 0;

    // Python
    // x = 0  --> A variavel é referencia para uma instancia de tipo

    std::cout << x << " " << &x <<std::endl;
    std::cout << c << " " << &c <<std::endl;
    std::cout << z << " " << &z <<std::endl;
}


