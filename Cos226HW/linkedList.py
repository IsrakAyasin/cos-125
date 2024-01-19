class ListNode:
    
   def __init__(self, data):
      self.data = data
      self.next = None
      return

   def hasValue(self, value):
      return self.data == value
      
class LinkedList:
   
   def __init__(self):
      self.head = None
      self.tail = None
      return
   
   def append(self, item):
      if not isinstance(item,ListNode):
         item = ListNode(item)
      if self.head is None:
         self.head = item
      else:
         self.tail.next = item
      
      self.tail = item
      return
   
   def list_length(self):
      count = 0
      current_node = self.head

      while current_node is not None:
         count = count + 1
         current_node = current_node.next
         
      return count
   
   def output_lists(self):

      current_node = self.head

      while current_node is not None:
         print(current_node.data)
         current_node = current_node.next
      
      return
   
   def search(self, value):
      current_node = self.head
      node_id=1
      result=[]

      while current_node is not None:
         if current_node.has_value(value):
            result.append(node_id)

         current_node = current_node.next
         node_id += 1
      
      return result
   
   def remove(self, item_id):
      current_node = self.head
      previous_node = None
      current_id = 1

      while current_node is not None:
         if current_id == item_id:
            if previous_node is not None:
               previous_node.next=current_node.next
            else:
               self.head=current_node.next
            return
         else:
            current_node = current_node.next
            previous_node = current_node
            current_id += 1
      return
       


   
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin") 
node4 = ListNode(15)
node5 = ListNode("Pickle")
node6 = ListNode("COS226")

example = LinkedList()

for i in [node1, node2, node3, node4, node5,node6]:
   example.append(i)
example.output_lists()
print("length", example.list_length())