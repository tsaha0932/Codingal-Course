class Volume  {
          public double getVolume() {
                return 0;
         }
 }

class Cube extends Volume{
    private double side;
    public Cube(double side) {
        if (side > 0) {
            this.side = side;
        }
}
public double getVolume() {
    return side * side * side;
}
}

class Cuboid extends Volume{
    private double length;
    private double width;
    private double height;

    public Cuboid(double length, double width, double height) {
        if (length > 0 && width > 0 && height > 0) {
            this.length = length;
            this.width = width;
            this.height = height;
        }
    }

    public double getVolume() {
        return length * width * height;
    }
}

class Mainn {
public static void main(String[] args) {
        Volume [] volume = new Volume[2];
        volume [0] = new Cube(4.0);
        volume [1] = new Cuboid(5.0, 3.0, 6.0);

        System.out.printf("Volume of the Cube: %.2f%n", volume[0].getVolume());
        System.out.printf("Volume of the Cuboid: %.2f%n", volume[1].getVolume());
    }
}