# 红黑树节点
class RBNode(object):
    def __init__(self, data):
        self.data = data  # 数据域
        self.color = 'red'
        self.left = None
        self.right = None
        self.parent = None


# 红黑树
class RBTree(object):
    def __init__(self):
        self.root = None

    def treePrint(self):
        print('红黑树: start')
        self.midTraverse(self.root)
        print('红黑树: end')

    # 中序遍历
    def midTraverse(self, node):
        if node is None:
            return
        self.midTraverse(node.left)
        colorStr = 'black' if node.color == 'black' else 'red'
        parentStr = '父=' + ('nil' if node.parent is None else str(node.parent.data))
        parentColorStr = 'black' if node.parent is not None and node.parent.color == 'black' else 'red'
        print(node.data, colorStr, parentStr, parentColorStr)
        self.midTraverse(node.right)

    # 添加一个节点
    def add(self, node):
        # 如果没有根节点 参数node作为根节点
        if self.root is None:
            self.root = node
            node.color = 'black'  # 根节点为black色
            return
        # 寻找合适的插入位置
        p = self.root
        while p is not None:
            if node.data < p.data:
                if p.left is None:
                    p.left = node
                    node.parent = p
                    self.addFix(node)
                    break
                p = p.left
            elif node.data > p.data:
                if p.right is None:
                    p.right = node
                    node.parent = p
                    self.addFix(node)
                    break
                p = p.right
            else:
                return

    # 调整红黑树
    def addFix(self, node):
        while True:
            if node == self.root:  # 如果处理到根节点了 则着色为black
                node.color = 'black'
                return
            p = node.parent  # 爸爸
            if p.color == 'black' or node.color == 'black':  # 自己和爸爸只要有一个是black的 就构不成双red 则返回
                return
            # 接下来分析红爸爸情况
            g = p.parent  # 爷爷 红爸爸肯定有爸爸，因为红色绝不是根节点
            u = g.left if p == g.right else g.right  # 叔叔 叔叔可能为空节点
            if u is not None and u.color == 'red':  # 红叔叔 则着色 然后从爷爷开始向上继续调整
                u.color = p.color = 'black'  # 叔叔和爸爸都变black色
                g.color = 'red'  # 爷爷变red色
                node = g  # 参数node（x）指向爷爷，然后继续循环
                continue
            # 接下来分析黑叔叔得情况 有四种情况 左左，左右，右左，右右
            if p == g.left and node == p.left:  # 左左
                # 以爸爸为支点右旋爷爷
                self.rotateRight(p)
            elif p == g.left and node == p.right:  # 左右
                # 以x为支点左旋爸爸
                self.rotateLeft(node)
                # 以x为支点右旋爷爷(上面的旋转把爷爷变成了新爸爸)
                self.rotateRight(node)
            elif p == g.right and node == p.right:  # 右右 其实就是 左左的镜像
                # 以爸爸为支点左旋爷爷
                self.rotateLeft(p)
            elif p == g.right and node == p.left:  # 右左 其实就是 左右的镜像
                # 以x为支点右旋爸爸
                self.rotateRight(node)
                # 以x为支点左旋爷爷(上面的旋转把爷爷变成了新爸爸)
                self.rotateLeft(node)

    #         * 左旋示意图：对节点node进行左旋
    #         *       parent              parent
    #         *       /                   /
    #         *     node              right
    #         *    /  \               /   \
    #         *   ln right ----->  node   ry
    #         *       /  \        /  \
    #         *      ly   ry     ln   ly
    #         * 左旋做了三件事：
    #         * 1. 将right的左子节点ly赋给node的右子节点,并将node赋给right左子节点ly的父节点(ly非空时)
    #         * 2. 将right的左子节点设为node，将node的父节点设为right
    #         * 3. 将node的父节点parent(非空时)赋给right的父节点，同时更新parent的子节点为right(左或右)
    #         :param node: 要左旋的节点
    # 关于红黑树的旋转，一直是个难搞的点
    # 这里我提供一个口诀：
    #   右旋： 支点占旋点原位，支点的右给旋点作为左，旋点作为支点的右
    #   左旋： 支点占旋点原位，支点的左给旋点作为右，旋点作为支点的左
    # 我们先忽略颜色，可以看到旋转操作不会影响旋转结点的父结点，父结点以上的结构还是保持不变的。
    # 左旋只影响旋转结点和其右子树的结构，把右子树的结点往左子树挪了。
    # 右旋只影响旋转结点和其左子树的结构，把左子树的结点往右子树挪了。
    # 对x进行左旋，意味着，将“x的右孩子”设为“x的父亲节点”；即，将
    # x变成了一个左节点(x成了为z的左孩子)！。 因此，左旋中的“左”，意味着“被旋转的节点将变成一个左节点”。
    # 对x进行左旋，意味着，将“x的右孩子”设为“x的父亲节点”；即，将 x变成了一个左节点(x成了为z的左孩子)！。 因此，左旋中的“左”，
    # 意味着“被旋转的节点将变成一个左节点”。
    # 右旋 p支点
    def rotateRight(self, p):
        g = p.parent  # 支点的父节点就是旋点
        # 右旋g
        if g == self.root:  # 若g是根节点 则p升为根节点
            self.root = p
            p.parent = None
        else:  # 若g不是根节点 那么必然存在g.parent p占据g的位置
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.left = p.right
        if p.right is not None:
            p.right.parent = g
        p.right = g
        g.parent = p
        # g和p颜色交换
        p.color, g.color = g.color, p.color

    # 左旋 p 支点
    def rotateLeft(self, p):
        g = p.parent  # 支点的父节点就是旋点
        # 左旋g
        if g == self.root:  # 若g是根节点 则p升为根节点
            self.root = p
            p.parent = None
        else:  # 若g不是根节点 那么必然存在g.parent p占据g的位置
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.right = p.left
        if p.left is not None:
            p.left.parent = g
        p.left = g
        g.parent = p
        # g和p颜色交换
        p.color, g.color = g.color, p.color

    # 删除一个节点
    def delete(self, node):
        # 查找要删除的节点
        d = self.root
        while d is not None:
            if node.data < d.data:
                d = d.left
            elif node.data > d.data:
                d = d.right
            else:
                break
        if d is None:
            print('要删除的', node.data, '已经不存在了')
            return
        # 如果要删除的节点不是叶子节点，我们需要做d的指向转移，直到d指向的是叶子节点就结束循环
        while d.left is not None or d.right is not None:
            # 如果存在右子树 则找直接后继（也就是右子树的最左后代），交换数据, d指向这个后继，重复循环
            if d.right is not None:
                nextNode = self.getMostLeft(d.right)
                d.data, nextNode.data = nextNode.data, d.data
                d = nextNode
                continue
            # 如果存在左子树 则找到直接前驱（也就是左子树的最右后代），交换数据，d指向这个前驱，重复循环
            elif d.left is not None:
                preNode = self.getMostRight(d.left)
                d.data, preNode.data = preNode.data, d.data
                d = preNode
                continue

        print('要删除的是', d.data)
        # 接下来处理要删除的节点是叶子节点的情况吧 #
        needDelete: bool = True
        while True:
            # 如果d是根节点，直接删除
            if self.root == d:
                if needDelete:
                    self.deleteDirectly(d)
                return

            # 如果d的是red色，那么直接删除
            if self.isRed(d):
                if needDelete:
                    self.deleteDirectly(d)
                return

            # 如果d是black色，设s指向兄弟节点（根据红黑树左右子树black色高度相等的性质，s指向的节点必定存在），分好几种情况
            p = d.parent
            s = p.right if d == p.left else p.left
            # print(d.data, d.color, p.data)
            # 1 如果s是red色
            if self.isRed(s):
                if d == p.left:
                    self.rotateLeft(s)
                else:
                    self.rotateRight(s)
                continue  # 旋转后 再重新判断
            sl = s.left
            sr = s.right
            # 2 如果s是黑色，又分好几种情况
            if d == p.left:  # d是p的左孩子
                # 2.1 如果d的远侄为红(有远侄的话必定为红，否则不满足红黑树的红色高度性质)
                if self.isRed(sr):
                    self.rotateLeft(s)
                    sr.color = 'black'
                    if needDelete:
                        self.deleteDirectly(d)
                    return
                # 2.2 如果d的远侄为黑，近侄为红(有近侄的话必定为红，否则不满足红黑树的黑色高度性质)
                if not self.isRed(sr) and self.isRed(sl):
                    self.rotateRight(sl)
                    self.rotateLeft(sl)
                    s.color = 'black'
                    if needDelete:
                        self.deleteDirectly(d)
                    return
                # 2.3 如果d的远侄和近侄都是黑，也就是d是叶子节点，分2种情况
                # 2.3.1 如果p是红色 s变红 p变黑 删除d
                if p.color == 'red':
                    s.color = 'red'
                    p.color = 'black'
                    if needDelete:
                        self.deleteDirectly(d)
                    return
                # 2.3.1 如果p是黑色 s变红 删除d 然后d指向p重复判断步骤
                s.color = 'red'
                if needDelete:
                    self.deleteDirectly(d)
                    needDelete = False
                d = p
                continue
            else:  # d是p的右孩子
                # 2.1 如果d的远侄为红(有远侄的话必定为红，否则不满足红黑树的黑色高度性质)
                if self.isRed(sl):
                    self.rotateRight(s)
                    sl.color = 'black'
                    if needDelete:
                        self.deleteDirectly(d)
                    return
                # 2.2 如果d的远侄为黑，近侄为红(有近侄的话必定为红，否则不满足红黑树的黑色高度性质)
                if not self.isRed(sl) and self.isRed(sr):
                    self.rotateLeft(sr)
                    self.rotateRight(sr)
                    s.color = 'black'
                    if needDelete:
                        self.deleteDirectly(d)
                    return
                # 2.3 如果d的远侄和近侄都是黑，也就是d是叶子节点，分2种情况
                # 2.3.1 如果p是红色 s变红 p变黑 删除d
                if p.color == 'red':
                    s.color = 'red'
                    p.color = 'black'
                    if needDelete:
                        self.deleteDirectly(d)
                    return
                # 2.3.1 如果p是黑色 s变红 删除d 然后d指向p重复判断步骤
                s.color = 'red'
                if needDelete:
                    self.deleteDirectly(d)
                    needDelete = False
                d = p
                continue

    # 是否是红色节点

    @staticmethod
    def isRed(node):
        return node is not None and node.color == 'red'

    # 找到x的最左的后代
    @staticmethod
    def getMostLeft(node):
        while node.left is not None:
            node = node.left
        return node

    # 找到y的最右后代
    @staticmethod
    def getMostRight(node):
        while node.right is not None:
            node = node.right
        return node

    # 直接删除x节点
    def deleteDirectly(self, node):
        if node == self.root:
            self.root = None
        else:
            p = node.parent
            if node == p.left:
                p.left = None
            else:
                p.right = None


if __name__ == '__main__':
    rbt = RBTree()

    # data's = [10, 20, 30, 15]
    # datas = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    datas = [12, 1, 9, 2, 0, 11, 7, 19, 4, 15,
             18, 5, 14, 13, 10, 16, 6, 3, 8, 17]
    for x in datas:
        rbt.add(RBNode(x))

    print('=====================================================')
    rbt.treePrint()
    print('=====================================================')
    rbt.delete(RBNode(12))
    rbt.delete(RBNode(1))
    rbt.delete(RBNode(9))
    rbt.delete(RBNode(2))
    rbt.delete(RBNode(0))
    rbt.delete(RBNode(11))
    rbt.delete(RBNode(7))
    rbt.delete(RBNode(19))
    rbt.delete(RBNode(4))
    rbt.delete(RBNode(15))
    rbt.delete(RBNode(18))
    # rbt.delete(RBNode(5))
    # rbt.delete(RBNode(14))
    # rbt.delete(RBNode(13))
    # rbt.delete(RBNode(10))
    # rbt.delete(RBNode(16))
    # rbt.delete(RBNode(6))
    # rbt.delete(RBNode(3))
    # rbt.delete(RBNode(8))
    # rbt.delete(RBNode(17))
    rbt.treePrint()
