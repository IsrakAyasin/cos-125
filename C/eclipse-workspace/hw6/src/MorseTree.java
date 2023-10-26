import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class MorseTree {
    private TreeNode<String> root;

    public MorseTree() {
        root = null;
    }

    public void buildTreeFromFile(String filePath) {
        try {
            File file = new File(filePath);
            Scanner scanner = new Scanner(file);

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(" ");
                String symbol = parts[0];
                String morseCode = parts[1];

                insert(symbol, morseCode);
            }

            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + filePath);
        }
    }

    public void insert(String symbol, String morseCode) {
        if (root == null) {
            root = new TreeNode<>(null);
        }

        TreeNode<String> current = root;

        for (int i = 0; i < morseCode.length(); i++) {
            char c = morseCode.charAt(i);

            if (c == '.') {
                if (current.getLeft() == null) {
                    current.setLeft(new TreeNode<>(null));
                }
                current = current.getLeft();
            } else if (c == '-') {
                if (current.getRight() == null) {
                    current.setRight(new TreeNode<>(null));
                }
                current = current.getRight();
            }
        }

        current.setElement(symbol);
    }

    public String preOrder() {
        if (root == null) {
            return "";
        }
        return root.preorder();
    }

    public String postOrder() {
        if (root == null) {
            return "";
        }
        return root.postorder();
    }

    public String toMorseCode(String englishText) {
        StringBuilder result = new StringBuilder();

        for (char c : englishText.toCharArray()) {
            String letter = Character.toString(c).toLowerCase();
            String morseCode = findMorseCode(root, letter);

            if (!morseCode.isEmpty()) {
                result.append(morseCode).append("|");
            }
        }

        return result.toString().replaceAll("\\|$", "");
    }

    public String toEnglish(String morseCode) {
        StringBuilder result = new StringBuilder();

        String[] symbols = morseCode.split("\\|");

        for (String symbol : symbols) {
            String letter = findEnglishLetter(root, symbol);
            result.append(letter);
        }

        return result.toString().trim();
    }

    private String findMorseCode(TreeNode<String> node, String letter) {
        if (node == null) {
            return "";
        }

        if (node.getElement() != null && node.getElement().equalsIgnoreCase(letter)) {
            return "";
        }

        String left = findMorseCode(node.getLeft(), letter);
        String right = findMorseCode(node.getRight(), letter);

        if (!left.isEmpty()) {
            return "." + left;
        } else if (!right.isEmpty()) {
            return "-" + right;
        }

        return "";
    }

    private String findEnglishLetter(TreeNode<String> node, String morseCode) {
        if (node == null) {
            return "";
        }

        if (node.getElement() != null && findMorseCode(node, node.getElement()).equals(morseCode)) {
            return node.getElement();
        }

        String left = findEnglishLetter(node.getLeft(), morseCode);
        String right = findEnglishLetter(node.getRight(), morseCode);

        if (!left.isEmpty()) {
            return left;
        } else if (!right.isEmpty()) {
            return right;
        }

        return "";
    }
}
