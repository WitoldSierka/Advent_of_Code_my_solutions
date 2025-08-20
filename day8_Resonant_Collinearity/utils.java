import java.io.File;

public class utils {
    public static void fileTest() {
        String currentDir = System.getProperty("user.dir");
        System.out.println("Working Directory = " + currentDir);
        File dir = new File(currentDir);
        String[] files = dir.list();

        if (files != null) {
            System.out.println("Files and directories:");
            for (String fileName : files) {
                System.out.println(" - " + fileName);
            }
        } else {
            System.out.println("Could not list directory contents.");
        }
    }
}
