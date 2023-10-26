
public class TreeNode<T> {
	private T element;
	private TreeNode<T> left;
	private TreeNode<T> right;
	
	public TreeNode(T element){
		this.element = element;
	}

	public T getElement() {
		return element;
	}

	public void setElement(T element) {
		this.element = element;
	}

	public TreeNode<T> getLeft() {
		return left;
	}

	public void setLeft(TreeNode<T> left) {
		this.left = left;
	}

	public TreeNode<T> getRight() {
		return right;
	}

	public void setRight(TreeNode<T> right) {
		this.right = right;
	}
	
	public boolean isLeaf(){
		return (left == right) && (left == null);
	}
	
	public String toString(){
		return element.toString();
	}
	
	//O(n)
	public String preorder(){
		if (isLeaf()){
			return element.toString();
		}
		else if ((left != null) && (right == null)){
			return element.toString() + " " + left.preorder();
		}
		else if ((left == null) && (right != null)){
			return element.toString() + " " + right.preorder();
		}
		else{
			return element.toString() + " " + left.preorder() + " " + right.preorder();
		}
	}
	
	//O(n)
	public String postorder(){
		if (isLeaf()){
			return element.toString();
		}
		else if ((left != null) && (right == null)){
			return left.postorder() + " " + element.toString();
		}
		else if ((left == null) && (right != null)){
			return right.postorder() + " " + element.toString();
		}
		else{
			return left.postorder() + " " + right.postorder() + " " + element.toString();
		}
	}
	
	//O(n)
	public int size(){
		if (isLeaf()){
			return 1;
		}
		else if ((left != null) && (right == null)){
			return 1 + left.size();
		}
		else if ((left == null) && (right != null)){
			return 1 + right.size();
		}
		else{
			return 1 + left.size() + right.size();
		}
	}
	
	//O(n)
	public int height(){
		if (isLeaf()){
			return 0;
		}
		else if (left != null && right == null){
			return left.height() + 1;
		}
		else if (left == null && right != null){
			return right.height() + 1;
		}
		else{
			return Math.max(left.height(), right.height()) + 1;
		}
	}
	
	//O(1)
	public void insertLeft(T element){
		if (left == null){
			left = new TreeNode<T>(element);
		}
		else{
			return;
		}
	}
	
	//O(1)
	public void insertRight(T element){
		if (right == null){
			right = new TreeNode<T>(element);
		}
		else{
			return;
		}
	}
	
	//O(n log n)
	public void insert(T element){
		if (isLeaf()){
			this.insertLeft(element);
		}
		else if (left == null && right != null){
			this.insertLeft(element);
		}
		else if (left != null && right == null){
			this.insertRight(element);
		}
		else{
			if (left.height() <= right.height()){
				left.insert(element);
			}
			else if (left.height() > right.height()){
				right.insert(element);
			}
		}
	}
	
	//O(n^2)
	public boolean isBalanced(){
		if (isLeaf()){
			return true;
		}
		else if (left != null && right == null){
			return Math.abs(left.height() - -1) <= 1;
		}
		else if (left == null && right != null){
			return Math.abs(right.height() - -1) <= 1;
		}
		else{
			return Math.abs(left.height() - right.height()) <= 1;
		}	
	}
	
//	//O(log n)
//	public void insertBalanced(T element){
//		if (element <= this.getElement()){
//			if (left == null){
//				insertLeft(element);
//			}
//			else{
//				left.insertBalanced(element);
//			}
//		}
//		else{
//			if (right == null){
//				insertRight(element);
//			}
//			else{
//				right.insertBalanced(element);
//			}
//		}
//	}

	//Best case: O(1)
	//Worst case: O(n)
	public boolean search(T element){
		if (this.element == element){
			return true;
		}
		else if (left == null && right == null){
			return false;
		}
		else if (left != null && right == null){
			return left.search(element);
		}
		else if (left == null && right != null){
			return right.search(element);
		}
		else{
			return left.search(element) || right.search(element);
		}
	}
	
	//Best case: O(1)
	//Worst case: O(n)
	public void remove(T element){
		if (this.element == element){
			//This can never happen/work
		}
		else if (left == null && right == null){
			return;
		}
		else if (left != null && right == null){
			if (left.element == element){
				left = left.getLeft();
				//left = null;
			}
			else{
				left.remove(element);
			}
		}
		else if (left == null && right != null){
			if (right.element == element){
				right = right.getRight();
			}
			else{
				right.remove(element);
			}
		}
		else{
			if (left.element == element){
				left = left.getLeft();
			}
			else{
				left.remove(element);
			}
			if (right.element == element){
				right = right.getRight();
			}
			else{
				right.remove(element);
			}
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
