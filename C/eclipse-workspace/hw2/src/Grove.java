public class Grove {
	Tree[] oneTree;
	String grove_name;
	int plantedTree=0;
	
	public Grove(String grove_name) {
		this.grove_name=grove_name;
		oneTree = new Tree[8];
	}
	
	public int plantTree(Tree tree) {
		for (int i=0; i<9; i++) {
			if(oneTree[i] == null) {
				oneTree[i]=tree;
				plantedTree++;
				return i;
			}
		}
		return -1;
	}
	
	public Tree removeTree(int i) {
		Tree tem = oneTree[i];
		oneTree[i]=null;
		plantedTree--;
		return tem;
	}
	
	public String toString() {
		return ""+plantedTree;
	}
}
