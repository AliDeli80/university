class BTnode():
    def __init__(self , data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
    
class BTree():
    def __init__(self , root = None):
        self.root = root

    def inorder(self , root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self,root) :
        if root is None:
            return
        else:
            print(root.data)   
            self.preorder(root.left)   
            self.preorder(root.right) 
    
    def postorder(self , root):
        if root is None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)


def check_full(root):
    full = []
    if root is None:
        return 
    else:
        check_full(root.left)
        if root.left and root.right != None:
            full.append(root.data)
        check_full(root.right)
    for i in full:
        print('full:',i)   
       

def check_semi_full(root):
    semi_full = []
    if root is None:
        return
    else:
        check_semi_full(root.left)
        if root.left == None and root.right != None:
            semi_full.append(root.data)
        elif root.left != None and root.right == None:
            semi_full.append(root.data)
        check_semi_full(root.right)

    for i in semi_full:
        print("semifull:" , i)
    
# if len(semi_full)==0:
#     print('True')
# else:
#     print('False')    
        
        

root = BTnode(10 , BTnode(5 , BTnode(2 , BTnode(1)) , BTnode(6)) , BTnode(11 , BTnode(12)))
ex = BTree(root)
ex.inorder(root)
check_full(root)
check_semi_full(root)
# print("full:" , full)
# print("semi_full:" , semi_full)