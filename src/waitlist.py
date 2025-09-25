# /src/waitlist.py

class _Node:
    __slots__ = ("name", "next")

    def __init__(self, name, next=None):
        self.name = name
        self.next = next


class Waitlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Return number of people on the waitlist."""
        return self._size

    def to_list(self):
        """Return names from head to tail as a Python list."""
        result = []
        cur = self.head
        while cur:
            result.append(cur.name)
            cur = cur.next
        return result

    def join(self, name):
        """Append name at the tail (O(1))."""
        node = _Node(name)
        if not self.head:
            # first person
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def find(self, name):
        """Return True if name exists, else False."""
        cur = self.head
        while cur:
            if cur.name == name:
                return True
            cur = cur.next
        return False

    def cancel(self, name):
        """Remove first occurrence; return True if removed."""
        prev = None
        cur = self.head
        while cur:
            if cur.name == name:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next

                if cur is self.tail:
                    self.tail = prev

                self._size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def bump(self, name):
        """
        Move first occurrence to the head; return True if moved.
        If already at head or not found, return False.
        """
        if not self.head or self.head.name == name:
            return False

        prev = None
        cur = self.head
        while cur:
            if cur.name == name:
                # detach node
                if prev:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev

                # move to head
                cur.next = self.head
                self.head = cur
                return True
            prev, cur = cur, cur.next
        return False
