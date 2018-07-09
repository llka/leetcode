import java.io.File;

public class ReadMeGenerator {
    private static final String LEETCODE_PROBLEMS_URL = "https://leetcode.com/problems/";
    private static final String SPACE_CODE = "%20";
    private static final int NUMBER_IDX = 0;
    private static final int NAME_IDX = 1;


    public ReadMeGenerator() {
    }

    private String folderName = "";

    public void printInConsoleReadMeFromFolder(String folderPath) {
        File folder = new File(folderPath);
        File[] listOfFiles = folder.listFiles();

        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isFile()) {
                String name = listOfFiles[i].getName();
                String[] numberAndName = listOfFiles[i].getName().split("\\.");
                System.out.println("|" + numberAndName[NUMBER_IDX] + "|"
                        + "[" + numberAndName[NAME_IDX] + "]"
                        + "(" + LEETCODE_PROBLEMS_URL + numberAndName[1].substring(1).toLowerCase().replaceAll(" ", "-") + "/description/"
                        + ") | [Java](./" + folderName + name.replaceAll(" ", SPACE_CODE) + ")|Easy| ");
            } else if (listOfFiles[i].isDirectory()) {
                if (!".git".equals(listOfFiles[i].getName())) {
                    folderName = listOfFiles[i].getName() + "/";
                    System.out.println();
                    System.out.println("Directory " + folderName);
                    printInConsoleReadMeFromFolder(folderPath + "\\" + folderName);
                }
            }
        }
    }

}
