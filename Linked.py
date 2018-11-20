#Class Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None




#class Linked_list
class Linked_list:

#constructor
    def __init__(self):
        self.head = None
#push() method to push a new node in the start of the list
    def push(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

#showlist() method to show the entire list (Traversing)
    def showlist(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

#insertAfter() method to push a new Node after a given Node
    def insertAfter(self, data, tar):
        if tar is None:
            print("Invalid Node")
            return
        n = Node(data)
        n.next = tar.next
        tar.next = n

#append() method to append a node at the end of the list
    def append(self, data):

        n = Node(data)

        if self.head is None:
            self.head = n
            return

        temp = self.head.next
        while temp.next:
            temp = temp.next
        temp.next = n

#deleteNode() method to delete a Node using key value
    def deleteNode(self, key):
        temp = self.head

        if temp.next is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp.next is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

#len_list() method to find the length of the linked list: Iterative method
    def len_list(self):
        count = 0
        current = self.head
        while current is not None:
            current= current.next
            count = count+1
        return count

#getcountrec() method to find the length of the linked list: Recursive method
    def getcountrec(self, node):

        if node is None:
            return 1
        else:
            return 1+self.getcountrec(node.next)

#getcount() method a wrapper for getcountrec() method
    def getcount(self):
        return self.getcountrec(self.head)

#search_ele() method to check whether the element is in the list or not

    def search_ele(self, key):

        flag = False
        current = self.head

        while current is not None:
            if current.data == key:
                flag = True
                return flag
            else:
                current = current.next
        return flag

#swapNodes() method to swap nodes using keys
    def swapNodes(self, x, y):

#if x and y are same nodes
        if x == y:
            return


        prevX = None
        currX = self.head

#search for x, keep track of currentX and previousX
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

#search for y, keep track of currentY and previousY
        prevY = None
        currY = self.head

        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

#if either x or y is not present then return nothing
        if currX == None or currY == None:
            return

#if x is not the head of the linked List
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

#if y is not the head of the linked List
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

#swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
