class MorseTester {
    public static void main(String[] args) {
        MorseTree tree = new MorseTree();
        tree.buildTreeFromFile("morse_code.txt");

        System.out.println("Preorder tree contents: " + tree.preOrder());
        System.out.println("Postorder tree contents: " + tree.postOrder());

        String englishText = "The quick fox";
        String morseCode = tree.toMorseCode(englishText);
        System.out.println("English to Morse Code: " + morseCode);

        String decodedText = tree.toEnglish(morseCode);
        System.out.println("Morse Code to English: " + decodedText);
    }
}