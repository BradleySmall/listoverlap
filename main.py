#!/usr/bin/python3
""" Find beginning of overlapping list
Wrote my own linked list for this. There is no error checking and all
assumptions are optimistic. This may be a fun project to flesh out with
some exception handling and proper error checking.
"""

class Node:
    """ The node will be the basis of a singly linked list """
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)


class LList:
    """ Linked list """
    def __init__(self, head):
        self.head = head
        self.current = head

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        temp = self.current
        if not temp:
            raise StopIteration
        self.current = self.current.next
        return temp

    def __str__(self):
        return '[ ' + ' -> '.join([str(node) for node in self]) + ' ]'


def main():
    """ Main driver create lists, reverse them, find beginning overlap """
    # This is just setup
    cnode = Node(8, Node(10))
    mlist = LList(Node(3, Node(7, cnode)))
    nlist = LList(Node(99, Node(1, cnode)))

#    nlist = LList(Node(99,Node(1)))
#
#    cnode = Node(3, Node(7, Node(8, Node(10))))
#    mlist = LList(cnode)
#    nlist = LList(cnode)

    print(mlist)
    print(nlist)

    non_destructive_find(mlist, nlist)
    destructive_find(mlist, nlist)


def non_destructive_find(mlist, nlist):
    """"
    solution using 2 "pointers" solves the O(m+n) in constant space
    aspect of the problem.
    """
    mwalker = mlist.head
    nwalker = nlist.head

    count_rollovers = 0
    while mwalker != nwalker:
        mwalker = mwalker.next
        nwalker = nwalker.next
        if not mwalker:
            mwalker = nlist.head
            count_rollovers += 1
        if not nwalker:
            nwalker = mlist.head
            count_rollovers += 1
        if count_rollovers > 2:
            print("There was no overlap")
            break
    else:
        print("The overlap = ", nwalker)

        # Getting the actual list, though not part of the problem
        # is pretty much free
        print("The overlap list is:", end='')
        print(LList(nwalker))


def destructive_find(mlist, nlist):
    """
    this solution is destructive as it sets
    all the "next" pointers to None so once the
    overlap is found you are done, but you no longer
    have the rest of the list
    """
    mnode = mlist.head
    while mnode:
        temp = mnode.next
        mnode.next = None
        mnode = temp

    # constant space
    # O(m+n) time

    overlap = None
    for overlap in nlist:
        pass


    print("The overlap = ", overlap.val)
    print("The overlap list : ", end='')
    print(LList(overlap))


if __name__ == "__main__":
    main()
