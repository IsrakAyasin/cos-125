public class OrderQueue {
    private LinkedQueue<CustomerOrder> orderQueue;
    private int stock;
    private int size;
    
    public OrderQueue() {
        orderQueue = new LinkedQueue<CustomerOrder>();
        stock = 0;
        size = 0;
    }
    
    public OrderQueue(int stock) {
        orderQueue = new LinkedQueue<CustomerOrder>();
        this.stock = stock;
        size = 0;
    }
    
    public void addOrder(String name, String date, int quantity) {
        CustomerOrder order = new CustomerOrder(name, date, quantity);
        orderQueue.enqueue(order);
        size++;
    }
    
    public void addStock(int additionalStock) {
        stock += additionalStock;
    }
    public void fulfillOrder() {
        if (!orderQueue.isEmpty()) {
            CustomerOrder order = orderQueue.getFront();
            order.shipProduct();
            stock--;
            if (order.getQuantity() == 0) {
                orderQueue.dequeue();
                size--;
            }
        }
    }
    
    public void sellRemainingStock() {
        while (!orderQueue.isEmpty() && stock > 0) {
            fulfillOrder();
        }
    }
    
    public String toString() {
        if (!orderQueue.isEmpty()) {
            return Integer.toString(orderQueue.getFront().getQuantity());
        } else {
            return "0";
        }
    }
}