# include <iostream>
int main() {
    int num1, num2;
    std::cout << "Ingrese el primer numero: " << std::endl;
    std::cin >> num1;
    std::cout << "Ingrese el segundo numero: " << std::endl;
    std::cin >> num2;

    if (num1 > num2) {
        std::cout << "El primer numero es mayor." << std::endl;
    } else if (num1 < num2) {
        std::cout << "El segundo numero es mayor." << std::endl;
    } else {
        std::cout << "Ambos numeros son iguales." << std::endl;
    }
    
    return 0;
    
}
