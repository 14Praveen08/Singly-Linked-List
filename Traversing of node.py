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
            


node1 = linkedlist()
node1.headval = node(int(input()))
e2 = node(int(input()))
e3 = node(int(input()))

node1.headval.nextval = e2
e2.nextval = e3

node1.traverse()
