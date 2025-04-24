import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Perguntar o nome
        System.out.println("Qual o seu nome?");
        String nome = scanner.nextLine();  // Lê o nome do usuário

        // Perguntar a idade
        System.out.println("Qual a sua idade?");
        int idade = scanner.nextInt();  // Lê a idade e converte automaticamente para inteiro

        // Exibir a mensagem de saudação
        System.out.println("Olá " + nome + "! Você tem " + idade + " anos.");

        scanner.close();  // Fechar o scanner após o uso
    }
}
