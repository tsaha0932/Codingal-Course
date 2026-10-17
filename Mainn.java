class Mainn {
    public static void main(String[] args) {
        Objects obj = new Sphere(); //object of sphere
        obj.showShape();
        obj = new Cuboid(); //object of cuboid
        obj.showShape();
        obj = new Prism(); //object of prism
        obj.showShape();
        obj.shape();
    }
}
