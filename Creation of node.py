class node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
class linkedlist:
    def __init__(self):
        self.headval = None
node1 = linkedlist()
node1.headval = node("first")
e2 = node("second")
e3 = node("third")

node1.headval.nextval = e2
e2.nextval = e3
