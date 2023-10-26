public class Patient {
	private int IdNumber;
	private double caffeineLevel;
	public Patient(int IdNumber, double caffeineLevel) {
		this.IdNumber=IdNumber;
		this.caffeineLevel=caffeineLevel;
	}
	public double getCaffeineLevel() {
		return caffeineLevel;
	}
	public int getId() {
		return IdNumber;
	}
	public void setCaffeineLevel(double newLevel) {
		caffeineLevel = newLevel;
	}
}
