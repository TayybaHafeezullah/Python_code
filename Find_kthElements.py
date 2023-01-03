

def kthSmallest(self, root, k):
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    return inorder(root)[k - 1]



def kthLargest(self, root, k):
    def inorder(r):
        return inorder(r.right) + [r.val] + inorder(r.left) if r else []
    return inorder(root)[k - 1]


import heapq
def kthLargest(self, nums, k):
    return heapq.nlargest(k, nums)[-1]

def kthLargest(self, matrix, k):
    return sorted([j for i in matrix for j in i])[-k]


class codec:
    def serialize(self, root):
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append('#')
        vals = []
        preorder(root)
        return ' '.join(vals)
    def desirialized(self, data):
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        vals = iter(data.split(""))
        return helper()
    
    
