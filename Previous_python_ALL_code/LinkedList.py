class LinkedList :

    def __init__(self,value , nextNode=None):
        self.value = value
        self.nextNode = nextNode

        # '3'->'7'->'10'

        node1 = LinkedList("3")
        node2 = LinkedList("7")
        node3 = LinkedList("10")

        # now connect them together

        node1.nextNode = node2
        node2.nextNode = node3

        # node1 -> node2 -> node3
def printLink(startNode):


        currentNode = startNode

        while True:
            print (currentNode.value , "->" , end=" ")

            if currentNode.nextNode is None:
                print ("None.")
                break

            currentNode = currentNode.nextNode

