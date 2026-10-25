//Main.java
import java.util.Scanner;
public class Mainn {
    public static Candidate getCandidateDetails() throws InvalidInternException{
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Candidate Details: ");
        System.out.println("Name: ");
        String name = sc.next();

        System.out.println("Gender: ");
        String gender = sc.next();

        System.out.println("Enter percentage in 10th: ");
        int percentage = sc.nextInt();
        if(percentage < 50){
            throw new InvalidInternException("Registration Failed. Percentage cannot  be less than 50%.");
        } else {
            Candidate candidate = new Candidate();
            candidate.setName(name);
            candidate.setGender(gender);
            candidate.setPercentage(percentage);

            return candidate;
        }
    }

    public static void main(String [] args){
        System.out.println("Welcome to InterHiring Tool");

        try{
            Candidate candidate = getCandidateDetails();
            System.out.println("Registration Successful");
        } catch (InvalidInternException e) {
            System.out.println(e.getMessage());
        }
    }
}