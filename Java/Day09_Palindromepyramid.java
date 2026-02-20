
/**
 * Day 09: Palindrome Pyramid
 * This one is cool! It prints numbers that look the same forward and backward.
 * We use spaces for alignment, then count down, then count up.
 */
import java.util.*;

public class Day09_Palindromepyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of n:");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = i; j >= 1; j--) {
                System.out.print(j);
            }
            for (int j = 2; j <= i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }

}
