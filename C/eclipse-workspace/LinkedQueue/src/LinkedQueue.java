public class LinkedQueue<T> implements Queue<T>{
	private LinearNode<T> head = null;
	private LinearNode<T> tail = null;
	private int size = 0;

	public void enqueue(T element) {
		if(tail == null) {
			head= new LinearNode<T>(element);
			tail=head;
			size++;
		}
		else if (head==tail) {
			head.setNext(new LinearNode<T>(element));
			tail = head.getNext();
			size++;
		}
		else {
			tail.setNext(new LinearNode<T>(element));
			tail = tail.getNext();
			size++;
		}
	}
	
	public T dequeue() {
		if(head==null) {
			return null;
		}
		else {
			LinearNode<T> tem = head;
			head = head.getNext();
			size--;
			return tem.getElement();
		}	
	}
	@Override
	public T getFront() {	//O(1)
		if (head == null){
			return null;
		}
		else{
			return head.getElement();
		}
	}

	@Override
	public boolean isEmpty() {  //O(1)
		return (head == null);
	}

	public int size() {	//O(1)
		return size;
	}

}

