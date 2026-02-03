/**
 * Day 04: Switch Case Button Selector
 * Same button problem but using switch instead of if-else.
 * Switch is cleaner when you have multiple exact value checks.
 */

import java.util.*;

public class Day04_Switch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of button:");
        int button = sc.nextInt();
        
        // Using switch case to handle different button values
        switch (button) {
            case 1:
                System.out.println("Music");
                break;
            case 2:
                System.out.println("Video");
                break;
            case 3:
                System.out.println("Nothing");
                break;
            default:
                System.out.println("Invalid Button");
                break;
        }
        sc.close();

    }
}
