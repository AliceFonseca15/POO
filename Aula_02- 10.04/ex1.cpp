#include <iostream>
#include <string>

int main() {
    std::string nome;
    int idade;

    // Perguntar o nome
    std::cout << "Qual o seu nome? ";
    std::getline(std::cin, nome);  // Lê o nome do usuário

    // Perguntar a idade
    std::cout << "Qual a sua idade? ";
    std::cin >> idade;  // Lê a idade e converte para inteiro automaticamente

    // Exibir a mensagem de saudação
    std::cout << "Olá " << nome << "! Você tem " << idade << " " << "anos." << std::endl;

    return 0;
}

