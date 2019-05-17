class node:#node creation
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
class linkedlist:
    def __init__(self):
        self.headval = None

    def traverse(self): #function for displaying of list
        printnode = self.headval
        while printnode is not None:
            if printnode.nextval is not None:
                print(printnode.dataval,"->",end="")
                printnode = printnode.nextval
            else:
                print(printnode.dataval)
                printnode = printnode.nextval
                
    def inbeginning(self,begnode): #function for adding node in the beggining of list
        newnode = node(begnode)
        newnode.nextval=self.headval
        self.headval=newnode

    def inend(self,endnode): #function for adding node in the end of list
        newnode = node(endnode)
        if self.headval is None:
            self.headval = newnode
            return
        lasst = self.headval
        while(lasst.nextval):
            lasst = lasst.nextval
        lasst.nextval = newnode

    def addbet(self,middle,btnode): #function for adding node in middle or desired postion in list
        if middle is None:
            print("There is no such node")
            return
        midd = node(btnode)
        midd.nextval = middle.nextval
        middle.nextval = btnode
        
#Main Program
print("Welcome to Insertion of Singly Linked List")
node1 = linkedlist() #node creation
print("Enter three initial to be entered in the list")
node1.headval = node(int(input()))
e2 = node(int(input()))
e3 = node(int(input()))
#connecction establishment
node1.headval.nextval = e2
e2.nextval = e3
choice = 1
while choice != 0:
    #Display choices for user
    print("1.Insertion at the beggining \n 2. Insertion at the middle \n 3.Insertion at the end \n 4.Display \n 0.Stop")
    choice = int(input()) #Get choice from user
    #Validation based on choice
    if choice == 1:
        print("Enter the value of the node which has to be added in the beginning")
        node1.inbeginning(int(input())) #function call for insertion at begining
        
    elif choice == 2:
        print("Enter the node which has to be inserted next to node 2")
        node1.addbet(e2.nextval,int(input())) #function call for insertion at between
        
    elif  choice == 3:
        print("Enter the node which has to be addded in the end")
        node1.inend(int(input())) #function call for insertion at end
        
    elif choice ==4:
        print("Here's your singly linked list")
        node1.traverse()#function call for display of list
        
    else:
        ()
