import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class SignInAndLogin {
    private static Map<String, String> users = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("1. Sign Up");
            System.out.println("2. Login");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();

            switch (option) {
                case 1:
                    signUp(scanner);
                    break;
                case 2:
                    login(scanner);
                    break;
                case 3:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid option. Please choose again.");
            }
        }

        System.out.println("Exiting the program.");
        scanner.close();
    }

    private static void signUp(Scanner scanner) {
        System.out.print("Enter username: ");
        String username = scanner.next();
        System.out.print("Enter password: ");
        String password = scanner.next();

        users.put(username, password);
        System.out.println("User registered successfully.");
    }

    private static void login(Scanner scanner) {
        System.out.print("Enter username: ");
        String username = scanner.next();
        System.out.print("Enter password: ");
        String password = scanner.next();

        if (users.containsKey(username) && users.get(username).equals(password)) {
            System.out.println("Login successful. Welcome, " + username + "!");
        } else {
            System.out.println("Invalid username or password. Please try again.");
        }
    }
}
