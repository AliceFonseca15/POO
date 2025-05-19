using System;

class Program
{
    static void Main()
    {
        // Perguntar o nome
        Console.WriteLine("Qual o seu nome?");
        string nome = Console.ReadLine();  // Lê o nome do usuário

        // Perguntar a idade
        Console.WriteLine("Qual a sua idade?");
        int idade = int.Parse(Console.ReadLine());  // Lê e converte a idade para inteiro

        // Exibir a mensagem de saudação
        Console.WriteLine($"Olá {nome}! Você tem {idade} anos.");
    }
}
