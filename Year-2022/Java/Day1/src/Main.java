import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filename = "Day1_input.txt";
        int calories = 0;
        List<Integer> elves = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (!line.equals("")) {
                    calories += Integer.parseInt(line);
                } else {
                    elves.add(calories);
                    calories = 0;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        int maxCalories = elves.stream().mapToInt(Integer::intValue).max().orElse(0);
        System.out.println(maxCalories);
    }
}
