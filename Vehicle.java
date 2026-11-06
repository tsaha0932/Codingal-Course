import java.util.Scanner;

class Vehicle {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter vehicle type (Truck/Bike): ");
        String vehicle = sc.nextLine();
        System.out.print("Enter current speed: ");
        int speed = Integer.parseInt(sc.nextLine());

        if (vehicle.equalsIgnoreCase("Truck")) {
            speed = speed + 20;
        }
        else if (vehicle.equalsIgnoreCase("Bike")) {
            speed = speed + 10;
        }
        else {
            System.out.println("Invalid vehicle type!");
            return;
        }
        System.out.println("Current speed of " + vehicle + " = " + speed + " km/h");
    }
}