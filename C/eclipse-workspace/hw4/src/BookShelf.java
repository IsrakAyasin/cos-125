import java.util.ArrayList;

public class BookShelf {
	private char letter;
	private ArrayList<Book> Books;
	
	public BookShelf(char letter) {
		this.letter = letter;
		Books = new ArrayList<Book>(8);}
	
	public char getLetter() {
		return letter;}
	
	public void setLetter(char newLetter) {
		letter= newLetter;}
	
	public void addBook(Book oneBook) {
	    if (oneBook.getTitle().charAt(0) == letter && Books.size() < 8) {
	        Books.add(oneBook);
	    }
	}
	
	public void remove(Book oneBook) {
		Books.remove(oneBook);
	}
	
	public String toString() {
		if(Books.isEmpty()) {
			return "empty";}
		else {
			String allBook="";
			for (int i= 0; i<Books.size(); i++) {
				if(Books.get(i)!=null) {
					allBook+=Books.get(i).getTitle();
					allBook+="   ";}}
			return allBook;
}}}