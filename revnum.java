import java.util.Scanner;
class revnum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();
        int temp = 0;
        int orgnum = num; 
        while (num != 0) {
            int a = num % 10;     
            temp = temp * 10 + a; 
            num = num / 10;       
        }
        
        System.out.println("The original number was: " + orgnum);
        System.out.println("The reversed number is: " + temp); 
    }
}
