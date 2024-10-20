import java.util.*;

public class Result {
    public static int giveChocolates(List<Integer> ratings) {
        int n = ratings.size();
        if (n == 0) return 0;

        int[] chocolates = new int[n];
        Arrays.fill(chocolates, 1);


        for (int i = 1; i < n; i++) {
            if (ratings.get(i) > ratings.get(i - 1)) {
                chocolates[i] = chocolates[i - 1] + 1;
            }
        }

        
        for (int i = n - 2; i >= 0; i--) {
            if (ratings.get(i) > ratings.get(i + 1)) {
                chocolates[i] = Math.max(chocolates[i], chocolates[i + 1] + 1);
            }
        }

    
        int totalChocolates = 0;
        for (int chocolate : chocolates) {
            totalChocolates += chocolate;
        }

        return totalChocolates;
    }

    public static void main(String[] args) {
        List<Integer> ratings1 = Arrays.asList(1, 0, 2);
        System.out.println(giveChocolates(ratings1));  

        List<Integer> ratings2 = Arrays.asList(1, 2, 2);
        System.out.println(giveChocolates(ratings2)); 
    }
}

