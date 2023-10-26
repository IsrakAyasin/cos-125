public class PatientManager {
	private Patient[] arrayPatient;

	public PatientManager() {
		arrayPatient=new Patient[10];
	}
	
	public int add(Patient newComer) {
		for (int i=0; i<arrayPatient.length; i++) {
			if(arrayPatient[i]==null) {
				arrayPatient[i]=newComer;
				return i;
			}
		}
		return -1;
	}
	
	public Patient remove(int num) {
		Patient temporary = arrayPatient[num];
		arrayPatient[num]=null;
		return temporary;
	}
	
	public void caffeineAbsorption() {
		for (int i = 0; i < arrayPatient.length; i++) {
			if(arrayPatient[i]!=null) {
				arrayPatient[i].setCaffeineLevel(arrayPatient[i].getCaffeineLevel() - 130);
                if (arrayPatient[i].getCaffeineLevel() <= 0) {
                	arrayPatient[i] = null;
                }
			}}}
	public String toString() {
		int count = 0;
		String result = "";
		for(int i = 0; i<10; i++) {
			if(arrayPatient[i]!=null) {
				count++;
			}
		}
		if (count == 0) {
			return"empty";
		}
		else {
			for(int i = 0; i<arrayPatient.length; i++) {
				if(arrayPatient[i] != null) {
				result+=arrayPatient[i].getId()+" "+arrayPatient[i].getCaffeineLevel()+"\n";
			}}
			return result;
		
		}
	}
}