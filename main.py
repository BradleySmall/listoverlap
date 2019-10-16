#!/usr/bin/python3
""" Find beginning of overlapping list """
""" Wrote my own linked list for this. There is no error checking and all
assumptions are optimistic. This may be a fun project to flesh out with
some exception handling and proper error checking. """

class Node:
    """ The node will be the basis of a singly linked list """
    def __init__(self, val, next=None):
        self.val = str(val);
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
            print(comma, n.val if n.val[0] != '~' else n.val[1:], end = '')
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
    # This is just setup
    cnode = Node(8,Node(10))
    mlist = LList(Node(3,Node(7,cnode)))
    nlist = LList(Node(99,Node(1,cnode)))

    mlist.show()
    nlist.show()


    # solution using 2 "pointers" solves the O(m+n) in constant space
    # aspect of the problem.
    mwalker = mlist.head
    nwalker = nlist.head

    while mwalker.val != nwalker.val:
        mwalker = mwalker.next
        nwalker = nwalker.next
        if not mwalker:
            mwalker = nlist.head
        if not nwalker:
            nwalker = mlist.heead
    print("The overlap = ", nwalker.val);

    # Getting the actual list, though not part of the problem
    # is pretty much free
    print("The overlap list is:", end ='')
    LList(nwalker).show();

    # this solution is partially destructive in that it
    # modifies the val. For this I changed it to a string
    # and added a ~ to ones visited in one list. when traversing
    # the other list finding the ~ shows the overlap. The show()
    # was modified to not show the ~. Certainly a cleanup could be
    # employed to go through an remove all the ~.
    # This is also O(n+m)
    mnode = mlist.rewind()
    while mnode:
        mnode.val = "~" + str(mnode.val)
        mnode = mnode.next

    nnode = nlist.rewind()
    while nnode.val[0] != '~':
        nnode = nlist.next()
    overlap = nnode
    print("The overlap = ", overlap.val[1:])
    print("The overlap list : ", end ='')
    LList(overlap).show()



    # this solution is destructive as it sets
    # all the "next" pointers to None so once the
    # overlap is found you are done, but you no longer
    # have the rest of the list
    mnode = mlist.rewind()
    while mnode:
        temp = mnode.next
        mnode.next = None
        mnode = temp

    # constant space
    # O(m+n) time
    nnode = nlist.rewind()

    overlap = None
    while nnode.next:
        nnode = nlist.next()
    overlap = nnode

    print("The overlap = ", overlap.val[1:])
    print("The overlap list : ", end ='')
    LList(overlap).show()


if __name__ == "__main__":
    main()
