public interface Queue<T> {
	public void enqueue(T element);
	
	public T dequeue();
	
	public T getFront();
	
	public boolean isEmpty();
	
	public int size();
}
