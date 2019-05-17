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

    def inend(self,endnode):
        newnode = node(endnode)
        if self.headval is None:
            self.headval = newnode
            return
        lasst = self.headval
        while(lasst.nextval):
            lasst = lasst.nextval
        lasst.nextval = newnode

    def addbet(self,middle,btnode):
        if middle is None:
            print("There is no such node")
            return
        midd = node(btnode)
        midd.nextval = middle.nextval
        middle.nextval = btnode
            

#Main Program
node1 = linkedlist()
print("Enter the values for the list")
node1.headval = node(int(input()))
e2 = node(int(input()))
e3 = node(int(input()))

node1.headval.nextval = e2
e2.nextval = e3

print("Enter the node which has to be added in the beginning")
node1.inbeginning(int(input()))

print("Enter the node which has to be addded in the end")
node1.inend(int(input()))

print("Enter the node which has to be inserted next to node 2")
node1.addbet(e2.nextval,int(input()))

node1.traverse()
