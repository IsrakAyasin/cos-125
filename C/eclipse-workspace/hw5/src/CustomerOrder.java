public class CustomerOrder {
    private String name;
    private String date;
    private int quantity;
    
    public CustomerOrder() {
        name = "";
        date = "";
        quantity = 0;
    }
    
    public CustomerOrder(String name, String date, int quantity) {
        this.name = name;
        this.date = date;
        this.quantity = quantity;
    }
    
    public void shipProduct() {
        if (quantity > 0) {
            quantity--;
        }
    }
    public int getQuantity() {
    	return quantity;
    }
}
