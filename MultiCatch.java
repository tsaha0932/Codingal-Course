import java.util.Scanner;

class ExceptionHandling {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter first number: ");
            int x = Integer.parseInt(sc.nextLine());

            System.out.print("Enter second number: ");
            int y = Integer.parseInt(sc.nextLine());

            int z = x / y;

            System.out.println("Result = " + z);
        }

        catch (ArithmeticException | NumberFormatException e) {
            System.out.println("Exception: " + e);
        }

        try {
            int arr[] = new int[2];

            System.out.println("\nEnter 2 numbers:");

            for (int i = 0; i < 2; i++) {
                arr[i] = Integer.parseInt(sc.nextLine());
            }

            System.out.println("Third element = " + arr[2]);
        }

        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception: " + e);
        }
    }
}