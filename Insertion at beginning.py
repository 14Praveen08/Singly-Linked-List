class node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
class linkedlist:
    def __init__(self):
        self.headval = None

    def traverse(self):
        printnode = self.headval
        while printnode is not None:
            if printnode.nextval is not None:
                print(printnode.dataval,"->",end="")
                printnode = printnode.nextval
               
            else:
                print(printnode.dataval)
                printnode = printnode.nextval
    def inbeginning(self,begnode):
        newnode = node(begnode)
        newnode.nextval=self.headval
        self.headval=newnode
            


node1 = linkedlist()
print("Enter the values for the list")
node1.headval = node(int(input()))
e2 = node(int(input()))
e3 = node(int(input()))

node1.headval.nextval = e2
e2.nextval = e3

print("Enter the node which has to be added in the beginning")
node1.inbeginning(int(input()))

node1.traverse()
