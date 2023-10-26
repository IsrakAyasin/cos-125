public class OrderTester {
    public static void main(String[] args) {
        OrderQueue orderQueue = new OrderQueue(14);
        
        orderQueue.addOrder("Customer 1", "2023-03-28", 5);
        orderQueue.addOrder("Customer 2", "2023-03-29", 5);
        orderQueue.addOrder("Customer 3", "2023-03-30", 8);
        
        System.out.println(orderQueue.toString());
        
        orderQueue.sellRemainingStock();
        
        System.out.println(orderQueue.toString());
        
        orderQueue.addStock(10);
        orderQueue.addOrder("Customer 4", "2023-03-31", 3);
        orderQueue.addOrder("Customer 5", "2023-04-01", 3);
        orderQueue.addOrder("Customer 6", "2023-04-02", 5);
        
        orderQueue.sellRemainingStock();
        
        System.out.println(orderQueue.toString());
    }
}