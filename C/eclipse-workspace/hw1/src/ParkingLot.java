public class ParkingLot {
	ParkingSpot[] spots;
	
	public ParkingLot() {
		spots = new ParkingSpot[20];
		for(int i=0; i<20; i++) {
			if(i<4) {
				spots[i]=new ParkingSpot(true);
				}
			else {
				spots[i]=new ParkingSpot(false);
			}
		}
	}
	
	public int park(Car oneCar) {
		if(oneCar.handicap) {
			for(int i =0; i<4; i++) {
				if(spots[i].parkedCar == null) {
					spots[i].parkedCar = oneCar;
					return i;}
				}
		}
		else{
			for(int i =4; i<20; i++) {
				if(spots[i].parkedCar == null) {
					spots[i].parkedCar = oneCar;
					return i;}
				}
		}
		return -1;
}
	
	public Car remove(int spotNum) {
		Car oneCar = spots[spotNum].parkedCar;
		spots[spotNum].parkedCar = null;
		return oneCar;		
	}
	
public String toString() {
	int x=0;
	int y=0;
	for(int i =0; i<4; i++) {
		if (spots[i].parkedCar == null) {
			x++;
		}
	}
	for(int i =4; i<20; i++) {
		if (spots[i].parkedCar == null) {
			y++;
		}
	}
	return ""+x+" "+y;
	}
}