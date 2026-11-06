import java.util.Scanner;

class BankingServices {
    
    static class InvalidMenuException extends Exception {
        InvalidMenuException(String msg) {
            super(msg);
        }
    }

    static class MinimumBalanceException extends Exception {
        MinimumBalanceException(String msg) {
            super(msg);
        }
    }

    static class InsufficientBalanceException extends Exception {
        InsufficientBalanceException(String msg) {
            super(msg);
        }
    }

    static class InvalidAmountException extends Exception {
        InvalidAmountException(String msg) {
            super(msg);
        }
    }

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        double balance = 0;
        int choice;

        try {
            System.out.print("Enter opening balance: ");
            balance = sc.nextDouble();

            if (balance < 1000) {
                throw new MinimumBalanceException(
                    "Opening balance must be at least Rs. 1000."
                );
            }

            System.out.println("\n----- SBI BANKING SERVICES -----");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. Exit");

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            if (choice < 1 || choice > 4) {
                throw new InvalidMenuException(
                    "Invalid menu choice!"
                );
            }

            switch (choice) {

                case 1:
                    System.out.print("Enter deposit amount: ");
                    double deposit = sc.nextDouble();

                    if (deposit <= 0) {
                        throw new InvalidAmountException(
                            "Deposit amount must be greater than zero."
                        );
                    }

                    balance = balance + deposit;

                    System.out.println("Amount deposited successfully.");
                    System.out.println("Current balance = Rs. " + balance);
                    break;

                case 2:
                    System.out.print("Enter withdrawal amount: ");
                    double withdraw = sc.nextDouble();

                    if (withdraw <= 0) {
                        throw new InvalidAmountException(
                            "Withdrawal amount must be greater than zero."
                        );
                    }

                    if (withdraw > balance) {
                        throw new InsufficientBalanceException(
                            "Insufficient balance!"
                        );
                    }

                    if (balance - withdraw < 1000) {
                        throw new MinimumBalanceException(
                            "Minimum balance of Rs. 1000 must be maintained."
                        );
                    }

                    balance = balance - withdraw;

                    System.out.println("Amount withdrawn successfully.");
                    System.out.println("Current balance = Rs. " + balance);
                    break;

                case 3:
                    System.out.println("Current balance = Rs. " + balance);
                    break;

                case 4:
                    System.out.println("Thank you for using SBI Banking Services.");
                    break;
            }
        }

        catch (InvalidMenuException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        catch (MinimumBalanceException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        catch (InsufficientBalanceException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        catch (InvalidAmountException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        finally {
            System.out.println("Transaction completed.");
        }
    }
}