import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Main {

    public static void main(String[] args) {
        /*String absolutePath = "E:\\Advent of Code\\AD2024\\day8_Resonant_Collinearity\\src\\example.txt";*/

        String currentDir = System.getProperty("user.dir");
        //String filePath = currentDir + "\\src\\example.txt";
        String filePath = currentDir + "\\src\\input.txt";

        ArrayList<String> initBatch = new ArrayList<String>();
        ArrayList<String> expected = new ArrayList<String>();
        ArrayList<String> funnel = initBatch;

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            System.out.println("Found file: " + filePath);
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.isEmpty()) {
                    funnel = expected;
                }
                funnel.add(line);

            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            System.out.println("Error opening file");
        }

        partOne(initBatch);

        if (!expected.isEmpty()) {
            expected.removeFirst();
            expected.removeFirst();
            //do testing here
        } else {
            System.out.println("No test case provided.");
        }

        partTwo(initBatch);

    }

    public static class Coords {
        char name;
        int x;
        int y;
        public Coords(int x, int y, char name) {
            this.name = name;
            this.x = x;
            this.y = y;
        }
    }

    public static ArrayList<ArrayList<Coords>> parseInputToBuckets(ArrayList<String> arr) {
        ArrayList<Coords> tempAntennas = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0, n = arr.get(i).length(); j < n; j++) {
                char c = arr.get(i).charAt(j);
                if (c != '.') {
                    Coords an = new Coords(j, i, c);
                    tempAntennas.add(an);
                }
            }
        }
        //sortCoords(tempAntennas);
        tempAntennas.sort( (a, b) -> { return a.name - b.name; });
        //pass antenna groups to buckets
        ArrayList<ArrayList<Coords>> buckets = new ArrayList<>();
        char lastName = '.';
        for (Coords ant : tempAntennas) {
            char currName = ant.name;
            if (currName != lastName) {
                buckets.add(new ArrayList<>());
            }
            buckets.getLast().add(ant);
            lastName = buckets.getLast().getLast().name;
        }
        return buckets;
    }

    public static void sortCoords(ArrayList<Coords> arr) {
        boolean swapDone = false;
        do {
            for (int i = 0, n = arr.size() - 1; i < n; i++) {
                if (arr.get(i).name > arr.get(i + 1).name) {
                    Collections.swap(arr, i, i + 1);
                    swapDone = true;
                }
            }
        } while (!swapDone);
    }

    public static void partOne(ArrayList<String> arr) {
        int maxHorizontal = arr.getFirst().length() - 1;
        int maxVertical = arr.size() - 1;
        HashSet<String> antinodesPositions = new HashSet<String>();

        ArrayList<ArrayList<Coords>> buckets = parseInputToBuckets(arr);
        //calculate antinodes' positions
        for (ArrayList<Coords> bucket : buckets) {
            int index = 0;
            for (Coords antenna : bucket) {
                for (int i = 0, n = bucket.size(); i < n; i++) {
                    if (i == index) {
                        continue;
                    }
                    int verticalDiff = 2 * (antenna.y - bucket.get(i).y);
                    int horizontalDiff = 2 * (antenna.x - bucket.get(i).x);
                    int antinodeX = antenna.x - horizontalDiff;
                    if (antinodeX < 0 || antinodeX > maxHorizontal) {
                        continue;
                    }
                    int antinodeY = antenna.y - verticalDiff;
                    if (antinodeY < 0 || antinodeY > maxVertical) {
                        continue;
                    }
                    String antinodePosition = antinodeX + "-" + antinodeY;
                    antinodesPositions.add(antinodePosition);
                }
                index++;
            }
        }
        //collect antennas with same positions
        int result = antinodesPositions.size();
        System.out.println("Distinct places of antinodes positions is " + result);
    }

    public static void partTwo(ArrayList<String> arr) {
        int maxHorizontal = arr.getFirst().length() - 1;
        int maxVertical = arr.size() - 1;
        HashSet<String> antinodesPositions = new HashSet<String>();
        ArrayList<ArrayList<Coords>> buckets = parseInputToBuckets(arr);
        //calculate antinodes' positions
        for (ArrayList<Coords> bucket : buckets) {
            int index = 0;
            for (Coords antenna : bucket) {
                for (int i = 0, n = bucket.size(); i < n; i++) {
                    if (i == index) {
                        continue;
                    }
                    int verticalDiff = antenna.y - bucket.get(i).y;
                    int horizontalDiff = antenna.x - bucket.get(i).x;
                    //iterate k times until both edges of map
                    //boolean onMap = true;
                    int antinodeX = antenna.x;   //starting position
                    int antinodeY = antenna.y;
                    while (true) {
                        if (antinodeX < 0 || antinodeX > maxHorizontal) {
                            //onMap = false;
                            break;
                        }
                        if (antinodeY < 0 || antinodeY > maxVertical) {
                            //onMap = false;
                            break;
                        }
                        String antinodePosition = antinodeX + "-" + antinodeY;
                        antinodesPositions.add(antinodePosition);
                        antinodeX = antinodeX + horizontalDiff;
                        antinodeY = antinodeY + verticalDiff;
                    }
                    //onMap = true;
                    antinodeX = antenna.x - horizontalDiff;
                    antinodeY = antenna.y - verticalDiff;
                    while (true) {
                        if (antinodeX < 0 || antinodeX > maxHorizontal) {
                            //onMap = false;
                            break;
                        }
                        if (antinodeY < 0 || antinodeY > maxVertical) {
                            //onMap = false;
                            break;
                        }
                        String antinodePosition = antinodeX + "-" + antinodeY;
                        antinodesPositions.add(antinodePosition);
                        antinodeX = antinodeX - horizontalDiff;
                        antinodeY = antinodeY - verticalDiff;
                    }
                }
                index++;
            }
        }
        //collect antennas with same positions
        int result = antinodesPositions.size();
        System.out.println("Updated amount of distinct places of antinodes positions is " + result);
    }
}
