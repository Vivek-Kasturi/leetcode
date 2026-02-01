# Node class for the linked list used in each bucket
class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        # store key
        self.key = key
        # store value
        self.value = value
        # pointer to next node
        self.next = next


class MyHashMap(object):

    def __init__(self):
        # initialize hash map with fixed size
        # each index contains a dummy node to simplify insert/remove
        self.map = [ListNode() for _ in range(10000)]

    def _hash(self, key):
        # hash function to convert key into array index
        return key % len(self.map)

    def put(self, key, value):
        # get the dummy head of the bucket
        current = self.map[self._hash(key)]

        # traverse the linked list
        while current.next:
            # if key already exists, update its value
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next

        # if key does not exist, add new node at the end
        current.next = ListNode(key, value)

    def get(self, key):
        # start from the first real node (skip dummy node)
        current = self.map[self._hash(key)].next

        # traverse the linked list
        while current:
            # if key is found, return its value
            if current.key == key:
                return current.value
            current = current.next

        # if key is not found, return -1
        return -1

    def remove(self, key):
        # start from dummy node to handle edge cases easily
        current = self.map[self._hash(key)]

        # traverse while checking the next node
        while current.next:
            # if key is found, remove the node
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
