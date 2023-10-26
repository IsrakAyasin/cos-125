import java.util.ArrayList;
public class ArrayStack<one> implements Stack<one>{
	private ArrayList<one> newone = new ArrayList<one>();
	private int size = 0;

	public void push(one elements) {
		newone.add(elements);
		this.size++;
	}
	
	public one pop(){
		try {
			this.size--;
			return newone.remove(this.size);
		}
		catch(Exception ex){
			return null;
		}		
	}
	
	public one peek() {
		return newone.get(this.size -1);
	}
	
	public boolean empty() {
		return this.size==0;
	}
	
	public int size() {
		return this.size;
	}
}
