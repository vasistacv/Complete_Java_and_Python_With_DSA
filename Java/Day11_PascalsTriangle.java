
/**
 * Day 11: Pascal's Triangle
 * Printing Pascal's Triangle using binomial coefficients.
 * It's actually a pretty cool math trick to calculate the numbers!
 */
import java.util.*;

public class Day11_PascalsTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            // Print spaces
            for (int j = 0; j < n - i; j++) {
                System.out.print(" ");
            }

            int number = 1;
            for (int j = 0; j <= i; j++) {
                System.out.print(number + " ");
                number = number * (i - j) / (j + 1);
            }
            System.out.println();
        }
    }
}
