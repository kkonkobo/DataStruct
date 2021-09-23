from collections import deque
class binaryTree:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
         
    def insert_right(self,val):

        

        if self.right_child == None:
            self.right_child = binaryTree(val)
        
        else:
            new_node =  binaryTree(val) 
            new_node.right_child = self.right_child
            self.right_child = new_node

    def insert_left(self, val):
        
        if self.left_child == None:
            self.left_child = binaryTree(val)
        
        else:
            new_node =  binaryTree(val) 
            new_node.left_child = self.left_child
            self.left_child = new_node

    def preOrder(self):
        print (self.value)

        if self.left_child != None:
            self.left_child.inOrder()
        if self.right_child != None:
            self.right_child.inOrder()
    
    def inOrder(self):
        

        if self.left_child != None:
            self.left_child.inOrder()

        print (self.value)
         
        if self.right_child != None:
            self.right_child.inOrder()


    def postOrder(self):
        if self.left_child != None:
            self.left_child.inOrder()
        if self.right_child != None:
            self.right_child.inOrder()
        
        print (self.value)

    def bfs(self):

        queue = deque()

        queue.append(self)

        while (len(queue) > 0):

            node = queue.popleft()

            print(node.value)

            if node.left_child != None:

                queue.append(node.left_child )
            if node.right_child != None:

                queue.append(node.right_child )
            
        
    
a_node = binaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child   

print(a_node.value) # a
print(b_node.value) # b
print(c_node.value) # c
print(d_node.value) # d
print(e_node.value) # e
print(f_node.value) # f    
print ('\n')
a_node.inOrder()
print ('\n')

a_node.postOrder()
print ('\n')

a_node.preOrder()
print ('\n')

a_node.bfs()           




