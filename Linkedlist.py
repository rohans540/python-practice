from Linked import Linked_list, Node









#main program
if __name__ == '__main__':

    l_list = Linked_list() #creating l_list object
    l_list.head = Node(10)  #Instantiating Node in head of l_list object
    sec = Node(20)
    thi = Node(30)

    #linking nodes
    l_list.head.next = sec
    sec.next = thi
    #calling showlist() method
    print("After creating linked list")
    l_list.showlist()
    print("\n")
    #pushing 50 inthe list
    l_list.push(50)
    print("After pushing 50 into list using push")
    l_list.showlist()
    print("\n")
    #inserting Rohan after sec Node using
    l_list.insertAfter("Rohan", sec)
    print("After inserting new node 'Rohan' after sec")
    l_list.showlist()
    print("\nList after appending a new Node 70")
    #appending 70 in the list using append() method
    l_list.append(70)
    l_list.showlist()
    print("\n")
    #deleting Node having value 50
    l_list.deleteNode(50)
    print("List after deleting a node by key")
    l_list.showlist()
    print("Length of the list is %d" %l_list.getcount())
    print(l_list.search_ele(90))
    l_list.swapNodes(10, "Rohan")
    print("\n list after swapping Nodes with values 10 and Rohan")
    l_list.showlist()
