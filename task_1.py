class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        res = []
        while current:
            res.append(str(current.data))
            current = current.next
        print(" -> ".join(res))


def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next


def merge_sort(head):
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)

    return merge_sorted_lists(left, right)


ll = LinkedList()
for value in [3, 1, 4, 2, 5]:
    ll.append(value)

print("Initial list:")
ll.print_list()

ll.head = reverse_list(ll.head)
print("Reversed list:")
ll.print_list()

ll.head = merge_sort(ll.head)
print("Sorted list:")
ll.print_list()

l1 = LinkedList()
l2 = LinkedList()
for v in [1, 3, 5]:
    l1.append(v)
for v in [2, 4, 6]:
    l2.append(v)

merged_head = merge_sorted_lists(l1.head, l2.head)

print("Merged sorted list:")
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.print_list()
