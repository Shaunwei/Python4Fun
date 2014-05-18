# The storage class for creating binary tree nodes

class _BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # add node will make it a complete tree
    def addNode(self, node):
        if self.left is None:
            self.left = node
        elif self.right is None:
            self.right = node
        else:
            raise Exception('This node is full.')
            
    def cal_dep(self, node):
        if node == None:
            return 0
        else:
            ldepth = self.cal_dep(node.left)
            rdepth = self.cal_dep(node.right)
            return max(ldepth, rdepth) + 1


def preorderTra(Node):
    if Node is not None:
        print(Node.data)
        preorderTra(Node.left)
        preorderTra(Node.right)

def inorderTra(Node):
    if Node is not None:
        inorderTra(Node.left)
        print(Node.data)
        inorderTra(Node.right)

def posorderTra(Node):
    if Node is not None:
        posorderTra(Node.left)
        posorderTra(Node.right)
        print(Node.data)

def bfs(root):
    from Queue import Queue
    q = Queue()
    q.put(root)
    
    while not q.empty():
        node = q.get()
        print(node.data)
        
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)


def cal_max_level(node):
    if node is None:
        return 0
    else:
        lmaxlevel = cal_max_level(node.left)
        rmaxlevel = cal_max_level(node.right)
    return max(lmaxlevel, rmaxlevel) + 1

def cal_paths(root):
    if root is None:
        return 1
    else:
        lcalpath = cal_paths(root.left)
        rcalpath = cal_paths(root.right)
    return lcalpath + rcalpath

def is_full(root):
    from Queue import Queue
    q = Queue()
    q.put(root)
    
    while not q.empty():
        node = q.get()
        if node.left and node.right:
            q.put(node.left)
            q.put(node.right)
        elif node.left == None and node.right == None:
            pass #the leaf node
        else:
            return False
    else:
        return True

def is_perfect(root):
    pass

def is_compelete(root):
    if root == None:
        return False

    from Queue import Queue
    q = Queue
    q.put(root)
    
    while not q.empty():
        cur_node = q.get()
        if cur_node.left != None:
            q.put(cur_node.left)
            if cur_node.right != None:
                q.put(cur_node.right)
            else:
                last_node = q.get()
                if last_node.left or last_node.right:
                    return False
        elif cur_node.right != None: # only have right node
            return False
        else:
            pass
    else:
        return True
            
        

# test case
if __name__ == '__main__':
    #create all nodes
    root = _BinTreeNode('T')
    X = _BinTreeNode('X')
    B = _BinTreeNode('B')
    G = _BinTreeNode('G')

    Z = _BinTreeNode('Z')
    C = _BinTreeNode('C')
    J = _BinTreeNode('J')
    R = _BinTreeNode('R')
    K = _BinTreeNode('K')
    M = _BinTreeNode('M')
    N = _BinTreeNode('N')
    O = _BinTreeNode('O')

    # construct the tree
    root.addNode(X)
    root.addNode(C)

    X.addNode(B)
    X.addNode(G)
    G.addNode(Z)
    G.addNode(N)

    C.addNode(J)
    C.addNode(R)

    R.addNode(K)
    R.addNode(M)

    M.addNode(O)

    

    # run traversal:
    print('pre order')
    preorderTra(root)
    print('in order')
    inorderTra(root)
    print('post order')
    posorderTra(root)
    print('b f s')
    bfs(root)
    
    print('max_level')
    print(cal_max_level(root))

    
    print('paths')
    print(cal_paths(root))
    
    print('is_full')
    print(is_full(root))

    print(root.cal_dep(root))

