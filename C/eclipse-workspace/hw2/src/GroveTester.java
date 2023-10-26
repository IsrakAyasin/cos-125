
public class GroveTester {
	public static void main(String[] args) {
		Grove GroveOne = new Grove("Spring Valley");
		System.out.println(GroveOne.toString());
		for(int i=0; i<7; i++) {
			Tree same = new Tree(0,37,"pine");
			GroveOne.plantTree(same);
		}
		System.out.println(GroveOne.toString());
		GroveOne.removeTree(3);
		GroveOne.removeTree(5);
		System.out.println(GroveOne.toString());
		Tree two = new Tree(1,13,"Spruce");
		GroveOne.plantTree(two);
		System.out.println(GroveOne.toString());

	}
}
