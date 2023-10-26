
	public class MorseTester {

	    public static void main(String[] args) {
	        MorseCodeTree tree = new MorseCodeTree();
	        System.out.println("Preorder: " + tree.preOrder());
	        System.out.println("Postorder: " + tree.postOrder());
	        String englishMessage = "The quick fox";
	        String morseMessage = tree.englishToMorse(englishMessage);
	        System.out.println("English to Morse: " + morseMessage);
	        String translatedMessage = tree.morseToEnglish(morseMessage);
	        System.out.println("Morse to English: " + translatedMessage);
	    }
	}
