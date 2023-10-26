class ListNode:
   def __init__(self, data):
      self.data = data
      self.next = None
      return
   
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
   
   def remove(self, value):
    current_node = self.head
    previous_node = None

    while current_node is not None:
        if current_node.data == value:
            if previous_node is not None:
                previous_node.next = current_node.next
            else:
                self.head = current_node.next
            if current_node.next is None:
                self.tail = previous_node
            return
        else:
            previous_node = current_node
            current_node = current_node.next
    return
   
   def outputLists(self):
      current_node = self.head

      while current_node is not None:
         print(current_node.data)
         current_node = current_node.next
         
      return
   
def mergeList(list1, list2):
    mergedList= LinkedList()
    temp1 = list1.head
    temp2 = list2.head

    while temp1 is not None and temp2 is not None:
       mergedList.append(temp1.data)
       mergedList.append(temp2.data)
       temp1 = temp1.next
       temp2 = temp2.next
    
    return mergedList

def sortList(list):
    sortedList = LinkedList()

    while list.head is not None:
        smallest = list.head
        temp = smallest.next
        
        while temp is not None:
            if temp.data < smallest.data:
                smallest = temp
            temp = temp.next
        sortedList.append(smallest.data)
        list.remove(smallest.data)
    return sortedList

#creating first example linked list
firList = LinkedList()
node1 = ListNode(15)
node2 = ListNode(8)
node3 = ListNode(3) 
for i in [node1, node2, node3]:
   firList.append(i)

#creating second example linked list
secList = LinkedList()
node5 = ListNode(18)
node6 = ListNode(26)
node7 = ListNode(14) 
for i in [node5, node6, node7]:
   secList.append(i)

sortList(mergeList(firList, secList)).outputLists()