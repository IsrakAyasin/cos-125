public class PatientTester {

	public static void main(String[] args) {
		PatientManager manager = new PatientManager();
		System.out.println(manager.toString());
		
		Patient one = new Patient(1,100);
		Patient two = new Patient(2,200);
		Patient three = new Patient(3,300);
		Patient four = new Patient(4,400);
		manager.add(one);
		manager.add(two);
		manager.add(three);
		manager.add(four);
		System.out.println(manager.toString());

		manager.caffeineAbsorption();
		System.out.println(manager.toString());
		manager.remove(3);
		System.out.println(manager.toString());
	}
}
