class Node(object):
    '''Node'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# ADT of the single link list
class Singlelinklist(object):
    '''single link list'''
    def __init__(self, node = None):
        self._head = None
# duixiang shuxing
    def is_empty(self):
        return self._head == None

    def length(self):
        count = 0
        cur = self._head
        # move the cur
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        ''' go travel all the list'''
        cur = self._head
        while cur != None :
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

        # pass

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else :
            cur = self._head
            while cur.next != None :
                cur = cur.next
            cur.next = node


    def insert(self, pos, item):
        pre = self._head
        node = Node(item)
        count = 0
        while count != (pos-1) :
            count += 1
            pre = pre.next
        node.next = pre.next
        pre.next = node
        # pass
    def remove(self, item):
        pre = self._head
        cur = pre.next
        node = Node(item)
        count = 0
        if node == cur :

    def search(self,item):
        pass
# node = Node(100)
#
# node2 = Node()
#
# if __name__ == ''__main__'':
ll = Singlelinklist()
print(ll.is_empty())
print(ll.length())

ll.append(1)
print(ll.is_empty())
print(ll.length())

ll.append(2)
ll.add(8)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.insert(2,32)

ll.travel()