from collections import deque
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeOrder():
    def preOrder(self, root):
        if not root:
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)
    def preOrder2(self, root):
        if not root:
            return
        st = [root]
        while st:
            tmp = st.pop()
            print(tmp.val, end=' ')
            if tmp.right:
                st.append(tmp.right)
            if tmp.left:
                st.append(tmp.left)
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print(root.val, end=' ')
        self.inOrder(root.right)
    def inOrder2(self, root):
        if not root:
            return
        st = [root]
        while st[-1].left:
            st.append(st[-1].left)
        while st:
            tmp = st.pop()
            print(tmp.val, end=' ')
            if tmp.right:
                st.append(tmp.right)
                while st[-1].left:
                    st.append(st[-1].left)
    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val, end=' ')
    def postOrder2(self, root):
        if not root:
            return
        st = [root]
        res = []
        while st:
            tmp = st.pop()
            res.append(tmp)
            if tmp.left:
                st.append(tmp.left)
            if tmp.right:
                st.append(tmp.right)
        for node in res[::-1]:
            print(node.val, end=' ')
    def levelOrder(self, root):
        if not root:
            return
        q = deque()
        q.append(root)
        while q:
            tmp = q.popleft()
            print(tmp.val, end=' ')
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    treeOrder = TreeOrder()
    print('递归前序遍历：')
    treeOrder.preOrder(root)
    print('\n非递归前序遍历：')
    treeOrder.preOrder2(root)
    print('\n递归中序遍历：')
    treeOrder.inOrder(root)
    print('\n非递归中序遍历：')
    treeOrder.inOrder2(root)
    print('\n递归后序遍历：')
    treeOrder.postOrder(root)
    print('\n非递归后序遍历：')
    treeOrder.postOrder2(root)
    print('\n层次遍历：')
    treeOrder.levelOrder(root)