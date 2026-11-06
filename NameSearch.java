import java.util.ArrayList;
import java.util.Scanner;

class NameSearch {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<String>();

        System.out.print("Enter number of names: ");
        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter name: ");
            String name = sc.nextLine();
            names.add(name);
        }

        System.out.print("Enter name to search: ");
        String search = sc.nextLine();

        names.forEach(name -> {
            if (name.equalsIgnoreCase(search)) {
                System.out.println("Eureka");
            }
        });
    }
}