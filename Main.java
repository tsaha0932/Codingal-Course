class Wonders{
    void location(){
        System.out.println("Location is: ");
    }
    void famousfor(){
        System.out.println("Famous for: ");
    }
}

class GreatWallOfChina extends Wonders{
    void location(){
        System.out.println("The Great Wall of China is located in China.");
    }
    void famousfor(){
        System.out.println("Bound together with sticky rice mortar, this 21,196-kilometre structure cannot actually be seen from space with the naked eye.");
    }
}

class Petra extends Wonders{
    void location() {
        System.out.println("Petra is located in Jordan");
    }

    void famousfor() {
        System.out.println(
                "Known as the \"Rose City\" for its pink sandstone cliffs, over 85% of this ancient desert metropolis remains unexcavated underground.");
    }
}

class Colosseum extends Wonders{
    void location() {
        System.out.println("The Colosseum is located in Italy.");
    }

    void famousfor() {
        System.out.println(
                "This massive Roman arena could hold 80,000 spectators for free gladiator games and was even flooded to host mock naval battles.");
    }
}

class ChichenItza extends Wonders{
    void location() {
        System.out.println("The Chichén Itzá is located in Mexico.");
    }

    void famousfor() {
        System.out.println(
                "The central pyramid acts as a 365-step calendar that creates the shadow of a slithering serpent during the spring and autumn equinoxes.");
    }
}

class MachuPichu extends Wonders{
    void location() {
        System.out.println("The Machu Pichu is located in Peru.");
    }

    void famousfor() {
        System.out.println(
                "Built with mortarless, earthquake-proof stones cut so precisely that a knife blade cannot fit between them, 60% of the city lies underground.");
    }
}

class TajMahal extends Wonders{
    void location() {
        System.out.println("The Taj Mahal is located in India.");
    }

    void famousfor() {
        System.out.println(
                "Built in perfect symmetry as a monument of love, its white marble changes colour from pink to gold depending on the time of day.");
    }
}

class Christ extends Wonders{
    void location() {
        System.out.println("The Statue of Christ the Redemeer is located in Brazil.");
    }

    void famousfor() {
        System.out.println(
                "Standing atop a peak in Rio, this 98-foot statue is covered in 6 million soapstone tiles and gets struck by lightning 3 to 6 times a year.");
    }
}

class Main{
    public static void main(String[] args) {
        Wonders A = new Wonders();
        Wonders G = new GreatWallOfChina();
        Wonders P = new Petra();
        Wonders Co = new Colosseum();
        Wonders Ch = new ChichenItza();
        Wonders M = new MachuPichu();
        Wonders T = new TajMahal();
        Wonders Chr = new Christ();

        A.location();
        A.famousfor();

        G.location();
        G.famousfor();

        P.location();
        P.famousfor();

        Co.location();
        Co.famousfor();

        Ch.location();
        Ch.famousfor();

        M.location();
        M.famousfor();

        T.location();
        T.famousfor();

        Chr.location();
        Chr.famousfor();
    }
}