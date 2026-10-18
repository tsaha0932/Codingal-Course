class Mainn  {
    public static void main(String[] args) {
        
        //creating an instance of Bicycle
        //doing some operations
        Bicycle bicycle = new Bicycle();
        bicycle.changeGear(2);
        bicycle.speedUp(3);
        bicycle.applyBrakes(1);

        System.out.println("Bicycle present state : ");
        bicycle.printStates();

        //creating instance of the car
        Car car = new Car();
        car.changeGear(1);
        car.speedUp(4);
        car.applyBrakes(3);

        System.out.println("Car present state : ");
        car.printStates();
    }
}
