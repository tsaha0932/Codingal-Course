class Counter{
    int number=10;
    //static int number=10

    void increment(){
        number=number+1;
    }

    void main(){
        Counter obj1 = new Counter(); 
        Counter obj2 = new Counter();
        Counter obj3 = new Counter();
        //Guess the answer
        obj1.increment(); // 11
        obj2.increment(); // 11
        obj3.increment(); // 11

        //to check your answers uncomment the next lines

        System.out.println(obj1.number);
        System.out.println(obj2.number);
        System.out.println(obj3.number);
    }
}