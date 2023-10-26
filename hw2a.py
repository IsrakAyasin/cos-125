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

    while temp1 is not None:
       mergedList.append(temp1.data)
       mergedList.append(temp2.data)
       temp1 = temp1.next
       temp2 = temp2.next
    return mergedList

#creating first example linked list
firList = LinkedList()
node1 = ListNode(15)
node2 = ListNode(8)
node3 = ListNode(3) 
node4 = ListNode(15)
for i in [node1, node2, node3, node4]:
   firList.append(i)

#creating second example linked list
secList = LinkedList()
node5 = ListNode(5)
node6 = ListNode(13)
node7 = ListNode(14) 
node8 = ListNode(29)
for i in [node5, node6, node7, node8]:
   secList.append(i)

mergeList(firList, secList).outputLists()