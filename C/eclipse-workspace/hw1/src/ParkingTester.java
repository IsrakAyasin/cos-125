public class ParkingTester {

	public static void main(String[] args) {
		ParkingLot andro = new ParkingLot();
		System.out.println(andro.toString());
		Car one = new Car("Infiniti","Red",true);
		andro.park(one);
		System.out.println(andro.toString());
		Car two = new Car("Cadilac","Gray",false);
		andro.park(two);
		System.out.println(andro.toString());
		andro.remove(0);
		System.out.println(andro.toString());
		
	}
}
