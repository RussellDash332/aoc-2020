import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long m = 20201227, p = 0, s = 1, a = 1, b = -1, f = 1;
        long cpk = sc.nextLong();
        long dpk = sc.nextLong();

        while (p <= m) {
            if (s % m == cpk) {
                a = p;
            }
            if (s % m == dpk) {
                b = p;
            }
            if (a > 0 && b > 0) {
                break;
            }
            p++;
            s = (s * 7) % m;
        }
        for (int i = 0; i < a; i++) {
            f = (f * s) % m;
        }
        System.out.println("Part 1: " + f);
        System.out.println("Part 2: THE END!");
    }
}