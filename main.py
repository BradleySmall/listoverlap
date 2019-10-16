""" Find beginning of overlapping list """
""" Wrote my own linked list for this. There is no error checking and all
assumptions are optimistic. This may be a fun project to flesh out with
some exception handling and proper error checking. """

class Node:
    """ The node will be the basis of a singly linked list """
    def __init__(self, val, next=None):
        self.val = val;
        self.next = next


class LList:
    """ Linked list """
    def __init__(self, head):
        self.head = head
        self.current = head

    def rewind(self):
        """ return current pointer to the head of the list """
        self.current = self.head
        return self.current

    def next(self):
        """ advance the current pointer """
        self.current = self.current.next
        return self.current

    def show(self):
        """ ouput in list format a linked list """
        n = self.head
        print("[", end = '')
        comma = ''
        while n:
            print(comma, n.val, end = '')
            comma = ','
            n = n.next
        print(" ]")

    def reverse(self):
        """ reverse a list in place """
        prev = None
        n = self.head
        while n:
            temp = n.next
            n.next = prev
            prev = n
            n = temp
            if n:
                self.head = n


def main():
    """ Main driver create lists, reverse them, find beginning overlap """

    mlist = LList(Node(3,Node(7,Node(8,Node(10)))))
    nlist = LList(Node(99,Node(1,Node(8,Node(10)))))

    mlist.show()
    nlist.show()

    nlist.reverse()
    mlist.reverse()

    # constant space
    # O(m+n) time
    nnode = nlist.rewind()
    mnode = mlist.rewind()

    overlap = None
    while nnode.val == mnode.val:
        overlap = nnode
        nnode = nlist.next()
        mnode = mlist.next()

    print("The overlap = ", overlap.val)
    nlist.reverse()
    mlist.reverse()

    overlapList = LList(overlap)
    print("The overlap list : ", end ='')
    overlapList.show()


if __name__ == "__main__":
    main()