public class Book {
	private String title;
	private String genre;
	
	public Book(String title,String genre) {
		this.title=title;
		this.genre=genre;
	}
	
	public String toString() {
		return (title);
	}
	
	public String getTitle() {
		return title;
	}
}
