
/**
 * Day 06: Inverted Half Pyramid (Rotated 180 deg)
 * Printing a triangle of stars aligned to the right.
 */
import java.util.*;

public class Day06_Invertedpyramidrotate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of n:");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
